import os
import requests
from dotenv import load_dotenv

load_dotenv()
KAKAO_API_KEY = os.getenv("KAKAO_API_KEY")
KAKAO_STORE_SEARCH_QUERY = "https://dapi.kakao.com/v2/local/search/keyword.json?query="


# 카카오 맵 API로 가게 검색
def count_store_by_location_with_kakao(gu, dong_list, store_name):
    headers = {"Authorization": f"KakaoAK {KAKAO_API_KEY}"}
    count = 0
    api_status = True

    for dong in dong_list:
        query = f"{gu} {dong} {store_name}"
        url = f"{KAKAO_STORE_SEARCH_QUERY}{query}"

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()

            places = response.json().get('documents', [])
            count += len(places)
        except requests.exceptions.HTTPError as http_err:
            print(f"[Kakao Search API] HTTPError {http_err}")
            api_status = False
        except requests.exceptions.RequestException as err:
            print(f"[Kakao Search API] RequestException {err}")
            api_status = False

    return count, api_status
