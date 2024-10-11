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

# MySQL DB 연결
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

# MySQL에서 구/동에 대한 면적 정보 가져오기 (동 이름으로 시작하는 모든 동의 면적 합산)
def get_total_area_from_db(gu, dong_prefix):
    connection = connect_to_db()
    try:
        with connection.cursor() as cursor:
            # dong_name이 dong_prefix로 시작하는 모든 동의 면적 합산
            query = """
            SELECT SUM(area) as total_area
            FROM all_district
            WHERE gu_name = %s AND dong_name LIKE %s
            """
            cursor.execute(query, (gu, dong_prefix + '%'))
            result = cursor.fetchone()
            return result['total_area'] if result['total_area'] else 0  # 면적 정보가 없으면 0 반환
    finally:
        connection.close()

# 해당 구에서 dong_prefix로 시작하는 모든 동 이름 가져오기
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

# 카카오 맵 API로 가게 검색 (동 리스트를 받아서 각 동별로 검색 후 합산)
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
    
    return total_places  # 모든 동에서 검색된 가게 리스트 반환

# 브랜드 별로 검색 후 밀도 구하기
def search_brand_in_region(gu, dong_prefix):
    # 브랜드 데이터를 json 파일에서 가져오기
    franchise_data = load_franchise_data()

    # 해당 구에서 dong_prefix로 시작하는 모든 동 이름 가져오기
    dong_list = get_dong_names_from_db(gu, dong_prefix)

    if not dong_list:
        print(f"{gu}에 '{dong_prefix}'로 시작하는 동을 찾을 수 없습니다.")
        return

    # 해당 동들의 총 면적 구하기
    total_area = get_total_area_from_db(gu, dong_prefix)

    if total_area == 0:
        print(f"{gu} {dong_prefix}에 대한 면적 정보를 찾을 수 없습니다.")
        return

    print(f"{gu}의 '{dong_prefix}'로 시작하는 동 목록: {dong_list}")
    print(f"총 면적은 {total_area} km² 입니다.\n")

    for store in franchise_data:
        store_name = store['store_name']
        print(f"\n{store_name} 검색 중...")

        # 카카오 API를 사용해서 해당 브랜드가 몇 개 있는지 확인
        places = search_store_kakao(gu, dong_list, store_name)
        store_count = len(places)
        if store_count > 0:
            density = store_count / total_area  # 밀도 계산
            print(f"{store_name}가 {gu}의 '{dong_prefix}'로 시작하는 동들에 {store_count}개 있습니다. 밀도: {density:.2f} 가게/km²")
        else:
            print(f"{store_name}가 {gu}의 '{dong_prefix}'로 시작하는 동들에 없습니다.")

# 메인 실행 함수
if __name__ == "__main__":
    # 하드코딩된 구, 동 설정
    gu = "강남구"
    dong_prefix = "역삼"  # 또는 "역삼"

    # 치킨 브랜드 검색
    search_brand_in_region(gu, dong_prefix)
