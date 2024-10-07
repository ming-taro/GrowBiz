from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error
import pandas as pd
from sklearn.model_selection import train_test_split

def analyze_data_xgboost():
    # 데이터 로드 및 전처리는 기존과 동일하게 유지
    df = pd.read_csv('chicken_franchise_data_consolidated_with_success_rate.csv')

    X = df[['closure_rate', 'asset', 'liability', 'equity', 'revenue', 
            'operating_income', 'net_income', 'advertising_expense', 'average_sales', 
            'franchise_count', 'initial_cost', 'interior_cost', 
            'business_fee', 'contract_initial', 'contract_renewal']]
    y = df['success_rate']  # 연속 값 (비율)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # XGBoost 회귀 모델 학습
    model = XGBRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # 예측 및 평가
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Model Mean Squared Error (XGBoost Regression): {mse:.4f}")

    # 특성 중요도
    importances = model.feature_importances_
    feature_importances = sorted(zip(X.columns, importances), key=lambda x: x[1], reverse=True)
    print("\nFeature Importances (XGBoost Regression):")
    for feature, importance in feature_importances:
        print(f"{feature}: {importance:.4f}")

if __name__ == "__main__":
    analyze_data_xgboost()  # 함수 호출
