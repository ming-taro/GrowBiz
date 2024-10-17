<template>
  <div class="container">
    <div class="container">
      <div class="title">
        <div class="mt-5 ms-5" style="display: flex; align-items: flex-end">
          <h1 style="font-weight: bold">시뮬레이션 리포트</h1>
          <h4 style="margin-left: 20px; margin-bottom: 5px">
            시뮬레이션을 완료하면 받을 수 있는 리포트의 견본입니다.
          </h4>
        </div>
      </div>
    </div>
    <div class="simul-area">
      <div class="container">
        <div class="title-sm mt-5">
          <div class="custom-line" />
          시뮬레이션 결과
          <div class="custom-line" />
        </div>

        <div class="row mb-10" style="display: flex">
          <div class="col-6" style="
              display: flex;
              flex-direction: column;
              justify-content: space-between;
            ">
            <div class="row">
              <div class="col-6">
                <div class="d-flex justify-content-center align-items-center mb-4 mt-4">
                  <!-- 수직, 수평 중앙 정렬 -->
                  <h2 style="font-weight: bold">강남구 외식업</h2>
                </div>
                <div class="align-self-end">
                  <div class="d-flex justify-content-between align-items-end">
                    <!-- 보증금 -->
                    <div class="circle d-flex flex-column justify-content-center align-items-center">
                      <h4 style="font-weight: 400">보증금</h4>
                      <h2 style="font-weight: 600">1억</h2>
                    </div>
                    <!-- 월세 -->
                    <div class="circle d-flex flex-column justify-content-center align-items-center">
                      <h4 style="font-weight: 400">월세</h4>
                      <h2 style="font-weight: 600">600만</h2>
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-6 ps-8 mt-10 mb-0 d-flex flex-column align-self-end">
                <!-- 부모 요소를 flex로 설정 -->
                <div>
                  <div class="d-flex justify-content-between align-items-center">
                    <h4 class="mb-2 fw-light">중분류</h4>
                    <h4 class="mb-2 me-5">치킨</h4>
                  </div>

                  <div class="d-flex justify-content-between align-items-center">
                    <h4 class="mb-2 fw-light">유형</h4>
                    <h4 class="mb-2 me-5">프랜차이즈</h4>
                  </div>

                  <div class="d-flex justify-content-between align-items-center">
                    <h4 class="mb-2 fw-light">거주지</h4>
                    <h4 class="mb-2 me-5">인근 30km</h4>
                  </div>

                  <div class="d-flex justify-content-between align-items-center">
                    <h4 class="mb-2 fw-light">교육</h4>
                    <h4 class="mb-2 me-5">필요</h4>
                  </div>

                  <div class="d-flex justify-content-between align-items-center">
                    <h4 class="fw-light">대출 계획</h4>
                    <h4 class="me-5">있음</h4>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-6" style="display: flex; align-items: stretch;">
            <img src="@/assets/img/report/kyochon.jpg" alt="" class="full-image" />
          </div>
        </div>
        <div>
        <img src="@/assets/img/main/location.png" alt="" />
      </div>
        <div class="row">
          <ReportGraph class="mt-10 col-6" />
          <ReportGraph2 class="mt-10 col-6" />
        </div>
      </div>
      <Loan class="mb-10 ms-4" />
    </div>
  </div>
</template>

<script setup>
import ReportGraph from '@/components/main/ReportGraph.vue';
import ReportGraph2 from '@/components/main/ReportGraph2.vue';
import Loan from '@/components/report/Loan.vue';


</script>

<style>
.container {
  padding: 0 0px;
}

.simul-area {
  /* border: 0.5px solid #dddddd; */
  background-color: #f6f6f6;
  border-radius: 10px;
  margin: -20px 0px 30px 0px;
  padding: 20px;
  border-radius: 20px;
}

.title {
  margin: 30px 0px;
}

.title-sm {
  font-size: 25px;
  font-weight: bold;
  color: #6184c6;
  margin-bottom: 15px;
}

.custom-line {
  width: 100%;
  /* 선의 길이 설정 */
  height: 1px;
  /* 선의 굵기 설정 */
  background-color: #6184c6;
  /* 선의 색상 설정 */
  margin: 6px 0;
  /* 원하는 여백 설정 */
}

.full-image {
  width: 100%;
  height: auto;
  object-fit: cover;
  align-self: stretch;
  border-radius: 10px;
}

.circle {
  width: 100%;
  /* 너비를 부모 크기에 맞추되 */
  max-width: 150px;
  /* 최대 크기를 제한 */
  aspect-ratio: 1/1;
  /* 1:1 비율로 원 모양을 유지 */
  background-color: #ffffff;
  /* 배경색 */
  border-radius: 50%;
  /* 원 모양 */
  display: flex;
  justify-content: end;
  align-items: center;
  text-align: center;
  margin: 0 3px;
  /* 원 사이 간격 */
  border: 1px solid #6184c6;
  /* 테두리 */
}
</style>
