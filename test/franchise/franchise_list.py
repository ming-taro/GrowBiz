import requests
from bs4 import BeautifulSoup
import re

# 요청을 보낼 URL
url = 'https://franchise.ftc.go.kr/mnu/00013/program/userRqst/list.do'

# 파라미터 설정 (해당 페이지에 맞게 필요한 부분 조정)
params = {
    'searchCondition': '',
    'searchKeyword': '',
    'column': 'brd',
    'selUpjong': '22',  # 업종
    'selIndus': 'A2',   # 산업
    'pageUnit': '10',
    'pageIndex': '1'
}

# GET 요청
response = requests.get(url, params=params)

# 요청이 성공했는지 확인
if response.status_code == 200:
    # HTML 파싱
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 예시: 페이지에서 데이터 추출
    rows = soup.find_all('tr')  # 테이블 행 추출 (페이지 구조에 맞게 수정 필요)
    for row in rows:
        columns = row.find_all('td')
        for col in columns:
            print(col.get_text(strip=True), end=", ")  # 각 열의 텍스트 출력
        link = row.find('a', class_='authCtrl')  # 클래스명을 통해 <a> 태그 찾기
        print("[link]")
        print(link)
        if link:  # <a> 태그가 존재할 경우
            print(link.get_text(strip=True))  # <a> 태그의 텍스트 출력4

            onclick_value = link['onclick']
            match = re.search(r'firMstSn=(\d+)', onclick_value)  # 정규 표현식 사용하여 숫자 추출
            
            if match:
                extracted_number = match.group(1)  # 매칭된 숫자 가져오기
                print(f"추출된 숫자: {extracted_number}")
            else:
                print("숫자를 추출할 수 없습니다.")
        print()
else:
    print(f"Error: {response.status_code}")
