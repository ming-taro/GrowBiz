<template>
  <div>
    <InfoPlazaHeader />
    <div class="container">
      <div class="row align-items-center">
        <!-- 헤딩 -->
        <div class="col-md-6">
          <h1
            class="h3 position-relative pb-sm-2 pb-md-3 mb-5"
            style="z-index: 1021"
          >
            Best 인기 업종 - My 위치
          </h1>
        </div>

        <!-- 필터링 -->
        <div class="row mb-14">
          <div class="col-2"></div>

          <div class="col-md-2"></div>

          <div class="col-1 d-flex justify-content-center align-items-center">
            <i
              class="fa-solid fa-rotate-right refresh-icon mb-2"
              :class="{ spinning: isSpinning }"
              style="font-size: 24px; color: #5a5a5a; cursor: pointer"
              @click="refreshIcon"
            ></i>
          </div>
          <!-- 서비스 업종 -->
          <div class="col-md-2">
            <select
              class="form-select round-corner"
              aria-label="Default select example"
              @change="onServiceChange"
              v-model="selectedService"
            >
              <option value="전체" selected disabled hidden>서비스 업종</option>
              <option value="전체">전체</option>
              <option value="수산물판매">수산물판매</option>
              <option value="일반의류">일반의류</option>
              <option value="컴퓨터및주변장치판매">컴퓨터및주변장치판매</option>
              <option value="반찬가게">반찬가게</option>
              <option value="시계및귀금속">시계및귀금속</option>
              <option value="가전제품">가전제품</option>
              <option value="청과상">청과상</option>
              <option value="육류판매">육류판매</option>
              <option value="일반의원">일반의원</option>
              <option value="조명용품">조명용품</option>
              <option value="한식음식점">한식음식점</option>
              <option value="운동경기용품">운동경기용품</option>
              <option value="화장품">화장품</option>
              <option value="일반교습학원">일반교습학원</option>
              <option value="의약품">의약품</option>
              <option value="문구">문구</option>
              <option value="커피-음료">커피-음료</option>
              <option value="미곡판매">미곡판매</option>
              <option value="외국어학원">외국어학원</option>
              <option value="슈퍼마켓">슈퍼마켓</option>
              <option value="편의점">편의점</option>
              <option value="치과의원">치과의원</option>
              <option value="의료기기">의료기기</option>
              <option value="양식음식점">양식음식점</option>
              <option value="신발">신발</option>
              <option value="전자상거래업">전자상거래업</option>
              <option value="완구">완구</option>
              <option value="화초">화초</option>
              <option value="호프-간이주점">호프-간이주점</option>
              <option value="일식음식점">일식음식점</option>
              <option value="가구">가구</option>
              <option value="안경">안경</option>
              <option value="가방">가방</option>
              <option value="중식음식점">중식음식점</option>
              <option value="미용실">미용실</option>
              <option value="핸드폰">핸드폰</option>
              <option value="분식전문점">분식전문점</option>
              <option value="제과점">제과점</option>
              <option value="자동차수리">자동차수리</option>
              <option value="피부관리실">피부관리실</option>
              <option value="패스트푸드점">패스트푸드점</option>
              <option value="서적">서적</option>
              <option value="인테리어">인테리어</option>
              <option value="한의원">한의원</option>
              <option value="스포츠 강습">스포츠 강습</option>
              <option value="섬유제품">섬유제품</option>
              <option value="부동산중개업">부동산중개업</option>
              <option value="예술학원">예술학원</option>
              <option value="여관">여관</option>
              <option value="스포츠클럽">스포츠클럽</option>
              <option value="자전거 및 기타운송장비">
                자전거 및 기타운송장비
              </option>
              <option value="노래방">노래방</option>
              <option value="치킨전문점">치킨전문점</option>
              <option value="PC방">PC방</option>
              <option value="철물점">철물점</option>
              <option value="골프연습장">골프연습장</option>
              <option value="자동차미용">자동차미용</option>
              <option value="당구장">당구장</option>
              <option value="세탁소">세탁소</option>
              <option value="애완동물">애완동물</option>
            </select>
          </div>

          <!-- 검색창 -->
          <div class="col-5">
            <div class="position-relative w-100 d-flex justify-content-md-end">
              <input
                type="search"
                class="form-control form-control-lg"
                placeholder="Search for products"
                aria-label="Search"
                style="
                  border: none;
                  border-bottom: 2px solid #ced4da;
                  border-radius: 0;
                "
              />
              <button
                type="button"
                class="btn btn-icon btn-ghost fs-lg text-bo border-0 position-absolute top-0 end-0 rounded-circle mt-1 me-1"
                aria-label="Search button"
              >
                <i class="fa-solid fa-magnifying-glass"></i>
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- 사업 아이템 리스트 -->
      <div class="row">
        <!-- 사업 아이템 리스트 본문 -->
        <div class="table-responsive">
          <table class="table table-hover table-sm table-nowrap">
            <thead>
              <tr>
                <th scope="col" class="text-center">순위</th>
                <th scope="col" class="text-center">구</th>
                <th scope="col" class="text-center">동</th>
                <th scope="col" class="text-center">상권</th>
                <th scope="col" class="text-center">서비스 업종</th>
                <th scope="col" class="text-center d-none d-xl-table-cell">
                  총 매출액
                </th>
                <th scope="col" class="text-center d-none d-xl-table-cell">
                  순위 변동
                </th>
                <th scope="col" class="text-center d-none d-xl-table-cell">
                  개업 점포 수
                </th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(item, index) in paginatedData" :key="index">
                <td class="text-center">
                  <div class="d-flex align-items-center gap-3 ps-1">
                    <div>
                      <span class="d-block text-heading fw-bold">{{
                        item.rank
                      }}</span>
                    </div>
                  </div>
                </td>
                <td class="text-center">{{ item.signguCdNm }}</td>
                <td class="text-center">{{ item.adstrdCdNm }}</td>
                <td class="text-center">{{ item.trdarSeCdNm }}</td>
                <td class="text-left d-none d-xl-table-cell">
                  <img
                    :src="'/images/businessItem/' + item.svcIndutyCdNm + '.png'"
                    alt=""
                    style="width: 30px"
                  />
                  {{ item.svcIndutyCdNm }}
                </td>
                <td class="text-center d-none d-xl-table-cell">
                  ₩ {{ item.thsmonSelngAmt.toLocaleString() }}
                </td>
                <td class="text-center d-none d-xl-table-cell">
                  <span
                    class="text-gray-800 fw-bold fs-6 me-3 col-4 text-center"
                    :class="{
                      'text-success': item.rankChange.startsWith('+'),
                      'text-danger':
                        item.rankChange.startsWith('-') &&
                        !/^-\s*$/.test(item.rankChange),
                    }"
                  >
                    {{ item.rankChange }}
                  </span>
                </td>
                <td class="text-center d-none d-xl-table-cell">
                  <span v-if="item.opbizStorCo > 0">
                    <span class="badge badge-light-success fs-base text-center">
                      <i class="fa-solid fa-angle-up"></i>
                      {{ item.opbizStorCo }} 점포</span
                    >
                  </span>
                  <span v-else>
                    <span class="badge badge-light-middle fs-base text-center">
                      {{ item.opbizStorCo }} 점포</span
                    >
                  </span>
                </td>
              </tr>
            </tbody>
          </table>
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
                      <i class="fa-solid fa-angles-left"></i>
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
                      <i class="fa-solid fa-angle-left"></i>
                    </a>
                  </li>
                  <!-- Ellipsis -->
                  <li v-if="currentPage >= 7" class="page-item disabled">
                    <span class="page-link">...</span>
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
                  <!-- Ellipsis -->
                  <li
                    v-if="currentPage <= totalPages - 10"
                    class="page-item disabled"
                  >
                    <span class="page-link">...</span>
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
                      <i class="fa-solid fa-angle-right"></i>
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
                      <i class="fa-solid fa-angles-right"></i>
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
import { ref, computed } from 'vue';
import axios from 'axios';

// 페이지네이션 관련 변수
const currentPage = ref(1); // 현재 페이지
const itemsPerPage = ref(20); // 한 페이지당 아이템 수

const totalItems = computed(() => dataList.value.length); // 전체 아이템 수
const totalPages = computed(() =>
  Math.ceil(totalItems.value / itemsPerPage.value)
); // 전체 페이지 수
const paginatedData = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage.value;
  return dataList.value.slice(start, start + itemsPerPage.value); // 현재 페이지에 표시할 데이터
});
const visiblePages = computed(() => {
  const pages = [];
  const maxVisiblePages = 10; // 한 번에 보여줄 최대 페이지 수
  const startPage = Math.max(1, currentPage.value - 5);

  const endPage = Math.min(startPage + maxVisiblePages - 1, totalPages.value);

  for (let i = startPage; i <= endPage; i++) {
    pages.push(i);
  }
  return pages;
});

// '구' 필터링 변수
const selectedService = ref('전체');

const BASEURI = '/api/infoPlaza/businessItem';

// 필터링된 전체 데이터 리스트
const dataList = ref([]);

// 데이터 리스트 가져오는 함수
const bringDataList = async () => {
  try {
    // Best 인기 업종 - 전체
    const response = await axios.get(BASEURI + '/getFilteredPortionList', {
      params: {
        service: selectedService.value,
      }, // 선택된 필터링 값을 쿼리 파라미터로 전송
    });
    if (response.status === 200) {
      dataList.value = response.data;
      // console.log(dataList.value);
    } else {
      console.log('데이터 조회 실패');
    }
  } catch (error) {
    console.log('에러발생 :' + error);
  }
};

// '서비스업종' 필터링 함수
const onServiceChange = (event) => {
  selectedService.value = event.target.value;
  bringDataList();
};

// 페이지 변경 메소드
const changePage = (page) => {
  if (page < 1 || page > totalPages.value) return;
  currentPage.value = page;
};

const isSpinning = ref(false);
// 리셋 버튼 함수
const refreshIcon = async () => {
  try {
    // Best 인기 업종 - 전체
    isSpinning.value = !isSpinning.value;
    const response = await axios.get(BASEURI + '/getPortion');
    setTimeout(() => {
      isSpinning.value = false; // 회전 후 원래 상태로 돌아오게 함
      selectedSigngu.value = '전체';
      selectedDong.value = '전체';
      selectedService.value = '전체';
    }, 500); // 애니메이션 시간에 맞춰 0.5초 후 해제
    if (response.status === 200) {
      dataList.value = response.data;
    } else {
      console.log('데이터 조회 실패');
    }
  } catch (error) {
    console.log('에러발생 :' + error);
  }
};

bringDataList();
</script>

<style scoped>
.round-corner {
  border-radius: 20px;
}

.badge-light-success {
  background-color: #d4edda !important; /* 밝은 녹색 배경색 */
  color: #155724 !important; /* 진한 녹색 텍스트 */
}
.badge-light-danger {
  background-color: rgba(220, 53, 69, 0.1); /* 연한 빨간색 배경 */
  color: #dc3545; /* 빨간색 텍스트 */
}
.badge-light-middle {
  background-color: rgba(255, 165, 0, 0.1); /* 연한 오렌지색 배경 */
  color: #ff8c00; /* 짙은 오렌지색 텍스트 */
}
.refresh-icon {
  transition: transform 0.5s ease, color 0.5s ease;
}

.refresh-icon.spinning {
  color: #000; /* 클릭 시 검은색으로 변경 */
  transform: rotate(360deg); /* 회전 애니메이션 */
}
</style>
