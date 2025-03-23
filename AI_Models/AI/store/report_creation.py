from datetime import datetime
import json


def process_and_insert_simulation_report(user_data, top_franchises, filtered_franchises, densities, mean_density,
                                         stations, passenger_results, excluded_franchises_sorted, user_id,
                                         top_property_listings, simulation_response_id,
                                         report_collection):
    # 1. 사용자 입력 및 처리된 데이터를 기반으로 한 실제 데이터 준비
    def convert_to_float(value):
        try:
            # '만원' 또는 ',' 등의 문자를 제거하고 float로 변환
            return float(value.replace('만원', '').replace(',', ''))
        except (ValueError, AttributeError):
            return 0.0  # 변환에 실패하면 0.0 반환

    def convert_to_float1(value):
        try:
            # '만원' 또는 ',' 등의 문자를 제거하고 float로 변환
            return float(value.replace('%', '').replace(',', ''))
        except (ValueError, AttributeError):
            return 0.0  # 변환에 실패하면 0.0 반환

    # 업종 평균값을 계산하기 위한 리스트 생성 (문자열을 float로 변환)
    average_sales_list = [convert_to_float(franchise['average_sales']) for franchise in filtered_franchises]
    average_sales_per_area_list = [convert_to_float(franchise['average_sales_per_area']) for franchise in
                                   filtered_franchises]
    initial_cost_list = [convert_to_float(franchise['initial_cost']) for franchise in filtered_franchises]
    interior_cost_list = [convert_to_float(franchise['interior_cost']) for franchise in filtered_franchises]
    # 업종 평균값 계산
    industry_average_sales = sum(average_sales_list) / len(average_sales_list)
    industry_average_sales_per_area = sum(average_sales_per_area_list) / len(average_sales_per_area_list)
    industry_initial_cost = sum(initial_cost_list) / len(initial_cost_list)
    industry_total_interior_cost = sum(interior_cost_list) / len(interior_cost_list)

    # 개업률과 폐업률의 평균 계산 추가
    # 폐업률과 개업률의 평균을 계산
    opening_rate_list = [convert_to_float1(franchise['opening_rate']) for franchise in filtered_franchises]
    closure_rate_list = [convert_to_float1(franchise['closure_rate']) for franchise in filtered_franchises]
    industry_opening_rate_average = sum(opening_rate_list) / len(opening_rate_list)
    industry_closing_rate_average = sum(closure_rate_list) / len(closure_rate_list)

    # formatted_industry_opening_rate = f"{industry_opening_rate_average:.2f}%"
    # formatted_industry_closing_rate = f"{industry_closing_rate_average:.2f}%"

    simulation_data = {
        "user_id": str(user_id),  # 사용자 ID
        "simulation_response_id": simulation_response_id,  # MongoDB에서 가져온 simulation_response_id 사용
        "created_at": "",  # 나중에 채워질 생성 시간
        "_class": "com.kb.simulation.dto.report.ResponseReport",  # 클래스 이름
        "brand_name": top_franchises[0][0],  # 상위 1위 프랜차이즈 이름
        "franchise_score": top_franchises[0][1],  # 해당 프랜차이즈의 점수
        "recommended_brand_density": densities[0],  # 계산된 밀도
        "industry_density_average": mean_density,  # 전체 밀도 평균

        # 여기서는 filtered_franchises에서 가져와야 함
        "recommended_brand_initial_cost": filtered_franchises[0]['initial_cost'],  # 프랜차이즈 초기 비용
        "recommended_brand_total_interior_cost": filtered_franchises[0]['interior_cost'],  # 인테리어 비용
        "recommended_brand_average_sales": filtered_franchises[0]['average_sales'],  # 평균 매출
        "recommended_brand_average_sales_per_area": filtered_franchises[0]['average_sales_per_area'],  # 평당 매출

        "industry_opening_rate_average": industry_opening_rate_average,  # 산업의 평균 개업률
        "industry_closing_rate_average": industry_closing_rate_average,  # 산업의 평균 폐업률
        "recommended_brand_opening_rate_average": filtered_franchises[0]['opening_rate'],  # 추천 브랜드 개업률
        "recommended_brand_closing_rate_average": filtered_franchises[0]['closure_rate'],  # 추천 브랜드 폐업률

        # 추가된 업종 평균 데이터
        "industry_average_sales": industry_average_sales,  # 업종 평균 매출
        "industry_average_sales_per_area": industry_average_sales_per_area,  # 업종 평당 매출액
        "industry_initial_cost": industry_initial_cost,  # 업종 초기 비용
        "industry_total_interior_cost": industry_total_interior_cost,  # 업종 인테리어 비용

        "top_3_nearby_stations": [  # 가까운 3개의 역 정보
            {"station_name": station, "people": passengers}
            for station, passengers in zip(stations, passenger_results)
        ],

        # top_listings에서 매물 정보 가져오기
        # "additional_recommended_brands": [ # 수정한 부분
        "top_property_listings": [
            {
                "franchise_name": recommendation['franchise_name'],
                "property_id": recommendation['property_id'],
                "property_address": recommendation['property_address'],
                "monthly_rent": recommendation['property_rent'],
                "deposit": recommendation['property_deposit'],
                "area": recommendation['property_area']
            }
            for recommendation in top_property_listings[:3]  # 최대 3개의 추천 매물 정보
        ],

        # ====================additional_recommended_brands==============================
        "additional_recommended_brands": [  # 가까운 3개의 역 정보
            {"brand_name": brand_name, "franchise_score": score}
            for brand_name, score in top_franchises[1:]
        ]
        # ====================additional_recommended_brands==============================
    }

    # 추천 비용(recommended_cost) 계산: 사용자 자금에서 인테리어비와 가맹비를 뺀 값
    recommended_cost = convert_to_float(filtered_franchises[0]['initial_cost']) + convert_to_float(
        filtered_franchises[0]['interior_cost'])
    simulation_data["recommended_cost"] = recommended_cost

    # excluded_franchises_sorted가 비어 있지 않은지 확인
    if excluded_franchises_sorted:
        # 문자열을 float로 변환하여 계산
        excluded_brand = {
            "brand_name": excluded_franchises_sorted[0]['store_name'],
            "franchise_score": excluded_franchises_sorted[0]['score'],
            "insufficient_funds": (
                                          float(excluded_franchises_sorted[0]['initial_cost'].replace('만원', '').replace(
                                              ',', '')) +
                                          float(excluded_franchises_sorted[0]['business_fee'].replace('만원', '').replace(
                                              ',', '')) +
                                          float(
                                              excluded_franchises_sorted[0]['interior_cost'].replace('만원', '').replace(
                                                  ',', ''))
                                  ) - user_data['initial_capital']
        }
        simulation_data["excluded_brand_due_to_capital"] = excluded_brand
    else:
        simulation_data["excluded_brand_due_to_capital"] = "No excluded franchises due to capital"

    # 데이터 출력 확인
    # print("\n=== Simulation Data ===")
    # for key, value in simulation_data.items():
    #     print(f"{key}: {value}")

    simulation_data['top_3_nearby_stations'] = sorted(simulation_data['top_3_nearby_stations'],
                                                      key=lambda x: x['people'], reverse=True)

    # 근처 역 정보 3개 출력
    # print("\nTop 3 Nearby Stations:")
    # for station in simulation_data['top_3_nearby_stations']:
    #     print(f"Station Name: {station['station_name']}, People: {station['people']}")

    # 추가 추천 브랜드 정보 출력
    # print("\nAdditional Recommended Brands:")
    # print("\nTop Listings:")
    # for brand in simulation_data['additional_recommended_brands']:
    # for brand in simulation_data['top_property_listings']:
    #     print(f"Franchise Name: {brand['franchise_name']}, Property ID: {brand['property_id']}, Address: {brand['property_address']}, Monthly Rent: {brand['monthly_rent']}, Deposit: {brand['deposit']}, Area: {brand['area']}")

    # print("\nExcluded Brand Due to Capital:")
    excluded_brand = simulation_data['excluded_brand_due_to_capital']

    # 2. 데이터를 JSON 파일로 저장
    json_file_path = 'simulation_data.json'
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(simulation_data, json_file, ensure_ascii=False, indent=4)

    print(f"Data saved to '{json_file_path}' for verification.")

    # 생성 시간 추가
    simulation_data['created_at'] = datetime.utcnow().isoformat()

    # UUID 생성
    simulation_data['simulation_response_id'] = simulation_response_id

    # MongoDB에 데이터 삽입
    result = report_collection.insert_one(simulation_data)

    if result.inserted_id:
        print(f"Inserted document with ID: {result.inserted_id}")
    else:
        print("Error inserting document")