<template>
  <div class="loan-section">
    <div class="container mw-screen-xl mt-3">
      <div class="title-sm"></div>
      <div class="con-card">
        <!-- Row to contain 4 cards in a single row -->
        <div class="row">
          <div v-if="excludedBrandName"
            class="col-3 me-3 d-flex flex-column align-items-center justify-content-center add_card"
            style="height: 100%; width:23%;">
            <img src="@/assets/img/report/cry.png" alt="" style="height: 150px" />
            <!-- <div v-if="excludedBrandName.brand_name"> -->
            <h5 class="mb-4 fw-light">자본금 부족으로 제외되었어요.</h5>
            <h3 class="mb-3">{{ excludedBrandName }}</h3>
          </div>
          <div v-else
            class="col-3 pb-12 pt-12 me-3 d-flex flex-column align-items-center justify-content-center add_card"
            style="height: 100%; width:23%;">
            <img src="@/assets/img/report/think.png" alt="" style="height: 50px" class="mb-6" />
            <h2 class="mb-2 ">
              추가 대출 상품을 <br /> 알아보세요.
            </h2>
            <h2 class="mb-2 fw-light">
              ->
            </h2>
          </div>

          <!-- 카드 1개 -->
          <div class="col-xl-3">
            <div class="card card-xl-stretch mb-5 mb-xl-8">
              <div class="card-body pt-5">
                <div id="kt_stats_widget_8_carousel" class="carousel carousel-custom carousel-stretch slide"
                  data-bs-ride="carousel" data-bs-interval="8000">
                  <div style="display: flex; align-items: center">
                    <img src="@/assets/img/banklogo/한국씨티은행.png" alt="" style="height: 50px; margin-right: 8px" />
                    <h4 class="ms-2 mb-0">한국씨티은행</h4>
                  </div>

                  <div class="d-flex flex-stack flex-wrap">
                    <span class="fs-4 text-gray-500 fw-bolder pe-2 pt-4">장기카드대출</span>
                  </div>
                  <div class="carousel-inner pt-6">
                    <div class="carousel-item active">
                      <div class="carousel-wrapper">
                        <div class="d-flex flex-column justify-content-between flex-grow-1">
                          <!-- 첫 번째 행: 신청기간 마감 -->
                          <div class="d-flex justify-content-between align-items-center">
                            <p class="fs-5">신청기간</p>
                            <p class="fs-5 fw-bolder">24/08/21 ~</p>
                          </div>

                          <!-- 두 번째 행: 구분 -->
                          <div class="d-flex justify-content-between align-items-center">
                            <p class="fs-5">구분</p>
                            <p class="fs-5 fw-bolder">장기카드대출(카드론)</p>
                          </div>

                          <!-- 세 번째 행: 금리 -->
                          <div class="d-flex justify-content-between align-items-center">
                            <p class="fs-5 0">금리</p>
                            <p class="fs-5 fw-bolder">5.2%</p>
                          </div>
                        </div>

                        <!-- Info (상세 보기 버튼) -->
                        <div class="d-flex justify-content-end pt-4">
                          <button @click="goToInfoPlaza"
                            class="btn btn-light btn-sm btn-color-muted fs-7 fw-bolder px-5">
                            상세 보기
                          </button>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- 카드 1개끝 -->
          <!-- 카드 1개 -->
          <div class="col-xl-3">
            <div class="card card-xl-stretch mb-5 mb-xl-8">
              <div class="card-body pt-5">
                <div id="kt_stats_widget_8_carousel" class="carousel carousel-custom carousel-stretch slide"
                  data-bs-ride="carousel" data-bs-interval="8000">
                  <div style="display: flex; align-items: center">
                    <img src="@/assets/img/banklogo/중소기업은행.png" alt="" style="height: 50px; margin-right: 8px" />
                    <h4 class="ms-2 mb-0">중소기업은행</h4>
                  </div>

                  <div class="d-flex flex-stack flex-wrap">
                    <span class="fs-4 text-gray-500 fw-bolder pe-2 pt-4">
                      장기카드대출</span>
                  </div>
                  <div class="carousel-inner pt-6">
                    <div class="carousel-item active">
                      <div class="carousel-wrapper">
                        <div class="d-flex flex-column justify-content-between flex-grow-1">
                          <!-- 첫 번째 행: 신청기간 마감 -->
                          <div class="d-flex justify-content-between align-items-center">
                            <p class="fs-5">신청기간</p>
                            <p class="fs-5 fw-bolder">24/08/21 ~</p>
                          </div>

                          <!-- 두 번째 행: 구분 -->
                          <div class="d-flex justify-content-between align-items-center">
                            <p class="fs-5">구분</p>
                            <p class="fs-5 fw-bolder">장기카드대출(카드론)</p>
                          </div>

                          <!-- 세 번째 행: 금리 -->
                          <div class="d-flex justify-content-between align-items-center">
                            <p class="fs-5 0">금리</p>
                            <p class="fs-5 fw-bolder">5.78%</p>
                          </div>
                        </div>

                        <!-- Info (상세 보기 버튼) -->
                        <div class="d-flex justify-content-end pt-4">
                          <button @click="goToInfoPlaza"
                            class="btn btn-light btn-sm btn-color-muted fs-7 fw-bolder px-5">
                            상세 보기
                          </button>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- 카드 1개끝 -->
          <!-- 카드 1개 -->
          <div class="col-xl-3">
            <div class="card card-xl-stretch mb-5 mb-xl-8">
              <div class="card-body pt-5">
                <div id="kt_stats_widget_8_carousel" class="carousel carousel-custom carousel-stretch slide"
                  data-bs-ride="carousel" data-bs-interval="8000">
                  <div style="display: flex; align-items: center">
                    <img src="@/assets/img/banklogo/국민은행.png" alt="" style="height: 50px; margin-right: 8px" />
                    <h4 class="ms-2 mb-0">KB국민은행</h4>
                  </div>

                  <div class="d-flex flex-stack flex-wrap">
                    <span class="fs-4 text-gray-500 fw-bolder pe-2 pt-4">KB사장님+ 마이너스통장</span>
                  </div>
                  <div class="carousel-inner pt-6">
                    <div class="carousel-item active">
                      <div class="carousel-wrapper">
                        <div class="d-flex flex-column justify-content-between flex-grow-1">
                          <!-- 첫 번째 행: 신청기간 마감 -->
                          <div class="d-flex justify-content-between align-items-center">
                            <p class="fs-5">신청기간</p>
                            <p class="fs-5 fw-bolder">이용 가능</p>
                          </div>

                          <!-- 두 번째 행: 구분 -->
                          <div class="d-flex justify-content-between align-items-center">
                            <p class="fs-5">구분</p>
                            <p class="fs-5 fw-bolder">마이너스한도대출</p>
                          </div>

                          <!-- 세 번째 행: 금리 -->
                          <div class="d-flex justify-content-between align-items-center">
                            <p class="fs-5 0">금리</p>
                            <p class="fs-5 fw-bolder">4.31%</p>
                          </div>
                        </div>
                        <!-- Info (상세 보기 버튼) -->
                        <div class="d-flex justify-content-end pt-4">
                          <button @click="goToKBInfoPlaza"
                            class="btn btn-light btn-sm btn-color-muted fs-7 fw-bolder px-5">
                            상세 보기
                          </button>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- 카드 1개끝 -->
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router'; // useRouter 가져오기
const router = useRouter(); // 라우터 인스턴스 생성

const excludedBrandName = ref('');
const excludedBrandScore = ref(0);
const excludedFunds = ref(0);

const props = defineProps(["report"]);

const fetchReportData = async () => {
  try {
    // const response = await axios.get(
    //   'http://localhost:8080/api/report/670a117bf2faf8abef449573'
    // );
    const data = props.report;
    const excludedBrand = data.excluded_brand_due_to_capital;

    console.log("대출>>", excludedBrand);

    // Update state with fetched data
    if (excludedBrand) {
      excludedBrandName.value = excludedBrand.brand_name;
      // excludedBrandName.value = 'BHC치킨';
      excludedBrandScore.value = excludedBrand.franchise_score;
      excludedFunds.value = excludedBrand.insufficient_funds;
    }
  } catch (error) {
    console.error('Error fetching report data:', error);
  }
  console.log(excludedBrandName.value);
};
// Method to handle the button click
const goToInfoPlaza = () => {
  router.push('/infoPlaza/personalCreditLoan');
};
const goToKBInfoPlaza = () => {
  router.push('/infoPlaza/KBLoan');
};
// Fetch data when the component mounts
onMounted(fetchReportData);
</script>
<style>
.container {
  padding: 0px 80px;
}

.title {
  padding: 5px 0px;
}

.add_card {
  border: 1px solid #f6a8b8;
  /* 카드 테두리 색상 */
  border-radius: 10px;
  /* 둥근 모서리 */
  padding: 33px;
  /* 내부 여백 */
  text-align: center;
  /* 텍스트 가운데 정렬 */
  background-color: white;
}
</style>
