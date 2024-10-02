import requests
from dotenv import load_dotenv
import os

load_dotenv()
OPEN_DATA_API_KEY = os.environ.get('OPENAI_API_KEY')

BRAND_INFO_URL = "http://apis.data.go.kr/1130000/FftcBrandRlsInfo2_Service/getBrandinfo"

result = set()

# 브랜드 정보
def find_brand_info(year):
    brand_info_params = {
        "serviceKey": OPEN_DATA_API_KEY,
        "pageNo": 1,
        "numOfRows": 10000,
        "resultType": "json",
        "jngBizCrtraYr": year
    }
    try:
        response = requests.get(BRAND_INFO_URL, params=brand_info_params)
        response.raise_for_status()

        data = response.json()
        items = data["items"]

        for item in items:
            # print(item['indutyMlsfcNm'])
            result.add(item['indutyMlsfcNm'])  # 산업 중분류 이름
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


def main():
    for i in range(10):
        find_brand_info(2024 - i)
    i = 0
    for item in result:
        print(i, ".", item)
        i += 1


if __name__ == "__main__":
    main()