import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

def logistic_regression_analysis():
    # CSV 파일에서 데이터 불러오기
    print("Loading data from 'chicken_franchise_data_with_trend.csv'...")
    df = pd.read_csv('chicken_franchise_data_with_trend3.csv')

    # 폐업 여부를 이진 값으로 변환 (폐업률 20% 이하면 성공으로 간주)
    df['success'] = (df['closure_rate'] <= 10).astype(int)

    # 사용할 특성에서 'closure_rate' 제거, 'opening_rate' 추가
    X = df[['asset', 'liability', 'equity', 'revenue', 
            'operating_income', 'net_income', 'advertising_expense', 'average_sales_per_area', 
            'franchise_count', 'initial_cost', 'interior_cost', 
            'business_fee', 'contract_initial', 'contract_renewal', 'opening_rate']]  # 개업률 추가

    # 목표 변수 설정 (성공 여부)
    y = df['success']

    # 데이터 표준화 (정규화)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # 데이터 분리 (훈련 세트와 테스트 세트)
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    # 로지스틱 회귀 모델 학습
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # 모델 예측 및 정확도 평가
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model accuracy: {accuracy:.4f}")

    # 특성 중요도 계산 (계수)
    coefficients = model.coef_[0]

    # 특성 중요도 출력 (절대값 기준으로 정렬)
    feature_importances = sorted(zip(X.columns, coefficients), key=lambda x: abs(x[1]), reverse=True)
    print("\nFeature Importances (sorted by coefficient, Logistic Regression):")
    for feature, importance in feature_importances:
        print(f"{feature}: {importance:.4f}")

    return accuracy

if __name__ == "__main__":
    logistic_regression_analysis()
