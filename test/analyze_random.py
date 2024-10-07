import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def analyze_data():
    # CSV 파일에서 데이터 불러오기
    print("Loading data from 'chicken_franchise_data_with_trend.csv'...")
    df = pd.read_csv('chicken_franchise_data_with_trend.csv')

    # 'success_rate' 계산 (성공 비율 = 개업률 - 폐업률)
    df['success_rate'] = df['opening_rate'] - df['closure_rate']

    # '개업률(opening_rate)'과 '폐업률(closure_rate)'을 제외한 사용할 특성 선택
    X = df[['asset', 'liability', 'equity', 'revenue', 
            'operating_income', 'net_income', 'advertising_expense', 'average_sales', 
            'franchise_count', 'initial_cost', 'interior_cost', 
            'business_fee', 'contract_initial', 'contract_renewal']]

    # 성공 비율을 목표 변수로 설정
    y = df['success_rate']

    # 데이터 분리 (훈련 세트와 테스트 세트)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 랜덤포레스트 회귀 모델 학습
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # 모델 예측 및 성능 평가 (MSE: 평균 제곱 오차)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Model MSE (excluding opening_rate and closure_rate): {mse:.4f}")

    # 특성 중요도 계산
    importances = model.feature_importances_

    # 특성 중요도 출력
    feature_importances = sorted(zip(X.columns, importances), key=lambda x: x[1], reverse=True)
    print("\nFeature Importances (sorted, excluding opening_rate and closure_rate):")
    for feature, importance in feature_importances:
        print(f"{feature}: {importance:.4f}")

if __name__ == "__main__":
    analyze_data()
