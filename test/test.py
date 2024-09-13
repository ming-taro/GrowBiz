# import requests

# # URL to request the data from
# url = "https://www.serve.co.kr/good/v1/map/getAtclDetail?atclNo=314537610&tabNo=4"

# # Make the GET request
# response = requests.get(url)

# # Check if the request was successful
# if response.status_code == 200:
#     data = response.json()  # Parse the response JSON
#     if 'data' in data and 'resultList' in data['data']:
#         # Extract the resultList part
#         result_list = data['data']['resultList']
#         # Print or process the resultList
#         print(result_list)
#     else:
#         print("resultList not found in response")
# else:
#     print(f"Failed to retrieve data. Status code: {response.status_code}")
# import requests

# # 기본 URL
# base_url = "https://www.serve.co.kr/good/v1/map/getAtclList"

# # 거래 종류에 따른 코드 매핑
# deal_types = {
#     "매매": "A1",
#     "전세": "B1",
#     "월세": "B2",
#     "단기임대": "B3"
# }

# # 선택한 거래 종류에 맞는 코드를 생성하는 함수
# def get_deal_kind_codes(selected_deal_types):
#     return ",".join([deal_types[deal] for deal in selected_deal_types])

# # 매물 정보를 가져오는 함수
# def get_real_estate_list(selected_deal_types):
#     deal_kind_cd_list_str = get_deal_kind_codes(selected_deal_types)
    
#     params = {
#         "tabNo": 4,
#         "sno": "",
#         "ldongCd": "1168010100",  # 서울 서초구 반포동 예시
#         "aptNo": "",
#         "laCrd": "",
#         "loCrd": "",
#         "maxLaCrd": "",
#         "maxLoCrd": "",
#         "minLaCrd": "",
#         "minLoCrd": "",
#         "orderCd": 1,
#         "ctgryCdList": "SHP01,SHP02,SHP03,OFC01,OFC02,OFC03,OFC05",
#         "zoneNo": "",
#         "dealKindCdListStr": deal_kind_cd_list_str,  # 거래 종류 코드
#         "maxBscTnthWuntAmt": "",
#         "maxAddTnthWuntAmt": "",
#         "selectPeriod": "PR"
#     }

#     # GET 요청 보내기
#     response = requests.get(base_url, params=params)

#     # 응답 확인 및 데이터 출력
#     if response.status_code == 200:
#         data = response.json()
#         print(data)
#     else:
#         print(f"Error: {response.status_code}")

# # 거래 종류 선택 (예시)
# # selected_deal_types = ["매매", "월세", "단기임대"]
# # selected_deal_types = ["매매"]
# selected_deal_types = ["월세"]

# # 매물 정보 가져오기
# get_real_estate_list(selected_deal_types)

#####

import requests

# 기본 URL
base_url = "https://www.serve.co.kr/good/v1/map/getAtclList"

# 거래 종류에 따른 코드 매핑
deal_types = {
    "매매": "A1",
    "전세": "B1",
    "월세": "B2",
    "단기임대": "B3"
}

# 선택한 거래 종류에 맞는 코드를 생성하는 함수
def get_deal_kind_codes(selected_deal_types):
    return ",".join([deal_types[deal] for deal in selected_deal_types])

# 매물 정보를 가져오는 함수
def get_real_estate_list(selected_deal_types):
    deal_kind_cd_list_str = get_deal_kind_codes(selected_deal_types)
    
    params = {
        "tabNo": 4,
        "sno": "",
        "ldongCd": "1165010600",  # 서울 서초구 반포동 예시
        "aptNo": "",
        "laCrd": "",
        "loCrd": "",
        "maxLaCrd": "",
        "maxLoCrd": "",
        "minLaCrd": "",
        "minLoCrd": "",
        "orderCd": 1,
        "ctgryCdList": "SHP01,SHP02,SHP03,OFC01,OFC02,OFC03,OFC05",
        "zoneNo": "",
        "dealKindCdListStr": deal_kind_cd_list_str,  # 거래 종류 코드
        "maxBscTnthWuntAmt": "",
        "maxAddTnthWuntAmt": "",
        # "selectPeriod": "PR",
        "pageNum": 0,  # 페이지 번호
        "offset": 100   # 데이터 오프셋
    }

    # GET 요청 보내기
    response = requests.get(base_url, params=params)

    # 응답 확인 및 필요한 데이터 추출
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'resultList' in data['data']:
            extract_columns(data['data']['resultList'])
        else:
            print("No valid data found.")
    else:
        print(f"Error: {response.status_code}")

# 컬럼 추출 함수 정의
def extract_columns(result_list):
    extracted_data = []
    for item in result_list:
        # 원하는 컬럼을 가져오기
        sido = item.get('sidoNm')  # 시/도
        sgg = item.get('sggNm')  # 구
        emd = item.get('emdNm')  # 동
        bsc_amt = item.get('bscTnthWuntAmt')  # 기본 월세 금액
        add_amt = item.get('addTnthWuntAmt')  # 추가 월세 금액
        deal_type = item.get('dealKindCdNm')  # 거래 유형
        naver_id = item.get('naverAtclNo')  # 네이버 매물 번호
        
        extracted_data.append({
            '시/도': sido,
            '구': sgg,
            '동': emd,
            '기본 월세 금액': bsc_amt,
            '추가 월세 금액': add_amt,
            '거래 유형': deal_type,
            '네이버 매물 번호': naver_id
        })
    
    # 추출된 데이터 출력
    for row in extracted_data:
        print(row)

# 거래 종류 선택 (예시)
selected_deal_types = ["월세"]
# selected_deal_types = ["매매", "월세", "단기임대"]

# 매물 정보 가져오기
get_real_estate_list(selected_deal_types)

