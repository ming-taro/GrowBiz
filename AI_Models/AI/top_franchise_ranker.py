import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import json
import os

def process_csv_file(file_name, category):
    # CSV 파일 불러오기
    df = pd.read_csv(file_name)

    # 필요한 열 선택 (standard_store_area 추가)
    columns = ['store_name', 'year', 'region', 'opening_rate', 'closure_rate', 'average_sales', 'average_sales_per_area', 
               'initial_cost', 'business_fee', 'interior_cost', 'standard_store_area']

    df_filtered = df[columns].copy()  # 슬라이스된 데이터 복사를 명시적으로 수행

    # 개업률과 폐업률을 백분율로 변환 (100으로 나누기)
    df_filtered['opening_rate'] = df_filtered['opening_rate'] / 100
    df_filtered['closure_rate'] = df_filtered['closure_rate'] / 100

    # 개업률이 폐업률 대비 1.5배 이상인 데이터만 필터링
    df_filtered = df_filtered[(df_filtered['opening_rate'] >= df_filtered['closure_rate'] * 1.5) & 
                              (df_filtered['closure_rate'] <= 31.4 / 100)]  # 폐업률 31.4% 이하

    # 필터링 후 데이터가 1개 이하일 경우 처리
    if len(df_filtered) < 10:
        print(f"Warning: 필터링 후 {len(df_filtered)}개의 데이터만 남았습니다.")
        if len(df_filtered) <= 1:
            print(f"데이터가 너무 적어서 모델을 학습할 수 없습니다. 데이터 수: {len(df_filtered)}")
            return

    # 폐업률이 낮을수록 좋으므로 음수로 변환
    df_filtered['adjusted_closure_rate'] = -df_filtered['closure_rate']

    # 독립 변수(X)와 종속 변수(y) 설정
    X = df_filtered[['opening_rate', 'adjusted_closure_rate', 'average_sales_per_area', 'initial_cost', 'business_fee', 'standard_store_area']]
    y = df_filtered['average_sales_per_area']

    # 랜덤포레스트 모델 학습
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    rf = RandomForestRegressor()
    rf.fit(X_train, y_train)

    # 예측 점수 계산
    df_filtered['predicted_score'] = rf.predict(X)

    # 점수를 100점 만점으로 정규화
    max_score = df_filtered['predicted_score'].max()
    df_filtered['normalized_score'] = (df_filtered['predicted_score'] / max_score) * 100

    # 금액 관련 데이터를 원래 값으로 돌린 후, 천원 단위에서 만원 단위로 변환
    df_filtered['average_sales'] = df_filtered['average_sales'] / 10  # 만원 단위로 변환
    df_filtered['average_sales_per_area'] = df_filtered['average_sales_per_area'] / 10  # 만원 단위로 변환
    df_filtered['initial_cost'] = df_filtered['initial_cost'] / 10  # 만원 단위로 변환
    df_filtered['business_fee'] = df_filtered['business_fee'] / 10  # 만원 단위로 변환
    df_filtered['interior_cost'] = df_filtered['interior_cost'] / 10  # 만원 단위로 변환

    # 상위 30개의 데이터 선택 (필터링 결과가 30개 미만이면, 나오는 개수만큼 출력)
    top_franchises = df_filtered.sort_values(by='normalized_score', ascending=False).head(30)

    # 순서 번호를 다시 매긴 데이터 출력 (standard_store_area 포함)
    for idx, row in enumerate(top_franchises.itertuples(index=False), 1):
        print(f"{idx}. {row.store_name}, 폐업률: {row.closure_rate * 100:.2f}%, 개업률: {row.opening_rate * 100:.2f}%, "
              f"1년 평균 매출액: {row.average_sales:.2f} 만원, 1평당 매출액: {row.average_sales_per_area:.2f} 만원, "
              f"초기비용: {row.initial_cost:.2f} 만원, 가맹비: {row.business_fee:.2f} 만원, 인테리어 비용: {row.interior_cost:.2f} 만원, "
              f"표준 스토어 면적: {row.standard_store_area} ㎡, 점수: {row.normalized_score:.2f}")

    # JSON 형식으로 저장할 데이터 구성 (standard_store_area 포함)
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

    # JSON 파일 경로
    output_folder = os.path.join('..', 'franchise_rank', 'preprocessing_stage2')
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    json_file_name = f"{category}_franchise_ranking.json"
    json_file_path = os.path.join(output_folder, json_file_name)
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(results, json_file, ensure_ascii=False, indent=4)

    print(f"Data saved to '{json_file_path}'")


if __name__ == "__main__":
    # preprocessing_stage1 폴더 내의 모든 CSV 파일에 대해 처리
    folder_path = os.path.join('..', 'franchise_rank', 'preprocessing_stage1')
    
    # 모든 CSV 파일을 찾고 처리
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".csv"):
            # 파일 이름에서 카테고리 추출 (예: '치킨_franchise_data_with_trend_10plus.csv'에서 '치킨' 추출)
            category = file_name.split('_')[0]
            file_path = os.path.join(folder_path, file_name)
            print(f"Processing file: {file_name}, Category: {category}")
            process_csv_file(file_path, category)
