import requests
from bs4 import BeautifulSoup
import re  # 정규식 사용을 위한 모듈

# Base URL
base_url = "https://franchise.ftc.go.kr/mnu/00013/program/userRqst/list.do"
params = {
    'searchCondition': '',
    'searchKeyword': '',
    'column': 'brd',
    'selUpjong': '21',
    'selIndus': 'H1',
    'pageUnit': '10',
    'pageIndex': '1'  # Change this for each page
}

# Function to crawl a single page and print 일련번호
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

                # 일련번호 출력 (DB 연결 없음)
                print(f"상호명: {cols[1].text.strip()}, 일련번호: {일련번호}")
    else:
        print(f"Failed to retrieve page {page_index}, Status code: {response.status_code}")

# 테스트: 페이지 1번에 대해 일련번호만 출력
crawl_page(1)
