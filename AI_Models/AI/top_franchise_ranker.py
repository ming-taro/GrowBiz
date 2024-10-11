import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import json

def process_csv_file(file_name, category):
    # CSV 파일 불러오기
    df = pd.read_csv(file_name)

    # 필요한 열 선택
    columns = ['store_name', 'year', 'region', 'opening_rate', 'closure_rate', 'average_sales', 'average_sales_per_area', 
               'initial_cost', 'business_fee']

    df_filtered = df[columns]

    # 개업률이 폐업률 대비 3배 이상인 데이터만 필터링
    df_filtered = df_filtered[(df_filtered['opening_rate'] >= df_filtered['closure_rate'] * 3) & 
                              (df_filtered['closure_rate'] <= 31.4)]  # 폐업률 31.4% 이하

    if len(df_filtered) < 10:
        print(f"Warning: 필터링 후 {len(df_filtered)}개의 데이터만 남았습니다.")

    # 독립 변수(X)와 종속 변수(y) 설정
    X = df_filtered[['opening_rate', 'closure_rate', 'average_sales_per_area', 'initial_cost', 'business_fee']]
    y = df_filtered['average_sales_per_area']

    # 랜덤포레스트 모델 학습
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    rf = RandomForestRegressor()
    rf.fit(X_train, y_train)

    # 예측 점수 계산
    df_filtered['predicted_score'] = rf.predict(X)

    # 점수를 100점 만점으로 정규화
    max_score = df_filtered['predicted_score'].max()
    df_filtered['normalized_score'] = (df_filtered['predicted_score'] / max_score) * 100

    # 상위 30개의 데이터 선택 (필터링 결과가 30개 미만이면, 나오는 개수만큼 출력)
    top_franchises = df_filtered.sort_values(by='normalized_score', ascending=False).head(30)

    # 순서 번호를 다시 매긴 데이터 출력 (itertuples 사용 시 index=False 추가)
    for idx, row in enumerate(top_franchises.itertuples(index=False), 1):
        average_sales_per_area = row.average_sales_per_area / 10  # 천원 단위에서 만원 단위로 변환
        average_sales = row.average_sales / 10  # 천원 단위에서 만원 단위로 변환
        initial_cost = row.initial_cost / 10  # 초기비용 천원에서 만원 단위로 변환
        business_fee = row.business_fee / 10  # 가맹비 천원에서 만원 단위로 변환
        print(f"{idx}. {row.store_name}, 폐업률: {row.closure_rate:.2f}%, 개업률: {row.opening_rate:.2f}%, "
              f"1년 평균 매출액: {average_sales:.2f} 만원, 1평당 매출액: {average_sales_per_area:.2f} 만원, "
              f"초기비용: {initial_cost:.2f} 만원, 가맹비: {business_fee:.2f} 만원, 점수: {row.normalized_score:.2f}")

    # JSON 형식으로 저장할 데이터 구성
    results = []
    for idx, row in enumerate(top_franchises.itertuples(index=False)):
        average_sales_per_area = row.average_sales_per_area / 10  # 천원 단위에서 만원 단위로 변환
        average_sales = row.average_sales / 10  # 천원 단위에서 만원 단위로 변환
        initial_cost = row.initial_cost / 10  # 초기비용 천원에서 만원 단위로 변환
        business_fee = row.business_fee / 10  # 가맹비 천원에서 만원 단위로 변환

        results.append({
            "rank": idx + 1,
            "store_name": row.store_name,
            "year": row.year,
            "region": row.region,
            "opening_rate": f"{row.opening_rate:.2f}%",
            "closure_rate": f"{row.closure_rate:.2f}%",
            "average_sales": f"{average_sales:.2f} 만원",
            "average_sales_per_area": f"{average_sales_per_area:.2f} 만원",
            "initial_cost": f"{initial_cost:.2f} 만원",
            "business_fee": f"{business_fee:.2f} 만원",
            "score": f"{row.normalized_score:.2f}"
        })

    # JSON 파일 경로
    json_file_name = f"{category}_franchise_ranking.json"
    with open(json_file_name, 'w', encoding='utf-8') as json_file:
        json.dump(results, json_file, ensure_ascii=False, indent=4)

    print(f"Data saved to '{json_file_name}'")


if __name__ == "__main__":
    # 각 CSV 파일과 카테고리명에 맞춰 호출
    process_csv_file('치킨_franchise_data.csv', '치킨')
    process_csv_file('커피_franchise_data.csv', '커피')
    process_csv_file('제과제빵_franchise_data.csv', '제과제빵')
