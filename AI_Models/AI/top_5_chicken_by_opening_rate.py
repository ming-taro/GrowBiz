import pandas as pd

def get_top_30_franchises():
    # CSV 파일 불러오기
    df = pd.read_csv('chicken_franchise_data_with_trend.csv')

    # 필요한 열 선택
    columns = ['store_name', 'year', 'region', 'opening_rate', 'closure_rate', 'total_change', 'franchise_count', 
               'asset', 'liability', 'equity', 'revenue', 'operating_income', 'net_income', 
               'advertising_expense', 'average_sales', 'initial_cost', 'interior_cost', 'average_sales_per_area',
               'business_fee', 'contract_initial', 'contract_renewal']

    df_filtered = df[columns]

    # 폐업률이 20% 이하인 데이터만 필터링
    df_filtered = df_filtered[df_filtered['closure_rate'] <=20]

    # 폐업률로 우선 정렬하고, 그다음 개업률로 정렬 (폐업률은 오름차순, 개업률은 내림차순)
    df_sorted = df_filtered.sort_values(by=['closure_rate', 'opening_rate'], ascending=[True, False])

    # 상위 30개의 데이터 선택
    top_30 = df_sorted.head(50)

    # 순서 번호를 다시 매긴 데이터 출력
    for idx, row in enumerate(top_30.itertuples(), 1):
        print(f"{idx}. {row.store_name}, 폐업률: {row.closure_rate:.2f}%, 개업률: {row.opening_rate:.2f}%")

    # 상위 30개의 데이터를 CSV로 저장하고 싶다면 아래 주석 해제
    # top_30.to_csv('top_30_franchises.csv', index=False)

if __name__ == "__main__":
    get_top_30_franchises()
