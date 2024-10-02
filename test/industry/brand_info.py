import requests
from dotenv import load_dotenv
import os
from brand_interrior import find_interior_cost
from brand_sales import get_brand_frc_bzmn_avrgsls

load_dotenv()
OPEN_DATA_API_KEY = os.environ.get('OPEN_DATA_API_KEY')

BRAND_INFO_URL = "http://apis.data.go.kr/1130000/FftcBrandRlsInfo2_Service/getBrandinfo"

categories = {
    "서비스": {
        "교육 (외국어)": {"induty_lclas_nm": "교육", "induty_mlsfc_nm": "외국어 교육"},
        "기타 교육": {"induty_lclas_nm": "교육", "induty_mlsfc_nm": "기타 교육"},
        "교육 (교과)": {"induty_lclas_nm": "교육", "induty_mlsfc_nm": "교과 교육"},
        "세탁": {"induty_lclas_nm": "서비스", "induty_mlsfc_nm": "세탁"},
        "기타 서비스": {"induty_lclas_nm": "서비스", "induty_mlsfc_nm": "기타 서비스"},
        "이미용": {"induty_lclas_nm": "패션/뷰티", "induty_mlsfc_nm": "미용서비스"},
        "자동차 관련": {"induty_lclas_nm": "서비스", "induty_mlsfc_nm": "자동차 관련"}
    },
    "도소매": {
        "편의점": {"induty_lclas_nm": "유통", "induty_mlsfc_nm": "편의점"},
        "기타도소매": {"induty_lclas_nm": "유통", "induty_mlsfc_nm": "할인점/슈퍼마켓"},
        "의류 / 패션": {"induty_lclas_nm": "패션/뷰티", "induty_mlsfc_nm": "패션/잡화"},
        "화장품": {"induty_lclas_nm": "패션/뷰티", "induty_mlsfc_nm": "화장품"}
    },
    "외식": {
        "한식": {"induty_lclas_nm": "음식/음료", "induty_mlsfc_nm": "한식"},
        "피자": {"induty_lclas_nm": "음식/음료", "induty_mlsfc_nm": "패스트푸드"},
        "기타 외식": {"induty_lclas_nm": "음식/음료", "induty_mlsfc_nm": "기타 요식"},
        "치킨": {"induty_lclas_nm": "음식/음료", "induty_mlsfc_nm": "패스트푸드"},
        "주점": {"induty_lclas_nm": "음식/음료", "induty_mlsfc_nm": "기타 요식"},
        "패스트푸드": {"induty_lclas_nm": "음식/음료", "induty_mlsfc_nm": "패스트푸드"},
        "커피": {"induty_lclas_nm": "음식/음료", "induty_mlsfc_nm": "커피"},
        "분식": {"induty_lclas_nm": "음식/음료", "induty_mlsfc_nm": "기타 요식"},
        "기타 외국식": {"induty_lclas_nm": "음식/음료", "induty_mlsfc_nm": "기타 요식"},
        "중식": {"induty_lclas_nm": "음식/음료", "induty_mlsfc_nm": "중식"},
        "음료 (커피 외)": {"induty_lclas_nm": "음식/음료", "induty_mlsfc_nm": "커피"},
        "제과제빵": {"induty_lclas_nm": "음식/음료", "induty_mlsfc_nm": "제과"},
        "일식": {"induty_lclas_nm": "음식/음료", "induty_mlsfc_nm": "일식"},
        "서양식": {"induty_lclas_nm": "음식/음료", "induty_mlsfc_nm": "양식"},
        "아이스크림/빙수": {"induty_lclas_nm": "음식/음료", "induty_mlsfc_nm": "기타 요식"}
    }
}


def classify_industry(induty_lclas_nm, induty_mlsfc_nm): # 대분류, 중분류
    if induty_lclas_nm not in categories or induty_mlsfc_nm not in categories[induty_lclas_nm]: # 위 기준에 분류되지 않는 업종은 기타로 분류
        return { "induty_lclas_nm": "기타",  "induty_mlsfc_nm": induty_mlsfc_nm }

    return categories[induty_lclas_nm][induty_mlsfc_nm]


# 해당 년도 총 브랜드 개수
def calc_total_brand_count(year):
    brand_info_params = {
        "serviceKey": OPEN_DATA_API_KEY,
        "pageNo": 1,
        "numOfRows": 1,
        "resultType": "json",
        "jngBizCrtraYr": year
    }
    response = requests.get(BRAND_INFO_URL, params=brand_info_params)
    total_count = response.json()["totalCount"]
    return total_count


# 브랜드 정보
def save_brand_info(page_count, data_count, brand_fntn_info, year, cursor):
    brand_info_params = {
        "serviceKey": OPEN_DATA_API_KEY,
        "pageNo": page_count,
        "numOfRows": data_count,
        "resultType": "json",
        "jngBizCrtraYr": year
    }

    try:
        response = requests.get(BRAND_INFO_URL, params=brand_info_params)
        response.raise_for_status()

        data = response.json()
        items = data["items"]

        for item in items:
            classification = classify_industry(item['indutyLclasNm'], item['indutyMlsfcNm'])

            brand = {
                "brand_mnno": item['brandMnno'],                       # 브랜드 모델 번호
                "jnghdqrtrs_rprsv_nm": item['jnghdqrtrsRprsvNm'],      # 본사 대표 이름
                "brand_nm": item['brandNm'],                           # 브랜드 이름
                "induty_lclas_nm": classification['induty_lclas_nm'],  # 산업 대분류 이름
                "induty_mlsfc_nm": classification['induty_mlsfc_nm'],  # 산업 중분류 이름
                "majr_gds_nm": item['majrGdsNm'],                      # 주요 상품명
                "fyer_avrg_sls_amt_scope_val": get_brand_frc_bzmn_avrgsls(item['brandMnno']), # 연평균 매출 범위
                "unit_ar_intrr_amt_scope_val": None,    # 단위 면적 계약 금액 범위
                "stor_crtra_ar": None,                  # 매장 계약 면적
                "intrr_amt_scope_val": None,            # 인테리어 총 금액 범위
                "jng_bzmn_jng_amt": None,               # 가맹 사업자 가맹 금액 (3300)
                "jng_bzmn_edu_amt": None,               # 가맹 사업자 교육비 (2200)
                "jng_bzmn_assrnc_amt": None,            # 가맹 사업자 보증금 (1000)
                "jng_bzmn_etc_amt": None,               # 가맹 사업자 기타 금액 (29133)
                "smtn_amt": None                        # 합계 금액 (35633)
            }

            find_interior_cost(brand, year)          # 인테리어 비용
            if brand['brand_nm'] in brand_fntn_info: # 창업 비용
                for key, value in brand_fntn_info[brand['brand_nm']].items():
                    brand[key] = value
            # print(json.dumps(brand, ensure_ascii=False, indent=4)) # json 형식으로 출력

            sql = "INSERT INTO industry (brand_mnno, jnghdqrtrs_rprsv_nm, brand_nm, induty_lclas_nm, induty_mlsfc_nm, majr_gds_nm, fyer_avrg_sls_amt_scope_val, unit_ar_intrr_amt_scope_val, stor_crtra_ar, intrr_amt_scope_val, jng_bzmn_jng_amt, jng_bzmn_edu_amt, jng_bzmn_assrnc_amt, jng_bzmn_etc_amt, smtn_amt) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (brand['brand_mnno'], brand['jnghdqrtrs_rprsv_nm'], brand['brand_nm'], brand['induty_lclas_nm'], brand['induty_mlsfc_nm'], brand['majr_gds_nm'], brand['fyer_avrg_sls_amt_scope_val'], brand['unit_ar_intrr_amt_scope_val'], brand['stor_crtra_ar'], brand['intrr_amt_scope_val'], brand['jng_bzmn_jng_amt'], brand['jng_bzmn_edu_amt'], brand['jng_bzmn_assrnc_amt'], brand['jng_bzmn_etc_amt'], brand['smtn_amt'])
            try:
                cursor.execute(sql, val)
            except Exception as e:
                print(f"Error occurred: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")