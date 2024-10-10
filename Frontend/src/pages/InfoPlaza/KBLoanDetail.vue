<template>
  <div>
    <InfoPlazaHeader />
    <div class="custom-container">
      <div class="row">
        <!-- Signle job content-->
        <div
          class="col-lg-6 position-relative pe-0 me-10 mb-5 mb-lg-0"
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
              <i class="fa-solid fa-coins text-muted me-2">                     
                </i
              ><span>
                {{ data.lowestInterestRate ? data.lowestInterestRate + '%' : '변동' }}
              </span>
            </li>
          </ul>
          <hr class="mb-4" />
          <ul class="list-unstyled">
            <li class="mb-4">
              <h4 class="mb-1">
                자격 요건
              </h4> 
              <span v-if="data.loanEligibility" v-html="formattedLoanEligibility"></span>
              <span v-else>- 영업점 문의</span>
            </li>
            <li class="mb-4">
              <h4 class="mb-1">  
              대출 한도
              </h4> 
              <span v-if="data.loanAmount" v-html="formattedLoanAmount"></span>
              <span v-else>- 영업점 문의</span>
            </li>
            <li class="mb-4">
              <h4 class="mb-1">대출 기간</h4> 
              <span v-if="data.loanDurationAndRepayment" v-html="formattedLoanDuration"></span>
              <span v-else>- 영업점 문의</span>
            </li>
            <li class="mb-4">
              <h4 class="mb-1">대출 신청 시간</h4> 
              <span v-if="data.availableHours" v-html="formattedAvailableHours"></span>
              <span v-else>- 영업점 문의</span>
            </li>
            <li class="mb-4">
              <h4 class="mb-1">유의사항</h4> 
                <span v-if="data.loanNotice" v-html="formattedLoanNotice"></span> <!-- 데이터가 있을 때 -->
                <span v-else>- 대표전화 1588-9999 / 1599-9999 / 1644-9999</span> <!-- 데이터가 없을 때 -->
            </li>
          </ul>
          </div>
        </div>
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
        <RouterLink :to="`/infoPlaza/KBLoan/`" class="btn btn-sm btn-neutral mb-5 mt-1">목록</RouterLink>
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
              <div @click="navigateToDetail(item.id)">
                <RouterLink
                  :to="`/infoPlaza/jeonseLoan/jeonseLoanDetail/${item.id}`"
                >
                  <div class="card card-xl-stretch h-100">
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
                                  :src="
                                    '/images/banklogo/국민은행.png'
                                  "
                                  alt=""
                                  style="width: 100px"
                                />
                              </div>
                              <div class="col-8 d-flex align-items-center">
                                <!-- Change align-items to center -->
                                <span
                                  class="fs-3 text-gray-500 fw-bolder pe-2 text-left text-truncate"
                                >
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

const route = useRoute();
const data = ref(null); // 초기화
const loanKey = route.params.loanKey;

const bringDataList = async() => {
  try {
    const response = await axios.get(`http://localhost:8080/infoPlaza/loan/getKBLoan/${loanKey}`);
    data.value = response.data;
    console.log(data.value);
  } catch (error) {
    console.error('Failed to select:', error);
  }
};


// 포맷팅 함수
const formatTextWithLineBreaks = (text) => {
  // `-`와 `·` 기호를 기준으로 줄 바꿈 적용
  const parts = text.split(/[-·]/); // - 또는 ·를 기준으로 분리
  return parts[0] + (parts.length > 1 ? '-' + parts.slice(1).join('<br />-') : '');
};


const formattedLoanEligibility = computed(() => {
  return formatTextWithLineBreaks(data.value?.loanEligibility || '');
});

const formattedLoanAmount = computed(() => {
  return formatTextWithLineBreaks(data.value?.loanAmount || '');
});

const formattedLoanDuration = computed(() => {
  return formatTextWithLineBreaks(data.value?.loanDurationAndRepayment || '');
});

const formattedAvailableHours = computed(() => {
  return formatTextWithLineBreaks(data.value?.availableHours || '');
});

const formattedLoanNotice = computed(() => {
  return formatTextWithLineBreaks(data.value?.loanNotice || '');
});

onMounted(async () => {
  bringDataList();
});

</script>

<style>
.custom-container {
  max-width: 1100px; /* 원하는 너비로 설정 */
  margin: 0 auto; /* 가운데 정렬 */
}
</style>
