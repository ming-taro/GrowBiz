<template>
  <div>
    <div class="">
      <canvas id="bar-chart2" style="height: 328px"></canvas>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { Chart } from 'chart.js/auto';
import {
  store_data_bar,
  store_barOptions,
  fetchChartData,
} from '@/assets/js/mainStoreChart.js';
import ChartDataLabels from 'chartjs-plugin-datalabels';

Chart.register(ChartDataLabels);

let barChartInstance = ref(null); // 막대 차트 인스턴스
const loanRepaymentStatus = ref(''); // 필요한 상태 데이터

onMounted(async () => {
  // 데이터를 먼저 가져옴
  await fetchChartData(loanRepaymentStatus);

  // 캔버스 컨텍스트를 가져와 차트 생성
  const mixedCtx = document.getElementById('bar-chart2').getContext('2d');

  // 데이터를 모두 가져온 후 차트 생성
  barChartInstance.value = new Chart(mixedCtx, {
    type: 'bar',
    data: store_data_bar,
    options: store_barOptions,
    maintainAspectRatio: false,
  });

  // 데이터가 업데이트된 차트를 다시 렌더링
  barChartInstance.value.update();
});
</script>

<style scoped>
canvas {
  max-width: 100%;
  height: auto;
}
</style>
