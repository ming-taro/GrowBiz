<template>
  <div>
    <InfoPlazaHeader />

    <div class="container">
      <div class="row">
        <!-- Signle job content-->
        <div
          class="col-lg-7 position-relative pe-lg-5 mb-5 mb-lg-0"
          style="z-index: 1025"
        >
          <div class="d-flex justify-content-between mb-2">
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
            <div class="text-end">
              <span class="badge bg-faded-accent rounded-pill mt-5">{{
                data.crdtPrdtTypeNm
              }}</span>
            </div>
          </div>
          <ul class="list-unstyled fs-sm ms-1 mb-4">
            <li class="mb-2">
              <i class="fa-solid fa-house-user text-muted me-2"></i
              ><span>{{ data.korCoNm }}</span>
            </li>
            <li class="d-flex align-items-center mb-2">
              <i class="fa-solid fa-calendar-days text-muted me-2"></i
              ><span
                >{{ formatDate(data.dclsStrtDay) }} ~
                {{ formatEndDate(data.dclsEndDay) }}</span
              >
            </li>
            <li class="d-flex align-items-center mb-2">
              <i class="fa-solid fa-coins text-muted me-2"></i
              ><span>{{ data.crdtGradAvg }}%</span>
            </li>
          </ul>
          <hr class="mb-4" />

          <h3 class="h5 pt-2">신용 점수별 금리</h3>
          <ul class="list-unstyled">
            <li class="d-flex">
              <span class="text-primary fs-lg me-2">&#8226;</span>
              <span class="label">900점 초과</span>
              <span class="colon">: </span>
              <span>{{ data.crdtGrad1 }}%</span>
            </li>
            <li class="d-flex">
              <span class="text-primary fs-lg me-2">&#8226;</span>
              <span class="label">801~900점</span>
              <span class="colon">: </span>
              <span>{{ data.crdtGrad4 }}</span>
            </li>
            <li class="d-flex">
              <span class="text-primary fs-lg me-2">&#8226;</span>
              <span class="label">701~800점</span>
              <span class="colon">: </span>
              <span>{{ data.crdtGrad5 }}%</span>
            </li>
            <li class="d-flex">
              <span class="text-primary fs-lg me-2">&#8226;</span>
              <span class="label">601~700점</span>
              <span class="colon">: </span>
              <span>{{ data.crdtGrad6 }}</span>
            </li>
            <li class="d-flex">
              <span class="text-primary fs-lg me-2">&#8226;</span>
              <span class="label">501~600점</span>
              <span class="colon">: </span>
              <span>{{ data.crdtGrad10 }}</span>
            </li>
            <li class="d-flex">
              <span class="text-primary fs-lg me-2">&#8226;</span>
              <span class="label">401~500점</span>
              <span class="colon">: </span>
              <span>{{ data.crdtGrad11 }}</span>
            </li>
            <li class="d-flex">
              <span class="text-primary fs-lg me-2">&#8226;</span>
              <span class="label">401~500점</span>
              <span class="colon">: </span>
              <span>{{ data.crdtGrad11 }}</span>
            </li>
            <li class="d-flex">
              <span class="text-primary fs-lg me-2">&#8226;</span>
              <span class="label">301~400점</span>
              <span class="colon">: </span>
              <span>{{ data.crdtGrad12 }}</span>
            </li>
            <li class="d-flex">
              <span class="text-primary fs-lg me-2">&#8226;</span>
              <span class="label">300점 이하</span>
              <span class="colon">: </span>
              <span>{{ data.crdtGrad13 }}</span>
            </li>
          </ul>
          <h3 class="h6 pt-2">Company offers:</h3>
          <ul class="list-unstyled">
            <li class="d-flex">
              <span class="text-primary fs-lg me-2">&#8226;</span>Et mattis sit
              imperdiet risus, fermentum ultrices non.
            </li>
            <li class="d-flex">
              <span class="text-primary fs-lg me-2">&#8226;</span>Sed phasellus
              consequat nunc enim interdum tristique ultrices egestas.
            </li>
            <li class="d-flex">
              <span class="text-primary fs-lg me-2">&#8226;</span>Molestie mus
              ultrices tellus enim.
            </li>
            <li class="d-flex">
              <span class="text-primary fs-lg me-2">&#8226;</span>Vitae pulvinar
              massa id lorem aliquam fermentum egestas.
            </li>
            <li class="d-flex">
              <span class="text-primary fs-lg me-2">&#8226;</span>Dictumst
              blandit sit mauris in consectetur.
            </li>
            <li class="d-flex">
              <span class="text-primary fs-lg me-2">&#8226;</span>Sem purus
              lorem odio donec faucibus ipsum ultricies.
            </li>
          </ul>
          <p class="pt-2 mb-1">
            Please, send your CV marked “Partnership Manager” in the subject via
            e-mail:
          </p>
          <a class="nav-link-muted fw-bold" href="mailto:contact@example.com"
            >contact@example.com</a
          >
          <hr class="my-4" />
          <div class="btn-group btn-group-lg">
            <button
              class="btn btn-primary rounded-pill rounded-end-0 ps-4 pe-3"
              type="button"
            >
              대출 신청하기
            </button>
            <div
              class="position-relative border-start border-light zindex-5"
              style="margin-left: -1px"
            ></div>
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
    </div>
  </div>
</template>
<script setup>
import InfoPlazaHeader from '@/components/infoplaza/InfoPlazaHeader.vue';
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
  min-width: 95px; /* Ensure labels align properly */
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

.rounded-pill {
  border-radius: 50rem !important;
}
</style>
