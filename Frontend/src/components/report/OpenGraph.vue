<template>
  <!-- 개업률, 폐업률, 유동인구 -->
  <div class=" d-flex align-items-center">
    <div class="chart-container w-100 ms-5 ">
      <div class="">
        <canvas id="bar-chart2" style="height: 320px; width:100%;"></canvas>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { Chart } from 'chart.js/auto';
import {
  data_bar2,
  barOptions2,
} from '@/assets/js/reportChart2.js';
import axios from 'axios';

const props = defineProps(["report"]);

let barChartInstance2 = ref(null);
const data = ref({});


onMounted(async () => {
  // API 호출
  // const response = await axios.get('http://localhost:8080/api/report/670a117bf2faf8abef449573');
  // console.log("지금 받고 있는 데이터:", response.data);
  // data.value = response.data;
  data.value = props.report;
  // 데이터 바 차트에 추가
  const barCtx2 = document.getElementById('bar-chart2').getContext('2d');
  barChartInstance2.value = new Chart(barCtx2, {
    type: 'bar',
    data: data_bar2(data.value), // 데이터에 따라 동적으로 생성
    options: barOptions2
  });


});

</script>

<style scoped>
.card {
  overflow: hidden;
  /* 카드가 내부 내용을 벗어나지 않도록 설정 */
  border-radius: 0.35rem;
  /* 카드의 모서리 라운드 설정 */
}

.text-overlay {
  /* position: absolute; */
  z-index: 1;
  /* 텍스트가 이미지 위에 표시되도록 설정 */
  text-align: left;
  /* 왼쪽 정렬 */
  font-weight: 600;
}

.text-purple {
  color: #fca3b9;
}
</style>