<template>

    <!-- 개업률, 폐업률, 유동인구 -->
    <div class="row">
        <div class="col-6">
          <div class="chart-container">
            <div class="p-5">
              <canvas id="bar-chart2" style="height: 200px"></canvas>
            </div>
          </div>
        </div>
        <div class="col-6">
          
        <!-- 1등 카드 -->
        <div class="col-4">
          <div class="card border-left-primary shadow h-100 py-2">
            <div
              class="card-body d-flex flex-column justify-content-center align-items-center"
            >
              <div class="text-center">
                <img
                  src="@/assets/img/medals/first_place_medal.png"
                  style="max-width: 60%; height: auto"
                  alt="..."
                />
              </div>
              <div
                class="row no-gutters align-items-center justify-content-center"
              >
                <div class="col text-center">
                  <div class="h3 mt-5 mb-2 font-weight-bold text-purple">
123                  </div>
                  <div class="h4 mb-1 text-gray-300">
                    <h4>
123
123                    </h4>
                  </div>
                  <p>
123
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- 2등, 3등 카드 -->
        <div class="col-2 d-flex flex-column">
          <!-- 2등 카드 -->
          <div
            class="card border-left-primary shadow py-2 mb-2"
            style="flex: 1"
          >
            <div class="card-body d-flex align-items-center">
              <div class="text-left me-2">
                <img
                  src="@/assets/img/medals/second_place_medal.png"
                  style="max-width: 60px; height: auto"
                  alt="2nd place medal"
                />
              </div>
              <div class="ml-3">
                <div class="h4 font-weight-bold text-purple mb-1">
                  123
                </div>
                <div class="h6 text-gray-300">
123                </div>
                <p class="text-gray-300">123</p>
              </div>
            </div>
          </div>

          <!-- 3등 카드 -->
          <div class="card border-left-primary shadow py-2" style="flex: 1">
            <div class="card-body d-flex align-items-center">
              <div class="text-left me-2">
                <img
                  src="@/assets/img/medals/third_place_medal.png"
                  style="max-width: 60px; height: auto"
                  alt="3rd place medal"
                />
              </div>
              <div class="ml-3">
                <div class="h4 font-weight-bold text-purple mb-1">
                 123
                </div>
                <div class="h6 text-gray-300">
                  123 123
                </div>
                <p class="text-gray-300">123</p>
              </div>
            </div>
          </div>
        </div>

        </div>
      </div>

      <div class="row">
  <div class="col-3">
    <img src="" alt="">
    <span>추가<br/>추천<br/>브랜드</span>
  </div>
  <div class="col-3">
    <div class="d-flex flex-column align-items-center">
      <div class="d-flex justify-content-center">
        <span>추천 브랜드</span>
        <span class="mx-3">추천 점수</span>
      </div>
      <div class="d-flex justify-content-center">
        <h2>뭐시기</h2>
        <h2 class="mx-3">00점</h2>
      </div>
    </div>
  </div>
  <div class="col-3">
    <div class="d-flex flex-column align-items-center">
      <div class="d-flex justify-content-center">
        <span>추천 브랜드</span>
        <span class="mx-3">추천 점수</span>
      </div>
      <div class="d-flex justify-content-center">
        <h2>뭐시기</h2>
        <h2 class="mx-3">00점</h2>
      </div>
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



let barChartInstance2 = ref(null);

onMounted(() => {
    const barCtx2 = document.getElementById('bar-chart2').getContext('2d');

  // 첫 번째 가로 양방향 막대 차트
  barChartInstance2.value = new Chart(barCtx2, {
    type: 'bar',
    data: data_bar2,
    options: barOptions2
}); 
});

</script>

<style scoped>
</style>