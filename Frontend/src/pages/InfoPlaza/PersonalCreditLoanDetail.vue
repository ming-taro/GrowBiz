<template>
  <div>
    <InfoPlazaHeader />
    <div class="container mw-screen-xl">
      <div class="row">
        <div class="">
          <div class="row">
            <div class="col-1">
              <PersonalLoanHeader class="" />
            </div>
            <div class="col-11">
              <!-- Product details-->
              <div class="">
                <div class="d-none d-md-block" style="margin-top: -90px"></div>
                <div
                  class="position-md-sticky top-0 ps-md-4 ps-lg-5 ps-xl-0 ms-5"
                >
                  <div
                    class="d-none d-md-block"
                    style="padding-top: 90px"
                  ></div>
                  <div class="d-flex align-items-center">
                    <div class="d-flex align-items-center me-5">
                      <img
                        :src="'/images/banklogo/' + data.korCoNm + '.png'"
                        alt=""
                        style="width: 50px"
                      />
                    </div>
                    <div class="d-flex align-items-center">
                      <div class="text-left">
                        <span class="fs-2 text-gray-500 fw-bolder d-block">
                          {{ data.finPrdtNm }}
                        </span>
                      </div>
                    </div>
                  </div>
                  <hr />
                  <div class="row">
                    <div
                      class="col-4 d-flex align-items-center justify-content-center"
                    >
                      <span>
                        <i
                          class="fa-solid fa-calendar-days"
                          style="font-size: 50px"
                        ></i>
                      </span>
                      <span class="text ms-3">
                        <span style="color: gray">신청기간</span> <br />
                        <strong
                          >{{ formatDate(data.dclsStrtDay) }} ~
                          {{ formatEndDate(data.dclsEndDay) }}</strong
                        >
                      </span>
                    </div>
                    <div
                      class="col-4 d-flex align-items-center justify-content-center"
                    >
                      <span>
                        <i
                          class="fa-solid fa-coins"
                          style="font-size: 50px"
                        ></i>
                      </span>
                      <span class="text ms-3">
                        <span style="color: gray">대출유형</span> <br />
                        <strong>{{ data.crdtPrdtTypeNm }}</strong>
                      </span>
                    </div>
                    <div
                      class="col-4 d-flex align-items-center justify-content-center"
                    >
                      <span>
                        <i
                          class="fa-solid fa-won-sign"
                          style="font-size: 50px"
                        ></i>
                      </span>
                      <span class="text ms-3">
                        <span style="color: gray">평균 금리</span> <br />
                        <strong style="color: brown"
                          >{{ data.crdtGradAvg }}%</strong
                        >
                      </span>
                    </div>
                  </div>

                  <hr />
                </div>
              </div>
              <div class="row">
                <div class="col-6">
                  <div class="content-box">
                    <h3>신용 점수별 금리</h3>
                    <br />
                    <div class="content-item">
                      <span class="label fw-bold">900점 초과</span>
                      <span class="colon">: </span>
                      <span class="value">{{ data.crdtGrad1 }}</span>
                    </div>
                    <div class="content-item">
                      <span class="label fw-bold">801~900점</span>
                      <span class="colon">: </span>
                      <span class="value">{{ data.crdtGrad4 }}</span>
                    </div>
                    <div class="content-item">
                      <span class="label fw-bold">701~800점</span>
                      <span class="colon">: </span>
                      <span class="value">{{ data.crdtGrad5 }}%</span>
                    </div>
                    <div class="content-item">
                      <span class="label fw-bold">601~700점</span>
                      <span class="colon">: </span>
                      <span class="value">{{ data.crdtGrad6 }}</span>
                    </div>
                    <div class="content-item">
                      <span class="label fw-bold">501~600점</span>
                      <span class="colon">: </span>
                      <span class="value">{{ data.crdtGrad10 }}</span>
                    </div>
                    <div class="content-item">
                      <span class="label fw-bold">401~500점</span>
                      <span class="colon">: </span>
                      <span class="value">{{ data.crdtGrad11 }}</span>
                    </div>
                    <div class="content-item">
                      <span class="label fw-bold">301~400점</span>
                      <span class="colon">: </span>
                      <span class="value">{{ data.crdtGrad12 }}</span>
                    </div>
                    <div class="content-item">
                      <span class="label fw-bold">300점 이하</span>
                      <span class="colon">: </span>
                      <span class="value">{{ data.crdtGrad13 }}</span>
                    </div>
                  </div>
                </div>
                <div class="col-6">
                  <h3>대출 계산기</h3>
                  <div
                    class="btn-group"
                    role="group"
                    aria-label="Basic example"
                  >
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
                  <div v-if="monthlyPayment || totalInterest" class="result">
                    <p>월 상환액: {{ monthlyPayment.toFixed(0) }}원</p>
                    <p>총 이자액: {{ totalInterest.toFixed(0) }}원</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- <div class="col-6">
            <h2>대출 계산기</h2>
          </div> -->
      </div>
    </div>
  </div>
</template>
<script setup>
import InfoPlazaHeader from '@/components/infoplaza/InfoPlazaHeader.vue';
import PersonalLoanHeader from '@/components/infoplaza/PersonalLoanHeader.vue';
import { useRoute } from 'vue-router';
import { ref, computed } from 'vue';
import axios from 'axios';

const activeButton = ref('left'); // 초기 활성화된 버튼 없음

const setActiveButton = (button) => {
  activeButton.value = button; // 클릭한 버튼을 활성화 상태로 설정
};

const route = useRoute();

const id = ref('');
id.value = route.params.id;
const BASEURI = '/api/infoPlaza/loan';

const data = ref();

// 데이터 리스트 가져오는 함수
const bringDataList = async () => {
  try {
    // Best 인기 업종 - 전체
    const response = await axios.get(BASEURI + '/getDetailItemCreditLoan', {
      params: {
        id: id.value,
      }, // 선택된 필터링 값을 쿼리 파라미터로 전송
    });
    if (response.status === 200) {
      data.value = response.data;
      console.log(data.value);
    } else {
      console.log('데이터 조회 실패');
    }
  } catch (error) {
    console.log('에러발생 :' + error);
  }
};

// 날짜 형식 변환
const formatDate = (date) => {
  const dateString = String(date);
  if (dateString.length !== 8) {
    return dateString;
  }

  const year = dateString.substring(0, 4);
  const month = dateString.substring(4, 6);
  const day = dateString.substring(6, 8);

  return `${year.substring(2)}/${month}/${day}`;
};

// dclsEndDay가 null일 경우를 처리하는 함수
const formatEndDate = (date) => {
  if (date === null) {
    return '';
  }
  return formatDate(date);
};
// 아래는 대출 계산 관련 변수와 함수들
const formattedLoanAmount = ref('');
const loanTerm = ref('');
// 월상환액과 총 이자액 저장할 변수
const monthlyPayment = ref(0);
const totalInterest = ref(0);

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
  const rawLoanAmount = parseInt(
    formattedLoanAmount.value.replace(/,/g, '').replace('₩', '')
  );
  const termMonths = parseInt(loanTerm.value);
  const interestRate = data.value.crdtGradAvg / 100; // 연 이자율을 소수로 변환
  let monthlyInterestRate = interestRate / 12;

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

bringDataList();
</script>

<style scoped>
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
  min-width: 120px; /* Ensure labels align properly */
  color: #333;
}
.value {
  color: #555;
}
.colon {
  padding-right: 5px; /* Optional additional spacing */
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
</style>
