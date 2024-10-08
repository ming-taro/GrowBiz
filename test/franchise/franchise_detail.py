import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import os
from dotenv import load_dotenv
import pymysql
import mysql.connector
from mysql.connector import Error

load_dotenv()

FRANCHISE_DETAIL_URL = "https://franchise.ftc.go.kr/mnu/00013/program/userRqst/view.do"

def find_franchise_detail(info):
    params = {
        'firMstSn': info[-1]
    }
    response = requests.get(FRANCHISE_DETAIL_URL, params)

    # 요청이 성공했는지 확인
    if response.status_code == 200:
        # HTML 내용 파싱
        soup = BeautifulSoup(response.text, 'html.parser')
        tbodys = soup.find_all('tbody')

        # 대표번호, 대표팩스 번호
        rows = tbodys[0].find_all('tr')
        col = rows[2].find_all('td')
        column_data = [c.get_text(strip=True) for c in col]
        # print('[대표번호:', column_data[2], "]")
        # print('[대표팩스 번호:', column_data[3], "]")
        # print()
        contact = {
            "phone": column_data[2].replace('\xa0', '').strip(),
            "fax" : column_data[3].replace('\xa0', '').strip()
        }

        # 가맹본부 재무상황
        financial = []
        # headers = ['연도', '자산', '부채', '자본', '매출액', '영업이익', '당기순이익']
        rows = tbodys[2].find_all('tr')
        for row in rows[1:]:
            columns = row.find_all('td')  # tr 안의 모든 td 요소 찾기
            column_data = [col.get_text(strip=True) for col in columns]  # 텍스트 추출
            financial.append({
                "year": int(column_data[0]),
                "asset": int(column_data[1].replace(",", "")) if column_data[1] else 0,
                "liability": int(column_data[2].replace(",", "")) if column_data[2] else 0,
                "equity": int(column_data[3].replace(",", "")) if column_data[3] else 0,
                "revenue": int(column_data[4].replace(",", "")) if column_data[4] else 0,
                "operating_income": int(column_data[5].replace(",", "")) if column_data[5] else 0,
                "net_income": int(column_data[6].replace(",", "")) if column_data[6] else 0
            })

        # 가맹점 및 직영점 현황
        store = []
        # headers = [
        #     "지역", 
        #     "2023년 - 전체", "2023년 - 가맹점수", "2023년 - 직영점수", 
        #     "2022년 - 전체", "2022년 - 가맹점수", "2022년 - 직영점수", 
        #     "2021년 - 전체", "2021년 - 가맹점수", "2021년 - 직영점수"
        # ]
        rows = tbodys[6].find_all('tr')  # tbody 안의 모든 tr 요소 찾기
        for row in rows[1:2]:
            columns = row.find_all('td')  # tr 안의 모든 td 요소 찾기
            column_data = [col.get_text(strip=True) for col in columns]  # 텍스트 추출
            year = 2023
            for i in range(1, 10, 3):
                store.append({
                    "region": column_data[0],
                    "year": year,
                    "total": int(column_data[i].replace(",", "")) if column_data[i] else 0,
                    "franchise_count": int(column_data[i + 1].replace(",", "")) if column_data[i + 1] else 0,
                    "company_store_count": int(column_data[i + 2].replace(",", "")) if column_data[i + 2] else 0
                })
                year -= 1

        # 가맹점 변동 현황
        franchise_change = []
        headers = ['연도', '신규개점', '계약종료', '계약해지', '명의변경']
        rows = soup.find_all('tr', class_='listOfOpenShow')
        for row in rows:
            data = [td.get_text(strip=True) for td in row.find_all('td')]
            franchise_change.append({
                "year": int(data[0]),
                "new_open": int(data[1].replace(",", "")) if data[1] else 0,
                "contract_termination": int(data[2].replace(",", "")) if data[2] else 0,
                "contract_cancellation": int(data[3].replace(",", "")) if data[3] else 0,
                "name_changes": int(data[4].replace(",", "")) if data[4] else 0
            })

        # 가맹점사업자 매출
        # headers = ['지역', '가맹점수', '평균매출액', '면적(3.3㎡)당 평균매출액']
        rows = soup.find_all('td', class_="listLocAvgShow")
        data = [td.get_text(strip=True) for td in rows]
        grouped_data = [data[i:i+3] for i in range(0, len(data), 3)] # 데이터 3 그룹씩 묶기
        franchise_revenue = {
            "region": "서울",
            "franchise_count": int(grouped_data[1][0].replace(",", "")) if grouped_data[1][0] else 0,
            "average_sales": int(grouped_data[1][1].replace(",", "")) if grouped_data[1][1] else 0,
            "average_sales_per_area": int(grouped_data[1][2].replace(",", "")) if grouped_data[1][2] else 0
        }

        # 광고·판촉비 내역
        # headers = ["연도", "광고비", "판촉비"]
        row = soup.find_all('tr', class_="listAdvPromtFeeHide")  # tbody 안의 모든 tr 요소 찾기
        columns = row[0].find_all('td')  # tr 안의 모든 td 요소 찾기
        column_data = [col.get_text(strip=True) for col in columns]  # 텍스트 추출
        advertising_cost = {
            "year": int(column_data[0]),
            "advertising_expense": int(column_data[1].replace(",", "")) if column_data[1] else 0,
            "promotion_expenses": int(column_data[2].replace(",", "")) if column_data[2] else 0
        }

        # 가맹금사업자의 부담금
        td_elements = soup.find_all('td', class_='al')
        data = [td.get_text(strip=True) for td in td_elements]
        business_fee = {
            "fee_type": data[0],
            "deposit_fee": int(data[1].replace(",", "")) if data[1] else 0
        }

        # 가맹점사업자의 부담 - 가맹점사업자의 부담금 (형태, 예치 가맹금)
        # headers = ['가입비(가맹비)', '교육비', '보증금', '기타비용', '합계']
        rows = tbodys[13].find_all('tr')  # tbody 안의 모든 tr 요소 찾기
        columns = rows[0].find_all('td')  # tr 안의 모든 td 요소 찾기
        column_data = [col.get_text(strip=True) for col in columns]  # 텍스트 추출
        initial_cost = {
            "franchise_fee": int(column_data[0].replace(",", "")) if column_data[0] else 0,
            "education_fee": int(column_data[1].replace(",", "")) if column_data[1] else 0,
            "deposit": int(column_data[2].replace(",", "")) if column_data[2] else 0,
            "other_cost": int(column_data[3].replace(",", "")) if column_data[3] else 0,
            "total": int(column_data[4].replace(",", "")) if column_data[4] else 0
        }

        # 가맹점사업자의 부담 - 인테리어 비용
        headers = ['단위면적(3.3㎡)당 인테리어 비용', '기준점포면적(㎡)', '인테리어 비용']
        rows = tbodys[14].find_all('tr')  # tbody 안의 모든 tr 요소 찾기
        columns = rows[0].find_all('td')  # tr 안의 모든 td 요소 찾기
        column_data = [col.get_text(strip=True) for col in columns]  # 텍스트 추출
        interior_cost = {
            "cost_per_area": int(column_data[0].replace(",", "")) if column_data[0] else 0,
            "standard_store_area": int(column_data[1].replace(",", "")) if column_data[1] else 0,
            "total": int(column_data[2].replace(",", "")) if column_data[2] else 0
        }

        # 가맹계약 기간
        element = soup.select_one('#frm > div:nth-child(16) > div > table')
        rows = element.find_all('tr')  # 모든 행(tr) 찾기
        headers = [th.get_text(strip=True) for th in rows[1].find_all('th')]  # "최초"와 "연장" 헤더 추출
        values = [td.get_text(strip=True) for td in rows[2].find_all('td')]   # 값 추출
        contract_period = {
            "initial": int(values[0].replace(",", "")) if values[0] else 0,
            "renewal": int(values[1].replace(",", "")) if values[1] else 0
        }

        return {
            "serial_number": info[3],
            "store_name": info[2],
            "main_category": info[0],
            "sub_category": info[1],
            "contact": contact,
            "financial": financial,
            "store": store,
            "franchise_change": franchise_change,
            "franchise_revenue": franchise_revenue,
            "advertising_cost": advertising_cost,
            "business_fee": business_fee,
            "initial_cost": initial_cost,
            "interior_cost": interior_cost,
            "contract_period": contract_period
        }

# 가맹본부 일반 현황 - 2개 -> 대표번호, 대표팩스 번호
# 가맹본부 재무상황 <연도 3개년>
# 가맹점 및 직영점 현황 - 서울 <연도 3개년>
# 가맹점 변동 현황 <연도 3개년>
# 가맹점사업자의 평균 매출액 및 면적(3.3㎡)당 매출액 - 서울 <연도 1개년>
# 광고·판촉비 내역
# 가맹금사업자의 부담금
# 가맹점사업자의 부담 - 2개
# 가맹계약 기간

mysql_connection = pymysql.connect(
    host=os.environ.get('DB_HOST'),
    user=os.environ.get('DB_USER'),
    password=os.environ.get('DB_PASSWORD'), 
    database="KB",
    charset='utf8'
)

mongo_client = MongoClient(
    host=os.environ.get('DB_HOST'),
    port=int(os.environ.get('MONGO_DB_PORT')),
    username=os.environ.get('MONGO_DB_USER'),
    password=os.environ.get('MONGO_DB_PASSWORD'),
    authSource=os.environ.get('AUTH_DB')
)

try:
    mongo_db = mongo_client['franchise']
    mongo_db_collection = mongo_db['franchise_detail']

    if mysql_connection.open:
        print("Successfully connected to the database")

        # 쿼리 실행
        query = "SELECT main_category, sub_category, store_name, serial_number FROM BusinessInfo"
        mysql_cursor = mysql_connection.cursor()
        mysql_cursor.execute(query)

        # 결과 가져오기
        result = mysql_cursor.fetchall()
        last = 0
        for i in range(0, len(result)):
            mongo_db_collection.insert_one(find_franchise_detail(result[i]))
            # print(i, "->", result[i])
except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    # 연결 종료
    if mysql_connection.open:
        mysql_cursor.close()
        mysql_connection.close()
        print("MySQL mysql_connection is closed")