<template>
  <div style="background-color: #f6f4f9">
    <div class="container mw-screen-xl">
      <div class="row">
        <div class="col-6">
          <div>
        <h4>추천 브랜드</h4>
      <span>ㅇㅇ치킨</span>
      </div>
      <div>
        <h4>추천 점수</h4>
      <span>ㅇㅇ점</span>
      <span>/ 지역 평균 ㅇㅇ점</span>

      </div>
      <div>
        <h4>저희가 추천한 브랜드로 창업하실 경우</h4>
      <span>ㅇㅇㅇ만원</span>
      <span>만큼 아끼실 수 있어요.</span>
      </div>
    </div>

    <div class="col-6">
      <div class="chart-container">
            <div class="p-5">
              <canvas id="bar-chart" style="height: 200px"></canvas>
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
  data_bar,
  barOptions,
} from '@/assets/js/reportChart1.js';

let barChartInstance1 = ref(null);

onMounted(() => {
  const barCtx = document.getElementById('bar-chart').getContext('2d');

  // 첫 번째 가로 양방향 막대 차트
  barChartInstance1.value = new Chart(barCtx, {
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
