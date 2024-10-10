import os
import mysql.connector
import requests
from bs4 import BeautifulSoup
import re  # 정규식 사용을 위한 모듈
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database connection
try:
    print("Connecting to the database...")
    conn = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )
    cursor = conn.cursor()
    print("DB 연결 성공")
except mysql.connector.Error as err:
    print(f"DB 연결 실패: {err}")
    exit(1)

# Base URL
base_url = "https://franchise.ftc.go.kr/mnu/00013/program/userRqst/list.do"
# params = {
#     'searchCondition': '',
#     'searchKeyword': '',
#     'column': 'brd',
#     'selUpjong': '21',
#     'selIndus': 'H1',
#     'pageUnit': '10',
#     'pageIndex': '1'  # Change this for each page
# } ->치킨
# Updated parameters to match the given URL
# params = {
#     'column': 'firRegNo',  # Updated 'column' parameter to 'firRegNo'
#     'searchKeyword': '',  # Search keyword left blank as in the given URL
#     'selUpjong': '22',  # Updated 'selUpjong' to '22'
#     'selIndus': 'A2',  # Updated 'selIndus' to 'A2'
#     'pageUnit': '10',  # Page size (10 items per page)
#     'pageIndex': '1',  # Start from the first page
#     'x': '17',  # Added 'x' parameter from the URL
#     'y': '20'   # Added 'y' parameter from the URL
# } ->편의점
# Updated parameters to match the given URL
# params = {
#     'column': 'firRegNo',  # Updated 'column' parameter to 'firRegNo'
#     'searchKeyword': '',  # Search keyword left blank as in the given URL
#     'selUpjong': '23',  # Updated 'selUpjong' to '23'
#     'selIndus': 'G3',  # Updated 'selIndus' to 'G3'
#     'pageUnit': '10',  # Page size (10 items per page)
#     'pageIndex': '1',  # Start from the first page
#     'x': '36',  # Added 'x' parameter from the URL
#     'y': '12'   # Added 'y' parameter from the URL
# }
# ->숙박
# Updated parameters to match the given URL
# params = {
#     'column': 'brd',  # Updated 'column' parameter to 'brd'
#     'searchKeyword': '',  # Search keyword left blank as in the given URL
#     'selUpjong': '21',  # Updated 'selUpjong' to '21'
#     'selIndus': 'L1',  # Updated 'selIndus' to 'L1'
#     'pageUnit': '10',  # Page size (10 items per page)
#     'pageIndex': '1',  # Start from the first page
#     'x': '33',  # Added 'x' parameter from the URL
#     'y': '21'   # Added 'y' parameter from the URL
# }
# ->커피

# Updated parameters to match the given URL
# params = {
#     'column': 'brd',  # Updated 'column' parameter to 'brd'
#     'searchKeyword': '',  # Search keyword left blank as in the given URL
#     'selUpjong': '21',  # Updated 'selUpjong' to '21'
#     'selIndus': 'J1',  # Updated 'selIndus' to 'J1'
#     'pageUnit': '10',  # Page size (10 items per page)
#     'pageIndex': '1',  # Start from the first page
#     'x': '25',  # Added 'x' parameter from the URL
#     'y': '17'   # Added 'y' parameter from the URL
# }
# ->제과제빵
# Function to insert data into the database

# Updated parameters to match the given URL
# params = {
#     'column': 'brd',  # Updated 'column' parameter to 'brd'
#     'searchKeyword': '',  # Search keyword left blank as in the given URL
#     'selUpjong': '21',  # Updated 'selUpjong' to '21'
#     'selIndus': 'K1',  # Updated 'selIndus' to 'K1'
#     'pageUnit': '10',  # Page size (10 items per page)
#     'pageIndex': '1',  # Start from the first page
#     'x': '41',  # Added 'x' parameter from the URL
#     'y': '8'   # Added 'y' parameter from the URL
# }
# #아이스크림
params = {
    'column': 'brd',  # Updated 'column' parameter to 'brd'
    'searchKeyword': '',  # Search keyword left blank as in the given URL
    'selUpjong': '23',  # Updated 'selUpjong' to '21'
    'selIndus': 'K3',  # Updated 'selIndus' to 'K1'
    'pageUnit': '10',  # Page size (10 items per page)
    'pageIndex': '1',  # Start from the first page
    'x': '35',  # Added 'x' parameter from the URL
    'y': '7'   # Added 'y' parameter from the URL
}
#PC방
def insert_into_db(data):
    try:
        query = """
        INSERT INTO BusinessInfo (number, 상호명, store_name, 대표자, 등록번호, 최초등록일, main_category, sub_category, serial_number)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (
            data['number'],
            data['상호명'],
            data['store_name'],  # 새로 추가된 영업표지 컬럼
            data['대표자'],
            data['등록번호'],
            data['최초등록일'],
            '서비스',  # 대분류 is fixed as '외식'
            'PC방',  # 중분류 is fixed as '치킨'
            data['일련번호']  # 일련번호 추가
        ))
        print(f"Data inserted for {data['number']}")
    except mysql.connector.Error as err:
        print(f"Data insert failed: {err}")

# Function to crawl a single page
def crawl_page(page_index):
    print(f"Fetching data for page {page_index}...")
    params['pageIndex'] = str(page_index)
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        table_rows = soup.select('table.table tbody tr')  # CSS selector for table rows

        for row in table_rows:
            cols = row.find_all('td')
            if cols:
                # 기본 일련번호 설정
                일련번호 = None

                # 일련번호 추출 (a 태그의 onclick에서)
                a_tag = cols[1].find('a')  # 두 번째 열에 a 태그가 있음
                if a_tag and 'onclick' in a_tag.attrs:
                    onclick_value = a_tag['onclick']
                    # 정규식으로 firMstSn 값 추출
                    match = re.search(r"firMstSn=(\d+)", onclick_value)
                    if match:
                        일련번호 = match.group(1)  # firMstSn 값을 추출

                # Gather the data
                data = {
                    'number': cols[0].text.strip(),
                    '상호명': cols[1].text.strip(),
                    'store_name': cols[2].text.strip(),  # 영업표지 추가
                    '대표자': cols[3].text.strip(),
                    '등록번호': cols[4].text.strip(),
                    '최초등록일': cols[5].text.strip(),  # 상태 대신 최초등록일로 변경
                    '일련번호': 일련번호  # 일련번호 추가
                }
                # Insert data into the database
                insert_into_db(data)
    else:
        print(f"Failed to retrieve page {page_index}, Status code: {response.status_code}")

# Loop through multiple pages (you can adjust the range)
for i in range(1, 3):  # Example: page 1 to 65
    crawl_page(i)

# Commit the changes and close the connection
conn.commit()
cursor.close()
conn.close()
