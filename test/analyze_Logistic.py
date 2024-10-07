import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import numpy as np

def analyze_data():
    # CSV 파일에서 데이터 불러오기
    print("Loading data from 'chicken_franchise_data_consolidated_with_success_rate.csv'...")
    df = pd.read_csv('chicken_franchise_data_consolidated_with_success_rate.csv')

    # '개업률(opening_rate)' 특성을 제외하고 사용할 특성 선택
    X = df[['closure_rate', 'asset', 'liability', 'equity', 'revenue', 
            'operating_income', 'net_income', 'advertising_expense', 'average_sales', 
            'franchise_count', 'initial_cost', 'interior_cost', 
            'business_fee', 'contract_initial', 'contract_renewal']]

    # 성공 비율 (성공률이 연속적인 값이므로 이를 성공 여부로 변환)
    y = (df['success_rate'] >= 0.5).astype(int)  # 0.5 이상을 성공으로 간주

    # 데이터를 표준화
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # 데이터 분리 (훈련 세트와 테스트 세트)
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    # 로지스틱 회귀 모델 학습
    model = LogisticRegression(max_iter=1000, random_state=42)
    model.fit(X_train, y_train)

    # 모델 예측 및 정확도 계산
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model accuracy (Logistic Regression): {accuracy * 100:.2f}%")

    # 특성 중요도 출력 (계수값을 사용하여 영향력 확인)
    feature_importances = np.abs(model.coef_[0])
    feature_names = X.columns

    # 특성 중요도를 내림차순으로 정렬하여 출력
    sorted_idx = np.argsort(feature_importances)[::-1]
    print("\nFeature Importances (sorted by Logistic Regression):")
    for idx in sorted_idx:
        print(f"{feature_names[idx]}: {feature_importances[idx]:.4f}")

if __name__ == "__main__":
    analyze_data()
