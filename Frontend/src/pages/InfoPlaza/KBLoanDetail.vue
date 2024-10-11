<template>
  <div>
    <InfoPlazaHeader />
    <div class="custom-container">
      <div class="row">
        <!-- Signle job content-->
        <div
          class="col-lg-6 position-relative pe-lg-0 mb-5 mb-lg-0"
          style="z-index: 1025"
        >
          <div v-if="data">
            <div class="d-flex justify-content-between mb-2">
              <div class="d-flex align-items-center">
                <div class="d-flex align-items-center me-5">
                  <img
                    :src="'/images/banklogo/국민은행.png'"
                    alt=""
                    style="width: 50px"
                  />
                </div>
                <div class="d-flex align-items-center">
                  <div class="text-left">
                    <span class="fs-2 text-gray-500 fw-bolder d-block">
                      {{ data.productName }}
                    </span>
                  </div>
                </div>
              </div>
            </div>
            <ul class="list-unstyled fs-sm ms-1 mb-4">
              <li class="mb-2">
                <i class="fa-solid fa-house-user text-muted me-2"></i
                ><span>KB국민은행</span>
              </li>

              <li class="d-flex align-items-center mb-2">
                <i class="fa-solid fa-coins text-muted me-2"> </i
                ><span>
                  {{
                    data.lowestInterestRate
                      ? data.lowestInterestRate + '%'
                      : '변동'
                  }}
                </span>
              </li>
            </ul>
            <hr class="mb-4" />
            <ul class="list-unstyled">
              <li class="mb-4">
                <h4 class="mb-1">자격 요건</h4>
                <span
                  v-if="data.loanEligibility"
                  v-html="formattedLoanEligibility"
                ></span>
                <span v-else>- 영업점 문의</span>
              </li>
              <li class="mb-4">
                <h4 class="mb-1">대출 한도</h4>
                <span
                  v-if="data.loanAmount"
                  v-html="formattedLoanAmount2"
                ></span>
                <span v-else>- 영업점 문의</span>
              </li>
              <li class="mb-4">
                <h4 class="mb-1">대출 기간</h4>
                <span
                  v-if="data.loanDurationAndRepayment"
                  v-html="formattedLoanDuration"
                ></span>
                <span v-else>- 영업점 문의</span>
              </li>
              <li class="mb-4">
                <h4 class="mb-1">대출 신청 시간</h4>
                <span
                  v-if="data.availableHours"
                  v-html="formattedAvailableHours"
                ></span>
                <span v-else>- 영업점 문의</span>
              </li>
              <li class="mb-4">
                <h4 class="mb-1">유의사항</h4>
                <span
                  v-if="data.loanNotice"
                  v-html="formattedLoanNotice"
                ></span>
                <!-- 데이터가 있을 때 -->
                <span v-else>- 대표전화 1588-9999 / 1599-9999 / 1644-9999</span>
                <!-- 데이터가 없을 때 -->
              </li>
            </ul>
          </div>
        </div>
        <div class="col-1" style="z-index: 1025"></div>
        <!-- Sticky sidebar-->
        <aside class="col-lg-5" style="margin-top: -6rem">
          <div class="sticky-top" style="padding-top: 6rem">
            <div class="card shadow-sm mb-3 mb-lg-0">
              <div class="card-body">
                <h3>대출 계산기</h3>
                <p>이 상품에 대한 대출 금액과 이자를 계산하세요!</p>
                <div class="btn-group" role="group" aria-label="Basic example">
                  <button
                    type="button"
                    class="btn btn-custom"
                    :class="{ active: activeButton === 'left' }"
                    @click="setActiveButton('left')"
                  >
                    원리금균등
                  </button>
                  <button
                    type="button"
                    class="btn btn-custom"
                    :class="{ active: activeButton === 'middle' }"
                    @click="setActiveButton('middle')"
                  >
                    원금균등
                  </button>
                  <button
                    type="button"
                    class="btn btn-custom"
                    :class="{ active: activeButton === 'right' }"
                    @click="setActiveButton('right')"
                  >
                    만기일시
                  </button>
                </div>
                <form @submit.prevent="calculate">
                  <div class="form-group">
                    <label for="loanAmount">대출금액</label>
                    <div class="input-group mb-3">
                      <input
                        type="text"
                        class="form-control"
                        id="loanAmount"
                        placeholder="대출금액을 입력하세요"
                        aria-label="대출금액"
                        v-model="formattedLoanAmount"
                        @input="formatCurrency"
                        required
                      />
                      <div class="input-group-append">
                        <span class="input-group-text">₩</span>
                      </div>
                    </div>
                  </div>
                  <div class="form-group">
                    <label for="loanTerm">대출 기간</label>
                    <div class="input-group mb-3">
                      <input
                        type="number"
                        class="form-control"
                        id="loanTerm"
                        placeholder="대출 기간을 입력하세요"
                        v-model="loanTerm"
                        required
                      />
                      <span class="input-group-text">개월</span>
                    </div>
                  </div>
                  <div
                    v-if="data.lowestInterestRate == null"
                    class="form-group"
                  >
                    <label for="rate">금리</label>
                    <div class="input-group mb-3">
                      <input
                        type="number"
                        class="form-control"
                        id="rate"
                        placeholder="금리를 입력하세요"
                        v-model="rate"
                        required
                      />
                      <span class="input-group-text">%</span>
                    </div>
                  </div>

                  <div class="d-flex justify-content-end">
                    <button type="submit" class="btn btn-primary mt-2">
                      계산하기
                    </button>
                  </div>
                </form>
                <hr class="my-4" />
                <div class="d-flex align-items-end">
                  <div v-if="monthlyPayment || totalInterest" class="result">
                    <p>월 상환액: {{ monthlyPayment.toFixed(0) }}원</p>
                    <p>총 이자액: {{ totalInterest.toFixed(0) }}원</p>
                  </div>
                  <a
                    class="btn btn-icon btn-translucent-primary btn-xs rounded-circle"
                    href="#"
                    ><i class="fi-telegram"></i
                  ></a>
                </div>
              </div>
            </div>
          </div>
        </aside>
      </div>
      <div class="text-center mt-10 mb-5">
        <RouterLink
          :to="`/infoPlaza/KBLoan/`"
          class="btn btn-sm btn-neutral mb-5 mt-1"
          >목록</RouterLink
        >
      </div>
      <div class="row mt-5">
        <h3>이 대출 상품이 마음에 드시나요?</h3>
        <div class="row mt-5">
          <!-- 카드 여러 개 -->
          <swiper
            :slides-per-view="3"
            :space-between="50"
            :navigation="true"
            :pagination="false"
            :modules="modules"
            :preventClicks="false"
            :preventClicksPropagation="false"
            style="padding-left: 70px; padding-right: 70px"
          >
            <swiper-slide v-for="(item, index) in recommandList" :key="index">
              <div @click="navigateToDetail(item.loanKey)">
                <RouterLink :to="`/infoPlaza/KBLoan/${item.loanKey}`">
                  <div class="card card-xl-stretch h-100 hover-card">
                    <div
                      class="card-body pt-5 d-flex flex-column justify-content-between"
                    >
                      <div>
                        <div class="d-flex flex-stack flex-wrap">
                          <span
                            class="fs-3 text-gray-500 pe-2"
                            style="font-weight: 500"
                          >
                            <div class="row mb-3" style="height: 70px">
                              <div class="col-4 d-flex align-items-center">
                                <img
                                  :src="'/images/banklogo/국민은행.png'"
                                  alt=""
                                  style="width: 100px"
                                />
                              </div>
                              <div class="col-8 d-flex align-items-center">
                                <!-- Change align-items to center -->
                                <span
                                  class="fs-3 text-gray-500 fw-bolder pe-2 text-left text-truncate"
                                  style="width: 220px"
                                >
                                  {{ item.productName }}
                                </span>
                              </div>
                            </div>
                            <div class="d-flex flex-stack flex-wrap">
                              <span
                                class="fs-3 text-gray-500 pe-2 text-truncate"
                                style="font-weight: 500"
                              >
                              </span>
                            </div>
                          </span>
                        </div>
                        <div class="carousel-inner pt-6">
                          <div class="carousel-item active">
                            <div class="carousel-wrapper">
                              <div class="d-flex flex-column flex-grow-1">
                                <!-- 콘텐츠 추가 가능 -->
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                      <!-- 금리 -->
                      <div
                        class="d-flex justify-content-end align-items-end ms-auto"
                      >
                        <p class="fs-6 text-gray-600 mb-1">금리</p>
                        <p class="h2 fw-bold mb-0 ms-2">
                          {{
                            item.lowestInterestRate
                              ? item.lowestInterestRate + '%'
                              : '변동'
                          }}
                        </p>
                      </div>
                    </div>
                  </div>
                </RouterLink>
              </div>
            </swiper-slide>
          </swiper>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>
import InfoPlazaHeader from '@/components/infoplaza/InfoPlazaHeader.vue';
import { useRoute } from 'vue-router';
import { ref, computed, onMounted } from 'vue';
import axios from 'axios';
import { Swiper, SwiperSlide } from 'swiper/vue';
import { Autoplay, Pagination, Navigation } from 'swiper/modules';
import 'swiper/css';
import 'swiper/css/bundle';
import 'swiper/css/a11y';
import 'swiper/css/autoplay';
import 'swiper/css/navigation';
import 'swiper/css/pagination';

const modules = [Autoplay, Pagination, Navigation];

const route = useRoute();

// ref로 상태를 선언합니다.
const data = ref({
  lowestInterestRate: null, // 초기값 설정
});

const loanKey = route.params.loanKey;
const recommandList = ref();
const rate = ref();

const bringDataList = async () => {
  try {
    const response = await axios.get(
      `http://localhost:8080/infoPlaza/loan/getKBLoan/${loanKey}`
    );
    data.value = response.data;
    console.log(data.value);
  } catch (error) {
    console.error('Failed to select:', error);
  }
};

// 데이터 리스트 가져오는 함수
const bringRecommandList = async () => {
  try {
    // Best 인기 업종 - 전체
    const response = await axios.get(
      'http://localhost:8080/infoPlaza/loan' + '/getKBLoanRecommand'
    );
    if (response.status === 200) {
      recommandList.value = response.data;
      console.log(recommandList.value);
    } else {
      console.log('데이터 조회 실패');
    }
  } catch (error) {
    console.log('에러발생 :' + error);
  }
};

// 포맷팅 함수
const formatTextWithLineBreaks = (text) => {
  // `-`와 `·` 기호를 기준으로 줄 바꿈 적용
  const parts = text.split(/[-·]/); // - 또는 ·를 기준으로 분리
  return (
    parts[0] + (parts.length > 1 ? '-' + parts.slice(1).join('<br />-') : '')
  );
};

// 수동 라우팅 함수
const navigateToDetail = (id) => {
  window.location.reload();
};

const formattedLoanEligibility = computed(() => {
  return formatTextWithLineBreaks(data.value?.loanEligibility || '');
});

const formattedLoanDuration = computed(() => {
  return formatTextWithLineBreaks(data.value?.loanDurationAndRepayment || '');
});

const formattedLoanAmount2 = computed(() => {
  return formatTextWithLineBreaks(data.value?.loanAmount || '');
});

const formattedAvailableHours = computed(() => {
  return formatTextWithLineBreaks(data.value?.availableHours || '');
});

const formattedLoanNotice = computed(() => {
  return formatTextWithLineBreaks(data.value?.loanNotice || '');
});

// 아래는 대출 계산 관련 변수와 함수들
const activeButton = ref('left');
const formattedLoanAmount = ref('');
const loanTerm = ref('');
// 월상환액과 총 이자액 저장할 변수
const monthlyPayment = ref(0);
const totalInterest = ref(0);

const setActiveButton = (button) => {
  activeButton.value = button; // 클릭한 버튼을 활성화 상태로 설정
};

const formatCurrency = () => {
  // Remove all non-numeric characters
  let value = formattedLoanAmount.value.replace(/[^0-9]/g, '');

  // Format number with commas
  if (value) {
    value = parseInt(value).toLocaleString(); // Use toLocaleString for formatting
  }

  // Update the ref value
  formattedLoanAmount.value = value;
};

const calculate = () => {
  console.log(formattedLoanAmount.value);
  const rawLoanAmount = parseInt(
    formattedLoanAmount.value.replace(/,/g, '').replace('₩', '')
  );
  const termMonths = parseInt(loanTerm.value);
  const interestRate =
    data.value.lowestInterestRate == null
      ? rate.value / 100
      : data.value.lowestInterestRate / 100;
  let monthlyInterestRate = interestRate / 12;
  console.log(interestRate);
  console.log(monthlyInterestRate);

  // 초기값 설정
  monthlyPayment.value = 0;
  totalInterest.value = 0;

  if (activeButton.value === 'left') {
    // 원리금균등상환
    monthlyPayment.value =
      (rawLoanAmount * monthlyInterestRate) /
      (1 - Math.pow(1 + monthlyInterestRate, -termMonths));
    totalInterest.value = monthlyPayment.value * termMonths - rawLoanAmount;
  } else if (activeButton.value === 'middle') {
    // 원금균등상환
    const principalPayment = rawLoanAmount / termMonths;
    monthlyPayment.value =
      principalPayment +
      (rawLoanAmount -
        principalPayment * Math.floor((termMonths - 1) / termMonths)) *
        monthlyInterestRate;
    totalInterest.value = monthlyPayment.value * termMonths - rawLoanAmount; // 적절한 이자 계산이 필요
  } else if (activeButton.value === 'right') {
    // 만기일시상환
    totalInterest.value = rawLoanAmount * interestRate; // 만기일시상환의 경우 전체 이자
    monthlyPayment.value = 0; // 만기일시상환은 만기일까지 월 상환액이 없음
  }

  console.log(`대출금액: ₩${rawLoanAmount}, 대출기간: ${loanTerm.value}개월`);
  console.log(
    `월 상환액: ₩${monthlyPayment.value.toFixed(
      2
    )}, 총 이자액: ₩${totalInterest.value.toFixed(2)}`
  );
};

onMounted(async () => {
  bringDataList();
  bringRecommandList();
});
</script>

<style scoped>
.hover-card {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.hover-card:hover {
  transform: translate(
    -3px,
    -3px
  ); /* Moves the card slightly to the top-left */
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1); /* Adds a subtle shadow effect */
}
.table {
  width: 200px;
  table-layout: auto;
}
.text-truncate {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.content-box {
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
  background-color: #f9f9f9;
}
.content-item {
  display: flex;
  margin-bottom: 8px;
}
.label {
  min-width: 110px; /* Ensure labels align properly */
  color: #333;
}
.value {
  color: #555;
}
.colon {
  padding-right: 0px; /* Optional additional spacing */
}
.btn-group {
  display: flex;
  justify-content: center; /* 버튼을 중앙에 배치 */
  margin: 20px 0; /* 버튼 그룹의 위 아래 여백 */
}

.btn-custom {
  background-color: #f0c040; /* 부드러운 노란색 배경 */
  color: #fff; /* 텍스트 색상 */
  border: none; /* 기본 테두리 제거 */
  padding: 12px 20px; /* 버튼의 안쪽 여백 */
  margin: 0 5px; /* 버튼 사이의 간격 */
  border-radius: 5px; /* 모서리를 둥글게 */
  font-size: 16px; /* 텍스트 크기 */
  transition: background-color 0.3s ease, transform 0.3s ease; /* 부드러운 애니메이션 */
}

.btn-custom:hover {
  background-color: #e0b030; /* 호버 시 배경색 변경 (조금 더 어두운 노란색) */
  transform: translateY(-2px); /* 호버 시 약간 위로 이동 */
}

.btn-custom.active {
  background-color: #d0a020; /* 활성화된 버튼의 배경색 (더 진한 노란색) */
}
.loan-calculator {
  max-width: 500px;
  margin: 0 auto;
}

.form-group {
  margin-bottom: 1.5rem;
}

.active {
  background-color: #ffc107; /* 진한 노란색 */
  color: white;
}
.badge {
  --fi-badge-padding-x: 0.75em;
  --fi-badge-padding-y: 0.4375em;
  --fi-badge-font-size: 0.8125em;
  --fi-badge-font-weight: 600;
  --fi-badge-color: black;
  --fi-badge-border-radius: 0.375rem;
  display: inline-block;
  padding: var(--fi-badge-padding-y) var(--fi-badge-padding-x);
  font-size: var(--fi-badge-font-size);
  font-weight: var(--fi-badge-font-weight);
  line-height: 1;
  color: var(--fi-badge-color);
  text-align: center;
  white-space: nowrap;
  vertical-align: baseline;
  border-radius: var(--fi-badge-border-radius);
}

.bg-faded-accent {
  background-color: rgba(80, 43, 246, 0.2) !important; /* 더 진한 배경색 */
}
.bg-faded-accent2 {
  background-color: rgba(255, 0, 0, 0.2) !important; /* 더 진한 배경색 */
}

.rounded-pill {
  border-radius: 50rem !important;
}
.custom-container {
  max-width: 1100px; /* 원하는 너비로 설정 */
  margin: 0 auto; /* 가운데 정렬 */
}
</style>
