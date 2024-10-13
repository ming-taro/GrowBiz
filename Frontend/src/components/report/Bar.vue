<template>
  <div style="background-color: #f6f4f9">
    <div class="container mw-screen-xl">
      <div class="row">
          <div class="col-6 mt-6">
            <div class="mb-5">
          <h4 class="mb-1">추천 브랜드</h4>
          <h2>{{ recommendedBrand }}</h2>
        </div>
        <div class="mb-5">
          <h4 class="mb-1">추천 점수</h4>
          <h2 class="mb-1">{{ recommendedScore }} 점</h2>
          <span>/ 지역 평균 {{ industryAverageScore }}</span>

        </div>
        <div class="mb-5">
          <h4 class="mb-1">저희가 추천한 브랜드로 창업하실 경우</h4>
          <h2 class="mb-1">{{ formatNumber(recommendedCost) }} 만원</h2> 
          <h4>만큼 아낄 수 있어요.</h4>
        </div>
      </div>

    <div class="col-6">
      <div class="chart-container">
            <div class="p-5">
              <canvas id="bar-chart" style="height: 300px"></canvas>
            </div>
          </div>
      </div>
    </div>
    </div>
  </div>
</template>
<script setup>
import { onMounted, ref } from 'vue';
import { Chart } from 'chart.js/auto';
import {
  barOptions
} from '@/assets/js/reportChart1.js';
import axios from 'axios';

let barChartInstance1 = ref(null);
const recommendedBrand = ref('');
const recommendedScore = ref('');
const industryAverageScore = ref('');
const recommendedCost = ref('');

const formatNumber = (num) => {
  return new Intl.NumberFormat('ko-KR').format(num);
};
onMounted(async () => {
  const response = await axios.get('http://localhost:8080/api/report/670a117bf2faf8abef449573');
  const data = response.data;
  console.log(data);
 // 데이터를 차트에 넣기
 const data_bar = {
      labels: ['밀도 (단위 : km²)', '가맹비 (단위 : 만원)','총 인테리어 비용 (단위 : 만원)'],
      datasets: [
        {
          label: '업종 평균',
          backgroundColor: '#fca3b9',
          data: [
        data.industry_density_average, // 업종 밀도 평균
        data.industry_initial_cost, // 업종 평균 가맹비
        data.industry_total_interior_cost // 업종 총 인테리어 비용
      ], 
          },
        {
          label: '추천 브랜드 평균',
          backgroundColor: '#fcd752',
          data: [data.recommended_brand_density, data.recommended_brand_initial_cost, data.recommended_brand_total_interior_cost], // 추천 브랜드 평균 데이터
        },
      ],
    };

  const barCtx = document.getElementById('bar-chart').getContext('2d');

  // 첫 번째 가로 양방향 막대 차트
  barChartInstance1.value = new Chart(barCtx, {
    type: 'bar',
    data: data_bar,
    options: barOptions,
  }); 

   // 브랜드와 점수 데이터 업데이트
    recommendedBrand.value = data.brand_name; // 추천 브랜드 이름 추가
    recommendedScore.value = data.franchise_score; // 추천 점수 추가
    industryAverageScore.value = data.average_brand_score; // 지역 평균 점수 추가
    recommendedCost.value = data.recommended_brand_initial_cost; // 추천 비용 추가



});

</script>


<style scoped>
canvas {
  max-width: 100%;
  height: auto;
}

.title {
  padding: 5px 0px 1px 0px;
}

.container {
  padding: 0px 80px;
}
.chart-container {
  background-color: white;
  margin: 5px;
}
.text-cont {
  padding: 4% 15% 0%;
}
.chart-text {
  overflow-wrap: break-word; /* 단어가 길 경우 줄바꿈 */
  word-break: break-all; /* 모든 단어를 줄바꿈 */
  white-space: normal; /* 연속된 공백을 줄바꿈으로 처리 */
  height: 78px;
}
</style>
