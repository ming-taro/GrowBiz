import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import json
import os
from sklearn.preprocessing import MinMaxScaler

user_data = {
    'region': '서울시, 강남구, 역삼동',
    'monthly_rent': 300,  # 만원
    'deposit': 10000,  # 만원 (1억)
    'industry': '외식업, 치킨',  # '치킨', '커피' 등 선택
    'initial_capital': 20000,  # 만원 (1억)
    'preference': '프랜차이즈',
    'franchise_fee_concern': '매우 아니다', #7 가맹비
    'trending_industry_preference': '보통', #8 유행업종
    'sales_importance': '보통', #9 매출액
    'closure_rate_concern': '보통', #10 폐업률
    'competition_confidence': '매우 아니다' #11 경쟁 할 자신? 
}

# 사용자 입력에서 구와 동을 추출 (동을 '역삼'처럼 변환)
gu = user_data['region'].split(', ')[1]  # '강남구'
dong_prefix = user_data['region'].split(', ')[2][:2]  # '역삼'

# 산업 카테고리에서 필요한 부분만 추출 ('치킨', '커피' 등)
industry_category = user_data['industry'].split(', ')[1]  # '치킨' 부분만 추출

# .csv 파일 경로 설정
csv_file_path = os.path.join('..', 'franchise_rank', 'preprocessing_stage1', f'{industry_category}_franchise_data_with_trend_10plus.csv')

# .csv 파일이 존재하는지 확인 후 읽기
if os.path.exists(csv_file_path):
    df = pd.read_csv(csv_file_path)
    print(f"{industry_category} 업종에 해당하는 데이터를 성공적으로 불러왔습니다.")
else:
    print(f"{csv_file_path} 파일을 찾을 수 없습니다.")


def process_csv_file(df_filtered, category):
    # 필요한 열 선택
    columns = ['store_name', 'year', 'region', 'opening_rate', 'closure_rate', 'average_sales', 'average_sales_per_area', 
               'initial_cost', 'business_fee', 'interior_cost', 'standard_store_area']

    df_filtered = df[columns].copy()

    # 스케일링 이전 원래 값 저장 (복원용)
    original_values = df_filtered.copy()

    # MinMaxScaler로 0과 1 사이로 스케일링 적용
    scaler = MinMaxScaler()
    scaled_columns = ['opening_rate', 'closure_rate', 'average_sales_per_area', 'initial_cost']
    df_filtered[scaled_columns] = scaler.fit_transform(df_filtered[scaled_columns])

    # 가중치 설정
    weight_map = {
        '매우 그렇다': 0.5,
        '그렇다': 0.4,
        '보통': 0.3,
        '아니다': 0.2,
        '매우 아니다': 0.1
    }

    # 사용자 입력에 따른 가중치 적용
    weights = {
        'franchise_fee': weight_map[user_data['franchise_fee_concern']],
        'trending': weight_map[user_data['trending_industry_preference']],
        'sales': weight_map[user_data['sales_importance']],
        'closure_rate': weight_map[user_data['closure_rate_concern']],
    }

    # 개업률(opening_rate)은 높을수록 좋으므로 가중치를 더합니다.
    df_filtered['opening_rate'] += weights['trending']
    
    # 폐업률(closure_rate)은 낮을수록 좋으므로 1에서 폐업률을 빼고 가중치를 더해줍니다.
    df_filtered['closure_rate'] = (1 - df_filtered['closure_rate']) * weights['closure_rate']
    
    # 평균 매출액(average_sales_per_area)은 높을수록 좋으므로 가중치를 더합니다.
    df_filtered['average_sales_per_area'] += weights['sales']
    
    # 초기 비용(initial_cost)은 낮을수록 좋으므로, 1에서 초기비용을 빼고 가중치를 더해줍니다.
    df_filtered['initial_cost'] = (1 - df_filtered['initial_cost']) * weights['franchise_fee']

    # 스케일링된 X 값 출력 (디버깅용)
    print("\n=== X values (scaled independent variables) ===")
    print(df_filtered[['opening_rate', 'closure_rate', 'average_sales_per_area', 'initial_cost']].head())

    # 독립 변수(X)와 종속 변수(y) 설정
    X = df_filtered[['opening_rate', 'closure_rate', 'average_sales_per_area', 'initial_cost']]

    # 가중치가 가장 높은 변수에 따라 y 변수를 설정
    max_weight = max(weights, key=weights.get)  # 가중치가 가장 큰 변수 확인

    # 가중치가 가장 큰 변수를 종속 변수(y)로 설정
    if max_weight == 'trending':
        y = df_filtered['opening_rate']  # 개업률
    elif max_weight == 'closure_rate':
        y = df_filtered['closure_rate']  # 폐업률
    elif max_weight == 'sales':
        y = df_filtered['average_sales_per_area']  # 매출액
    elif max_weight == 'franchise_fee':
        y = df_filtered['initial_cost']  # 초기비용

    print(f"종속 변수 y는 '{max_weight}'로 선택되었습니다.")

    # 랜덤포레스트 모델 학습
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    rf = RandomForestRegressor()
    rf.fit(X_train, y_train)

    # 예측 점수 계산
    df_filtered['predicted_score'] = rf.predict(X)

    # 점수를 100점 만점으로 정규화
    max_score = df_filtered['predicted_score'].max()
    df_filtered['normalized_score'] = (df_filtered['predicted_score'] / max_score) * 100

    # 원래 값을 그대로 사용하여 출력 (original_values에 저장된 값)
    df_filtered['average_sales'] = original_values['average_sales'] / 10  # 만원 단위로 복원
    df_filtered['average_sales_per_area'] = original_values['average_sales_per_area'] / 10  # 만원 단위로 복원
    df_filtered['initial_cost'] = original_values['initial_cost'] / 10  # 만원 단위로 복원
    df_filtered['business_fee'] = original_values['business_fee'] / 10  # 만원 단위로 복원
    df_filtered['interior_cost'] = original_values['interior_cost'] / 10  # 만원 단위로 복원
    df_filtered['closure_rate'] = original_values['closure_rate'] / 100  # 폐업률 원래 값 복원
    df_filtered['opening_rate'] = original_values['opening_rate'] / 100  # 개업률 원래 값 복원

    # 상위 30개의 데이터 선택
    top_franchises = df_filtered.sort_values(by='normalized_score', ascending=False).head(30)

    # 결과 출력
    for idx, row in enumerate(top_franchises.itertuples(index=False), 1):
        print(f"{idx}. {row.store_name}, 폐업률: {row.closure_rate * 100:.2f}%, 개업률: {row.opening_rate * 100:.2f}%, "
              f"1년 평균 매출액: {row.average_sales:.2f} 만원, 1평당 매출액: {row.average_sales_per_area:.2f} 만원, "
              f"가맹비: {row.initial_cost:.2f} 만원, 가맹 보험비: {row.business_fee:.2f} 만원, 인테리어 비용: {row.interior_cost:.2f} 만원, "
              f"표준 스토어 면적: {row.standard_store_area} ㎡, 점수: {row.normalized_score:.2f}")

    # JSON 파일 저장
    results = []
    for idx, row in enumerate(top_franchises.itertuples(index=False)):
        results.append({
            "rank": idx + 1,
            "store_name": row.store_name,
            "year": row.year,
            "region": row.region,
            "opening_rate": f"{row.opening_rate * 100:.2f}%",
            "closure_rate": f"{row.closure_rate * 100:.2f}%",
            "average_sales": f"{row.average_sales:.2f} 만원",
            "average_sales_per_area": f"{row.average_sales_per_area:.2f} 만원",
            "initial_cost": f"{row.initial_cost:.2f} 만원",
            "business_fee": f"{row.business_fee:.2f} 만원",
            "interior_cost": f"{row.interior_cost:.2f} 만원",
            "standard_store_area": f"{row.standard_store_area} ㎡",
            "score": f"{row.normalized_score:.2f}"
        })

    output_folder = os.path.join('..', 'franchise_rank', 'preprocessing_stage2')
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    json_file_name = f"{category}_1franchise_ranking.json"
    json_file_path = os.path.join(output_folder, json_file_name)
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(results, json_file, ensure_ascii=False, indent=4)

    print(f"Data saved to '{json_file_path}'")

    # JSON 형식으로 저장할 데이터 구성
    results = []
    for idx, row in enumerate(top_franchises.itertuples(index=False)):
        results.append({
            "rank": idx + 1,
            "store_name": row.store_name,
            "year": row.year,
            "region": row.region,
            "opening_rate": f"{row.opening_rate * 100:.2f}%",
            "closure_rate": f"{row.closure_rate * 100:.2f}%",
            "average_sales": f"{row.average_sales:.2f} 만원",
            "average_sales_per_area": f"{row.average_sales_per_area:.2f} 만원",
            "initial_cost": f"{row.initial_cost:.2f} 만원",
            "business_fee": f"{row.business_fee:.2f} 만원",
            "interior_cost": f"{row.interior_cost:.2f} 만원",
            "standard_store_area": f"{row.standard_store_area} ㎡",
            "score": f"{row.normalized_score:.2f}"
        })

    # JSON 파일 경로 설정
    output_folder = os.path.join('..', 'franchise_rank', 'preprocessing_stage2')
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    json_file_name = f"{category}_1franchise_ranking.json"
    json_file_path = os.path.join(output_folder, json_file_name)
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(results, json_file, ensure_ascii=False, indent=4)

    print(f"Data saved to '{json_file_path}'")


if __name__ == "__main__":

    # 0. 사용자 입력에 따른 CSV 파일 처리 (프랜차이즈 랭킹 매기기)
    csv_file_path = os.path.join('..', 'franchise_rank', 'preprocessing_stage1', f'{industry_category}_franchise_data_with_trend_10plus.csv')
    
    if os.path.exists(csv_file_path):
        print(f"{industry_category} 업종에 해당하는 데이터를 성공적으로 불러왔습니다.")
        
        # CSV 파일 처리 (df_filtered 반환)
        df_filtered = pd.read_csv(csv_file_path)

        # 이후에 랜덤포레스트 모델 학습 및 예측 -> top_franchises 저장
        top_franchises = process_csv_file(df_filtered, industry_category)
    else:
        print(f"{csv_file_path} 파일을 찾을 수 없습니다.")
        exit()
