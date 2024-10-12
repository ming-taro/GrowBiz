import pandas as pd
import json
import os

def convert_numberlong(value):
    """MongoDB의 $numberLong 값을 정수로 변환 또는 숫자로 변환"""
    if isinstance(value, dict) and '$numberLong' in value:
        return int(value['$numberLong'])
    return value

def process_json_to_csv():
    # JSON 파일 경로 설정
    json_file_path = os.path.join('..', 'franchise_rank', 'franchise_detail.json')
    
    # 'preprocessing_stage1' 폴더가 없으면 생성
    preprocessing_folder = os.path.join('..', 'franchise_rank', 'preprocessing_stage1')
    if not os.path.exists(preprocessing_folder):
        os.makedirs(preprocessing_folder)
    
    # JSON 파일 불러오기
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # sub_category별로 데이터를 분류하기 위한 딕셔너리
    category_data = {}

    for store_data in data:
        # sub_category에 따른 필터링
        store_name = store_data.get('store_name', 'Unknown')
        sub_category = store_data.get('sub_category', 'Unknown')  # sub_category 필터링
        total_franchise_count = 0
        valid_years = 0  # To track if the franchise has data for all required years

        # 2021, 2022, 2023년의 서울 지역의 가맹점 수가 모두 10개 이상인 경우만 처리
        for store in store_data['store']:
            if store['region'] == '서울' and store['year'] in [2021, 2022, 2023]:
                if store['franchise_count'] >= 10:  # 각 연도의 가맹점 수가 10개 이상이어야 함
                    total_franchise_count += store['franchise_count']
                    valid_years += 1

        # 3년 모두 가맹점 수가 10개 이상인 경우에만 데이터 처리
        if valid_years == 3:
            yearly_closure_rates = []
            yearly_opening_rates = []
            total_new_open = 0
            total_contract_termination = 0
            total_contract_cancellation = 0
            total_ownership_change = 0
            standard_store_area = 0

            # 2020년부터 2023년까지 연도별로 폐업률/개업률 및 총 변경 사항 계산
            for year in [2020, 2021, 2022, 2023]:
                franchise_changes = next((change for change in store_data['franchise_change'] if change['year'] == year), None)
                if franchise_changes:
                    year_new_open = franchise_changes.get('new_open', 0)
                    year_contract_termination = franchise_changes.get('contract_termination', 0)
                    year_contract_cancellation = franchise_changes.get('contract_cancellation', 0)
                    year_ownership_change = franchise_changes.get('ownership_change', 0)

                    year_total_store = total_franchise_count + year_new_open + year_contract_termination + year_contract_cancellation + year_ownership_change
                    if year_total_store > 0:
                        year_closure_rate = ((year_contract_termination + year_contract_cancellation) / year_total_store) * 100
                        year_opening_rate = (year_new_open / year_total_store) * 100
                        yearly_closure_rates.append(year_closure_rate)
                        yearly_opening_rates.append(year_opening_rate)

                    # 연도별 값 합산
                    total_new_open += year_new_open
                    total_contract_termination += year_contract_termination
                    total_contract_cancellation += year_contract_cancellation
                    total_ownership_change += year_ownership_change

            # 평균 폐업률 및 개업률 계산
            opening_rate = sum(yearly_opening_rates) / len(yearly_opening_rates) if yearly_opening_rates else 0
            closure_rate = sum(yearly_closure_rates) / len(yearly_closure_rates) if yearly_closure_rates else 0
            total_change = total_new_open - (total_contract_termination + total_contract_cancellation + total_ownership_change)

            # 점포 면적 처리 (interior_cost에 포함된 standard_store_area)
            if 'interior_cost' in store_data and 'standard_store_area' in store_data['interior_cost']:
                standard_store_area = store_data['interior_cost']['standard_store_area']

            # 2023년 재무 데이터가 없는 경우, 2022년 데이터를 사용
            financial_2023 = next((f for f in store_data['financial'] if f['year'] == 2023), None)
            financial_latest = financial_2023 if financial_2023 else next((f for f in store_data['financial'] if f['year'] == 2022), None)

            if financial_latest:
                advertising_expense = convert_numberlong(store_data['advertising_cost']['advertising_expense'])
                average_sales = convert_numberlong(store_data['franchise_revenue']['average_sales'])
                average_sales_per_area = convert_numberlong(store_data['franchise_revenue'].get('average_sales_per_area', None))
                initial_cost = convert_numberlong(store_data['initial_cost']['total'])
                interior_cost = convert_numberlong(store_data['interior_cost']['total'])
                business_fee = convert_numberlong(store_data['business_fee']['deposit_fee'])

                # 계약 기간 추가
                contract_initial = store_data['contract_period'].get('initial_contract', 0)
                contract_renewal = store_data['contract_period'].get('renewal_contract', 0)

                # 재무 정보에서 숫자 값을 변환
                asset = convert_numberlong(financial_latest['asset'])
                liability = convert_numberlong(financial_latest['liability'])
                equity = convert_numberlong(financial_latest['equity'])
                revenue = convert_numberlong(financial_latest['revenue'])
                operating_income = convert_numberlong(financial_latest['operating_income'])
                net_income = convert_numberlong(financial_latest['net_income'])

                # sub_category별로 데이터를 딕셔너리에 추가
                if sub_category not in category_data:
                    category_data[sub_category] = []

                category_data[sub_category].append({
                    "store_name": store_name,
                    "year": "2020-2023",
                    "region": '서울',
                    "opening_rate": opening_rate,
                    "closure_rate": closure_rate,
                    "total_change": total_change,
                    "franchise_count": total_franchise_count,
                    "asset": asset,
                    "liability": liability,
                    "equity": equity,
                    "revenue": revenue,
                    "operating_income": operating_income,
                    "net_income": net_income,
                    "advertising_expense": advertising_expense,
                    "average_sales": average_sales,
                    "initial_cost": initial_cost,
                    "interior_cost": interior_cost,
                    "average_sales_per_area": average_sales_per_area,
                    "business_fee": business_fee,
                    "contract_initial": contract_initial,  # 초기 계약 기간
                    "contract_renewal": contract_renewal,  # 갱신 계약 기간
                    "standard_store_area": standard_store_area  # 점포 면적 추가
                })

    # sub_category별로 CSV 파일 저장
    for sub_category, data_list in category_data.items():
        df = pd.DataFrame(data_list, columns=[
            'store_name', 'year', 'region', 'opening_rate', 'closure_rate', 'total_change', 'franchise_count',
            'asset', 'liability', 'equity', 'revenue', 'operating_income', 'net_income',
            'advertising_expense', 'average_sales', 'initial_cost', 'interior_cost', 'average_sales_per_area',
            'business_fee', 'contract_initial', 'contract_renewal', 'standard_store_area'  # 점포 면적 및 계약 기간 추가
        ])
        
        # 'preprocessing_stage1' 폴더 내에 sub_category 이름으로 CSV 파일 저장
        csv_file_name = f'{sub_category}_franchise_data_with_trend_10plus.csv'
        csv_file_path = os.path.join(preprocessing_folder, csv_file_name)
        df.to_csv(csv_file_path, index=False)
        print(f"Data for sub_category '{sub_category}' saved to '{csv_file_path}'")

if __name__ == "__main__":
    process_json_to_csv()
