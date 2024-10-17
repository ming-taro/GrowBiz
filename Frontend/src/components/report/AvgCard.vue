<template>
  <div class="container pd">
    <div class="row">
      <div class="col card">
        <span>업종 브랜드 평균 매출</span>
        <h2>{{ industry_average_sales }} 원</h2>
      </div>
      <div class="col card">
        <span>추천 브랜드 평균 매출</span>
        <h2>{{ recommended_brand_average_sales }}</h2>
      </div>
      <div class="col card">
        <span>업종 브랜드 평당 평균 매출</span>
        <h2>{{ industry_average_sales_per_area }} 원</h2>
      </div>
      <div class="col card">
        <span>추천 브랜드 평당 평균 매출</span>
        <h2>{{ recommended_brand_average_sales_per_area }}</h2>
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

const addCommas = (num) => {
  return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

function formatNumber(amountString) {
  const amount = parseFloat(amountString.replace(' 만원', '').replace(',', ''));
  const wonAmount = Math.round(amount * 10000);

  return addCommas(wonAmount) + ' 원';
}

const props = defineProps(["report"]);

onMounted(async () => {
  const report = props.report;

  industry_average_sales.value = (parseInt(parseFloat(report.industry_average_sales.toFixed(2)) * 10000)).toLocaleString(); // 업종 브랜드 평균 매출
  recommended_brand_average_sales.value = formatNumber(report.recommended_brand_average_sales); // 추천 브랜드 평균 매출
  industry_average_sales_per_area.value = (parseInt(parseFloat(report.industry_average_sales_per_area.toFixed(2)) * 10000)).toLocaleString(); // 업종 브랜드 평당 평균 매출
  recommended_brand_average_sales_per_area.value = formatNumber(report.recommended_brand_average_sales_per_area); // 추천 브랜드 평당 평균 매출
});
</script>

<style scoped>
.row {
  display: flex;
  /* 수평 배열 */
  justify-content: space-between;
  /* 카드 사이의 공간을 균등하게 분배 */
}

.card {
  border: 1px solid #F6A8B8;
  /* 카드 테두리 색상 */
  border-radius: 10px;
  /* 둥근 모서리 */
  padding: 20px;
  /* 내부 여백 */
  text-align: center;
  /* 텍스트 가운데 정렬 */
  margin: 10px;
  /* 카드 간의 외부 여백 */
}

.pd {
  padding-left: 120px;
  padding-right: 120px;
}
</style>