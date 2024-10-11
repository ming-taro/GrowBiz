import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def random_forest_analysis():
    # CSV 파일에서 데이터 불러오기
    print("Loading data from 'chicken_franchise_data_with_trend.csv'...")
    df = pd.read_csv('chicken_franchise_data_with_trend3.csv')

    # 성공 여부를 이진 값으로 변환 (폐업률 20% 이하면 성공으로 간주)
    df['fail'] = (df['closure_rate'] <= 10).astype(int)

    # 사용할 특성에서 'closure_rate' 제거, 'opening_rate' 추가
    X = df[['asset', 'liability', 'equity', 'revenue', 
            'operating_income', 'net_income', 'advertising_expense', 'average_sales_per_area',
            'franchise_count', 'initial_cost', 'interior_cost', 
            'business_fee', 'contract_initial', 'contract_renewal', 'opening_rate']]  # 개업률 추가

    # 한국어로 컬럼명 변경
    feature_names_ko = ['자산', '부채', '자본', '수익', 
                        '영업이익', '순이익', '광고비', '평당 평균 매출', 
                        '가맹점 수', '초기 비용', '인테리어 비용', 
                        '비용', '초기 계약 기간', '재계약 기간', '개업률']

    # 목표 변수 설정 (폐업률 기준 성공 여부)
    y = df['fail']

    # 데이터 분리 (훈련 세트와 테스트 세트)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 랜덤 포레스트 모델 학습
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # 모델 예측 및 정확도 평가
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model accuracy: {accuracy:.4f}")

    # 특성 중요도 계산
    importances = model.feature_importances_

    # 특성 중요도 출력
    feature_importances = sorted(zip(feature_names_ko, importances), key=lambda x: x[1], reverse=True)
    print("\n특성 중요도 (정렬된 결과, 랜덤 포레스트):")
    for feature, importance in feature_importances:
        print(f"{feature}: {importance:.4f}")

    return accuracy

if __name__ == "__main__":
    random_forest_analysis()
