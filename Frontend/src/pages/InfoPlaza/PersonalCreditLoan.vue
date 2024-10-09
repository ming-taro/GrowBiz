<template>
  <div>
    <InfoPlazaHeader />
    <div class="container mw-screen-xl">
      <div class="row">
        <ul
          class="nav nav-tabs custom justify-content-center"
          id="myTab"
          role="tablist"
        >
          <li class="nav-item">
            <RouterLink
              class="nav-link active"
              to="/infoPlaza/personalCreditLoan"
              ><h4>개인신용</h4></RouterLink
            >
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" to="/infoPlaza/jeonseLoan"
              ><h4>전세자금</h4></RouterLink
            >
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" to="/infoPlaza/mortgageLoan"
              ><h4>주택담보</h4></RouterLink
            >
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" to="/infoPlaza/governmentFund"
              ><h4>정책자금</h4></RouterLink
            >
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" to="/infoPlaza/KBLoan"
              ><h4>국민은행</h4></RouterLink
            >
          </li>
        </ul>
      </div>
      <!-- Best 금리상품 title-->
      <div class="d-flex justify-content-center align-items-center mt-5">
        <div class="row">
          <div class="d-flex align-items-center mb-6">
            <img
              src="@/assets/img/infoplaza/thumbsUp.png"
              alt=""
              style="height: auto; max-height: 30px"
            />
            <h2 class="ms-2" style="font-weight: 700">BEST 금리 상품</h2>
          </div>
        </div>
      </div>
      <div class="card mb-10 p-4" style="background-color: #f6f4f9">
        <!-- Best 금리상품 내용-->
        <div class="row">
          <!-- 카드 여러 개 -->
          <div class="col-xl-3" v-for="(item, index) in best4List" :key="index">
            <RouterLink
              :to="`/infoPlaza/personalCreditLoan/personalCreditLoanDetail/${item.id}`"
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
                              :src="'/images/banklogo/' + item.korCoNm + '.png'"
                              alt=""
                              style="width: 100px"
                            />
                          </div>
                          <div class="col-8 d-flex align-items-center">
                            <!-- Change align-items to center -->
                            <span
                              class="fs-3 text-gray-500 fw-bolder pe-2 text-left"
                            >
                              {{ item.korCoNm }}
                            </span>
                          </div>
                        </div>
                        <div class="d-flex flex-stack flex-wrap">
                          <span
                            class="fs-3 text-gray-500 pe-2"
                            style="font-weight: 500"
                          >
                            {{ item.finPrdtNm }}
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
                    <p class="h2 fw-bold mb-0 ms-2">{{ item.crdtGradAvg }} %</p>
                  </div>
                </div>
              </div>
            </RouterLink>
          </div>
        </div>
      </div>

      <div class="row mb-4 d-flex justify-content-end">
        <!-- d-flex 및 justify-content-end 추가 -->
        <!-- 필터링 및 검색 -->
        <div class="col-7 d-flex">
          <div class="col-1">
            <i
              class="fa-solid fa-rotate-right refresh-icon mt-2"
              :class="{ spinning: isSpinning }"
              style="font-size: 24px; color: #5a5a5a; cursor: pointer"
              @click="refreshIcon"
            ></i>
          </div>
          <div class="col-2">
            <select
              class="form-select round-corner"
              aria-label="Default select example"
              @change="onTypeChange"
              v-model="selectedType"
            >
              <option value="전체" selected disabled hidden>유형</option>
              <option value="전체">전체</option>
              <option value="일반신용대출">일반신용대출</option>
              <option value="마이너스한도대출">마이너스한도대출</option>
              <option value="장기카드대출(카드론)">장기카드대출(카드론)</option>
            </select>
          </div>
          <!-- 은행명 구분 -->
          <div class="col-2">
            <select
              class="form-select round-corner"
              aria-label="은행명 선택"
              @change="onBankChange"
              v-model="selectedBank"
            >
              <option value="전체" selected disabled hidden>은행명</option>
              <option value="전체">전체</option>
              <option value="우리은행">우리은행</option>
              <option value="한국씨티은행">한국씨티은행</option>
              <option value="부산은행">부산은행</option>
              <option value="제주은행">제주은행</option>
              <option value="전북은행">전북은행</option>
              <option value="중소기업은행">중소기업은행</option>
              <option value="한국산업은행">한국산업은행</option>
              <option value="농협은행주식회사">농협은행주식회사</option>
              <option value="하나은행">하나은행</option>
              <option value="토스뱅크 주식회사">토스뱅크 주식회사</option>
              <option value="한화생명보험주식회사">한화생명보험주식회사</option>
              <option value="교보생명보험주식회사">교보생명보험주식회사</option>
              <option value="농협생명보험주식회사">농협생명보험주식회사</option>
              <option value="애큐온저축은행">애큐온저축은행</option>
              <option value="키움예스저축은행">키움예스저축은행</option>
              <option value="고려저축은행">고려저축은행</option>
              <option value="한화저축은행">한화저축은행</option>
              <option value="우리금융저축은행">우리금융저축은행</option>
              <option value="스타저축은행">스타저축은행</option>
              <option value="한국투자저축은행">한국투자저축은행</option>
              <option value="아이비케이저축은행">아이비케이저축은행</option>
              <option value="비엔케이저축은행">비엔케이저축은행</option>
              <option value="제이티친애저축은행">제이티친애저축은행</option>
              <option value="오케이저축은행">오케이저축은행</option>
              <option value="현대카드㈜">현대카드㈜</option>
              <option value="롯데카드㈜">롯데카드㈜</option>
              <option value="비씨카드㈜">비씨카드㈜</option>
              <option value="삼성카드㈜">삼성카드㈜</option>
              <option value="신한카드㈜">신한카드㈜</option>
              <option value="케이비캐피탈㈜">케이비캐피탈㈜</option>
              <option value="우리금융캐피탈㈜">우리금융캐피탈㈜</option>
              <option value="롯데캐피탈㈜">롯데캐피탈㈜</option>
              <option value="제이비우리캐피탈㈜">제이비우리캐피탈㈜</option>
              <option value="하나캐피탈㈜">하나캐피탈㈜</option>
              <option value="현대캐피탈㈜">현대캐피탈㈜</option>
              <option value="미래에셋캐피탈㈜">미래에셋캐피탈㈜</option>
              <option value="알씨아이파이낸셜서비스코리아㈜">
                알씨아이파이낸셜서비스코리아㈜
              </option>
              <option value="현대커머셜㈜">현대커머셜㈜</option>
              <option value="엔에이치농협캐피탈㈜">엔에이치농협캐피탈㈜</option>
              <option value="㈜아이엠캐피탈">㈜아이엠캐피탈</option>
              <option value="비엔케이캐피탈㈜">비엔케이캐피탈㈜</option>
              <option value="㈜케이비국민카드">㈜케이비국민카드</option>
              <option value="메리츠캐피탈㈜">메리츠캐피탈㈜</option>
              <option value="㈜우리카드">㈜우리카드</option>
              <option value="하나카드㈜">하나카드㈜</option>
              <option value="한국투자캐피탈㈜">한국투자캐피탈㈜</option>
            </select>
          </div>
          <!-- 검색창 -->
          <div class="col-7">
            <div class="h-100">
              <form class="h-100 form-group">
                <div class="h-100 input-group input-group-sm">
                  <input
                    type="text"
                    class="rounded form-control ms-1"
                    placeholder="검색어를 입력해 주세요."
                  />
                  <span class="ms-1 rounded input-group-text">
                    <i class="bi bi-search"></i>
                  </span>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>

      <div class="row">
        <!-- 대출 상품 카드 내용 -->
        <div class="row">
          <!-- 대출 상품 카드 여러개 -->
          <div
            class="col-xl-4 mb-5"
            v-for="(item, index) in paginatedDataList"
            :key="index"
          >
            <div class="card card-xl-stretch mb-5 mb-xl-8" style="height: 100%">
              <div
                class="card-body pt-5 d-flex flex-column justify-content-between"
                style="height: 100%"
              >
                <div>
                  <div
                    id="kt_stats_widget_8_carousel"
                    class="carousel carousel-custom carousel-stretch slide"
                    data-bs-ride="carousel"
                    data-bs-interval="8000"
                  >
                    <div class="row mb-3" style="height: 70px">
                      <div class="col-3 d-flex align-items-center">
                        <img
                          :src="'/images/banklogo/' + item.korCoNm + '.png'"
                          alt=""
                          style="width: 100px"
                        />
                      </div>
                      <div class="col-9 d-flex align-items-center">
                        <div class="text-left">
                          <span class="fs-4 text-gray-500 fw-bolder d-block">
                            {{ item.korCoNm }}
                          </span>
                          <span class="fs-4 text-gray-400">
                            {{ item.finPrdtNm }}
                          </span>
                        </div>
                      </div>
                    </div>

                    <div class="carousel-inner pt-0">
                      <div class="carousel-item active">
                        <div class="carousel-wrapper">
                          <div class="d-flex flex-column flex-grow-1">
                            <!-- 첫 번째 행: 신청기간 마감 -->
                            <div
                              class="d-flex align-items-center"
                              style="min-height: 2.5rem"
                            >
                              <p class="fs-5 justify-content-start">신청기간</p>
                              <p
                                class="fs-5 fw-bolder justify-content-start text-start ms-6"
                              >
                                <!-- text-start 추가 -->
                                {{ formatDate(item.dclsStrtDay) }} ~
                                {{ formatEndDate(item.dclsEndDay) }}
                              </p>
                            </div>

                            <!-- 두 번째 행: 구분 -->
                            <div
                              class="d-flex justify-content-start align-items-left"
                              style="min-height: 2.5rem"
                            >
                              <p class="fs-5 me-1">구분</p>
                              <p class="fs-5 fw-bolder text-start ms-12">
                                <!-- text-start 추가 -->
                                {{ item.crdtPrdtTypeNm }}
                              </p>
                            </div>

                            <!-- 세 번째 행: 금리 -->
                            <div
                              class="d-flex justify-content-start align-items-left"
                              style="min-height: 2.5rem"
                            >
                              <p class="fs-5 me-1">금리</p>
                              <p class="fs-5 fw-bolder text-start ms-12">
                                <!-- text-start 추가 -->
                                {{ item.crdtGradAvg }}
                              </p>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- Info (상세 보기 버튼) -->
                <div class="d-flex justify-content-end pt-0 mt-auto">
                  <RouterLink
                    :to="`/infoPlaza/personalCreditLoan/personalCreditLoanDetail/${item.id}`"
                    class="btn btn-light btn-sm btn-color-muted fs-7 fw-bolder px-5"
                    >상세 보기</RouterLink
                  >
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- 페이지네이션 -->
        <div class="py-4 px-6 mt-3">
          <div
            class="row align-items-center justify-content-center text-center"
          >
            <div class="col-md-12 d-flex flex-column align-items-center">
              <!-- Pagination -->
              <nav aria-label="Page navigation example">
                <ul class="pagination pagination-spaced gap-1">
                  <!-- First Page Button -->
                  <li
                    class="page-item"
                    :class="{ disabled: currentPage === 1 }"
                  >
                    <a
                      class="page-link"
                      href="#"
                      @click.prevent="changePage(1)"
                    >
                      <<
                    </a>
                  </li>
                  <!-- Previous Page Button -->
                  <li
                    class="page-item"
                    :class="{ disabled: currentPage === 1 }"
                  >
                    <a
                      class="page-link"
                      href="#"
                      @click.prevent="changePage(currentPage - 1)"
                    >
                      <i class="bi bi-chevron-left"></i>
                    </a>
                  </li>
                  <!-- Page Numbers -->
                  <li
                    v-for="page in visiblePages"
                    :key="page"
                    class="page-item"
                    :class="{ active: currentPage === page }"
                  >
                    <a
                      class="page-link"
                      href="#"
                      @click.prevent="changePage(page)"
                    >
                      {{ page }}
                    </a>
                  </li>
                  <!-- Next Page Button -->
                  <li
                    class="page-item"
                    :class="{ disabled: currentPage === totalPages }"
                  >
                    <a
                      class="page-link"
                      href="#"
                      @click.prevent="changePage(currentPage + 1)"
                    >
                      <i class="bi bi-chevron-right"></i>
                    </a>
                  </li>
                  <!-- Last Page Button -->
                  <li
                    class="page-item"
                    :class="{ disabled: currentPage === totalPages }"
                  >
                    <a
                      class="page-link"
                      href="#"
                      @click.prevent="changePage(totalPages)"
                    >
                      >>
                    </a>
                  </li>
                </ul>
              </nav>
              <!-- Showing Items Text -->
              <span class="text-muted text-sm mt-3">
                Showing {{ (currentPage - 1) * itemsPerPage + 1 }} to
                {{ Math.min(currentPage * itemsPerPage, totalItems) }} items out
                of {{ totalItems }} results found
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>
import InfoPlazaHeader from '@/components/infoplaza/InfoPlazaHeader.vue';
import LoanHeader from '@/components/infoplaza/LoanHeader.vue';

import { ref, computed } from 'vue';
import axios from 'axios';

const selectedBank = ref('전체');
const selectedType = ref('전체');
const dataList = ref([]);
const best4List = ref([]);

const currentPage = ref(1);
const itemsPerPage = 6;
const totalItems = ref(16);
const totalPages = computed(() => Math.ceil(totalItems.value / itemsPerPage));

const BASEURI = '/api/infoPlaza/loan';

// 데이터 리스트 가져오는 함수
const bringLoanList = async () => {
  try {
    // Best 인기 업종 - 전체
    const response = await axios.get(BASEURI + '/getFilteredCreditLoanList', {
      params: {
        companyName: selectedBank.value,
        type: selectedType.value,
      }, // 선택된 필터링 값을 쿼리 파라미터로 전송
    });
    console.log(selectedBank.value);
    if (response.status === 200) {
      dataList.value = response.data;
      totalItems.value = dataList.value.length;
      // console.log(dataList.value);
    } else {
      console.log('데이터 조회 실패');
    }
  } catch (error) {
    console.log('에러발생 :' + error);
  }
};

// 데이터 리스트 가져오는 함수
const bringBest4List = async () => {
  try {
    // Best 인기 업종 - 전체
    const response = await axios.get(BASEURI + '/getBestCreditLoan4List');
    if (response.status === 200) {
      best4List.value = response.data;
      // console.log(best4List);
    } else {
      console.log('데이터 조회 실패');
    }
  } catch (error) {
    console.log('에러발생 :' + error);
  }
};

// 은행명 바꾸기
const onBankChange = (event) => {
  selectedBank.value = event.target.value;
  bringLoanList();
};

// 상품 유형 바꾸기
const onTypeChange = (event) => {
  selectedType.value = event.target.value;
  bringLoanList();
};

// 현재 페이지에 해당하는 데이터만 반환하는 계산된 속성
const paginatedDataList = computed(() => {
  const startIndex = (currentPage.value - 1) * itemsPerPage;
  const endIndex = startIndex + itemsPerPage;
  return dataList.value.slice(startIndex, endIndex);
});

// 페이지 전환 함수
function changePage(page) {
  if (page >= 1 && page <= totalPages.value) {
    currentPage.value = page;
  }
}

const visiblePages = computed(() => {
  const pages = [];
  for (let i = 1; i <= totalPages.value; i++) {
    pages.push(i);
  }
  return pages;
});

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

// 새로고침
const isSpinning = ref(false);

// 데이터 리스트 가져오는 함수
const bringTotalList = async () => {
  try {
    // Best 인기 업종 - 전체
    const response = await axios.get(BASEURI + '/getFilteredCreditLoanList', {
      params: {
        companyName: '전체',
        type: '전체',
      }, // 선택된 필터링 값을 쿼리 파라미터로 전송
    });
    if (response.status === 200) {
      dataList.value = response.data;
      totalItems.value = dataList.value.length;
      // console.log(dataList.value);
    } else {
      console.log('데이터 조회 실패');
    }
  } catch (error) {
    console.log('에러발생 :' + error);
  }
};

const refreshIcon = () => {
  isSpinning.value = !isSpinning.value;
  bringTotalList();
  setTimeout(() => {
    isSpinning.value = false; // 회전 후 원래 상태로 돌아오게 함
    selectedBank.value = '전체';
    selectedType.value = '전체';
  }, 500); // 애니메이션 시간에 맞춰 0.5초 후 해제
};

bringBest4List();
bringLoanList();
</script>

<style scoped>
/* nav 아래 hr 같은 선 제거 */
.nav {
  border-bottom: none !important;
}

/* li 간격을 늘리기 위한 스타일 */
.nav-item {
  margin: 0 30px; /* li 요소 간의 좌우 간격을 15px로 설정 */
}
/* 활성화된 탭 스타일 */
.nav-link.active {
  background-color: transparent !important; /* 배경 투명 */
  border-bottom: 2px solid #007bff !important; /* 파란색 밑줄 */
  border-radius: 0 !important; /* 테두리 둥글게 하지 않음 */
  border-width: 0;
}

.nav-link.active h4 {
  color: #0056b3 !important; /* 파란색 텍스트 */
}

/* 비활성화된 탭 스타일 */
.nav-link {
  color: #555 !important; /* 약간 어두운 회색 텍스트 */
  border-width: 0;
}

.nav-link:hover h4 {
  color: #007bff !important; /* 호버 시 파란색 */
  text-decoration: none !important; /* 호버 시 밑줄 제거 */
}
.row.d-flex {
  display: flex;
  flex-wrap: wrap;
}

.card-link {
  width: 100%;
}

.card {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.custom-card {
  padding: 1rem; /* 기본 패딩을 줄입니다 */
  font-size: 0.875rem; /* 폰트 크기를 줄입니다 */
}
.refresh-icon {
  transition: transform 0.5s ease, color 0.5s ease;
}

.refresh-icon.spinning {
  color: #000; /* 클릭 시 검은색으로 변경 */
  transform: rotate(360deg); /* 회전 애니메이션 */
}
</style>
