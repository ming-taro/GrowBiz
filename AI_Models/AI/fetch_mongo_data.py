# import pandas as pd
# import json

# def process_json_to_csv():
#     # JSON 파일 불러오기
#     with open('franchise_detail.json', 'r', encoding='utf-8') as file:
#         data = json.load(file)
    
#     results = []

#     for store_data in data:
#         # 치킨 카테고리와 서울 지역 필터링
#         if store_data['sub_category'] == '치킨':
#             store_name = store_data.get('store_name', 'Unknown')
#             total_franchise_count = 0

#             # 서울 지역의 가맹점수만 카운트 (모든 연도 포함)
#             for store in store_data['store']:
#                 if store['region'] == '서울':
#                     total_franchise_count += store['franchise_count']

#             if total_franchise_count >= 10:
#                 total_new_open = 0
#                 total_contract_termination = 0
#                 total_contract_cancellation = 0

#                 # 2020년부터 2023년까지 신규개점, 계약종료, 계약해지 합산
#                 for year in [2020, 2021, 2022, 2023]:
#                     franchise_changes = next((change for change in store_data['franchise_change'] if change['year'] == year), None)
#                     if franchise_changes:
#                         total_new_open += franchise_changes.get('new_open', 0)
#                         total_contract_termination += franchise_changes.get('contract_termination', 0)
#                         total_contract_cancellation += franchise_changes.get('contract_cancellation', 0)
                
#                 # 전체 점포 수 계산 (기존 가맹점수 + 신규 개점 수)
#                 total_store = total_franchise_count + total_new_open

#                 # 개업률 = (신규 개점 수 / 전체 점포 수) * 100
#                 opening_rate = (total_new_open / total_store) * 100 if total_store != 0 else 0
                
#                 # 폐업률 = (계약 해지 수 / 전체 점포 수) * 100
#                 closure_rate = (total_contract_cancellation / total_store) * 100 if total_store != 0 else 0

#                 financial_2023 = next((f for f in store_data['financial'] if f['year'] == 2023), None)
#                 if financial_2023:
#                     advertising_expense = store_data['advertising_cost']['advertising_expense']
#                     average_sales = store_data['franchise_revenue']['average_sales']
#                     average_sales_per_area = store_data['franchise_revenue'].get('average_sales_per_area', None)  # 평당 평균 매출액 추가
#                     initial_cost = store_data['initial_cost']['total']
#                     interior_cost = store_data['interior_cost']['total']
#                     business_fee = store_data['business_fee']['deposit_fee']
#                     contract_initial = store_data['contract_period']['initial']
#                     contract_renewal = store_data['contract_period']['renewal']

#                     results.append({
#                         "store_name": store_name,
#                         "year": "2020-2023",
#                         "region": '서울',
#                         "opening_rate": opening_rate,
#                         "closure_rate": closure_rate,
#                         "total_change": total_new_open - (total_contract_termination + total_contract_cancellation),
#                         "franchise_count": total_franchise_count,
#                         "asset": financial_2023['asset'],
#                         "liability": financial_2023['liability'],
#                         "equity": financial_2023['equity'],
#                         "revenue": financial_2023['revenue'],
#                         "operating_income": financial_2023['operating_income'],
#                         "net_income": financial_2023['net_income'],
#                         "advertising_expense": advertising_expense,
#                         "average_sales": average_sales,
#                         "average_sales_per_area": average_sales_per_area,  # 평당 평균 매출액 추가
#                         "initial_cost": initial_cost,
#                         "interior_cost": interior_cost,
#                         "business_fee": business_fee,
#                         "contract_initial": contract_initial,
#                         "contract_renewal": contract_renewal
#                     })
    
#     # 결과를 CSV로 저장
#     df = pd.DataFrame(results)
#     df.to_csv('chicken_franchise_data_with_trend2.csv', index=False)
#     print("Data saved to 'chicken_franchise_data_with_trend2.csv'")

# if __name__ == "__main__":
#     process_json_to_csv()
import pandas as pd
import json

def process_json_to_csv():
    # JSON 파일 불러오기
    with open('franchise_detail.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    results = []

    for store_data in data:
        # 치킨 카테고리와 서울 지역 필터링
        if store_data['sub_category'] == '치킨':
            store_name = store_data.get('store_name', 'Unknown')
            total_franchise_count = 0

            # 서울 지역의 가맹점수만 카운트 (모든 연도 포함)
            for store in store_data['store']:
                if store['region'] == '서울':
                    total_franchise_count += store['franchise_count']

            if total_franchise_count >= 10:
                yearly_closure_rates = []
                yearly_opening_rates = []
                total_new_open = 0
                total_contract_termination = 0
                total_contract_cancellation = 0

                # 2020년부터 2023년까지 연도별로 폐업률/개업률 및 총 변경 사항 계산
                for year in [2020, 2021, 2022, 2023]:
                    franchise_changes = next((change for change in store_data['franchise_change'] if change['year'] == year), None)
                    if franchise_changes:
                        year_new_open = franchise_changes.get('new_open', 0)
                        year_contract_termination = franchise_changes.get('contract_termination', 0)
                        year_contract_cancellation = franchise_changes.get('contract_cancellation', 0)

                        year_total_store = total_franchise_count + year_new_open
                        if year_total_store > 0:
                            year_closure_rate = (year_contract_cancellation / year_total_store) * 100
                            year_opening_rate = (year_new_open / year_total_store) * 100
                            yearly_closure_rates.append(year_closure_rate)
                            yearly_opening_rates.append(year_opening_rate)

                        # 연도별 값 합산
                        total_new_open += year_new_open
                        total_contract_termination += year_contract_termination
                        total_contract_cancellation += year_contract_cancellation

                # 평균 폐업률 및 개업률 계산
                opening_rate = sum(yearly_opening_rates) / len(yearly_opening_rates) if yearly_opening_rates else 0
                closure_rate = sum(yearly_closure_rates) / len(yearly_closure_rates) if yearly_closure_rates else 0
                total_change = total_new_open - (total_contract_termination + total_contract_cancellation)

                financial_2023 = next((f for f in store_data['financial'] if f['year'] == 2023), None)
                if financial_2023:
                    advertising_expense = store_data['advertising_cost']['advertising_expense']
                    average_sales = store_data['franchise_revenue']['average_sales']
                    average_sales_per_area = store_data['franchise_revenue'].get('average_sales_per_area', None)
                    initial_cost = store_data['initial_cost']['total']
                    interior_cost = store_data['interior_cost']['total']
                    business_fee = store_data['business_fee']['deposit_fee']
                    contract_initial = store_data['contract_period']['initial']
                    contract_renewal = store_data['contract_period']['renewal']

                    results.append({
                        "store_name": store_name,
                        "year": "2020-2023",
                        "region": '서울',
                        "opening_rate": opening_rate,
                        "closure_rate": closure_rate,
                        "total_change": total_change,
                        "franchise_count": total_franchise_count,
                        "asset": financial_2023['asset'],
                        "liability": financial_2023['liability'],
                        "equity": financial_2023['equity'],
                        "revenue": financial_2023['revenue'],
                        "operating_income": financial_2023['operating_income'],
                        "net_income": financial_2023['net_income'],
                        "advertising_expense": advertising_expense,
                        "average_sales": average_sales,
                        "initial_cost": initial_cost,
                        "interior_cost": interior_cost,
                        "average_sales_per_area": average_sales_per_area,
                        "business_fee": business_fee,
                        "contract_initial": contract_initial,
                        "contract_renewal": contract_renewal
                    })
    
    # 결과를 CSV로 저장 (요청한 컬럼들에 맞게 구성)
    df = pd.DataFrame(results, columns=[
        'store_name', 'year', 'region', 'opening_rate', 'closure_rate', 'total_change', 'franchise_count',
        'asset', 'liability', 'equity', 'revenue', 'operating_income', 'net_income',
        'advertising_expense', 'average_sales', 'initial_cost', 'interior_cost', 'average_sales_per_area',
        'business_fee', 'contract_initial', 'contract_renewal'
    ])
    
    df.to_csv('chicken_franchise_data_with_trend.csv', index=False)
    print("Data saved to 'chicken_franchise_data_with_trend.csv'")

if __name__ == "__main__":
    process_json_to_csv()
