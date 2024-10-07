from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np

# CSV 파일에서 데이터 불러오기
df = pd.read_csv('chicken_franchise_data_seoul.csv')

# 성공 여부를 타겟으로 설정 (True는 1, False는 0)
df['success'] = df['success'].astype(int)

# 사용할 특성 선택
X = df[['opening_rate', 'closure_rate', 'asset', 'liability', 'equity', 'revenue',
        'operating_income', 'net_income', 'advertising_expense', 'average_sales',
        'average_sales_per_area', 'franchise_count', 'initial_cost', 'interior_cost',
        'business_fee', 'contract_initial', 'contract_renewal']]
y = df['success']

# 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 데이터 스케일링 (Lasso 회귀는 데이터의 스케일에 민감하므로 표준화가 필요)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Lasso 회귀 모델 학습
lasso = Lasso(alpha=0.01)  # alpha 값은 규제 강도를 조정하는 하이퍼파라미터
lasso.fit(X_train_scaled, y_train)

# 계수 확인 (가중치)
coefficients = lasso.coef_

# 특성 중요도 출력
print("\nFeature Importances (Lasso Coefficients):")
for feature, coef in zip(X.columns, coefficients):
    print(f"{feature}: {coef:.4f}")
