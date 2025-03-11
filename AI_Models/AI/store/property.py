from .mysql_connector import MySQLConnector


# DB에서 매물 데이터 가져오기
def get_property_listings(gu, dong_prefix, user_data):
    # 사용자 입력에서 주소 필터 생성 ('서울시, 강남구, 역삼동' -> '%서울시 강남구 역삼%')
    address_filter = f"%{gu} {dong_prefix}%"

    connection = MySQLConnector().get_connection()
    with connection.cursor() as cursor:
        query = f"""
        SELECT 
            plno,                  -- 매물 ID
            add_tnth_wunt_amt,      -- 월세
            bsc_tnth_wunt_amt,      -- 보증금
            addr,                  -- 주소
            area2
        FROM 
            KB.property_listing  -- 테이블 명
        WHERE 
            ctgry_cd1_nm = '상가점포'      -- 카테고리 1에서 '상가점포'만
            AND deal_kind_cd_nm = '월세'       -- 거래 유형이 '월세'
            AND addr LIKE %s                  -- 주소 필터 적용 (주소에서 강남구 역삼 포함)
            AND add_tnth_wunt_amt <= %s       -- 사용자 입력 월세 필터
            AND bsc_tnth_wunt_amt <= %s       -- 사용자 입력 보증금 필터
            AND is_first_floor =1
        ORDER BY 
            atcl_reg_dttm DESC;  -- 정렬
        """
        # 파라미터로 주소 필터, 월세, 보증금 전달
        cursor.execute(query, (address_filter, user_data['monthly_rent'], user_data['deposit']))
        results = cursor.fetchall()
        return results


# 동 이름과 면적 가져오기
def get_total_area_from_db(gu, dong_prefix):
    connection = MySQLConnector().get_connection()
    with connection.cursor() as cursor:
        query = """
        SELECT SUM(area) as total_area
        FROM all_district
        WHERE gu_name = %s AND dong_name LIKE %s
        """
        cursor.execute(query, (gu, dong_prefix + '%'))
        result = cursor.fetchone()
        return result['total_area'] if result['total_area'] else 0


# 동 리스트 가져오기
def get_dong_names_from_db(gu, dong_prefix):
    connection = MySQLConnector().get_connection()
    with connection.cursor() as cursor:
        query = """
        SELECT dong_name
        FROM all_district
        WHERE gu_name = %s AND dong_name LIKE %s
        """
        cursor.execute(query, (gu, dong_prefix + '%'))
        results = cursor.fetchall()
        return [row['dong_name'] for row in results]


# 매물 면적과 프랜차이즈 평균 면적을 비교하여 추천할 수 있는 매물 필터링
def filter_listings_by_franchise_area(listings, franchise_data):
    valid_recommendations = []  # 프랜차이즈와 매물이 모두 추천 가능한 리스트

    for franchise in franchise_data:
        try:
            # 프랜차이즈의 표준 스토어 면적을 가져와서 '㎡'를 제거하고 숫자로 변환
            franchise_area_str = franchise.get('standard_store_area', '0').replace('㎡', '').replace(',', '').strip()
            franchise_area = float(franchise_area_str)  # 프랜차이즈 평균 면적 (제곱미터 단위)
        except ValueError:
            print(f"Error converting franchise area: {franchise_area_str}")
            continue

        # 매물과 프랜차이즈의 면적을 비교하여 추천 가능한 매물 필터링
        for listing in listings:
            if listing['area2'] >= franchise_area:  # 매물 면적이 프랜차이즈 요구 면적 이상인 경우
                valid_recommendations.append({
                    'franchise_name': franchise['store_name'],
                    'franchise_score': franchise['score'],
                    'property_id': listing['plno'],
                    'property_address': listing['addr'],
                    'property_rent': listing['add_tnth_wunt_amt'],
                    'property_deposit': listing['bsc_tnth_wunt_amt'],
                    'property_area': listing['area2']  # 매물 면적
                })

    return valid_recommendations