from bson.objectid import ObjectId


# 1. 지역을 선택해주세요.
# 2. 점포 임대 계약 시 수용 가능한 월세
# 3. 점포 임대 계약 시 수용 가능한 보증금
# 4. 업종 중 분류, 대분류 선택
# 5. 보증금을 포함하여, 자본금은 어느 정도 가지고 계신가요?
# 6. 개인창업과 프랜차이즈 중 어느 것을 선호하시나요?
# 7. 가맹비를 크게 신경쓰고 계신가요?     7부터 매우그렇다, 그렇다, 보통, 아니다, 매우 아니다
# 8. 현재 유행 중인 업종을 원하십니까?
# 9. 매출액이 얼마나 중요하신가요?
# 10. 폐업률을 신경 쓰시나요?
# 11. 근처에 같은 브랜드 매장과 경쟁 할 자신 있으신가요?
# 사용자 입력 데이터


# 삽입할 데이터를 정의 (주어진 임시 JSON 데이터)
# simulation_data = {
#     "user_id": "test123",
#     "simulation_response_id": "",
#     "created_at": "",
#     "_class": "com.kb.simulation.dto.report.ResponseReport",
#     "plno_list": [43577, 43588, 43608],
#     "brand_name": "청년치킨",
#     "franchise_score": 85.25,
#     "average_brand_score": 30.32,
#     "industry_density_average": 2.05,
#     "recommended_brand_density": 1.02,
#     "industry_initial_cost": 5000,
#     "recommended_brand_initial_cost": 4500,
#     "industry_total_interior_cost": 12000,
#     "recommended_brand_total_interior_cost": 10000,
#     "industry_opening_rate_average": 3.77,
#     "industry_closing_rate_average": 1.73,
#     "recommended_brand_opening_rate_average": 4.23,
#     "recommended_brand_closing_rate_average": 1.13,
#     "top_3_nearby_stations": [
#         {
#             "station_name": "강남역",
#             "people": 55000,
#             "date": "2024-09-28"
#         },
#         {
#             "station_name": "역삼역",
#             "people": 43000,
#             "date": "2024-09-28"
#         },
#         {
#             "station_name": "선릉역",
#             "people": 75000,
#             "date": "2024-09-28"
#         }
#     ],
#     "recommended_brand_average_sales_per_area": 1800,
#     "recommended_brand_average_sales": 120000,
#     "industry_average_sales_per_area": 1500,
#     "industry_average_sales": 100000,
#     "contract_period": {
#         "initial_contract": 5,
#         "renewal_contract": 3
#     },
#     "additional_recommended_brands": [
#         {
#             "brand_name": "기영이숯불두마리치킨",
#             "franchise_score": 80.5
#         },
#         {
#             "brand_name": "교촌치킨",
#             "franchise_score": 78.2
#         }
#     ],
#     "excluded_brand_due_to_capital": {
#         "brand_name": "구도로통닭",
#         "franchise_score": 75.3,
#         "insufficient_funds": 2500
#     }
# }


def fetch_simulation_response_by_id(simulation_response_id, simulation_response_collection):
    query = {"_id": ObjectId(simulation_response_id)}

    response = simulation_response_collection.find_one(query)

    # 응답 정보 출력
    if response:
        user_id = response.get('user_id', None)  # user_id 추출
        if user_id:
            print(f"User ID: {user_id}")
        else:
            print(f"No user_id found for simulation response ID: {simulation_response_id}")

        # 'answer' 필드에서 데이터 추출
        answers = response.get('answer', {})
        # if answers:
        #     print("User responses:")
        #     for key, value in answers.items():
        #         print(f"Question {key}: {value}")
        # else:
        #     print("No answers found.")

        return response  # response 객체 반환

    else:
        print(f"No simulation response found for ID: {simulation_response_id}")


def update_user_data_from_response(simulation_response):
    # 기본값 설정
    user_data = {
        'region': '',
        'monthly_rent': 0,  # 만원
        'deposit': 0,  # 만원 (1억)
        'industry': '',  # '치킨', '커피' 등 선택
        'initial_capital': 0,  # 만원 (1억)
        'preference': '',
        'franchise_fee_concern': '',  # 가맹비 신경 쓰는 정도
        'trending_industry_preference': '보통',  # 유행 업종 선호도
        'sales_importance': '보통',  # 매출액 중요도
        'closure_rate_concern': '보통',  # 폐업률 신경 정도
        'competition_confidence': '보통'  # 경쟁 자신감
    }

    # simulation_response가 None인지 확인
    if simulation_response is None:
        print("Error: simulation_response is None.")
        return user_data

    # simulation_response가 어떤 구조로 넘어오는지 확인
    # print(f"Received simulation_response: {simulation_response}")

    # 'answer' 필드가 simulation_response에 있는지 확인
    if 'answer' in simulation_response:
        answer = simulation_response['answer']
        # print(f"Answer found in simulation_response: {answer}")
    else:
        print("Error: 'answer' key not found in simulation_response")
        return user_data

    # 지역 (district + neighborhoods) 처리 부분
    try:
        district = answer.get('0', {}).get('district', '알 수 없음')  # 기본값 '알 수 없음' 설정
        neighborhoods = answer.get('0', {}).get('neighborhoods', '알 수 없음')  # 기본값 '알 수 없음' 설정
        user_data['region'] = f"서울시, {district}, {neighborhoods}"
        # 지역 정보 출력
        # print(f"Region updated to: {user_data['region']}")
    except KeyError as e:
        print(f"KeyError in region update: {e}")

    # 월세
    try:
        user_data['monthly_rent'] = int(answer.get('1', {}).get('text', '0'))  # '300' -> 300
        # 월세 정보 출력
        # print(f"Monthly rent updated to: {user_data['monthly_rent']}")
    except KeyError as e:
        print(f"KeyError in monthly_rent update: {e}")

    # 보증금
    try:
        user_data['deposit'] = int(answer.get('2', {}).get('text', '0'))  # '10000' -> 10000
        # 보증금 정보 출력
        # print(f"Deposit updated to: {user_data['deposit']}")
    except KeyError as e:
        print(f"KeyError in deposit update: {e}")

    # 업종 (category + subcategories)
    try:
        category = answer.get('3', {}).get('category', '')
        subcategories = answer.get('3', {}).get('subcategories', '')  # 기본값으로 빈 문자열 설정
        user_data['industry'] = f"{category}, {subcategories}".strip(', ')
        # 업종 정보 출력
        # print(f"Industry updated to: {user_data['industry']}")
    except KeyError as e:
        print(f"KeyError in industry update: {e}")

    # 초기 자본금
    try:
        user_data['initial_capital'] = int(answer.get('4', {}).get('text', '0'))
        # 초기 자본금 정보 출력
        # print(f"Initial capital updated to: {user_data['initial_capital']}")
    except KeyError as e:
        print(f"KeyError in initial_capital update: {e}")

    # 프랜차이즈 선호도
    try:
        user_data['preference'] = answer.get('5', {}).get('text', '')
        # 프랜차이즈 선호도 출력
        # print(f"Preference updated to: {user_data['preference']}")
    except KeyError as e:
        print(f"KeyError in preference update: {e}")

    # 가맹비 신경 정도
    try:
        user_data['franchise_fee_concern'] = answer.get('6', {}).get('text', '')
        # 가맹비 신경 정도 출력
        # print(f"Franchise fee concern updated to: {user_data['franchise_fee_concern']}")
    except KeyError as e:
        print(f"KeyError in franchise_fee_concern update: {e}")

    # 유행 업종 선호도
    try:
        user_data['trending_industry_preference'] = answer.get('7', {}).get('text', '')
        # 유행 업종 선호도 출력
        # print(f"Trending industry preference updated to: {user_data['trending_industry_preference']}")
    except KeyError as e:
        print(f"KeyError in trending_industry_preference update: {e}")

    # 매출액 중요도
    try:
        user_data['sales_importance'] = answer.get('8', {}).get('text', '')
        # 매출액 중요도 출력
        # print(f"Sales importance updated to: {user_data['sales_importance']}")
    except KeyError as e:
        print(f"KeyError in sales_importance update: {e}")

    # 폐업률 신경 정도
    try:
        user_data['closure_rate_concern'] = answer.get('9', {}).get('text', '')
        # 폐업률 신경 정도 출력
        # print(f"Closure rate concern updated to: {user_data['closure_rate_concern']}")
    except KeyError as e:
        print(f"KeyError in closure_rate_concern update: {e}")

    # 경쟁 자신감
    try:
        user_data['competition_confidence'] = answer.get('10', {}).get('text', '')
        # 경쟁 자신감 출력
        # print(f"Competition confidence updated to: {user_data['competition_confidence']}")
    except KeyError as e:
        print(f"KeyError in competition_confidence update: {e}")

    return user_data
