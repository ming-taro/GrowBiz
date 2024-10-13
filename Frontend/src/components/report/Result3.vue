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
        <div class="col-6 d-flex">
            <!-- 1등 카드 -->
            <div class="col-7 me-3">
                <div class="card border-left-primary shadow h-100 py-2">
                    <div class="card-body d-flex flex-column justify-content-center align-items-center">
                        <div class="text-center">
                            <img src="@/assets/img/medals/first_place_medal.png" style="max-width: 60%; height: auto" alt="1등 메달" />
                        </div>
                        <div class="row no-gutters align-items-center justify-content-center">
                            <div class="col text-center">
                                <div class="h3 mt-5 mb-2 font-weight-bold text-purple">{{ firstStation }}</div>
                                <div class="h4 mb-1 text-gray-300"><h4>{{ firstPeople }}명</h4></div>
                                <p>{{ firstDate }} 기준</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- 2등, 3등 카드 -->
            <div class="col-4 d-flex flex-column justify-content-between">
                <!-- 2등 카드 -->
                <div class="card border-left-primary shadow py-2 mb-2">
                    <div class="card-body d-flex align-items-center">
                        <div class="text-left me-2">
                            <img src="@/assets/img/medals/second_place_medal.png" style="max-width: 60px; height: auto" alt="2등 메달" />
                        </div>
                        <div>
                            <div class="h4 font-weight-bold text-purple mb-1">{{ secondStation }}</div>
                            <div class="h6 text-gray-300">{{ secondPeople }}명</div>
                        </div>
                    </div>
                </div>

                <!-- 3등 카드 -->
                <div class="card border-left-primary shadow py-2">
                    <div class="card-body d-flex align-items-center">
                        <div class="text-left me-2">
                            <img src="@/assets/img/medals/third_place_medal.png" style="max-width: 60px; height: auto" alt="3등 메달" />
                        </div>
                        <div>
                            <div class="h4 font-weight-bold text-purple mb-1">{{ thirdStation }}</div>
                            <div class="h6 text-gray-300">{{ thirdPeople }}명</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>


     <!-- 추가 추천 브랜드 -->
     <div class="row mt-4 d-flex align-items-center justify-content-center">
        <div class="col-3 d-flex flex-column align-items-center">
      <h2 class="text-center">추가 추천<br/>브랜드<br /></h2>
    </div>
    <div class="col-4 d-flex flex-column align-items-center add_card">
      <h5 class="mb-2 fw-light">추천 브랜드</h5>
      <h2 class="mb-3">{{ firstBrandName }}</h2>
      <h5 class="mb-2 fw-light">추천 점수</h5>
      <h2>{{ firstBrandScore }}점</h2>
    </div>
    <div class="col-4 d-flex flex-column align-items-center add_card">
      <h5 class="mb-2 fw-light">추천 브랜드</h5>
      <h2 class="mb-3">{{ secondBrandName }}</h2>
      <h5 class="mb-2 fw-light">추천 점수</h5>
      <h2>{{ secondBrandScore }}점</h2>
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

let barChartInstance2 = ref(null);
const data = ref({});
const firstBrandName = ref(''); // 빈 배열로 초기화
const firstBrandScore = ref(''); // 빈 배열로 초기화
const secondBrandName = ref(''); // 빈 배열로 초기화
const secondBrandScore = ref(''); // 빈 배열로 초기화



// 역 데이터
const firstStation = ref('');
const secondStation = ref('');
const thirdStation = ref('');
const firstPeople = ref(0);
const secondPeople = ref(0);
const thirdPeople = ref(0);
const firstDate = ref('');
const secondDate = ref('');
const thirdDate = ref('');

onMounted(async () => {
  // API 호출
  const response = await axios.get('http://localhost:8080/api/report/670a117bf2faf8abef449573');
  data.value = response.data;


  // 각 역 데이터 할당
  firstStation.value = data.value.top_3_nearby_stations[0].station_name;
  firstPeople.value = data.value.top_3_nearby_stations[0].people;
  firstDate.value = data.value.top_3_nearby_stations[0].date;

  secondStation.value = data.value.top_3_nearby_stations[1].station_name;
  secondPeople.value = data.value.top_3_nearby_stations[1].people;
  secondDate.value = data.value.top_3_nearby_stations[1].date;

  thirdStation.value = data.value.top_3_nearby_stations[2].station_name;
  thirdPeople.value = data.value.top_3_nearby_stations[2].people;
  thirdDate.value = data.value.top_3_nearby_stations[2].date;


  firstBrandName.value = data.value.additional_recommended_brands[0].brand_name;
firstBrandScore.value = data.value.additional_recommended_brands[0].franchise_score;
secondBrandName.value = data.value.additional_recommended_brands[1].brand_name;
secondBrandScore.value = data.value.additional_recommended_brands[1].franchise_score;
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
  overflow: hidden; /* 카드가 내부 내용을 벗어나지 않도록 설정 */
  border-radius: 0.35rem; /* 카드의 모서리 라운드 설정 */
}

.text-overlay {
  /* position: absolute; */
  z-index: 1; /* 텍스트가 이미지 위에 표시되도록 설정 */
  text-align: left; /* 왼쪽 정렬 */
  font-weight: 600;
}
.text-purple {
  color: #fca3b9;
}




.add_card {
  border: 1px solid #F6A8B8; /* 카드 테두리 색상 */
  border-radius: 10px; /* 둥근 모서리 */
  padding: 20px; /* 내부 여백 */
  text-align: center; /* 텍스트 가운데 정렬 */
  margin: 10px; /* 카드 간의 외부 여백 */
}

</style>