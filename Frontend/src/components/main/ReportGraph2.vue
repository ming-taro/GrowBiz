<template>
  <div>
    <div class="title-sm">
      <div class="custom-line" />
      개업/폐업률
      <div class="custom-line" />
    </div>
    <div class="p-5">
      <canvas id="bar-chart20" style="height: 200px"></canvas>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { Chart } from 'chart.js/auto';
import { barOptions2, data_bar2 } from '@/assets/js/mainReportChart2.js';

let barChartInstance2 = ref(null); // 막대 차트 인스턴스

onMounted(() => {
  const barCtx2 = document.getElementById('bar-chart20').getContext('2d');

  // 데이터 바 차트에 추가
  barChartInstance2.value = new Chart(barCtx2, {
    type: 'bar',
    data: data_bar2(), // 데이터에 따라 동적으로 생성
    options: barOptions2,
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
