<template>
  <div>
    <InfoPlazaHeader />
    <div class="container mw-screen-xl">
      <form class="form-horizontal card" @submit.prevent="submitOptions">
        <div class="col-12 d-flex justify-content-center mt-4">
          <h4>검색 옵션</h4>
        </div>
        <div class="row m-3">
          <!-- 사업주기별 -->
          <label for="cycle" class="col-2 col-form-label">사업주기별</label>
          <div class="col-9">
            <div class="mt-2">
              <div
                v-for="item in options[0].items"
                :key="item.value"
                class="form-check form-check-inline"
              >
                <input
                  type="checkbox"
                  class="form-check-input"
                  :id="`cycleCheck${item.value}`"
                  :value="item.value"
                  v-model="selectedOptions['사업주기']"
                />
                <label
                  class="form-check-label"
                  :for="`cycleCheck${item.value}`"
                  >{{ item.label }}</label
                >
              </div>
            </div>
          </div>

          <!-- 업종별 -->
          <label for="industry" class="col-2 col-form-label">업종별</label>
          <div class="col-9">
            <div class="mt-2">
              <div
                v-for="item in options[1].items"
                :key="item.value"
                class="form-check form-check-inline"
              >
                <input
                  type="checkbox"
                  class="form-check-input"
                  :id="`industryCheck${item.value}`"
                  :value="item.value"
                  v-model="selectedOptions['업종']"
                />
                <label
                  class="form-check-label"
                  :for="`industryCheck${item.value}`"
                  >{{ item.label }}</label
                >
              </div>
            </div>
          </div>

          <!-- 과목별 -->
          <label for="subject" class="col-2 col-form-label">과목별</label>
          <div class="col-9">
            <div class="mt-2">
              <div
                v-for="item in options[2].items"
                :key="item.value"
                class="form-check form-check-inline"
              >
                <input
                  type="checkbox"
                  class="form-check-input"
                  :id="`subjectCheck${item.value}`"
                  :value="item.value"
                  v-model="selectedOptions['과목']"
                />
                <label
                  class="form-check-label"
                  :for="`subjectCheck${item.value}`"
                  >{{ item.label }}</label
                >
              </div>
            </div>
          </div>

          <!-- 키워드 검색 -->
          <label for="keyword" class="col-2 col-form-label">키워드 검색</label>
          <div class="col-9">
            <div class="mt-2">
              <div class="input-group input-group-sm">
                <div class="btn-group dropdown">
                  <select
                    class="form-select"
                    aria-label="Default select example"
                    v-model="searchType"
                  >
                    <option selected value="all">전체</option>
                    <option value="title">제목</option>
                    <option value="content">내용</option>
                  </select>
                </div>
                <input
                  type="text"
                  class="form-control ms-1 rounded"
                  placeholder="검색어를 입력해 주세요."
                  v-model="searchValue"
                />
              </div>
            </div>
          </div>

          <div class="col-12 d-flex justify-content-center mt-4">
            <button type="submit" class="btn btn-primary mb-4">검색하기</button>
          </div>
        </div>
      </form>

      <div class="cards">
        <h3 class="mb-5" style="font-weight: 600">영상 목록</h3>
        <!-- Row to contain 4 cards in a single row -->
        <div class="row">
          <div
            class="col-3"
            v-for="(item, index) in paginatedData"
            :key="item.vno"
          >
            <div
              class="card mb-5 hover-card"
              style="cursor: pointer"
              @click="goToDetail(item.vno)"
            >
              <img
                :src="item.thumbnail"
                class="card-img-top"
                alt="Card image"
              />
              <div class="card-body">
                <h5 class="card-title">{{ item.title }}</h5>
                <div class="d-flex justify-content-center align-items-center">
                  <button
                    @click="openVideoPopup(item.videoUrl)"
                    class="btn btn-sm btn-primary mt-2"
                  >
                    시청하기
                  </button>
                  <router-link
                    :to="`/infoplaza/education/video/${item.vno}`"
                    class="btn btn-sm btn-primary mt-2 ms-2"
                  >
                    상세보기
                  </router-link>
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
import axios from 'axios';
import { ref, computed, onMounted } from 'vue';
import { useRouter } from 'vue-router';

const BASEURI = '/api/infoPlaza/education';

const selectedOptions = ref({
  사업주기: [],
  업종: [],
  과목: [],
});
const searchType = ref('all'); // 검색 타입 (과정명, 내용 등)
const searchValue = ref(''); // 검색어

const totalList = ref([]); // 전체 데이터를 저장할 리스트

// 페이지네이션 관련 변수
const currentPage = ref(1); // 현재 페이지
const itemsPerPage = ref(12); // 한 페이지당 아이템 수

const totalItems = computed(() => totalList.value.length); // 전체 아이템 수
const totalPages = computed(() =>
  Math.ceil(totalItems.value / itemsPerPage.value)
); // 전체 페이지 수
const paginatedData = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage.value;
  return totalList.value.slice(start, start + itemsPerPage.value); // 현재 페이지에 표시할 데이터
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

// 페이지 변경 메소드
const changePage = (page) => {
  if (page < 1 || page > totalPages.value) return;
  currentPage.value = page;
};

// 초기 화면 렌더링 시 불러올 초기 데이터 불러오기
const fetchList = async () => {
  try {
    // 전체 데이터 불러오기
    const response = await axios.get(
      'http://localhost:8080/api/infoPlaza/education/list'
    );
    if (response.status === 200) {
      totalList.value = response.data; // 조회된 데이터를 totalList에 저장
    } else {
      alert('데이터 조회 실패');
    }
  } catch (error) {
    alert('에러발생 :' + error);
  }
};
const submitOptions = async () => {

  // Check if both options are selected and searchValue is not empty
  const hasSelectedOptions = Object.values(selectedOptions.value).some(
    (options) => options.length > 0
  );

  if (searchValue.value.trim() && hasSelectedOptions) {
    alert('키워드 검색을 하려면 선택된 옵션을 해제해야 합니다.');
    return; // Prevent form submission if both are filled
  }

  // 키워드가 입력되었을 경우
  if (searchValue.value.trim()) {
    await searchByKeyword(searchValue.value, searchType.value);
    return; // 키워드 검색 후 함수 종료
  }

  // 옵션이 선택된 경우
  const selectedQuery = {};

  if (selectedOptions.value['사업주기'].length > 0) {
    selectedQuery['사업주기'] = selectedOptions.value['사업주기'].join(',');
  }
  if (selectedOptions.value['업종'].length > 0) {
    selectedQuery['업종'] = selectedOptions.value['업종'].join(',');
  }
  if (selectedOptions.value['과목'].length > 0) {
    selectedQuery['과목'] = selectedOptions.value['과목'].join(',');
  }

  // 선택된 옵션이 없으면 아무 것도 하지 않음
  if (Object.keys(selectedQuery).length === 0) {
    return; // 아무 일도 하지 않음
  }

  await searchByOptions(selectedQuery); // 옵션을 기반으로 검색
};



const searchByKeyword = async (keyword, type) => {
  try {
    const response = await axios.get(`http://localhost:8080/api/infoPlaza/education/search/keyword`, {
      params: {
        searchType: type,
        searchKeyword: keyword,
      },
    });

    if (response.status === 200) {
      totalList.value = response.data.content || response.data; // content가 없는 경우 전체 데이터 사용
    } else {
      console.error('키워드 검색 실패:', response.status);
    }
  } catch (error) {
    console.error('키워드 검색 중 에러 발생:', error);
    totalList.value = [];
  }
};

const searchByOptions = async (selectedQuery) => {
  const options = [];
  for (const key in selectedQuery) {
    if (selectedQuery[key]) {
      options.push(...selectedQuery[key].split(','));
    }
  }

  const url = new URL('http://localhost:8080/api/infoPlaza/education/search');
  options.forEach((option) => {
    url.searchParams.append('option', option);
  });

  try {
    const response = await axios.get(url.toString());
    if (response.status === 200) {
      totalList.value = response.data.content || response.data; // content가 없는 경우 전체 데이터 사용
    } else {
      console.error('옵션 검색 실패:', response.status);
    }
  } catch (error) {
    console.error('옵션 검색 중 에러 발생:', error);
    totalList.value = [];
  }
};

const load = async (options) => {
  try {
    // URL 객체 생성
    const url = new URL('http://localhost:8080/api/infoPlaza/education/search');

    // 각 옵션을 URL의 쿼리 파라미터로 추가
    options.forEach((option) => {
      url.searchParams.append('option', option);
    });


    const response = await axios.get(url.toString());

    if (response.status === 200) {
      if (response.data.content) {
        totalList.value = response.data.content;
      } else {
        totalList.value = response.data; // content가 없는 경우 전체 데이터 사용
      }
    } else {
      console.error('데이터 조회 실패:', response.status);
    }
  } catch (error) {
    console.error('데이터 불러오기 실패:', error);
    totalList.value = [];
  }
};

function openVideoPopup(videoUrl) {
  if (videoUrl) {
    window.open(videoUrl, '_blank', 'width=800,height=600');
  } else {
    alert('비디오 URL이 없습니다.');
  }
}

const router = useRouter();

const goToDetail = (vno) => {
  router.push(`/infoplaza/education/video/${vno}`);
};

const options = [
  {
    category: '사업주기',
    items: [
      { label: '전체', value: '전체' },
      { label: '창업', value: '창업' },
      { label: '성장', value: '성장' },
      { label: '폐업, 재기', value: '폐업, 재기' },
    ],
  },
  {
    category: '업종',
    items: [
      { label: '전체', value: '전체' },
      { label: '업종무관', value: '업종무관' },
      { label: '제조업', value: '제조업' },
      { label: '도소매업', value: '도소매업' },
      { label: '음식점업', value: '음식점업' },
      { label: '서비스업', value: '서비스업' },
      { label: '숙박업', value: '숙박업' },
    ],
  },
  {
    category: '과목',
    items: [
      { label: '전체', value: '전체' },
      { label: '마케팅', value: '마케팅' },
      { label: '사업장 운영', value: '사업장 운영' },
      { label: '노무&세무&법', value: '노무&세무&법' },
      { label: '수출입', value: '수출입' },
      { label: '지원사업', value: '지원사업' },
      { label: '기업가정신', value: '기업가정신' },
      { label: '교양', value: '교양' },
    ],
  },
];

// 페이지 로딩 시 데이터 호출
onMounted(() => {
  fetchList();
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
.form-horizontal {
  margin: 20px;
}
.cards {
  margin: 60px 0px;
}
.container {
  padding: 0px 80px 0px 80px;
}
.col-form-label {
  font-weight: 500;
}
.card-title {
  display: -webkit-box; /* 플렉스 박스 레이아웃 */
  -webkit-line-clamp: 2; /* 두 줄로 제한 */
  -webkit-box-orient: vertical; /* 수직 정렬 */
  overflow: hidden; /* 넘치는 텍스트 숨김 */
  text-overflow: ellipsis; /* 말줄임표(...) 처리 */
  height: 3em; /* 기본 높이 설정 (line-height: 1.5em이면 두 줄에 해당하는 높이) */
  line-height: 1.5em; /* 줄 간격 설정 */
}
</style>
