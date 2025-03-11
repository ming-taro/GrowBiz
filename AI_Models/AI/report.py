import os
import asyncio
from dotenv import load_dotenv
import pandas as pd
import uuid  # UUID 생성용
import sys

from store.station import fetch_all_data
from store.property import get_property_listings, filter_listings_by_franchise_area
from store.analyze import process_csv_file, filter_franchises_by_cost, adjust_density_scores, calculate_final_scores, \
    search_brand_in_region
from store.user_response import fetch_simulation_response_by_id, update_user_data_from_response
from store.report_creation import process_and_insert_simulation_report

from store.mongo_db_connector import MongoDBConnector

sys.stdout.reconfigure(encoding='utf-8')

load_dotenv()

industry_1franchise_ranking_file_path = ""
simulation_response_collection = MongoDBConnector().get_db()['simulation_response']  # 컬렉션 접근
report_collection = MongoDBConnector().get_db()[os.getenv("REPORT_COLLECTION_NAME")]


# 메인 실행 함수
if __name__ == "__main__":
    try:
        response_id = sys.argv[1]
        print("사용자 응답 ID: ", response_id)
        simulation_response = fetch_simulation_response_by_id(response_id, simulation_response_collection)
        user_data = update_user_data_from_response(simulation_response)

        if simulation_response:
            user_id = simulation_response.get('user_id')

        # 사용자 입력에서 구와 동을 추출 (동을 '역삼'처럼 변환)
        if 'region' in user_data and len(user_data['region'].split(', ')) >= 3:
            gu = user_data['region'].split(', ')[1].strip()  # '강남구' 공백 제거
            dong_prefix = user_data['region'].split(', ')[2].strip()[:2]  # '역삼' 공백 제거
            # print(f"구: {gu}, 동: {dong_prefix}")
        else:
            print("Error: Invalid region format in user_data['region']")

        # gu = ''  # 기본값 설정
        # dong_prefix = ''  # 기본값 설정

        # 3. 산업 카테고리에서 필요한 부분만 추출 ('치킨', '커피' 등)
        if ', ' in user_data['industry']:
            industry_category = user_data['industry'].split(', ')[1].strip()  # '치킨' 부분만 추출
        else:
            industry_category = user_data['industry'].strip()  # 공백 제거 후 industry 그대로 사용

        # 산업 카테고리 출력
        # print(f"Industry category: {industry_category}")

        # 0. 사용자 입력에 따른 CSV 파일 처리 (프랜차이즈 랭킹 매기기)
        csv_file_path = os.path.join('..', 'franchise_rank', 'preprocessing_stage1',
                                     f'{industry_category}_franchise_data_with_trend_10plus.csv')

        if os.path.exists(csv_file_path):
            print(f"{industry_category} 업종에 해당하는 데이터를 성공적으로 불러왔습니다.")

            # CSV 파일 처리 (df_filtered 반환)
            df_filtered = pd.read_csv(csv_file_path)

            # 이후에 랜덤포레스트 모델 학습 및 예측 -> top_franchises 저장
            industry_1franchise_ranking_file_path = process_csv_file(df_filtered, industry_category, user_data)
        else:
            print(f"{csv_file_path} 파일을 찾을 수 없습니다.")
            exit()

        # 1. 매물 리스트 가져오기
        property_listings = get_property_listings(gu, dong_prefix, user_data)
        # 매물 리스트 출력
        # print("\n=== 매물 리스트 (plno) ===")
        # for listing in property_listings:
        #     print(f"매물 ID: {listing['plno']}, 월세: {listing['add_tnth_wunt_amt']}만원, 보증금: {listing['bsc_tnth_wunt_amt']}만원, 주소: {listing['addr']}, 면적: {listing['area2']}평")

        # 2. 프랜차이즈 밀도 계산 후 밀도 리스트 얻기
        densities = search_brand_in_region(gu, dong_prefix, industry_1franchise_ranking_file_path, response_id)  # 밀도 계산 후 지역별 밀도 리스트 반환

        page_size = 500  # 한 번에 가져올 데이터 수 (500개씩 요청)
        # 비동기 실행
        stations, passenger_results = asyncio.run(fetch_all_data(page_size, user_data))  # 비동기 함수 호출 후 반환 값 받기

        if densities:
            # 3. 밀도의 평균과 표준편차 계산 및 밀도 점수 조정
            adjusted_density_scores, mean_density, std_density = adjust_density_scores(densities)
            # 밀도 평균 출력
            # print(f"밀도 평균: {mean_density}, 표준편차: {std_density}")

            # 4. 초기 자본금 조건을 만족하는 프랜차이즈 필터링 (제외된 프랜차이즈 포함)
            filtered_franchises, excluded_franchises = filter_franchises_by_cost(
                user_data['initial_capital'], industry_1franchise_ranking_file_path, response_id)

            # 5. 필터링된 프랜차이즈의 최종 점수 계산
            final_scores = calculate_final_scores(filtered_franchises, adjusted_density_scores)

            # 6. 상위 3개의 프랜차이즈 선택 (청년치킨 포함)
            top_franchises = sorted(final_scores, key=lambda x: x[1], reverse=True)[:3]  # 상위 3개의 프랜차이즈 선택
            # 상위 프랜차이즈 출력
            # print("\n=== 상위 3개 추천 프랜차이즈 ===")
            # for franchise, score in top_franchises:
            #     print(f"{franchise} - 최종 점수: {score:.2f}")

            # 7. 제외된 프랜차이즈 3개를 출력
            # print("\n=== 초기 자본금이 부족해서 제외된 프랜차이즈 3개 ===")
            excluded_franchises_sorted = sorted(
                excluded_franchises,
                key=lambda x: (
                    float(x['initial_cost'].replace('만원', '').replace(',', '').strip()),
                    float(x['business_fee'].replace('만원', '').replace(',', '').strip()),
                    float(x['interior_cost'].replace('만원', '').replace(',', '').strip())
                )
            )[:3]
            for franchise in excluded_franchises_sorted:
                total_cost = (
                        float(franchise['initial_cost'].replace('만원', '').replace(',', '').strip()) +
                        float(franchise['business_fee'].replace('만원', '').replace(',', '').strip()) +
                        float(franchise['interior_cost'].replace('만원', '').replace(',', '').strip())
                )
                # 자본금에서 제외된 프랜차이즈 출력
                # print(f"프랜차이즈: {franchise['store_name']}, 가맹비: {franchise['business_fee']}만원, "
                #     f"초기 비용: {franchise['initial_cost']}만원, 인테리어 비용: {franchise['interior_cost']}만원, "
                #     f"총 비용: {total_cost}만원, 점수: {franchise['score']}")

            # 8. 추천된 프랜차이즈 중에서 매물 필터링 (청년치킨에 해당하는 매물만)
            top_franchise_name = top_franchises[0][0]  # 상위 1개의 프랜차이즈 이름 (청년치킨)
            valid_recommendations = filter_listings_by_franchise_area(property_listings,
                                                                      [store for store in filtered_franchises if
                                                                       store['store_name'] == top_franchise_name])

            # 9. 보증금과 월세가 적은 매물 3개 선택
            top_property_listings = sorted(valid_recommendations,
                                           key=lambda x: (x['property_deposit'], x['property_rent']))[:3]

            # print("\n=== 추천 가능한 매물 (청년치킨에 해당하는 상위 3개) ===")
            # if top_property_listings:
            #     for recommendation in top_property_listings:
            #         print(f"프랜차이즈: {recommendation['franchise_name']}, 점수: {recommendation['franchise_score']}")
            #         print(f"매물 ID: {recommendation['property_id']}, 주소: {recommendation['property_address']}, 월세: {recommendation['property_rent']}만원, 보증금: {recommendation['property_deposit']}만원, 면적: {recommendation['property_area']}평\n")
            # else:
            #     print("조건에 맞는 추천 가능한 매물이 없습니다.")

            process_and_insert_simulation_report(user_data, top_franchises, filtered_franchises, densities,
                                                 mean_density, stations, passenger_results, excluded_franchises_sorted,
                                                 user_id, top_property_listings, response_id,
                                                 report_collection)  # 수정
    except Exception as exception:
        print(f"Error : {exception}")
    finally:
        os.remove(industry_1franchise_ranking_file_path);  # 상위 프랜차이즈 순위 분석 json 파일 삭제
