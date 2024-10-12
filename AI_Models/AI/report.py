import json
import requests
import os
import pymysql
from dotenv import load_dotenv

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
        return

    total_area = get_total_area_from_db(gu, dong_prefix)

    if total_area == 0:
        print(f"{gu} {dong_prefix}에 대한 면적 정보를 찾을 수 없습니다.")
        return

    print(f"{gu}의 '{dong_prefix}'로 시작하는 동 목록: {dong_list}")
    print(f"총 면적은 {total_area} km² 입니다.\n")

    for store in franchise_data:
        store_name = store['store_name']
        places = search_store_kakao(gu, dong_list, store_name)
        store_count = len(places)
        if store_count > 0:
            density = store_count / total_area  # 밀도 계산
            print(f"{store_name}가 {gu}의 '{dong_prefix}'로 시작하는 동들에 {store_count}개 있습니다. 밀도: {density:.2f} 가게/km²")
        else:
            print(f"{store_name}가 {gu}의 '{dong_prefix}'로 시작하는 동들에 없습니다.")

# 메인 실행 함수
if __name__ == "__main__":
    # 1. 매물 리스트 가져오기
    property_listings = get_property_listings()
    print("\n=== 매물 리스트 (plno) ===")
    for listing in property_listings:
        print(f"매물 ID: {listing['plno']}, 월세: {listing['add_tnth_wunt_amt']}만원, 보증금: {listing['bsc_tnth_wunt_amt']}만원, 주소: {listing['addr']}")

    # 2. 프랜차이즈 브랜드 검색 및 밀도 계산
    search_brand_in_region()
