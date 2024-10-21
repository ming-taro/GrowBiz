<template>
  <div>
    <div class="container mw-screen-xl pb-5">
      <div class="row align-items-start"> <!-- align-items-start 추가 -->
        <div class="col-3 mt-2">
          <div class="mb-5">
            <h4 class="mb-1 fw-normal">추천 브랜드</h4>
            <h2 class="fw-bold">{{ recommendedBrand }}</h2>
          </div>
          <div class="mb-5">
            <h4 class="mb-1 fw-normal">추천 점수</h4>
            <h2 class="mb-1 fw-bold">{{ recommendedScore }} 점</h2>

          </div>
          <div class="mb-5">
            <h5 class="mb-1 fw-normal">저희가 추천한 브랜드로 창업하실 경우</h5>
            <h2 class="mb-1 fw-bold">{{ recommendedCost }} 만원</h2>
            <h5 class="fw-normal">만큼 아낄 수 있어요.</h5>
          </div>
        </div>

        <div class="col-4 d-flex align-items-center"> <!-- d-flex align-items-center 추가 -->
          <OpenGraph class="opengraph-adjust" v-bind:report=props.report /> <!-- 클래스 추가 -->
        </div>

        <div class="col-5 mt-3 d-flex align-items-end"> <!-- d-flex align-items-center 추가 -->
          <div class="chart-container w-100">
            <div class="">
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
import ChartDataLabels from 'chartjs-plugin-datalabels';
import OpenGraph from '@/components/report/OpenGraph.vue';

const props = defineProps(["report"]);

let barChartInstance1 = ref(null);
const recommendedBrand = ref('');
const recommendedScore = ref('');
const industryAverageScore = ref('');
const recommendedCost = ref('');

const formatNumber = (num) => {
  return new Intl.NumberFormat('ko-KR').format(num);
};

onMounted(async () => {
  const data = props.report;

  console.log("바 차트 내용");
  console.log(data);

  // 데이터를 차트에 넣기
  const data_bar = {
    labels: ['밀도 (단위 : km²)', '가맹비 (단위 : 만원)', '총 인테리어 비용 (단위 : 만원)'],
    datasets: [
      {
        label: '업종 평균',
        backgroundColor: '#fca3b9',
        originalData: [ // 원본 데이터 추가
          data.industry_density_average.toFixed(2), // 원본 업종 밀도 평균
          (parseInt(parseFloat(data.industry_initial_cost.toFixed(0)))).toLocaleString(), // 원본 업종 평균 가맹비
          (parseInt(parseFloat(data.industry_total_interior_cost.toFixed(0)))).toLocaleString() // 원본 업종 총 인테리어 비용
        ],
        data: [
          data.industry_density_average * 10, // 업종 밀도 평균
          data.industry_initial_cost / 2, // 업종 평균 가맹비
          data.industry_total_interior_cost // 업종 총 인테리어 비용
        ],
      },
      {
        label: '추천 브랜드 평균',
        backgroundColor: '#fcd752',
        originalData: [ // 원본 데이터 추가
          Number(data.recommended_brand_density.toFixed(2)).toLocaleString(), // 원본 추천 브랜드 밀도 평균
          parseFloat(data.recommended_brand_initial_cost.replace(' 만원', '').replace(',', '')).toLocaleString(), // 원본 추천 브랜드 평균 가맹비
          parseFloat(data.recommended_brand_total_interior_cost.replace(' 만원', '').replace(',', '')).toLocaleString() // 원본 추천 브랜드 총 인테리어 비용
        ],
        data: [data.recommended_brand_density * 10,
        (parseFloat(data.recommended_brand_initial_cost.replace(' 만원', '').replace(',', ''))), // 원본 추천 브랜드 평균 가맹비
        parseFloat(data.recommended_brand_total_interior_cost.replace(' 만원', '').replace(',', ''))
        ] // 원본 추천 브랜드 총 인테리어 비용
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

  console.log("확인:", data.recommended_cost);

  // 브랜드와 점수 데이터 업데이트
  recommendedBrand.value = data.brand_name; // 추천 브랜드 이름 추가
  recommendedScore.value = data.franchise_score.toFixed(2); // 추천 점수 추가
  recommendedCost.value = (data.recommended_cost).toLocaleString();
});
Chart.register(ChartDataLabels);

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
  overflow-wrap: break-word;
  /* 단어가 길 경우 줄바꿈 */
  word-break: break-all;
  /* 모든 단어를 줄바꿈 */
  white-space: normal;
  /* 연속된 공백을 줄바꿈으로 처리 */
  height: 78px;
}

.opengraph-adjust {
  margin-top: -4px;
  /* 1px 위로 올리기 */
}
</style>
