import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

def get_top_30_franchises():
    # CSV 파일 불러오기
    df = pd.read_csv('chicken_franchise_data_with_trend.csv')

    # 필요한 열 선택
    columns = ['store_name', 'year', 'region', 'opening_rate', 'closure_rate', 'average_sales', 'average_sales_per_area']

    df_filtered = df[columns]

    # 개업률이 폐업률 대비 2배 이상인 데이터만 필터링
    df_filtered = df_filtered[(df_filtered['opening_rate'] >= df_filtered['closure_rate'] * 2) &
                              (df_filtered['closure_rate'] <= 31.4)]  # 폐업률 31.4% 이하인 데이터만

    # 만약 결과가 적으면 조건을 완화하지 않고 결과를 그대로 출력
    if len(df_filtered) < 50:
        print(f"Warning: 필터링 후 {len(df_filtered)}개의 데이터만 남았습니다.")

    # 독립 변수(X)와 종속 변수(y) 설정
    X = df_filtered[['opening_rate', 'closure_rate', 'average_sales_per_area']]
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

    # 순서 번호를 다시 매긴 데이터 출력
    for idx, row in enumerate(top_franchises.itertuples(), 1):
        average_sales_per_area = row.average_sales_per_area / 10  # 천원 단위에서 만원 단위로 변환
        average_sales = row.average_sales / 10  # 천원 단위에서 만원 단위로 변환
        print(f"{idx}. {row.store_name}, 폐업률: {row.closure_rate:.2f}%, 개업률: {row.opening_rate:.2f}%, "
              f"1년 평균 매출액: {average_sales:.2f} 만원, 1평당 매출액: {average_sales_per_area:.2f} 만원, "
              f"점수: {row.normalized_score:.2f}")

    # 상위 프랜차이즈 데이터를 CSV로 저장하고 싶다면 아래 주석 해제
    # top_franchises.to_csv('top_30_franchises.csv', index=False)

if __name__ == "__main__":
    get_top_30_franchises()
