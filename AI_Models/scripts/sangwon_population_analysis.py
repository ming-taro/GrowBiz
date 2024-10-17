import asyncio
import aiohttp
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

# .env 파일에서 환경 변수 로드
load_dotenv()

# 환경 변수로부터 API 키 가져오기
business_api_key = os.getenv('BUSINESS_API_KEY')
passenger_api_key = os.getenv('PASSENGER_API_KEY')
kakao_api_key = os.getenv('KAKAO_API_KEY')

# 사용자 데이터
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

# 서울시 상권 API 비동기 호출 함수
async def fetch_sangwon_data(session, api_key, start_index, end_index):
    url = f"http://openapi.seoul.go.kr:8088/{api_key}/xml/VwsmSignguStorW/{start_index}/{end_index}/"
    async with session.get(url) as response:
        if response.status == 200:
            return await response.text()
        else:
            print(f"Error: {response.status}")
            return None

# Kakao Map API 비동기 호출 함수
async def get_nearby_station(session, region, kakao_api_key):
    gu_name, dong_name = region.split(", ")[1:]  # 구와 동 정보 추출
    query = f"{gu_name} {dong_name} 근처역"
    url = f"https://dapi.kakao.com/v2/local/search/keyword.json?query={query}"
    headers = {"Authorization": f"KakaoAK {kakao_api_key}"}
    
    async with session.get(url, headers=headers) as response:
        if response.status == 200:
            data = await response.json()
            stations = []
            for place in data['documents']:
                station_name = place['place_name']
                if "역" in station_name:
                    station_name = station_name[:station_name.rfind("역")]  # '역' 바로 앞까지 가져옴
                    if station_name not in stations:  # 중복된 역 이름은 제외
                        stations.append(station_name)
            return stations  # 상위 3개 역이 아니라 전체 역을 반환
        elif response.status == 401:
            print(f"Error: {response.status} - Invalid API key or permissions.")
            return []
        else:
            print(f"Error: {response.status}")
            return []

# 서울시 승차 인원 API 비동기 호출 함수
async def fetch_passenger_data(session, api_key, station_name, use_ymd):
    url = f"http://openapi.seoul.go.kr:8088/{api_key}/xml/CardSubwayStatsNew/1/1000/{use_ymd}"
    async with session.get(url) as response:
        if response.status == 200:
            xml_data = await response.text()
            root = ET.fromstring(xml_data)
            total_boarding = 0
            total_alighting = 0
            
            for row in root.findall(".//row"):
                station = row.find('SBWY_STNS_NM').text
                if station_name == station:  # 역 이름이 완전히 일치할 때만 처리
                    boarding = int(row.find('GTON_TNOPE').text)
                    alighting = int(row.find('GTOFF_TNOPE').text)
                    total_boarding += boarding
                    total_alighting += alighting
            
            return total_boarding + total_alighting
        else:
            print(f"Error: {response.status}")
            return 0

# 날짜 -2일 설정 함수
def get_date_minus_days(days):
    target_date = datetime.now() - timedelta(days=days)
    return target_date.strftime("%Y%m%d")

# 비동기적으로 서울시 상권 데이터, 카카오 API, 승차 인원 API를 모두 호출하는 함수
async def fetch_all_data(page_size):
    async with aiohttp.ClientSession() as session:
        # user_data에서 region 값을 사용하여 Kakao Map API 호출
        region = user_data['region']
        stations_task = get_nearby_station(session, region, kakao_api_key)
        stations = await stations_task
        print(f"주변역: {stations}")

        # 서울시 상권 데이터 비동기 호출
        sangwon_data_task = fetch_sangwon_data(session, business_api_key, 1, page_size)
        sangwon_data = await sangwon_data_task
        print(f"1부터 {page_size}까지 데이터 요청 중...")

        # 서울시 승차 인원 데이터를 가져오기 위한 날짜 설정
        use_ymd = get_date_minus_days(14)

        # 역별로 승차 인원 수 확인
        passenger_tasks = [fetch_passenger_data(session, passenger_api_key, station, use_ymd) for station in stations]
        passenger_results = await asyncio.gather(*passenger_tasks)

        # 결과 출력
        for station, total_passengers in zip(stations, passenger_results):
            print(f"{station}역: {total_passengers}명, 날짜 {use_ymd}")

# 실행 코드
if __name__ == "__main__":
    page_size = 500  # 한 번에 가져올 데이터 수 (500개씩 요청)

    # 비동기 실행
    asyncio.run(fetch_all_data(page_size))
