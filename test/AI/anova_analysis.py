import numpy as np
from scipy import stats
from analyze_Logistic import logistic_regression_analysis
from analyze_forest import random_forest_analysis
from analyze_GBM import gbm_analysis

def run_anova():
    # 각 모델의 정확도 불러오기
    logistic_scores = []
    rf_scores = []
    gbm_scores = []

    # 각 모델 정확도를 여러 번 측정해서 평균 정확도 배열 만들기
    for i in range(5):  # 5번씩 실행
        logistic_scores.append(logistic_regression_analysis())
        rf_scores.append(random_forest_analysis())
        gbm_scores.append(gbm_analysis())

    # ANOVA 테스트 실행
    f_value, p_value = stats.f_oneway(logistic_scores, rf_scores, gbm_scores)

    print(f"ANOVA F-value: {f_value}")
    print(f"ANOVA P-value: {p_value}")

    # P-value가 0.05 이하이면, 세 모델의 성능 차이가 유의미하다고 결론
    if p_value < 0.05:
        print("세 모델 간 성능 차이가 유의미합니다.")
    else:
        print("세 모델 간 성능 차이가 유의미하지 않습니다.")

if __name__ == "__main__":
    run_anova()
