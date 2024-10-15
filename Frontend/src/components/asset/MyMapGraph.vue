<template>
  <div>
    <div style="height: 400px">
      <div>
        <div>
          <h4 class="mb-2">주간 매출 데이터 비교</h4>
        </div>
        <div style="position: relative">
          <div :class="{ blur_text: isActive, disnon: nonActive }">
            로그인 후 이용하실 수 있습니다.
          </div>
          <div :class="{ blur: isActive }">
            <div :class="{ blur_overlay: isActive }"></div>
            <canvas id="mixed-chart2" style="height: 202px"></canvas>
          </div>
        </div>
      </div>
      <div>
        <div>
          <h4>월간 매출 데이터 비교</h4>
        </div>
        <div style="position: relative">
          <div :class="{ blur_text: isActive, disnon: nonActive }">
            로그인 후 이용하실 수 있습니다.
          </div>
          <div :class="{ blur: isActive }">
            <div :class="{ blur_overlay: isActive }"></div>
            <canvas id="mixed-chart3" width="550" height="203"></canvas>
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

  const doughnutCtx = document.getElementById('mixed-chart2').getContext('2d');
  const mixedCtx = document.getElementById('mixed-chart3').getContext('2d');

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

<script>
import { useAuthStore } from '@/stores/auth';

const authStore = useAuthStore();

const mno = authStore.state.mno;

let id = '1234';
export default {
  data() {
    return {
      isActive: true,
      nonActive: true,
    };
  },
  mounted() {
    this.loadpage();
  },
  methods: {
    loadpage() {
      if (mno != '') {
        this.isActive = false;
        id = mno;
      } else {
        this.nonActive = false;
      }
    },
  },
};
</script>

<style scoped>
.he-half {
  width: 80%;
  height: 60%;
}
.blur {
  background-size: cover;
  filter: blur(5px);
  top: 0;
  left: 0;
  z-index: 1;
}

.blur_overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(128, 128, 128, 0.5);
  z-index: 2;
}

.blur_text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 3;
  color: black;
  font-size: 20px;
  font-weight: bold;
}
.disnon {
  display: none;
}
</style>
