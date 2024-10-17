<template>
  <div>
        <div class="title-sm">
          <div class="custom-line" />
          밀도 및 비용
          <div class="custom-line" />
        </div>
        <div></div>
        <div class="p-5">
          <canvas id="bar-chart1" style="height: 200px"></canvas>
        </div>
      </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { Chart } from 'chart.js/auto';
import {
  data_bar,
  barOptions
} from '@/assets/js/mainReportChart.js';

let barChartInstance1 = ref(null); // 막대 차트 인스턴스

onMounted(() => {
  const barCtx1 = document.getElementById('bar-chart1').getContext('2d');

  // 첫 번째 가로 양방향 막대 차트
  barChartInstance1.value = new Chart(barCtx1, {
    type: 'bar',
    data: data_bar,
    options: barOptions,
  }); 


});
</script>

<style scoped>
canvas {
  max-width: 100%;
  height: auto;
}
.bg {
  background-color: white;
  padding: 5px 5px 5px 5px;
}
</style>
