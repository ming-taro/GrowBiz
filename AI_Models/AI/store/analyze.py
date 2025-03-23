import tempfile
import os
import json
import numpy as np

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MinMaxScaler

from .property import get_dong_names_from_db, get_total_area_from_db
from .store import count_store_by_location_with_kakao


def process_csv_file(df_filtered, category, user_data):
    # 필요한 열 선택
    columns = ['store_name', 'year', 'region', 'opening_rate', 'closure_rate', 'average_sales',
               'average_sales_per_area',
               'initial_cost', 'business_fee', 'interior_cost', 'standard_store_area']

    df_filtered = df_filtered[columns].copy()

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
    # print("\n=== X values (scaled independent variables) ===")
    # print(df_filtered[['opening_rate', 'closure_rate', 'average_sales_per_area', 'initial_cost']].head())

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

    # 여기에 상위 30개의 브랜드에서 폐업률 평균이랑, 개업률 평균치 , 평균 매출액,initial_cost의 평균 인테리어 평균 도 가져와줘.
    # 상위 30개의 브랜드에서 평균값 계산
    avg_closure_rate = top_franchises['closure_rate'].mean()
    avg_opening_rate = top_franchises['opening_rate'].mean()
    avg_average_sales = top_franchises['average_sales'].mean()
    avg_initial_cost = top_franchises['initial_cost'].mean()
    avg_interior_cost = top_franchises['interior_cost'].mean()

    # 상위 30개 브랜드 정보 출력
    # print("\n=== 상위 30개의 브랜드 평균 ===")
    # print(f"폐업률 평균: {avg_closure_rate * 100:.2f}%")
    # print(f"개업률 평균: {avg_opening_rate * 100:.2f}%")
    # print(f"평균 매출액: {avg_average_sales:.2f} 만원")
    # print(f"초기 비용 평균: {avg_initial_cost:.2f} 만원")
    # print(f"인테리어 비용 평균: {avg_interior_cost:.2f} 만원")

    # 결과 출력
    # for idx, row in enumerate(top_franchises.itertuples(index=False), 1):
    #     print(f"{idx}. {row.store_name}, 폐업률: {row.closure_rate * 100:.2f}%, 개업률: {row.opening_rate * 100:.2f}%, "
    #           f"1년 평균 매출액: {row.average_sales:.2f} 만원, 1평당 매출액: {row.average_sales_per_area:.2f} 만원, "
    #           f"가맹비: {row.initial_cost:.2f} 만원, 가맹 보험비: {row.business_fee:.2f} 만원, 인테리어 비용: {row.interior_cost:.2f} 만원, "
    #           f"표준 스토어 면적: {row.standard_store_area} ㎡, 점수: {row.normalized_score:.2f}")

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
    # json_file_name = f"{response_id}_1franchise_ranking.json"
    # json_file_path = os.path.join(output_folder, json_file_name)
    print("파일 경로 = " + output_folder)

    with tempfile.NamedTemporaryFile(
            delete=False,
            suffix='.json',
            mode='w',
            encoding='utf-8',
            dir=output_folder) as json_file:
        json.dump(results, json_file, ensure_ascii=False, indent=4)
        industry_1franchise_ranking_file_path = json_file.name

    print(f"Data saved to '{output_folder}'")
    return industry_1franchise_ranking_file_path


# 보증금과 초기 자본금 조건을 만족하는지 확인하는 함수
def filter_franchises_by_cost(initial_capital, industry_1franchise_ranking_file_path, response_id):
    franchise_data = load_franchise_data(industry_1franchise_ranking_file_path, response_id)  # JSON 파일에서 프랜차이즈 데이터 가져오기
    filtered_franchises = []
    excluded_franchises = []

    for store in franchise_data:
        initial_cost = float(store['initial_cost'].replace('만원', '').replace(',', ''))  # 초기 비용 변환
        business_fee = float(store['business_fee'].replace('만원', '').replace(',', ''))  # 가맹비 변환
        interior_cost = float(store['interior_cost'].replace('만원', '').replace(',', ''))  # 인테리어 비용 변환

        # 조건: 초기 비용 + 가맹비 + 인테리어 비용 <= 사용자가 입력한 자본금
        total_initial_cost = initial_cost + business_fee + interior_cost

        if total_initial_cost <= initial_capital:
            filtered_franchises.append(store)  # 조건 만족
        else:
            excluded_franchises.append(store)  # 조건 불만족 (제외됨)

    return filtered_franchises, excluded_franchises


# 밀도 계산 후 조정하는 함수
def adjust_density_scores(densities):
    mean_density = np.mean(densities)
    std_density = np.std(densities)

    adjusted_scores = []
    for density in densities:
        if density < mean_density:
            # 평균보다 밀도가 작으면 가산점
            score_adjustment = 1 + (mean_density - density) / std_density
        else:
            # 평균보다 크면 감점
            score_adjustment = 1 - (density - mean_density) / std_density

        adjusted_scores.append(score_adjustment)

    return adjusted_scores, mean_density, std_density


# 밀도 점수와 기존 랭킹 점수를 결합하여 최종 점수를 계산
def calculate_final_scores(franchise_data, adjusted_density_scores):
    final_scores = []
    for i, store in enumerate(franchise_data):
        rank_score = float(store['score'])  # 기존 랭킹 점수
        density_score = adjusted_density_scores[i] * 5  # 밀도 점수 (5점 만점)

        # 기존 랭킹 점수와 밀도 점수의 가중치를 5:5로 반영
        final_score = ((rank_score * 7 + density_score * 3) / 10) + (20)
        final_scores.append((store['store_name'], final_score))

    return final_scores


# 치킨 프랜차이즈 데이터를 json 파일에서 읽기
def load_franchise_data(industry_1franchise_ranking_file_path, response_id):
    # 산업 카테고리에 맞는 JSON 파일을 불러옴
    if os.path.exists(industry_1franchise_ranking_file_path):
        with open(industry_1franchise_ranking_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    else:
        print(f"{response_id}_1franchise_ranking.json 파일을 찾을 수 없습니다.")
        return []


# 브랜드 별로 검색 후 밀도 구하기
def search_brand_in_region(gu, dong_prefix, industry_1franchise_ranking_file_path, response_id):
    franchise_data = load_franchise_data(industry_1franchise_ranking_file_path, response_id)  # 산업 카테고리에 맞는 데이터 불러오기
    dong_list = get_dong_names_from_db(gu, dong_prefix)

    if not dong_list:
        print(f"{gu}에 '{dong_prefix}'로 시작하는 동을 찾을 수 없습니다.")
        return []

    total_area = get_total_area_from_db(gu, dong_prefix)

    if total_area == 0:
        print(f"{gu} {dong_prefix}에 대한 면적 정보를 찾을 수 없습니다.")
        return []

    # 창업 지역 정보 출력
    # print(f"{gu}의 '{dong_prefix}'로 시작하는 동 목록: {dong_list}")
    # print(f"총 면적은 {total_area} km² 입니다.\n")

    densities = []  # 밀도 리스트를 저장할 배열

    for store in franchise_data:
        store_name = store['store_name']
        store_count, api_status = count_store_by_location_with_kakao(gu, dong_list, store_name)
        if store_count > 0:
            density = store_count / total_area  # 밀도 계산
            densities.append(density)  # 밀도를 리스트에 저장
            # 밀도 정보 출력
            # print(f"{store_name}가 {gu}의 '{dong_prefix}'로 시작하는 동들에 {store_count}개 있습니다. 밀도: {density:.2f} 가게/km²")
        else:
            densities.append(0)  # 밀도가 없을 경우 0으로 처리
            # print(f"{store_name}가 {gu}의 '{dong_prefix}'로 시작하는 동들에 없습니다.")

    return densities  # 계산된 밀도 리스트 반환