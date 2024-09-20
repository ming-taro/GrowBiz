<template>
  <div class="container">
    <div class="col-6">
      <canvas id="bar-chart" style="height: 200px"></canvas>
    </div>
    <!-- 차트를 렌더링할 캔버스 -->
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { Chart } from 'chart.js/auto';
import { data, options } from '@/chartConfig';

let chartInstance = ref(null); // Chart.js 인스턴스

onMounted(() => {
  const ctx = document.getElementById('bar-chart').getContext('2d');

  // Chart.js를 사용하여 바 차트 생성
  chartInstance.value = new Chart(ctx, {
    type: 'bar', // 차트 타입: 막대 그래프
    data, // chartConfig.js에서 가져온 data 사용
    options, // chartConfig.js에서 가져온 options 사용
  });
});
</script>

<style scoped>
canvas {
  max-width: 100%;
  height: auto;
}
</style>
