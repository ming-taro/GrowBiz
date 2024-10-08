<template>
  <div>
    <div style="height: 400px">
      <div class="he-half">
        <div>
          <h4 class="mb-2">주변 상권 별 매출 데이터 비교</h4>
        </div>
        <div>
          <canvas id="doughnut-chart2" style="height: 202px"></canvas>
        </div>
      </div>
      <div>
        <div class="he-half">
          <h4 class="">대분류 별 월매출 비교</h4>
        </div>
        <div>
          <canvas id="mixed-chart2" height="100px"></canvas>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { Chart } from 'chart.js/auto';
import {
  mixed_data2,
  mixed_options2,
  mixed_data,
  mixed_options,
  fetchChartData,
} from '@/assets/js/mapChart.js';
import ChartDataLabels from 'chartjs-plugin-datalabels';
Chart.register(ChartDataLabels);

let mixedChartInstance2 = ref(null); // 도넛 차트 인스턴스
let mixedChartInstance = ref(null); // 혼합 차트 인스턴스
let loanRepaymentStatus = ref(''); // 대출 상환 현황 상태 추가

onMounted(async () => {
  const asdf = await fetchChartData(loanRepaymentStatus); // loanRepaymentStatus를 매개변수로 전달

  const doughnutCtx = document
    .getElementById('doughnut-chart2')
    .getContext('2d');
  const mixedCtx = document.getElementById('mixed-chart2').getContext('2d');

  // Chart.js를 사용하여 도넛 차트 생성
  mixedChartInstance2.value = new Chart(doughnutCtx, {
    type: 'bar',
    data: mixed_data2,
    options: {
      ...mixed_options2, // asset_doughnutoptions의 모든 속성을 가져옴
      maintainAspectRatio: false, // 이 속성을 덮어쓰는 방식으로 추가
    },
  });

  // Chart.js를 사용하여 혼합 차트 생성
  mixedChartInstance.value = new Chart(mixedCtx, {
    type: 'bar', // 기본 차트 유형은 'bar'입니다. 혼합 차트 데이터셋에 따라 조정됩니다.
    data: mixed_data,
    options: mixed_options,
    maintainAspectRatio: false,
  });
});
</script>

<style scoped>
.he-half {
  width: 80%;
  height: 60%;
}
</style>
