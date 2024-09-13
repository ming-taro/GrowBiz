import requests
import csv
from datetime import datetime

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
    codes = [deal_types.get(deal) for deal in selected_deal_types if deal in deal_types]
    return ",".join(codes)

# 매물 정보를 가져오는 함수
def get_real_estate_list(selected_deal_types, page_num=0, offset=0):
    deal_kind_cd_list_str = get_deal_kind_codes(selected_deal_types)
    
    params = {
        "tabNo": 4,
        "sno": "",
        "ldongCd": "1165010600",  # 서울 서초구 반포동 예시
        "aptNo": "",
        "laCrd": "",
        "loCrd": "",
        "maxLaCrd": "37.48947143554688",  # 좌표 범위 설정
        "maxLoCrd": "127.01431274414062",
        "minLaCrd": "37.48809814453125",
        "minLoCrd": "127.012939453125",
        "orderCd": 1,
        "ctgryCdList": "SHP01,SHP02,SHP03,OFC01,OFC02,OFC03,OFC05",  # 카테고리 설정
        "zoneNo": "",
        "pageNum": page_num,   # 페이지 번호
        "offset": offset,      # 오프셋
        "selectPeriod": "PR",
    }

    # 거래 종류 필터링 (필요시 아래와 같이 추가)
    if deal_kind_cd_list_str:
        params["dealKindCdList"] = deal_kind_cd_list_str  # 실제 API에서 지원하는지 확인 필요

    # GET 요청 보내기
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # HTTP 오류 발생 시 예외 발생
        data = response.json()
        
        if data.get('status') == 'success':
            result_list = data.get('data', {}).get('resultList', [])
            if result_list:
                return result_list
            else:
                print("결과 목록이 비어 있습니다.")
                return []
        else:
            print(f"데이터 조회 실패: {data.get('message')}")
            return []
    except requests.exceptions.RequestException as e:
        print(f"요청 중 오류 발생: {e}")
        return []

# 컬럼 추출 함수 정의
def extract_columns(result_list):
    extracted_data = []
    for item in result_list:
        # 원하는 컬럼을 가져오기
        atcl_no = item.get('atclNo')  # 매물 번호
        sido = item.get('sidoNm')  # 시/도
        sgg = item.get('sggNm')  # 구
        emd = item.get('emdNm')  # 동
        bsc_amt = item.get('bscTnthWuntAmt')  # 기본 월세 금액
        add_amt = item.get('addTnthWuntAmt')  # 추가 월세 금액
        deal_type = item.get('dealKindCdNm')  # 거래 유형
        naver_id = item.get('naverAtclNo')  # 네이버 매물 번호
        atcl_reg_dttm = item.get('atclRegDttm')  # 매물 등록 시간
        area1 = item.get('area1')  # 공급 면적
        area2 = item.get('area2')  # 전용 면적
        flr1 = item.get('flr1')  # 최하층
        flr2 = item.get('flr2')  # 최고층
        direction = item.get('drcCdNm')  # 건물 방향
        atcl_sfe_cn = item.get('atclSfeCn')  # 매물 설명
        agency_name = item.get('mdiatBzestNm')  # 중개사무소 이름
        agent_name = item.get('mdiatBzestChrgrNm')  # 담당자 이름
        agency_phone = item.get('mdiatBzestRepTelno')  # 중개사무소 연락처
        latitude = item.get('laCrd')  # 위도
        longitude = item.get('loCrd')  # 경도
        photo_list = item.get('photoList', [])  # 사진 목록

        # 사진 URL 추출 (첫 번째 사진만 예시로)
        photo_urls = [photo.get('photoUrl') for photo in photo_list if photo.get('photoUrl')]
        photo_url = photo_urls[0] if photo_urls else ""

        extracted_data.append({
            '매물 번호': atcl_no,
            '시/도': sido,
            '구': sgg,
            '동': emd,
            '기본 월세 금액': bsc_amt,
            '추가 월세 금액': add_amt,
            '거래 유형': deal_type,
            '네이버 매물 번호': naver_id,
            '매물 등록 시간': atcl_reg_dttm,
            '공급 면적': area1,
            '전용 면적': area2,
            '층수': f"{flr1} ~ {flr2}층",
            '방향': direction,
            '매물 설명': atcl_sfe_cn,
            '중개사무소 이름': agency_name,
            '담당자 이름': agent_name,
            '중개사무소 연락처': agency_phone,
            '위도': latitude,
            '경도': longitude,
            '사진 URL': photo_url
        })
    
    return extracted_data

# CSV 파일로 저장하는 함수
def save_to_csv(data, filename='real_estate_data.csv'):
    if not data:
        print("저장할 데이터가 없습니다.")
        return
    
    # CSV 헤더 설정
    headers = list(data[0].keys())
    
    try:
        with open(filename, mode='w', newline='', encoding='utf-8-sig') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)
        print(f"데이터가 {filename} 파일에 저장되었습니다.")
    except IOError as e:
        print(f"파일 저장 중 오류 발생: {e}")

# 전체 프로세스를 실행하는 함수
def main():
    # 거래 종류 선택 (예시)
    selected_deal_types = ["월세"]
    
    all_extracted_data = []
    
    # 페이지 순회 (예시로 1페이지만)
    # 필요한 경우 반복문을 통해 여러 페이지를 순회할 수 있습니다.
    page_num = 0
    offset = 0
    result_list = get_real_estate_list(selected_deal_types, page_num, offset)
    
    if result_list:
        extracted_data = extract_columns(result_list)
        all_extracted_data.extend(extracted_data)
    
    # 추가 페이지가 있는 경우 반복 처리
    total_pages = 1  # total pages API가 응답에 포함되어 있을 경우 가져옴
    for page in range(1, total_pages):
        result_list = get_real_estate_list(selected_deal_types, page, offset + page * 30)
        if result_list:
            extracted_data = extract_columns(result_list)
            all_extracted_data.extend(extracted_data)
    
    # 추출된 데이터 저장
    if all_extracted_data:
        # 파일 이름에 현재 날짜 추가
        filename = f"real_estate_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        save_to_csv(all_extracted_data, filename)
    else:
        print("추출된 데이터가 없습니다.")

if __name__ == "__main__":
    main()
