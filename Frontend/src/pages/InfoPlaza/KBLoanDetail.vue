<template>
  <div>
    <InfoPlazaHeader />
    <div class="container mw-screen-xl">
      <div class="row">
        <!-- 데이터가 있을 때만 렌더링 -->
        <div v-if="data">
          <!-- Product details-->
          <div class="offset-xl-1">
            <h1>{{ data.productName }}</h1>
            <hr />
            <div class="row">
              <div class="col-4 d-flex align-items-center justify-content-center">
                <span>
                  <i class="fa-solid fa-calendar-days" style="font-size: 50px"></i>
                </span>
                <span class="text ms-3">
                  <span style="color: gray">신청기간</span> <br />
                  <strong>{{ data.applicationPeriod }}</strong>
                </span>
              </div>
              <div class="col-4 d-flex align-items-center justify-content-center">
                <span>
                  <i class="fa-solid fa-coins" style="font-size: 50px"></i>
                </span>
                <span class="text ms-3">
                  <span style="color: gray">금리</span> <br />
                  <strong style="color: brown">{{ data.totalInterestRate }}</strong>
                </span>
              </div>
              <div class="col-4 d-flex align-items-center justify-content-center">
                <span>
                  <i class="fa-solid fa-won-sign" style="font-size: 50px"></i>
                </span>
                <span class="text ms-3">
                  <span style="color: gray">가산금리</span> <br />
                  <strong style="color: brown">{{ data.additionalInterestRate }}</strong>
                </span>
              </div>
            </div>
            <hr />
            <h3>상품 안내</h3>
            <div>
              <h5>
              자격 요건
            </h5> 
            <span v-html="formattedLoanEligibility"></span> <!-- 줄 바꿈 적용 -->
          </div>

            <div>
              <h5>
              대출 한도
            </h5> 
            <span v-html="formattedLoanAmount"></span> <!-- 줄 바꿈 적용 -->
          </div>
          <div>
            <h5>대출 기간</h5> 
            <span v-html="formattedLoanDuration"></span> <!-- 줄 바꿈 적용 -->
          </div>
          <div>
            <h5>대출 신청 시간</h5> 
            <span v-html="formattedAvailableHours"></span> <!-- 줄 바꿈 적용 -->
          </div>
          <div>
            <h5>유의사항</h5> 
            <span v-html="formattedLoanNotice"></span> <!-- 줄 바꿈 적용 -->
          </div>
            <hr />
          </div>
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

<style></style>
