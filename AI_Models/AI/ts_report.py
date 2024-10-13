import json
import os
import requests
import pymysql
from dotenv import load_dotenv
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

# .env 파일에서 API 키 및 DB 정보 불러오기
load_dotenv()

KAKAO_API_KEY = os.getenv("KAKAO_API_KEY")
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

# 1. 지역을 선택해주세요.    
# 2. 점포 임대 계약 시 수용 가능한 월세    
# 3. 점포 임대 계약 시 수용 가능한 보증금
# 4. 업종 중 분류, 대분류 선택
# 5. 보증금을 포함하여, 자본금은 어느 정도 가지고 계신가요?
# 6. 개인창업과 프랜차이즈 중 어느 것을 선호하시나요?
# 7. 가맹비를 크게 신경쓰고 계신가요?     7부터 매우그렇다, 그렇다, 보통, 아니다, 매우 아니다
# 8. 현재 유행 중인 업종을 원하십니까?
# 9. 매출액이 얼마나 중요하신가요?
# 10. 폐업률을 신경 쓰시나요?
# 11. 근처에 같은 브랜드 매장과 경쟁 할 자신 있으신가요?
# 사용자 입력 데이터

user_data = {
    'region': '서울시, 강남구, 역삼동',
    'monthly_rent': 300,  # 만원
    'deposit': 10000,  # 만원 (1억)
    'industry': '외식업, 커피',  # '치킨', '커피' 등 선택
    'initial_capital': 20000,  # 만원 (1억)
    'preference': '프랜차이즈',
    'franchise_fee_concern': '매우 아니다', #7 가맹비
    'trending_industry_preference': '보통', #8 유행업종
    'sales_importance': '보통', #9 매출액
    'closure_rate_concern': '매우 그렇다', #10 폐업률
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


# 치킨 프랜차이즈 데이터를 json 파일에서 읽기
def load_franchise_data(industry):
    # 산업 카테고리에 맞는 JSON 파일을 불러옴
    json_file_path = os.path.join('..', 'franchise_rank', 'preprocessing_stage2', f'{industry}_1franchise_ranking.json')
    
    if os.path.exists(json_file_path):
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    else:
        print(f"{industry}_franchise_ranking.json 파일을 찾을 수 없습니다.")
        return []

# MySQL DB 연결 함수
def connect_to_db():
    connection = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

# DB에서 매물 데이터 가져오기
def get_property_listings():
    # 사용자 입력에서 주소 필터 생성 ('서울시, 강남구, 역삼동' -> '%서울시 강남구 역삼%')
    address_filter = f"%{gu} {dong_prefix}%"
    
    connection = connect_to_db()
    try:
        with connection.cursor() as cursor:
            query = f"""
            SELECT 
                plno,                  -- 매물 ID
                add_tnth_wunt_amt,      -- 월세
                bsc_tnth_wunt_amt,      -- 보증금
                addr,                  -- 주소
                area2
            FROM 
                KB.property_listing  -- 테이블 명
            WHERE 
                ctgry_cd1_nm = '상가점포'      -- 카테고리 1에서 '상가점포'만
                AND deal_kind_cd_nm = '월세'       -- 거래 유형이 '월세'
                AND addr LIKE %s                  -- 주소 필터 적용 (주소에서 강남구 역삼 포함)
                AND add_tnth_wunt_amt <= %s       -- 사용자 입력 월세 필터
                AND bsc_tnth_wunt_amt <= %s       -- 사용자 입력 보증금 필터
            ORDER BY 
                atcl_reg_dttm DESC;  -- 정렬
            """
            # 파라미터로 주소 필터, 월세, 보증금 전달
            cursor.execute(query, (address_filter, user_data['monthly_rent'], user_data['deposit']))
            results = cursor.fetchall()
            return results
    finally:
        connection.close()

# 동 이름과 면적 가져오기
def get_total_area_from_db(gu, dong_prefix):
    connection = connect_to_db()
    try:
        with connection.cursor() as cursor:
            query = """
            SELECT SUM(area) as total_area
            FROM all_district
            WHERE gu_name = %s AND dong_name LIKE %s
            """
            cursor.execute(query, (gu, dong_prefix + '%'))
            result = cursor.fetchone()
            return result['total_area'] if result['total_area'] else 0
    finally:
        connection.close()

# 동 리스트 가져오기
def get_dong_names_from_db(gu, dong_prefix):
    connection = connect_to_db()
    try:
        with connection.cursor() as cursor:
            query = """
            SELECT dong_name
            FROM all_district
            WHERE gu_name = %s AND dong_name LIKE %s
            """
            cursor.execute(query, (gu, dong_prefix + '%'))
            results = cursor.fetchall()
            return [row['dong_name'] for row in results]
    finally:
        connection.close()

# 카카오 맵 API로 가게 검색
def search_store_kakao(gu, dong_list, store_name):
    headers = {"Authorization": f"KakaoAK {KAKAO_API_KEY}"}
    total_places = []

    for dong in dong_list:
        query = f"{gu} {dong} {store_name}"
        url = f"https://dapi.kakao.com/v2/local/search/keyword.json?query={query}"
        
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            places = response.json().get('documents', [])
            total_places.extend(places)
        else:
            print(f"Error {response.status_code}: {response.text}")
    
    return total_places

# 브랜드 별로 검색 후 밀도 구하기
def search_brand_in_region():
    franchise_data = load_franchise_data(industry_category)  # 산업 카테고리에 맞는 데이터 불러오기
    dong_list = get_dong_names_from_db(gu, dong_prefix)

    if not dong_list:
        print(f"{gu}에 '{dong_prefix}'로 시작하는 동을 찾을 수 없습니다.")
        return []

    total_area = get_total_area_from_db(gu, dong_prefix)

    if total_area == 0:
        print(f"{gu} {dong_prefix}에 대한 면적 정보를 찾을 수 없습니다.")
        return []

    print(f"{gu}의 '{dong_prefix}'로 시작하는 동 목록: {dong_list}")
    print(f"총 면적은 {total_area} km² 입니다.\n")

    densities = []  # 밀도 리스트를 저장할 배열

    for store in franchise_data:
        store_name = store['store_name']
        places = search_store_kakao(gu, dong_list, store_name)
        store_count = len(places)
        if store_count > 0:
            density = store_count / total_area  # 밀도 계산
            densities.append(density)  # 밀도를 리스트에 저장
            print(f"{store_name}가 {gu}의 '{dong_prefix}'로 시작하는 동들에 {store_count}개 있습니다. 밀도: {density:.2f} 가게/km²")
        else:
            densities.append(0)  # 밀도가 없을 경우 0으로 처리
            print(f"{store_name}가 {gu}의 '{dong_prefix}'로 시작하는 동들에 없습니다.")
    
    return densities  # 계산된 밀도 리스트 반환


# 보증금과 초기 자본금 조건을 만족하는지 확인하는 함수
def filter_franchises_by_cost(initial_capital):
    franchise_data = load_franchise_data(industry_category)  # JSON 파일에서 프랜차이즈 데이터 가져오기
    filtered_franchises = []
    excluded_franchises = []
    
    for store in franchise_data:
        initial_cost = float(store['initial_cost'].replace('만원', '').replace(',', ''))  # 초기 비용 변환
        business_fee = float(store['business_fee'].replace('만원', '').replace(',', ''))  # 가맹비 변환
        
        # 조건: 초기 비용 + 가맹비 <= 사용자가 입력한 자본금
        total_initial_cost = initial_cost + business_fee
        
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
        final_score = (rank_score * 5 + density_score * 5) / 10
        final_scores.append((store['store_name'], final_score))
    
    return final_scores

# 매물 면적과 프랜차이즈 평균 면적을 비교하여 추천할 수 있는 매물 필터링
def filter_listings_by_franchise_area(listings, franchise_data):
    valid_recommendations = []  # 프랜차이즈와 매물이 모두 추천 가능한 리스트
    
    for franchise in franchise_data:
        try:
            # 프랜차이즈의 표준 스토어 면적을 가져와서 '㎡'를 제거하고 숫자로 변환
            franchise_area_str = franchise.get('standard_store_area', '0').replace('㎡', '').replace(',', '').strip()
            franchise_area = float(franchise_area_str)  # 프랜차이즈 평균 면적 (제곱미터 단위)
        except ValueError:
            print(f"Error converting franchise area: {franchise_area_str}")
            continue
        
        # 매물과 프랜차이즈의 면적을 비교하여 추천 가능한 매물 필터링
        for listing in listings:
            if listing['area2'] >= franchise_area:  # 매물 면적이 프랜차이즈 요구 면적 이상인 경우
                valid_recommendations.append({
                    'franchise_name': franchise['store_name'],
                    'franchise_score': franchise['score'],
                    'property_id': listing['plno'],
                    'property_address': listing['addr'],
                    'property_rent': listing['add_tnth_wunt_amt'],
                    'property_deposit': listing['bsc_tnth_wunt_amt'],
                    'property_area': listing['area2']  # 매물 면적
                })
    
    return valid_recommendations

# 메인 실행 함수
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

    # 1. 매물 리스트 가져오기
    property_listings = get_property_listings()
    print("\n=== 매물 리스트 (plno) ===")
    for listing in property_listings:
        print(f"매물 ID: {listing['plno']}, 월세: {listing['add_tnth_wunt_amt']}만원, 보증금: {listing['bsc_tnth_wunt_amt']}만원, 주소: {listing['addr']}, 면적: {listing['area2']}평")

    # 2. 프랜차이즈 밀도 계산 후 밀도 리스트 얻기
    densities = search_brand_in_region()  # 밀도 계산 후 지역별 밀도 리스트 반환

    if densities:
        # 3. 밀도의 평균과 표준편차 계산 및 밀도 점수 조정
        adjusted_density_scores, mean_density, std_density = adjust_density_scores(densities)
        print(f"밀도 평균: {mean_density}, 표준편차: {std_density}")

        # 4. 초기 자본금 조건을 만족하는 프랜차이즈 필터링 (제외된 프랜차이즈 포함)
        filtered_franchises, excluded_franchises = filter_franchises_by_cost(user_data['initial_capital'])  
        
        # 5. 필터링된 프랜차이즈의 최종 점수 계산
        final_scores = calculate_final_scores(filtered_franchises, adjusted_density_scores)

        # 6. 상위 3개의 프랜차이즈 선택 (청년치킨 포함)
        top_franchises = sorted(final_scores, key=lambda x: x[1], reverse=True)[:3]  # 상위 3개의 프랜차이즈 선택
        print("\n=== 상위 3개 추천 프랜차이즈 ===")
        for franchise, score in top_franchises:
            print(f"{franchise} - 최종 점수: {score:.2f}")

            
        # 7. 제외된 프랜차이즈 3개를 출력
        print("\n=== 가맹비가 비싸서 제외된 프랜차이즈 3개 ===")
        excluded_franchises_sorted = sorted(
            excluded_franchises, 
            key=lambda x: (
                float(x['initial_cost'].replace('만원', '').replace(',', '').strip()), 
                float(x['business_fee'].replace('만원', '').replace(',', '').strip())
            )
        )[:3]
        for franchise in excluded_franchises_sorted:
            print(f"프랜차이즈: {franchise['store_name']}, 가맹비: {franchise['business_fee']}만원, 초기 비용: {franchise['initial_cost']}만원, 점수: {franchise['score']}")

        # 8. 추천된 프랜차이즈 중에서 매물 필터링 (청년치킨에 해당하는 매물만)
        top_franchise_name = top_franchises[0][0]  # 상위 1개의 프랜차이즈 이름 (청년치킨)
        valid_recommendations = filter_listings_by_franchise_area(property_listings, [store for store in filtered_franchises if store['store_name'] == top_franchise_name])

        # 9. 보증금과 월세가 적은 매물 3개 선택
        top_listings = sorted(valid_recommendations, key=lambda x: (x['property_deposit'], x['property_rent']))[:3]

        print("\n=== 추천 가능한 매물 (청년치킨에 해당하는 상위 3개) ===")
        if top_listings:
            for recommendation in top_listings:
                print(f"프랜차이즈: {recommendation['franchise_name']}, 점수: {recommendation['franchise_score']}")
                print(f"매물 ID: {recommendation['property_id']}, 주소: {recommendation['property_address']}, 월세: {recommendation['property_rent']}만원, 보증금: {recommendation['property_deposit']}만원, 면적: {recommendation['property_area']}평\n")
        else:
            print("조건에 맞는 추천 가능한 매물이 없습니다.")

