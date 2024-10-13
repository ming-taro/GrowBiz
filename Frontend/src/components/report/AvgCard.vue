<template>
    <div class="container pd">
    <div class="row">
      <div class="col card">
        <span>업종 브랜드 평균 매출</span>
        <h2>{{ formatNumber(industry_average_sales) }}만원</h2>
      </div>
      <div class="col card">
        <span>추천 브랜드 평균 매출</span>
        <h2>{{ formatNumber(recommended_brand_average_sales) }}만원</h2>
      </div>
      <div class="col card">
        <span>업종 브랜드 평당 평균 매출</span>
        <h2>{{ formatNumber(industry_average_sales_per_area) }}만원</h2>
      </div>
      <div class="col card">
        <span>추천 브랜드 평당 평균 매출</span>
        <h2>{{ formatNumber(recommended_brand_average_sales_per_area) }}만원</h2>
      </div>
    </div>
</div>
  </template>
  
  <script setup>
  import { onMounted, ref } from 'vue';
  import axios from 'axios';
  
  // 상태 변수를 정의합니다.
  const industry_average_sales = ref(0);
  const recommended_brand_average_sales = ref(0);
  const industry_average_sales_per_area = ref(0);
  const recommended_brand_average_sales_per_area = ref(0);
  // 숫자를 쉼표로 포맷팅하는 함수
const formatNumber = (num) => {
  return new Intl.NumberFormat('ko-KR').format(num);
};
  onMounted(async () => {
    try {
      // API 호출
      const response = await axios.get('http://localhost:8080/api/report/670a117bf2faf8abef449573');
  
      // 데이터 할당
      industry_average_sales.value = response.data.industry_average_sales; // 업종 브랜드 평균 매출
      recommended_brand_average_sales.value = response.data.recommended_brand_average_sales; // 추천 브랜드 평균 매출
      industry_average_sales_per_area.value = response.data.industry_average_sales_per_area; // 업종 브랜드 평당 평균 매출
      recommended_brand_average_sales_per_area.value = response.data.recommended_brand_average_sales_per_area; // 추천 브랜드 평당 평균 매출
    } catch (error) {
      console.error('API 호출 중 오류 발생:', error);
    }
  });
  </script>
  
  <style scoped>
.row {
  display: flex; /* 수평 배열 */
  justify-content: space-between; /* 카드 사이의 공간을 균등하게 분배 */
}

.card {
  border: 1px solid #F6A8B8; /* 카드 테두리 색상 */
  border-radius: 10px; /* 둥근 모서리 */
  padding: 20px; /* 내부 여백 */
  text-align: center; /* 텍스트 가운데 정렬 */
  margin: 10px; /* 카드 간의 외부 여백 */
}

.pd{
    padding-left: 120px;
    padding-right: 120px;
}
  </style>
  