<template>
  <div>
    <InfoPlazaHeader />
    <div class="row">
      <ul
        class="nav nav-tabs custom justify-content-center"
        id="myTab"
        role="tablist"
      >
        <li class="nav-item">
          <RouterLink class="nav-link" to="/infoPlaza/personalCreditLoan"
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
          <RouterLink class="nav-link active" to="/infoPlaza/KBLoan"
            ><h4>국민은행</h4></RouterLink
          >
        </li>
      </ul>
    </div>
    <div class="container mw-screen-xl">
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
              :to="`/infoPlaza/governmentFund/governmentFundDetail/${item.ProductName}`"
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
                        {{ item.productName }}
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
                      {{ item.lowestInterestRate }}%
                    </p>
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
        <div class="col-5 d-flex">
          <!-- col-auto 사용 -->
          <!-- 대출 구분 -->
          <div class="col-4">
            <select
              class="form-select round-corner"
              aria-label="Default select example"
              @change="onCategoryChange"
            >
              <option selected disabled hidden>구분</option>
              <option value="전체">전체</option>
              <option value="직접대출">직접대출</option>
              <option value="대리대출">대리대출</option>
            </select>
          </div>
          <!-- 검색창 -->
          <div class="col-8">
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
            v-for="(item, index) in loanProductList"
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
                          :src="'/images/banklogo/' + '국민은행' + '.png'"
                          alt=""
                          style="width: 100px"
                        />
                      </div>
                      <div class="col-9 d-flex align-items-center">
                        <!-- Change align-items to center -->
                        <span
                          class="fs-3 text-gray-500 fw-bolder pe-2 text-left"
                        >
                          {{ item.productName }}
                        </span>
                      </div>
                    </div>
                    <div class="carousel-inner pt-0">
                      <div class="carousel-item active">
                        <div class="carousel-wrapper">
                          <div class="d-flex flex-column flex-grow-1">
                            <!-- 첫 번째 행: 신청기간 마감 -->
                            

                            <!-- 세 번째 행: 금리 -->
                            <div
                              class="d-flex justify-content-between align-items-center"
                              style="min-height: 2.5rem"
                            >
                              <p class="fs-3">금리</p>
                              <p class="fs-3 fw-bolder">
                                {{ item.lowestInterestRate ? item.lowestInterestRate + '%' : '변동' }}
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
                    :to="`/infoPlaza/governmentFund/governmentFundDetail/${item.loanProductName}`"
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
              
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>
import InfoPlazaHeader from '@/components/infoplaza/InfoPlazaHeader.vue';
import PersonalLoanHeader from '@/components/infoplaza/PersonalLoanHeader.vue';
import { ref, computed, onMounted  } from 'vue';
import axios from 'axios';

const selectedCategory = ref('전체');
const dataList = ref([]);
const best4List = ref([]);

const currentPage = ref(1);
const itemsPerPage = 6;
const totalItems = ref(16);
const totalPages = computed(() => Math.ceil(totalItems.value / itemsPerPage));


const loanProductList = ref([]);

// 데이터 가져오는 함수
const fetchKBLoanAll = async () => {
  try {
    const response = await axios.get('http://localhost:8080/infoPlaza/loan/getKBLoanAll');
    loanProductList.value = response.data;
  } catch (error) {
    console.error('에러 발생: ', error);

  }
};

// BEST 4 상품 데이터 가져오는 함수
const fetchKBLoanBest4 = async () => {
  try {
    const response = await axios.get('http://localhost:8080/infoPlaza/loan/getKBLoanBest4');
    best4List.value = response.data;
  } catch (error) {
    console.error('에러 발생: ', error);
  }
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

// 컴포넌트가 마운트되면 데이터 요청
onMounted(() => {
  fetchKBLoanAll();
  fetchKBLoanBest4();
});

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
</style>
