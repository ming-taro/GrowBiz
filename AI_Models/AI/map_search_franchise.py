import json
import requests
import os
from dotenv import load_dotenv

# .env 파일에서 API 키 불러오기
load_dotenv()

KAKAO_API_KEY = os.getenv("KAKAO_API_KEY")

# 치킨 프랜차이즈 데이터를 json 파일에서 읽기
def load_franchise_data():
    with open('치킨_franchise_ranking.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

# 카카오 맵 API로 가게 검색
def search_store_kakao(gu, dong, store_name):
    headers = {"Authorization": f"KakaoAK {KAKAO_API_KEY}"}
    query = f"{gu} {dong} {store_name}"
    url = f"https://dapi.kakao.com/v2/local/search/keyword.json?query={query}"
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        places = response.json().get('documents', [])
        return places  # 검색된 가게 리스트 반환
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

# 브랜드 별로 검색 후 밀도 구하기
def search_brand_in_region(gu, dong, sub_category):
    # 브랜드 데이터를 json 파일에서 가져오기
    franchise_data = load_franchise_data()

    for store in franchise_data:
        if store['sub_category'] == sub_category:
            store_name = store['store_name']
            print(f"\n{store_name} 검색 중...")

            # 카카오 API를 사용해서 해당 브랜드가 몇 개 있는지 확인
            places = search_store_kakao(gu, dong, store_name)
            if places:
                store_count = len(places)
                print(f"{store_name}가 {gu} {dong}에 {store_count}개 있습니다.")
            else:
                print(f"{store_name}가 {gu} {dong}에 없습니다.")

# 메인 실행 함수
if __name__ == "__main__":
    # 하드코딩된 구, 동, 서브 카테고리 설정
    gu = "강남구"
    dong = "역삼동"
    sub_category = "치킨"

    # 치킨 브랜드 검색
    search_brand_in_region(gu, dong, sub_category)
