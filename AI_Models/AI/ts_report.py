import json
import os
import requests
import pymysql
import asyncio
import aiohttp
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
from dotenv import load_dotenv
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
from pymongo import MongoClient
import uuid  # UUID 생성용
from bson.objectid import ObjectId

# .env 파일에서 API 키 및 DB 정보 불러오기
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")
db = client[MONGO_DB_NAME]  # 여기는 데이터베이스 객체를 가져오는 부분입니다.
simulation_response_collection = db['simulation_response']  # 컬렉션에 접근
report_collection=db['report']

def fetch_simulation_response_by_id(simulation_response_id):
    query = {"_id": ObjectId(simulation_response_id)}

    response = simulation_response_collection.find_one(query)

    if response:
        user_id = response.get('user_id', None)  # user_id 추출
        if user_id:
            print(f"User ID: {user_id}")
        else:
            print(f"No user_id found for simulation response ID: {simulation_response_id}")
        
        # 'answer' 필드에서 데이터 추출
        answers = response.get('answer', {})
        if answers:
            print("User responses:")
            for key, value in answers.items():
                print(f"Question {key}: {value}")
        else:
            print("No answers found.")
            
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
    print(f"Received simulation_response: {simulation_response}")

    # 'answer' 필드가 simulation_response에 있는지 확인
    if 'answer' in simulation_response:
        answer = simulation_response['answer']
        print(f"Answer found in simulation_response: {answer}")
    else:
        print("Error: 'answer' key not found in simulation_response")
        return user_data

    # 지역 (district + neighborhoods) 처리 부분
    try:
        district = answer.get('0', {}).get('district', '알 수 없음')  # 기본값 '알 수 없음' 설정
        neighborhoods = answer.get('0', {}).get('neighborhoods', '알 수 없음')  # 기본값 '알 수 없음' 설정
        user_data['region'] = f"서울시, {district}, {neighborhoods}"
        print(f"Region updated to: {user_data['region']}")
    except KeyError as e:
        print(f"KeyError in region update: {e}")

    # 월세
    try:
        user_data['monthly_rent'] = int(answer.get('1', {}).get('text', '0'))  # '300' -> 300
        print(f"Monthly rent updated to: {user_data['monthly_rent']}")
    except KeyError as e:
        print(f"KeyError in monthly_rent update: {e}")

    # 보증금
    try:
        user_data['deposit'] = int(answer.get('2', {}).get('text', '0'))  # '10000' -> 10000
        print(f"Deposit updated to: {user_data['deposit']}")
    except KeyError as e:
        print(f"KeyError in deposit update: {e}")

    # 업종 (category + subcategories)
    try:
        category = answer.get('3', {}).get('category', '')
        subcategories = answer.get('3', {}).get('subcategories', '')  # 기본값으로 빈 문자열 설정
        user_data['industry'] = f"{category}, {subcategories}".strip(', ')
        print(f"Industry updated to: {user_data['industry']}")
    except KeyError as e:
        print(f"KeyError in industry update: {e}")

    # 초기 자본금
    try:
        user_data['initial_capital'] = int(answer.get('4', {}).get('text', '0'))
        print(f"Initial capital updated to: {user_data['initial_capital']}")
    except KeyError as e:
        print(f"KeyError in initial_capital update: {e}")

    # 프랜차이즈 선호도
    try:
        user_data['preference'] = answer.get('5', {}).get('text', '')
        print(f"Preference updated to: {user_data['preference']}")
    except KeyError as e:
        print(f"KeyError in preference update: {e}")

    # 가맹비 신경 정도
    try:
        user_data['franchise_fee_concern'] = answer.get('6', {}).get('text', '')
        print(f"Franchise fee concern updated to: {user_data['franchise_fee_concern']}")
    except KeyError as e:
        print(f"KeyError in franchise_fee_concern update: {e}")

    # 유행 업종 선호도
    try:
        user_data['trending_industry_preference'] = answer.get('7', {}).get('text', '')
        print(f"Trending industry preference updated to: {user_data['trending_industry_preference']}")
    except KeyError as e:
        print(f"KeyError in trending_industry_preference update: {e}")

    # 매출액 중요도
    try:
        user_data['sales_importance'] = answer.get('8', {}).get('text', '')
        print(f"Sales importance updated to: {user_data['sales_importance']}")
    except KeyError as e:
        print(f"KeyError in sales_importance update: {e}")

    # 폐업률 신경 정도
    try:
        user_data['closure_rate_concern'] = answer.get('9', {}).get('text', '')
        print(f"Closure rate concern updated to: {user_data['closure_rate_concern']}")
    except KeyError as e:
        print(f"KeyError in closure_rate_concern update: {e}")

    # 경쟁 자신감
    try:
        user_data['competition_confidence'] = answer.get('10', {}).get('text', '')
        print(f"Competition confidence updated to: {user_data['competition_confidence']}")
    except KeyError as e:
        print(f"KeyError in competition_confidence update: {e}")

    return user_data



# MongoDB 클라이언트 설정
client = MongoClient(MONGO_URI)
db = client[MONGO_DB_NAME]

KAKAO_API_KEY = os.getenv("KAKAO_API_KEY")
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

business_api_key = os.getenv('BUSINESS_API_KEY')
passenger_api_key = os.getenv('PASSENGER_API_KEY')
kakao_api_key = os.getenv('KAKAO_API_KEY')

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

def process_and_insert_simulation_report(user_data, top_franchises, filtered_franchises, densities, mean_density, std_density, stations, passenger_results, excluded_franchises_sorted, user_id, top_listings):
    # 1. 사용자 입력 및 처리된 데이터를 기반으로 한 실제 데이터 준비
    def convert_to_float(value):
        try:
            # '만원' 또는 ',' 등의 문자를 제거하고 float로 변환
            return float(value.replace('만원', '').replace(',', ''))
        except (ValueError, AttributeError):
            return 0.0  # 변환에 실패하면 0.0 반환
    
    # 업종 평균값을 계산하기 위한 리스트 생성 (문자열을 float로 변환)
    average_sales_list = [convert_to_float(franchise['average_sales']) for franchise in filtered_franchises]
    average_sales_per_area_list = [convert_to_float(franchise['average_sales_per_area']) for franchise in filtered_franchises]
    initial_cost_list = [convert_to_float(franchise['initial_cost']) for franchise in filtered_franchises]
    interior_cost_list = [convert_to_float(franchise['interior_cost']) for franchise in filtered_franchises]

    # 업종 평균값 계산
    industry_average_sales = sum(average_sales_list) / len(average_sales_list)
    industry_average_sales_per_area = sum(average_sales_per_area_list) / len(average_sales_per_area_list)
    industry_initial_cost = sum(initial_cost_list) / len(initial_cost_list)
    industry_total_interior_cost = sum(interior_cost_list) / len(interior_cost_list)

    simulation_data = {
        "user_id": str(user_id),  # 사용자 ID
        "simulation_response_id": str(simulation_response['_id']),  # MongoDB에서 가져온 simulation_response_id 사용
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

        "industry_opening_rate_average": mean_density,  # 산업의 평균 개업률
        "industry_closing_rate_average": std_density,  # 산업의 평균 폐업률
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
        "additional_recommended_brands": [
            {
                "franchise_name": recommendation['franchise_name'],
                "property_id": recommendation['property_id'],
                "property_address": recommendation['property_address'],
                "monthly_rent": recommendation['property_rent'],
                "deposit": recommendation['property_deposit'],
                "area": recommendation['property_area']
            }
            for recommendation in top_listings[:3]  # 최대 3개의 추천 매물 정보
        ]
    }

    # 추천 비용(recommended_cost) 계산: 사용자 자금에서 인테리어비와 가맹비를 뺀 값
    recommended_cost = user_data['initial_capital'] - convert_to_float(filtered_franchises[0]['initial_cost']) - convert_to_float(filtered_franchises[0]['interior_cost'])
    simulation_data["recommended_cost"] = recommended_cost

    # excluded_franchises_sorted가 비어 있지 않은지 확인
    if excluded_franchises_sorted:
        # 문자열을 float로 변환하여 계산
        excluded_brand = {
            "brand_name": excluded_franchises_sorted[0]['store_name'],
            "franchise_score": excluded_franchises_sorted[0]['score'],
            "insufficient_funds": (
                float(excluded_franchises_sorted[0]['initial_cost'].replace('만원', '').replace(',', '')) +
                float(excluded_franchises_sorted[0]['business_fee'].replace('만원', '').replace(',', '')) +
                float(excluded_franchises_sorted[0]['interior_cost'].replace('만원', '').replace(',', ''))
            ) - user_data['initial_capital']
        }
        simulation_data["excluded_brand_due_to_capital"] = excluded_brand
    else:
        simulation_data["excluded_brand_due_to_capital"] = "No excluded franchises due to capital"

    # 데이터 출력 확인
    print("\n=== Simulation Data ===")
    for key, value in simulation_data.items():
        print(f"{key}: {value}")

    print("\nTop 3 Nearby Stations:")
    for station in simulation_data['top_3_nearby_stations']:
        print(f"Station Name: {station['station_name']}, People: {station['people']}")

    print("\nAdditional Recommended Brands:")
    for brand in simulation_data['additional_recommended_brands']:
        print(f"Franchise Name: {brand['franchise_name']}, Property ID: {brand['property_id']}, Address: {brand['property_address']}, Monthly Rent: {brand['monthly_rent']}, Deposit: {brand['deposit']}, Area: {brand['area']}")

    print("\nExcluded Brand Due to Capital:")
    excluded_brand = simulation_data['excluded_brand_due_to_capital']

    # 2. 데이터를 JSON 파일로 저장
    json_file_path = 'simulation_data.json'
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(simulation_data, json_file, ensure_ascii=False, indent=4)

    print(f"Data saved to '{json_file_path}' for verification.")

    # 생성 시간 추가
    simulation_data['created_at'] = datetime.utcnow().isoformat()

    # UUID 생성
    simulation_data['simulation_response_id'] = str(ObjectId())

    # MongoDB에 데이터 삽입
    result = report_collection.insert_one(simulation_data)

    if result.inserted_id:
        print(f"Inserted document with ID: {result.inserted_id}")
    else:
        print("Error inserting document")




# # 사용자 입력에서 구와 동을 추출 (동을 '역삼'처럼 변환)
# gu = user_data['region'].split(', ')[1]  # '강남구'
# dong_prefix = user_data['region'].split(', ')[2][:2]  # '역삼'

# # 산업 카테고리에서 필요한 부분만 추출 ('치킨', '커피' 등)
# industry_category = user_data['industry'].split(', ')[1]  # '치킨' 부분만 추출

# # .csv 파일 경로 설정
# csv_file_path = os.path.join('..', 'franchise_rank', 'preprocessing_stage1', f'{industry_category}_franchise_data_with_trend_10plus.csv')

# # .csv 파일이 존재하는지 확인 후 읽기
# if os.path.exists(csv_file_path):
#     df = pd.read_csv(csv_file_path)
#     print(f"{industry_category} 업종에 해당하는 데이터를 성공적으로 불러왔습니다.")
# else:
#     print(f"{csv_file_path} 파일을 찾을 수 없습니다.")


def process_csv_file(df_filtered, category):
    # 필요한 열 선택
    columns = ['store_name', 'year', 'region', 'opening_rate', 'closure_rate', 'average_sales', 'average_sales_per_area', 
               'initial_cost', 'business_fee', 'interior_cost', 'standard_store_area']

    df_filtered = df_filtered[columns].copy()

    # 스케일링 이전 원래 값 저장 (복원용)
    original_values = df_filtered.copy()

    # MinMaxScaler로 0과 1 사이로 스케일링 적용
    scaler = MinMaxScaler()
    scaled_columns = ['opening_rate', 'closure_rate', 'average_sales_per_area', 'initial_cost']
    df_filtered[scaled_columns] = scaler.fit_transform(df_filtered[scaled_columns])

    # 가중치 설정
    weight_map = {
        '매우 그렇다': 0.5,
        '그렇다': 0.4,
        '보통': 0.3,
        '아니다': 0.2,
        '매우 아니다': 0.1
    }

    # 사용자 입력에 따른 가중치 적용
    weights = {
        'franchise_fee': weight_map[user_data['franchise_fee_concern']],
        'trending': weight_map[user_data['trending_industry_preference']],
        'sales': weight_map[user_data['sales_importance']],
        'closure_rate': weight_map[user_data['closure_rate_concern']],
    }

    # 개업률(opening_rate)은 높을수록 좋으므로 가중치를 더합니다.
    df_filtered['opening_rate'] += weights['trending']
    
    # 폐업률(closure_rate)은 낮을수록 좋으므로 1에서 폐업률을 빼고 가중치를 더해줍니다.
    df_filtered['closure_rate'] = (1 - df_filtered['closure_rate']) * weights['closure_rate']
    
    # 평균 매출액(average_sales_per_area)은 높을수록 좋으므로 가중치를 더합니다.
    df_filtered['average_sales_per_area'] += weights['sales']
    
    # 초기 비용(initial_cost)은 낮을수록 좋으므로, 1에서 초기비용을 빼고 가중치를 더해줍니다.
    df_filtered['initial_cost'] = (1 - df_filtered['initial_cost']) * weights['franchise_fee']

    # 스케일링된 X 값 출력 (디버깅용)
    print("\n=== X values (scaled independent variables) ===")
    print(df_filtered[['opening_rate', 'closure_rate', 'average_sales_per_area', 'initial_cost']].head())

    # 독립 변수(X)와 종속 변수(y) 설정
    X = df_filtered[['opening_rate', 'closure_rate', 'average_sales_per_area', 'initial_cost']]

    # 가중치가 가장 높은 변수에 따라 y 변수를 설정
    max_weight = max(weights, key=weights.get)  # 가중치가 가장 큰 변수 확인

    # 가중치가 가장 큰 변수를 종속 변수(y)로 설정
    if max_weight == 'trending':
        y = df_filtered['opening_rate']  # 개업률
    elif max_weight == 'closure_rate':
        y = df_filtered['closure_rate']  # 폐업률
    elif max_weight == 'sales':
        y = df_filtered['average_sales_per_area']  # 매출액
    elif max_weight == 'franchise_fee':
        y = df_filtered['initial_cost']  # 초기비용

    print(f"종속 변수 y는 '{max_weight}'로 선택되었습니다.")

    # 랜덤포레스트 모델 학습
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    rf = RandomForestRegressor()
    rf.fit(X_train, y_train)

    # 예측 점수 계산
    df_filtered['predicted_score'] = rf.predict(X)

    # 점수를 100점 만점으로 정규화
    max_score = df_filtered['predicted_score'].max()
    df_filtered['normalized_score'] = (df_filtered['predicted_score'] / max_score) * 100

    # 원래 값을 그대로 사용하여 출력 (original_values에 저장된 값)
    df_filtered['average_sales'] = original_values['average_sales'] / 10  # 만원 단위로 복원
    df_filtered['average_sales_per_area'] = original_values['average_sales_per_area'] / 10  # 만원 단위로 복원
    df_filtered['initial_cost'] = original_values['initial_cost'] / 10  # 만원 단위로 복원
    df_filtered['business_fee'] = original_values['business_fee'] / 10  # 만원 단위로 복원
    df_filtered['interior_cost'] = original_values['interior_cost'] / 10  # 만원 단위로 복원
    df_filtered['closure_rate'] = original_values['closure_rate'] / 100  # 폐업률 원래 값 복원
    df_filtered['opening_rate'] = original_values['opening_rate'] / 100  # 개업률 원래 값 복원

    # 상위 30개의 데이터 선택
    top_franchises = df_filtered.sort_values(by='normalized_score', ascending=False).head(30)


    #여기에 상위 30개의 브랜드에서 폐업률 평균이랑, 개업률 평균치 , 평균 매출액,initial_cost의 평균 인테리어 평균 도 가져와줘.
    # 상위 30개의 브랜드에서 평균값 계산
    avg_closure_rate = top_franchises['closure_rate'].mean()
    avg_opening_rate = top_franchises['opening_rate'].mean()
    avg_average_sales = top_franchises['average_sales'].mean()
    avg_initial_cost = top_franchises['initial_cost'].mean()
    avg_interior_cost = top_franchises['interior_cost'].mean()

    print("\n=== 상위 30개의 브랜드 평균 ===")
    print(f"폐업률 평균: {avg_closure_rate * 100:.2f}%")
    print(f"개업률 평균: {avg_opening_rate * 100:.2f}%")
    print(f"평균 매출액: {avg_average_sales:.2f} 만원")
    print(f"초기 비용 평균: {avg_initial_cost:.2f} 만원")
    print(f"인테리어 비용 평균: {avg_interior_cost:.2f} 만원")
    
    # 결과 출력
    for idx, row in enumerate(top_franchises.itertuples(index=False), 1):
        print(f"{idx}. {row.store_name}, 폐업률: {row.closure_rate * 100:.2f}%, 개업률: {row.opening_rate * 100:.2f}%, "
              f"1년 평균 매출액: {row.average_sales:.2f} 만원, 1평당 매출액: {row.average_sales_per_area:.2f} 만원, "
              f"가맹비: {row.initial_cost:.2f} 만원, 가맹 보험비: {row.business_fee:.2f} 만원, 인테리어 비용: {row.interior_cost:.2f} 만원, "
              f"표준 스토어 면적: {row.standard_store_area} ㎡, 점수: {row.normalized_score:.2f}")

    # JSON 파일 저장
    results = []
    for idx, row in enumerate(top_franchises.itertuples(index=False)):
        results.append({
            "rank": idx + 1,
            "store_name": row.store_name,
            "year": row.year,
            "region": row.region,
            "opening_rate": f"{row.opening_rate * 100:.2f}%",
            "closure_rate": f"{row.closure_rate * 100:.2f}%",
            "average_sales": f"{row.average_sales:.2f} 만원",
            "average_sales_per_area": f"{row.average_sales_per_area:.2f} 만원",
            "initial_cost": f"{row.initial_cost:.2f} 만원",
            "business_fee": f"{row.business_fee:.2f} 만원",
            "interior_cost": f"{row.interior_cost:.2f} 만원",
            "standard_store_area": f"{row.standard_store_area} ㎡",
            "score": f"{row.normalized_score:.2f}"
        })

    output_folder = os.path.join('..', 'franchise_rank', 'preprocessing_stage2')
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    json_file_name = f"{category}_1franchise_ranking.json"
    json_file_path = os.path.join(output_folder, json_file_name)
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(results, json_file, ensure_ascii=False, indent=4)

    print(f"Data saved to '{json_file_path}'")

    # JSON 형식으로 저장할 데이터 구성
    results = []
    for idx, row in enumerate(top_franchises.itertuples(index=False)):
        results.append({
            "rank": idx + 1,
            "store_name": row.store_name,
            "year": row.year,
            "region": row.region,
            "opening_rate": f"{row.opening_rate * 100:.2f}%",
            "closure_rate": f"{row.closure_rate * 100:.2f}%",
            "average_sales": f"{row.average_sales:.2f} 만원",
            "average_sales_per_area": f"{row.average_sales_per_area:.2f} 만원",
            "initial_cost": f"{row.initial_cost:.2f} 만원",
            "business_fee": f"{row.business_fee:.2f} 만원",
            "interior_cost": f"{row.interior_cost:.2f} 만원",
            "standard_store_area": f"{row.standard_store_area} ㎡",
            "score": f"{row.normalized_score:.2f}"
        })

    # JSON 파일 경로 설정
    output_folder = os.path.join('..', 'franchise_rank', 'preprocessing_stage2')
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    json_file_name = f"{category}_1franchise_ranking.json"
    json_file_path = os.path.join(output_folder, json_file_name)
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(results, json_file, ensure_ascii=False, indent=4)

    print(f"Data saved to '{json_file_path}'")


# 치킨 프랜차이즈 데이터를 json 파일에서 읽기
def load_franchise_data(industry):
    # 산업 카테고리에 맞는 JSON 파일을 불러옴
    json_file_path = os.path.join('..', 'franchise_rank', 'preprocessing_stage2', f'{industry}_1franchise_ranking.json')
    
    if os.path.exists(json_file_path):
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    else:
        print(f"{industry}_1franchise_ranking.json 파일을 찾을 수 없습니다.")
        return []

# MySQL DB 연결 함수
def connect_to_db():
    connection = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

# DB에서 매물 데이터 가져오기
def get_property_listings():
    # 사용자 입력에서 주소 필터 생성 ('서울시, 강남구, 역삼동' -> '%서울시 강남구 역삼%')
    address_filter = f"%{gu} {dong_prefix}%"
    
    connection = connect_to_db()
    try:
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
    finally:
        connection.close()

# 동 이름과 면적 가져오기
def get_total_area_from_db(gu, dong_prefix):
    connection = connect_to_db()
    try:
        with connection.cursor() as cursor:
            query = """
            SELECT SUM(area) as total_area
            FROM all_district
            WHERE gu_name = %s AND dong_name LIKE %s
            """
            cursor.execute(query, (gu, dong_prefix + '%'))
            result = cursor.fetchone()
            return result['total_area'] if result['total_area'] else 0
    finally:
        connection.close()

# 동 리스트 가져오기
def get_dong_names_from_db(gu, dong_prefix):
    connection = connect_to_db()
    try:
        with connection.cursor() as cursor:
            query = """
            SELECT dong_name
            FROM all_district
            WHERE gu_name = %s AND dong_name LIKE %s
            """
            cursor.execute(query, (gu, dong_prefix + '%'))
            results = cursor.fetchall()
            return [row['dong_name'] for row in results]
    finally:
        connection.close()

# 카카오 맵 API로 가게 검색
def search_store_kakao(gu, dong_list, store_name):
    headers = {"Authorization": f"KakaoAK {KAKAO_API_KEY}"}
    total_places = []

    for dong in dong_list:
        query = f"{gu} {dong} {store_name}"
        url = f"https://dapi.kakao.com/v2/local/search/keyword.json?query={query}"
        
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            places = response.json().get('documents', [])
            total_places.extend(places)
        else:
            print(f"Error {response.status_code}: {response.text}")
    
    return total_places

# 브랜드 별로 검색 후 밀도 구하기
def search_brand_in_region():
    franchise_data = load_franchise_data(industry_category)  # 산업 카테고리에 맞는 데이터 불러오기
    dong_list = get_dong_names_from_db(gu, dong_prefix)

    if not dong_list:
        print(f"{gu}에 '{dong_prefix}'로 시작하는 동을 찾을 수 없습니다.")
        return []

    total_area = get_total_area_from_db(gu, dong_prefix)

    if total_area == 0:
        print(f"{gu} {dong_prefix}에 대한 면적 정보를 찾을 수 없습니다.")
        return []

    print(f"{gu}의 '{dong_prefix}'로 시작하는 동 목록: {dong_list}")
    print(f"총 면적은 {total_area} km² 입니다.\n")

    densities = []  # 밀도 리스트를 저장할 배열

    for store in franchise_data:
        store_name = store['store_name']
        places = search_store_kakao(gu, dong_list, store_name)
        store_count = len(places)
        if store_count > 0:
            density = store_count / total_area  # 밀도 계산
            densities.append(density)  # 밀도를 리스트에 저장
            print(f"{store_name}가 {gu}의 '{dong_prefix}'로 시작하는 동들에 {store_count}개 있습니다. 밀도: {density:.2f} 가게/km²")
        else:
            densities.append(0)  # 밀도가 없을 경우 0으로 처리
            print(f"{store_name}가 {gu}의 '{dong_prefix}'로 시작하는 동들에 없습니다.")
    
    return densities  # 계산된 밀도 리스트 반환


# 보증금과 초기 자본금 조건을 만족하는지 확인하는 함수
def filter_franchises_by_cost(initial_capital):
    franchise_data = load_franchise_data(industry_category)  # JSON 파일에서 프랜차이즈 데이터 가져오기
    filtered_franchises = []
    excluded_franchises = []
    
    for store in franchise_data:
        initial_cost = float(store['initial_cost'].replace('만원', '').replace(',', ''))  # 초기 비용 변환
        business_fee = float(store['business_fee'].replace('만원', '').replace(',', ''))  # 가맹비 변환
        interior_cost = float(store['interior_cost'].replace('만원', '').replace(',', ''))  # 인테리어 비용 변환
        
        # 조건: 초기 비용 + 가맹비 + 인테리어 비용 <= 사용자가 입력한 자본금
        total_initial_cost = initial_cost + business_fee + interior_cost
        
        if total_initial_cost <= initial_capital:
            filtered_franchises.append(store)  # 조건 만족
        else:
            excluded_franchises.append(store)  # 조건 불만족 (제외됨)
    
    return filtered_franchises, excluded_franchises


# 밀도 계산 후 조정하는 함수
def adjust_density_scores(densities):
    mean_density = np.mean(densities)
    std_density = np.std(densities)
    
    adjusted_scores = []
    for density in densities:
        if density < mean_density:
            # 평균보다 밀도가 작으면 가산점
            score_adjustment = 1 + (mean_density - density) / std_density
        else:
            # 평균보다 크면 감점
            score_adjustment = 1 - (density - mean_density) / std_density
        
        adjusted_scores.append(score_adjustment)
    
    return adjusted_scores, mean_density, std_density

# 밀도 점수와 기존 랭킹 점수를 결합하여 최종 점수를 계산
def calculate_final_scores(franchise_data, adjusted_density_scores):
    final_scores = []
    for i, store in enumerate(franchise_data):
        rank_score = float(store['score'])  # 기존 랭킹 점수
        density_score = adjusted_density_scores[i] * 5  # 밀도 점수 (5점 만점)
        
        # 기존 랭킹 점수와 밀도 점수의 가중치를 5:5로 반영
        final_score = (rank_score * 5 + density_score * 5) / 10
        final_scores.append((store['store_name'], final_score))
    
    return final_scores

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

# 서울시 상권 API 비동기 호출 함수
async def fetch_sangwon_data(session, api_key, start_index, end_index):
    url = f"http://openapi.seoul.go.kr:8088/{api_key}/xml/VwsmSignguStorW/{start_index}/{end_index}/"
    async with session.get(url) as response:
        if response.status == 200:
            return await response.text()
        else:
            print(f"Error: {response.status}")
            return None

# Kakao Map API 비동기 호출 함수
async def get_nearby_station(session, region, kakao_api_key):
    gu_name, dong_name = region.split(", ")[1:]  # 구와 동 정보 추출
    query = f"{gu_name} {dong_name} 근처역"
    url = f"https://dapi.kakao.com/v2/local/search/keyword.json?query={query}"
    headers = {"Authorization": f"KakaoAK {kakao_api_key}"}
    
    async with session.get(url, headers=headers) as response:
        if response.status == 200:
            data = await response.json()
            stations = []
            for place in data['documents']:
                station_name = place['place_name']
                if "역" in station_name:
                    station_name = station_name[:station_name.rfind("역")]  # '역' 바로 앞까지 가져옴
                    if station_name not in stations:  # 중복된 역 이름은 제외
                        stations.append(station_name)
            return stations[:3]  # 상위 3개 역만 반환
        elif response.status == 401:
            print(f"Error: {response.status} - Invalid API key or permissions.")
            return []
        else:
            print(f"Error: {response.status}")
            return []

# 서울시 승차 인원 API 비동기 호출 함수
async def fetch_passenger_data(session, api_key, station_name, use_ymd):
    url = f"http://openapi.seoul.go.kr:8088/{api_key}/xml/CardSubwayStatsNew/1/1000/{use_ymd}"
    async with session.get(url) as response:
        if response.status == 200:
            xml_data = await response.text()
            root = ET.fromstring(xml_data)
            total_boarding = 0
            total_alighting = 0
            
            for row in root.findall(".//row"):
                station = row.find('SBWY_STNS_NM').text
                if station_name == station:  # 역 이름이 완전히 일치할 때만 처리
                    boarding = int(row.find('GTON_TNOPE').text)
                    alighting = int(row.find('GTOFF_TNOPE').text)
                    total_boarding += boarding
                    total_alighting += alighting
            
            return total_boarding + total_alighting
        else:
            print(f"Error: {response.status}")
            return 0

# 날짜 -2일 설정 함수
def get_date_minus_days(days):
    target_date = datetime.now() - timedelta(days=days)
    return target_date.strftime("%Y%m%d")

# 비동기적으로 서울시 상권 데이터, 카카오 API, 승차 인원 API를 모두 호출하는 함수
async def fetch_all_data(page_size):
    async with aiohttp.ClientSession() as session:
        # user_data에서 region 값을 사용하여 Kakao Map API 호출
        region = user_data['region']
        stations_task = get_nearby_station(session, region, kakao_api_key)
        stations = await stations_task
        print(f"주변역: {stations}")

        # 서울시 상권 데이터 비동기 호출
        sangwon_data_task = fetch_sangwon_data(session, business_api_key, 1, page_size)
        sangwon_data = await sangwon_data_task
        print(f"1부터 {page_size}까지 데이터 요청 중...")

        # 서울시 승차 인원 데이터를 가져오기 위한 날짜 설정
        use_ymd = get_date_minus_days(14)

        # 역별로 승차 인원 수 확인
        passenger_tasks = [fetch_passenger_data(session, passenger_api_key, station, use_ymd) for station in stations]
        passenger_results = await asyncio.gather(*passenger_tasks)

        # 결과 출력
        for station, total_passengers in zip(stations, passenger_results):
            print(f"{station}역: {total_passengers}명, 날짜 {use_ymd}")
        # stations와 passenger_results 반환
        return stations, passenger_results


# 메인 실행 함수
if __name__ == "__main__":
    simulation_response=fetch_simulation_response_by_id("670c78ddc9263c1f31d2089b")
    user_data=update_user_data_from_response(simulation_response)

    if simulation_response:
        user_id = simulation_response.get('user_id')

    # 사용자 입력에서 구와 동을 추출 (동을 '역삼'처럼 변환)
    if 'region' in user_data and len(user_data['region'].split(', ')) >= 3:
        gu = user_data['region'].split(', ')[1].strip()  # '강남구' 공백 제거
        dong_prefix = user_data['region'].split(', ')[2].strip()[:2]  # '역삼' 공백 제거
        print(f"구: {gu}, 동: {dong_prefix}")
    else:
        print("Error: Invalid region format in user_data['region']")

    # gu = ''  # 기본값 설정
    # dong_prefix = ''  # 기본값 설정

    # 3. 산업 카테고리에서 필요한 부분만 추출 ('치킨', '커피' 등)
    if ', ' in user_data['industry']:
        industry_category = user_data['industry'].split(', ')[1].strip()  # '치킨' 부분만 추출
    else:
        industry_category = user_data['industry'].strip()  # 공백 제거 후 industry 그대로 사용

    print(f"Industry category: {industry_category}")

    
    # 0. 사용자 입력에 따른 CSV 파일 처리 (프랜차이즈 랭킹 매기기)
    csv_file_path = os.path.join('..', 'franchise_rank', 'preprocessing_stage1', f'{industry_category}_franchise_data_with_trend_10plus.csv')
    
    if os.path.exists(csv_file_path):
        print(f"{industry_category} 업종에 해당하는 데이터를 성공적으로 불러왔습니다.")
        
        # CSV 파일 처리 (df_filtered 반환)
        df_filtered = pd.read_csv(csv_file_path)

        # 이후에 랜덤포레스트 모델 학습 및 예측 -> top_franchises 저장
        top_franchises = process_csv_file(df_filtered, industry_category)
    else:
        print(f"{csv_file_path} 파일을 찾을 수 없습니다.")
        exit()


    # 1. 매물 리스트 가져오기
    property_listings = get_property_listings()
    print("\n=== 매물 리스트 (plno) ===")
    for listing in property_listings:
        print(f"매물 ID: {listing['plno']}, 월세: {listing['add_tnth_wunt_amt']}만원, 보증금: {listing['bsc_tnth_wunt_amt']}만원, 주소: {listing['addr']}, 면적: {listing['area2']}평")

    # 2. 프랜차이즈 밀도 계산 후 밀도 리스트 얻기
    densities = search_brand_in_region()  # 밀도 계산 후 지역별 밀도 리스트 반환

    page_size = 500  # 한 번에 가져올 데이터 수 (500개씩 요청)
    # 비동기 실행
    stations, passenger_results = asyncio.run(fetch_all_data(page_size))  # 비동기 함수 호출 후 반환 값 받기

    if densities:
        # 3. 밀도의 평균과 표준편차 계산 및 밀도 점수 조정
        adjusted_density_scores, mean_density, std_density = adjust_density_scores(densities)
        print(f"밀도 평균: {mean_density}, 표준편차: {std_density}")

        # 4. 초기 자본금 조건을 만족하는 프랜차이즈 필터링 (제외된 프랜차이즈 포함)
        filtered_franchises, excluded_franchises = filter_franchises_by_cost(user_data['initial_capital'])  
        
        # 5. 필터링된 프랜차이즈의 최종 점수 계산
        final_scores = calculate_final_scores(filtered_franchises, adjusted_density_scores)

        # 6. 상위 3개의 프랜차이즈 선택 (청년치킨 포함)
        top_franchises = sorted(final_scores, key=lambda x: x[1], reverse=True)[:3]  # 상위 3개의 프랜차이즈 선택
        print("\n=== 상위 3개 추천 프랜차이즈 ===")
        for franchise, score in top_franchises:
            print(f"{franchise} - 최종 점수: {score:.2f}")

            
        # 7. 제외된 프랜차이즈 3개를 출력
        print("\n=== 초기 자본금이 부족해서 제외된 프랜차이즈 3개 ===")
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
            print(f"프랜차이즈: {franchise['store_name']}, 가맹비: {franchise['business_fee']}만원, "
                f"초기 비용: {franchise['initial_cost']}만원, 인테리어 비용: {franchise['interior_cost']}만원, "
                f"총 비용: {total_cost}만원, 점수: {franchise['score']}")

        # 8. 추천된 프랜차이즈 중에서 매물 필터링 (청년치킨에 해당하는 매물만)
        top_franchise_name = top_franchises[0][0]  # 상위 1개의 프랜차이즈 이름 (청년치킨)
        valid_recommendations = filter_listings_by_franchise_area(property_listings, [store for store in filtered_franchises if store['store_name'] == top_franchise_name])

        # 9. 보증금과 월세가 적은 매물 3개 선택
        top_listings = sorted(valid_recommendations, key=lambda x: (x['property_deposit'], x['property_rent']))[:3]

        print("\n=== 추천 가능한 매물 (청년치킨에 해당하는 상위 3개) ===")
        if top_listings:
            for recommendation in top_listings:
                print(f"프랜차이즈: {recommendation['franchise_name']}, 점수: {recommendation['franchise_score']}")
                print(f"매물 ID: {recommendation['property_id']}, 주소: {recommendation['property_address']}, 월세: {recommendation['property_rent']}만원, 보증금: {recommendation['property_deposit']}만원, 면적: {recommendation['property_area']}평\n")
        else:
            print("조건에 맞는 추천 가능한 매물이 없습니다.")

        process_and_insert_simulation_report(user_data, top_franchises, filtered_franchises, densities, mean_density, std_density, stations, passenger_results, excluded_franchises_sorted,user_id,top_listings)

