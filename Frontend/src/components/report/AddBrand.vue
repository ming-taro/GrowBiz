<template>
  <!-- 추가 추천 브랜드 -->
  <div style="background-color: #f6f4f9; padding: 20px" class="">
    <div class="container">
      <div class="row d-flex align-items-center justify-content-center">
        <div class="col-3 d-flex flex-column align-items-center">
          <img :src="'/src/assets/img/report/' + brandImageSrc" style="width:50px; height:50px" class="mb-2" />
          <h2 class="text-center">추가 추천<br />브랜드<br /></h2>
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
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import axios from 'axios';
import { useRoute } from 'vue-router';
const route = useRoute();

const data = ref({});
const firstBrandName = ref(''); // 빈 배열로 초기화
const firstBrandScore = ref(''); // 빈 배열로 초기화
const secondBrandName = ref(''); // 빈 배열로 초기화
const secondBrandScore = ref(''); // 빈 배열로 초기화

const brandImageSrc = ref(''); // 이미지 경로를 저장할 변수

onMounted(async () => {
  try {
    const reportId = route.query.id;

    // 첫 번째 API 호출
    const response1 = await axios.get(`http://localhost:8080/api/report/${reportId}`);
    data.value = response1.data;

    firstBrandName.value = data.value.additional_recommended_brands[0].brand_name;
    firstBrandScore.value = data.value.additional_recommended_brands[0].franchise_score.toFixed(2);;
    secondBrandName.value = data.value.additional_recommended_brands[1].brand_name;
    secondBrandScore.value = data.value.additional_recommended_brands[1].franchise_score.toFixed(2);;

    // 두 번째 API 호출
    const simulationId = data.value.simulation_response_id;

    const response2 = await axios.get(`http://localhost:8080/api/simulation/answer/${simulationId}`);
    const simulationData = response2.data;
    // 카테고리 확인 및 이미지 경로 설정
    const category = simulationData.answer[3].subcategories;

    if (category === '제과제빵') {
      brandImageSrc.value = 'bread.png';
    }
    else if (category === '커피') {
      brandImageSrc.value = 'cafe.png';
    }
    else if (category === '아이스크림') {
      brandImageSrc.value = 'icecream.png';
    }
    else if (category === '숙박') {
      brandImageSrc.value = 'hotel.png';
    } else {
      brandImageSrc.value = 'chicken.png';
    }
  } catch (error) {
    console.error("API 호출 중 오류 발생:", error);
  }
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




.add_card {
  border: 1px solid #F6A8B8;
  /* 카드 테두리 색상 */
  border-radius: 10px;
  /* 둥근 모서리 */
  padding: 20px;
  /* 내부 여백 */
  text-align: center;
  /* 텍스트 가운데 정렬 */
  margin: 10px;
  /* 카드 간의 외부 여백 */
}
</style>