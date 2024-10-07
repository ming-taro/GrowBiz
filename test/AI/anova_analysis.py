# import numpy as np
# from scipy import stats
# from analyze_Logistic import logistic_regression_analysis
# from analyze_forest import random_forest_analysis
# from analyze_GBM import gbm_analysis

# def run_anova():
#     # 각 모델의 정확도 불러오기
#     logistic_scores = []
#     rf_scores = []
#     gbm_scores = []

#     # 각 모델 정확도를 여러 번 측정해서 평균 정확도 배열 만들기
#     for i in range(5):  # 5번씩 실행
#         logistic_scores.append(logistic_regression_analysis())
#         rf_scores.append(random_forest_analysis())
#         gbm_scores.append(gbm_analysis())

#     # ANOVA 테스트 실행
#     f_value, p_value = stats.f_oneway(logistic_scores, rf_scores, gbm_scores)

#     print(f"ANOVA F-value: {f_value}")
#     print(f"ANOVA P-value: {p_value}")

#     # P-value가 0.05 이하이면, 세 모델의 성능 차이가 유의미하다고 결론
#     if p_value < 0.05:
#         print("세 모델 간 성능 차이가 유의미합니다.")
#     else:
#         print("세 모델 간 성능 차이가 유의미하지 않습니다.")

# if __name__ == "__main__":
#     run_anova()
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score
from scipy.stats import f_oneway

# CSV 파일에서 데이터 불러오기
df = pd.read_csv('chicken_franchise_data_with_trend.csv')
df['success'] = (df['opening_rate'] >= 50).astype(int)

# 사용할 특성 선택
X = df[['asset', 'liability', 'equity', 'revenue', 'operating_income', 'net_income', 
        'advertising_expense', 'average_sales', 'franchise_count', 
        'initial_cost', 'interior_cost', 'business_fee', 'contract_initial', 'contract_renewal']]
y = df['success']

# 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Logistic Regression
log_model = LogisticRegression(max_iter=1000)
log_model.fit(X_train, y_train)
log_pred = log_model.predict(X_test)
log_acc = accuracy_score(y_test, log_pred)
log_f1 = f1_score(y_test, log_pred)
log_auc = roc_auc_score(y_test, log_pred)

# Random Forest
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
rf_pred = rf_model.predict(X_test)
rf_acc = accuracy_score(y_test, rf_pred)
rf_f1 = f1_score(y_test, rf_pred)
rf_auc = roc_auc_score(y_test, rf_pred)

# Gradient Boosting
gbm_model = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, random_state=42)
gbm_model.fit(X_train, y_train)
gbm_pred = gbm_model.predict(X_test)
gbm_acc = accuracy_score(y_test, gbm_pred)
gbm_f1 = f1_score(y_test, gbm_pred)
gbm_auc = roc_auc_score(y_test, gbm_pred)

# 성능 출력
print(f"Logistic Regression - Accuracy: {log_acc:.4f}, F1: {log_f1:.4f}, AUC: {log_auc:.4f}")
print(f"Random Forest - Accuracy: {rf_acc:.4f}, F1: {rf_f1:.4f}, AUC: {rf_auc:.4f}")
print(f"GBM - Accuracy: {gbm_acc:.4f}, F1: {gbm_f1:.4f}, AUC: {gbm_auc:.4f}")

# ANOVA 분석 - Accuracy
f_stat, p_value = f_oneway([log_acc], [rf_acc], [gbm_acc])
print(f"ANOVA F-value (Accuracy): {f_stat}")
print(f"ANOVA P-value (Accuracy): {p_value}")

# ANOVA 분석 - F1
f_stat_f1, p_value_f1 = f_oneway([log_f1], [rf_f1], [gbm_f1])
print(f"ANOVA F-value (F1): {f_stat_f1}")
print(f"ANOVA P-value (F1): {p_value_f1}")
