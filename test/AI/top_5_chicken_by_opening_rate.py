import pandas as pd

def get_top_5_franchises():
    # CSV 파일 불러오기
    df = pd.read_csv('chicken_franchise_data_with_trend.csv')

    # 필요한 열 선택
    columns = ['store_name', 'year', 'region', 'opening_rate', 'closure_rate', 'total_change', 'franchise_count', 
               'asset', 'liability', 'equity', 'revenue', 'operating_income', 'net_income', 
               'advertising_expense', 'average_sales', 'initial_cost', 'interior_cost', 
               'business_fee', 'contract_initial', 'contract_renewal']

    df_filtered = df[columns]

    # opening_rate와 success_rate (여기선 closure_rate 대신 사용)로 정렬 (내림차순)
    df_sorted = df_filtered.sort_values(by=['opening_rate', 'closure_rate'], ascending=[False, True])

    # 상위 5개의 데이터 선택
    top_5 = df_sorted.head(5)

    # 상위 5개의 데이터 출력
    print(top_5)

    # 상위 5개의 데이터를 CSV로 저장하고 싶다면 아래 주석 해제
    # top_5.to_csv('top_5_franchises.csv', index=False)

if __name__ == "__main__":
    get_top_5_franchises()
