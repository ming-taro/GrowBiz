import json
import requests
import os
import pymysql
from dotenv import load_dotenv
import numpy as np
from sklearn.ensemble import RandomForestRegressor

# .env 파일에서 API 키 및 DB 정보 불러오기
load_dotenv()

KAKAO_API_KEY = os.getenv("KAKAO_API_KEY")
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

# 사용자 입력 데이터
user_data = {
    'region': '서울시, 강남구, 역삼동',
    'monthly_rent': 300,  # 만원
    'deposit': 10000,  # 만원 (1억)
    'industry': '외식업, 치킨',
    'initial_capital': 10000,  # 만원 (2억)
    'preference': '프랜차이즈',
    'trending_industry': '아니오',
    'cost_burden': '중간',
    'stability_concern': '중간',
    'franchise_fee_burden': '중간'
}

# 사용자 입력에서 구와 동을 추출 (동을 '역삼'처럼 변환)
gu = user_data['region'].split(', ')[1]  # '강남구'
dong_prefix = user_data['region'].split(', ')[2][:2]  # '역삼'

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
                addr                   -- 주소
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

# 치킨 프랜차이즈 데이터를 json 파일에서 읽기
def load_franchise_data():
    with open('치킨_franchise_ranking.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

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
    franchise_data = load_franchise_data()
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
def filter_franchises_by_cost(franchise_data, property_listings, initial_capital):
    filtered_franchises = []
    
    for store in franchise_data:
        initial_cost = float(store['initial_cost'].replace('만원', '').replace(',', ''))  # 초기 비용 변환
        for listing in property_listings:
            deposit = listing['bsc_tnth_wunt_amt']  # 매물의 보증금
            
            # 조건: 초기 비용 + 보증금 <= 사용자가 입력한 자본금
            if initial_cost + deposit <= initial_capital:
                filtered_franchises.append(store)
    
    return filtered_franchises

# 밀도 계산 후 평균과 표준편차를 구해 가산/감점 적용
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

def recommend_top_3_franchises(final_scores):
    # final_scores는 (store_name, final_score) 형식의 리스트
    # 데이터를 학습시키기 위해 (score, 밀도) 형식으로 변환
    store_names = [store[0] for store in final_scores]
    scores = [store[1] for store in final_scores]
    
    # RandomForest 모델을 사용해 상위 3개의 점수를 가진 프랜차이즈 추천
    model = RandomForestRegressor(n_estimators=100)
    
    # 임시로 X, y를 동일하게 설정 (RandomForest 학습을 위한 형태)
    X = np.array(scores).reshape(-1, 1)
    y = np.array(scores)
    
    model.fit(X, y)
    
    # 예측을 위해 학습된 결과를 다시 활용
    predictions = model.predict(X)
    
    # 상위 3개 프랜차이즈 선택
    top_3_indices = np.argsort(predictions)[-3:]  # 점수가 높은 상위 3개 선택
    top_3_franchises = [(store_names[i], predictions[i]) for i in top_3_indices]
    
    return sorted(top_3_franchises, key=lambda x: x[1], reverse=True)


# 메인 실행 함수
if __name__ == "__main__":
    # 1. 매물 리스트 가져오기
    property_listings = get_property_listings()
    print("\n=== 매물 리스트 (plno) ===")
    for listing in property_listings:
        print(f"매물 ID: {listing['plno']}, 월세: {listing['add_tnth_wunt_amt']}만원, 보증금: {listing['bsc_tnth_wunt_amt']}만원, 주소: {listing['addr']}")

    # 2. 프랜차이즈 브랜드 검색 및 밀도 계산
    densities = search_brand_in_region()  # 밀도 계산 후 지역별 밀도 리스트 반환

    if densities:
        # 3. 밀도의 평균과 표준편차 계산
        adjusted_density_scores, mean_density, std_density = adjust_density_scores(densities)
        print(f"밀도 평균: {mean_density}, 표준편차: {std_density}")

        # 4. 기존 랭킹 데이터 로드
        franchise_data = load_franchise_data()  # 기존 랭킹 데이터를 JSON에서 로드
        
        # 5. 초기 자본금 조건을 만족하는 프랜차이즈 필터링
        filtered_franchises = filter_franchises_by_cost(franchise_data, property_listings, user_data['initial_capital'])
        
        # 6. 필터링된 프랜차이즈의 최종 점수 계산
        final_scores = calculate_final_scores(filtered_franchises, adjusted_density_scores)
        
        # 7. 상위 3개 프랜차이즈 추천
        top_3_franchises = recommend_top_3_franchises(final_scores)
        print("\n=== 추천 프랜차이즈 상위 3개 ===")
        for franchise, score in top_3_franchises:
            print(f"{franchise} - 최종 점수: {score:.2f}")