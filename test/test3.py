import asyncio
import aiohttp
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os
import json  # JSON 모듈 추가

# .env 파일에서 환경 변수 로드
load_dotenv()

# 환경 변수로부터 API 키 가져오기
business_api_key = os.getenv('BUSINESS_API_KEY')

# 서울시 상권 API 비동기 호출 함수
async def fetch_sangwon_data(session, api_key, start_index, end_index):
    url = f"http://openapi.seoul.go.kr:8088/{api_key}/xml/VwsmSignguStorW/{start_index}/{end_index}/"
    async with session.get(url) as response:
        if response.status == 200:
            return await response.text()
        else:
            print(f"Error: {response.status}")
            return None

# 강남구, 기준 년분기 코드 '20242'인 industry_name 추출
def extract_industry_names(sangwon_data):
    root = ET.fromstring(sangwon_data)
    industry_names = set()  # 중복 없이 저장하기 위한 set

    # XML 파싱 및 강남구, 기준 년분기 코드 '20242' 데이터 필터링
    for row in root.findall(".//row"):
        gu_name = row.find('SIGNGU_CD_NM').text
        industry_name = row.find('SVC_INDUTY_CD_NM').text
        year_quarter_code = row.find('STDR_YYQU_CD').text

        # 강남구, 기준 년분기 코드 '20242' 필터링
        if year_quarter_code == "20242":
            industry_names.add(industry_name)

    return list(industry_names)  # JSON으로 저장하기 위해 set을 list로 변환

# JSON 파일로 저장하는 함수
def save_to_json(data, filename="industry_names.json"):
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
    print(f"데이터가 {filename} 파일에 저장되었습니다.")

# 비동기적으로 서울시 상권 데이터를 호출하여 강남구에서 중복 없는 industry_name 출력
async def fetch_all_data(page_size):
    async with aiohttp.ClientSession() as session:
        # 서울시 상권 데이터 비동기 호출
        sangwon_data_task = fetch_sangwon_data(session, business_api_key, 1, page_size)
        sangwon_data = await sangwon_data_task  # 상권 데이터 가져오기
        print(f"1부터 {page_size}까지 데이터 요청 중...")

        # 강남구, 기준 년분기 코드 '20242'인 industry_name 추출
        industry_names = extract_industry_names(sangwon_data)

        # 결과 출력 (리스트 번호 매기기 및 총 개수 출력)
        print(f"강남구에서 기준 년분기 '20242'에 해당하는 업종 중분류 종류 총 {len(industry_names)}개:")
        for idx, name in enumerate(industry_names, 1):
            print(f"{idx}. {name}")

        # JSON 파일로 저장
        save_to_json(industry_names)

# 실행 코드
if __name__ == "__main__":
    page_size = 500  # 한 번에 가져올 데이터 수 (500개씩 요청)

    # 비동기 실행
    asyncio.run(fetch_all_data(page_size))
