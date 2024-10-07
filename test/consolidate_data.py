import pandas as pd

# CSV 파일을 불러옵니다.
df = pd.read_csv('chicken_franchise_data_with_trend.csv')

# 동일한 매장(store_name)과 지역(region)을 기준으로 그룹화하고, 합산 또는 평균화합니다.
grouped_df = df.groupby(['store_name', 'region']).agg({
    'opening_rate': 'mean',       # 개업률의 평균
    'closure_rate': 'mean',       # 폐업률의 평균
    'total_change': 'sum',        # 총 변화량의 합계
    'franchise_count': 'max',     # 가맹점 수 (최대값을 사용)
    'asset': 'sum',               # 자산의 합계
    'liability': 'sum',           # 부채의 합계
    'equity': 'sum',              # 자본의 합계
    'revenue': 'sum',             # 매출의 합계
    'operating_income': 'sum',    # 영업 이익의 합계
    'net_income': 'sum',          # 순이익의 합계
    'advertising_expense': 'sum', # 광고비의 합계
    'average_sales': 'mean',      # 평균 매출 (평균값을 사용)
    'initial_cost': 'mean',       # 초기 비용 (평균값을 사용)
    'interior_cost': 'mean',      # 인테리어 비용 (평균값을 사용)
    'business_fee': 'mean',       # 사업 수수료 (평균값을 사용)
    'contract_initial': 'mean',   # 최초 계약 기간 (평균값을 사용)
    'contract_renewal': 'mean'    # 연장 계약 기간 (평균값을 사용)
}).reset_index()

# 성공 비율 계산 (성공 비율 = 개업률 - 폐업률)
grouped_df['success_rate'] = (grouped_df['opening_rate'] - grouped_df['closure_rate']) / 100

# 결과를 CSV로 저장합니다.
grouped_df.to_csv('chicken_franchise_data_consolidated_with_success_rate.csv', index=False)

print("전처리된 데이터가 'chicken_franchise_data_consolidated_with_success_rate.csv'에 저장되었습니다.")
