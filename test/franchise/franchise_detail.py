# import requests
# from bs4 import BeautifulSoup

# # API 요청할 URL
# url = 'https://franchise.ftc.go.kr/api/search.do'

# def find_franchise(year):
#     # API 요청에 사용할 파라미터 설정
#     params = {
#         'serviceKey': 't0y5gacvM9gX1+Iiq85HCj+9VkCPURiR2K8JhS2T',  # API 키
#         'yr': year,          # 요청할 데이터 연도
#         'pageUnit': '10000',      # 한 페이지에 나올 항목 수
#         'viewType': 'html',    # 응답 형식(html로 받음)
#         'pageIndex': '1'       # 페이지 번호
#     }

#     # API 요청
#     response = requests.get(url, params=params)

#     # 응답이 성공적이면
#     if response.status_code == 200:
#         # HTML 파싱
#         soup = BeautifulSoup(response.content, 'html.parser')
        
#         # tbody 추출
#         tbody = soup.find('tbody')
        
#         # tbody의 모든 행(tr) 추출
#         rows = tbody.find_all('tr')
        
#         # 각 행에서 데이터 추출
#         for row in rows:
#             cells = row.find_all('td')
#             # 각 셀의 텍스트 출력
#             data = [cell.get_text(strip=True) for cell in cells]
#             # print(data)
#             # print(data)
#             if "깐" in data[1]:
#                 print(year)
#                 print(data)
#     else:
#         print(f"요청 실패: {response.status_code}")

# for i in range(0, 100):
#     find_franchise(2024 - i)

import requests
from bs4 import BeautifulSoup

# 요청할 URL
url = "https://franchise.ftc.go.kr/mnu/00013/program/userRqst/view.do"

params = {
    'firMstSn': 106369
}

# GET 요청 보내기
response = requests.get(url, params)

# 요청이 성공했는지 확인
if response.status_code == 200:
    # HTML 내용 파싱
    soup = BeautifulSoup(response.text, 'html.parser')
    tbodys = soup.find_all('tbody')

    # 대표번호, 대표팩스 번호
    rows = tbodys[0].find_all('tr')
    col = rows[2].find_all('td')
    column_data = [c.get_text(strip=True) for c in col]
    print('[대표번호:', column_data[2], "]")
    print('[대표팩스 번호:', column_data[3], "]")
    # for row in rows:
    #     columns = row.find_all('td')  # tr 안의 모든 td 요소 찾기
    #     column_data = [col.get_text(strip=True) for col in columns]  # 텍스트 추출
    #     print(column_data)  # 추출한 데이터 출력
    print()

    # 가맹본부 재무상황
    headers = ['연도', '자산', '부채', '자본', '매출액', '영업이익', '당기순이익']
    print(headers)
    rows = tbodys[2].find_all('tr')
    for row in rows[1:]:
        columns = row.find_all('td')  # tr 안의 모든 td 요소 찾기
        column_data = [col.get_text(strip=True) for col in columns]  # 텍스트 추출
        print(column_data)  # 추출한 데이터 출력
    print()

    # 가맹점 및 직영점 현황
    headers = [
        "지역", 
        "2023년 - 전체", "2023년 - 가맹점수", "2023년 - 직영점수", 
        "2022년 - 전체", "2022년 - 가맹점수", "2022년 - 직영점수", 
        "2021년 - 전체", "2021년 - 가맹점수", "2021년 - 직영점수"
    ]
    print(headers)
    rows = tbodys[6].find_all('tr')  # tbody 안의 모든 tr 요소 찾기
    for row in rows:
        columns = row.find_all('td')  # tr 안의 모든 td 요소 찾기
        column_data = [col.get_text(strip=True) for col in columns]  # 텍스트 추출
        print(column_data)
    print()

    # 가맹점 변동 현황
    headers = ['연도', '신규개점', '계약종료', '계약해지', '명의변경']
    print(headers)
    rows = soup.find_all('tr', class_='listOfOpenShow')
    for row in rows:
        data = [td.get_text(strip=True) for td in row.find_all('td')]
        print(data)
    print()

    # 2023년 가맹점사업자의 평균 매출액 및 면적(3.3㎡)당 매출액
    headers = ['지역', '가맹점수', '평균매출액', '면적(3.3㎡)당 평균매출액']
    print(headers)
    rows = soup.find_all('td', class_="listLocAvgShow")
    data = [td.get_text(strip=True) for td in rows]
    grouped_data = [data[i:i+3] for i in range(0, len(data), 3)] # 데이터 3 그룹씩 묶기
    print(grouped_data[1])
    print()

    # 광고·판촉비 내역
    headers = ["연도", "광고비", "판촉비"]
    print(headers)
    rows = soup.find_all('tr', class_="listAdvPromtFeeHide")  # tbody 안의 모든 tr 요소 찾기
    print(headers)
    for row in rows:
        columns = row.find_all('td')  # tr 안의 모든 td 요소 찾기
        column_data = [col.get_text(strip=True) for col in columns]  # 텍스트 추출
        print(column_data)  # 추출한 데이터 출력
    print()

    # 가맹금사업자의 부담금
    td_elements = soup.find_all('td', class_='al')
    data = [td.get_text(strip=True) for td in td_elements]
    print(data)
    print()

    # 가맹점사업자의 부담 - 가맹점사업자의 부담금
    headers = ['가입비(가맹비)', '교육비', '보증금', '기타비용', '합계']
    print(headers)
    rows = tbodys[13].find_all('tr')  # tbody 안의 모든 tr 요소 찾기
    for row in rows:
        columns = row.find_all('td')  # tr 안의 모든 td 요소 찾기
        column_data = [col.get_text(strip=True) for col in columns]  # 텍스트 추출
        print(column_data)
    print()

    # 가맹점사업자의 부담 - 인테리어 비용
    headers = ['단위면적(3.3㎡)당 인테리어 비용', '기준점포면적(㎡)', '인테리어 비용']
    print(headers)
    rows = tbodys[14].find_all('tr')  # tbody 안의 모든 tr 요소 찾기
    for row in rows:
        columns = row.find_all('td')  # tr 안의 모든 td 요소 찾기
        column_data = [col.get_text(strip=True) for col in columns]  # 텍스트 추출
        print(column_data)
    print()


    print("==========================")
    # "최초" 텍스트가 포함된 tr 찾기
    contract_period_th = soup.find('th', string=lambda text: text and "계약기간" in text)
    print(contract_period_th)
    tbody = contract_period_th.find_parent('tbody')
    print(tbody)
    


    # for index, tbody in enumerate(tbodys):
        # if index == 6: # 가맹점 및 직영점 현황
        #     headers = [
        #         "지역", 
        #         "2023년 - 전체", "2023년 - 가맹점수", "2023년 - 직영점수", 
        #         "2022년 - 전체", "2022년 - 가맹점수", "2022년 - 직영점수", 
        #         "2021년 - 전체", "2021년 - 가맹점수", "2021년 - 직영점수"
        #     ]
        #     data = []
        #     rows = tbody.find_all('tr')  # tbody 안의 모든 tr 요소 찾기
        
        #     for row in rows:
        #         columns = row.find_all('td')  # tr 안의 모든 td 요소 찾기
        #         column_data = [col.get_text(strip=True) for col in columns]  # 텍스트 추출

        # if index == 8: # 가맹점 변동 현황
        #     print(tbody)

        # if index == 10: # 광고·판촉비 내역


        # print(f"tbody {index}의 데이터:")
        # rows = tbody.find_all('tr')  # tbody 안의 모든 tr 요소 찾기
        
        # for row in rows:
        #     columns = row.find_all('td')  # tr 안의 모든 td 요소 찾기
        #     column_data = [col.get_text(strip=True) for col in columns]  # 텍스트 추출
        #     print(column_data)  # 추출한 데이터 출력
        # print()  # 가독성을 위한 빈 줄 추가
else:
    print(f"오류: {response.status_code}")

# 가맹본부 일반 현황 - 2개 -> 대표번호, 대표팩스 번호
# 가맹본부 재무상황
# 가맹점 및 직영점 현황 - 서울
# 가맹점 변동 현황
# 가맹점사업자의 평균 매출액 및 면적(3.3㎡)당 매출액 - 서울
# 광고·판촉비 내역
# 가맹금사업자의 부담금
# 가맹점사업자의 부담 - 2개

# 가맹계약 기간