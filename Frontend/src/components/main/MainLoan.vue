<template>
  <div>
    <div class="d-flex align-items-center justify-content-between mb-5">
      <h3>대출정보</h3>
      <router-link
        to="/infoplaza/personalCreditLoan"
        class="text-primary fw-bold"
      >
        더보기 &gt;
      </router-link>
    </div>
    <!-- Best 금리상품 내용-->
    <div class="row">
      <div class="col-6">
        <div class="card card-xl-stretch">
          <!--begin::Body-->
          <div class="card-body pt-5">
            <div
              id="kt_stats_widget_8_carousel"
              class="carousel carousel-custom carousel-stretch slide"
              data-bs-ride="carousel"
              data-bs-interval="8000"
            >
              <!--begin::Heading-->

              <div class="row mb-3 mt-1" style="height: 20px">
                <div class="col-2 ps-3 me-3 pe-0 d-flex align-items-center">
                  <img
                    :src="'/images/banklogo/한국씨티은행.png'"
                    alt=""
                    style="width: 35px"
                  />
                </div>
                <div class="col-8 p-0 d-flex align-items-center">
                  <!-- Change align-items to center -->
                  <span class="fs-4 text-gray-500 fw-bolder pe-2 text-left">
                    장기카드대출
                  </span>
                </div>
              </div>
              <!--end::Heading-->
              <!--begin::Carousel-->
              <div class="carousel-inner pt-6">
                <!--begin::Item-->
                <div class="carousel-item active">
                  <div class="carousel-wrapper">
                    <div
                      class="d-flex flex-column justify-content-between flex-grow-1"
                    >
                      <!-- 첫 번째 행: 신청기간 마감 -->
                      <div
                        class="d-flex justify-content-between align-items-center mb-1"
                      >
                        <p class="fs-5 text-gray-600 fw-bolder">신청기간</p>
                        <p class="fs-5 text-gray-600">24/08/21 ~</p>
                      </div>

                      <!-- 두 번째 행: 구분 -->
                      <div
                        class="d-flex justify-content-between align-items-center mb-1"
                      >
                        <p class="fs-5 text-gray-600 fw-bolder">구분</p>
                        <p class="fs-5 text-gray-600">장기카드대출(카드론)</p>
                      </div>

                      <!-- 세 번째 행: 금리 -->
                      <div
                        class="d-flex justify-content-between align-items-center mb-2"
                      >
                        <p class="fs-5 text-gray-600 fw-bolder">금리</p>
                        <p class="fs-5 text-gray-600">5.2%</p>
                      </div>
                    </div>
                  </div>
                </div>
                <!--end::Item-->
              </div>
              <!--end::Carousel-->
            </div>
          </div>
          <!--end::Body-->
        </div>
      </div>
      <!-- 카드 1개 -->
      <div class="col-6">
        <div class="card card-xl-stretch">
          <!--begin::Body-->
          <div class="card-body pt-5">
            <div
              id="kt_stats_widget_8_carousel"
              class="carousel carousel-custom carousel-stretch slide"
              data-bs-ride="carousel"
              data-bs-interval="8000"
            >
              <!--begin::Heading-->

              <div class="row mb-3 mt-1" style="height: 20px">
                <div class="col-2 ps-3 me-3 pe-0 d-flex align-items-center">
                  <img
                    :src="'/images/banklogo/우리은행.png'"
                    alt=""
                    style="width: 35px"
                  />
                </div>
                <div class="col-9 ps-0 d-flex align-items-center">
                  <!-- Change align-items to center -->
                  <span
                    class="fs-4 text-gray-500 fw-bolder text-left"
                  >
                    개인신용대출 우대고객
                  </span>
                </div>
              </div>
              <!--end::Heading-->
              <!--begin::Carousel-->
              <div class="carousel-inner pt-6">
                <!--begin::Item-->
                <div class="carousel-item active">
                  <div class="carousel-wrapper">
                    <div
                      class="d-flex flex-column justify-content-between flex-grow-1"
                    >
                      <!-- 첫 번째 행: 신청기간 마감 -->
                      <div
                        class="d-flex justify-content-between align-items-center mb-1"
                      >
                        <p class="fs-5 text-gray-600 fw-bolder">신청기간</p>
                        <p class="fs-5 text-gray-600">24/08/20 ~</p>
                      </div>

                      <!-- 두 번째 행: 구분 -->
                      <div
                        class="d-flex justify-content-between align-items-center mb-1"
                      >
                        <p class="fs-5 text-gray-600 fw-bolder">구분</p>
                        <p class="fs-5 text-gray-600">일반신용대출</p>
                      </div>

                      <!-- 세 번째 행: 금리 -->
                      <div
                        class="d-flex justify-content-between align-items-center  mb-2"
                      >
                        <p class="fs-5 text-gray-600 fw-bolder">금리</p>
                        <p class="fs-5 text-gray-600">5.24%</p>
                      </div>
                    </div>
                  </div>
                </div>
                <!--end::Item-->
              </div>
              <!--end::Carousel-->
            </div>
          </div>
          <!--end::Body-->
        </div>
        <!--end::Slider Widget 1-->
      </div>
    </div>
  </div>
</template>
<script setup>
import { ref } from 'vue';
import axios from 'axios';

const best4List = ref([]);
const BASEURI = '/api/infoPlaza/loan';

// 데이터 리스트 가져오는 함수
const bringBest4List = async () => {
  try {
    // Best 인기 업종 - 전체
    const response = await axios.get(BASEURI + '/getBestCreditLoan4List');
    if (response.status === 200) {
      best4List.value = response.data;
    } else {
      console.log('데이터 조회 실패');
    }
  } catch (error) {
    console.log('에러발생 :' + error);
  }
};
bringBest4List();
</script>

<style scoped>

</style>
