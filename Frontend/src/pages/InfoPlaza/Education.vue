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
          <label for="inputEmail3" class="col-2 col-form-label"
            >사업주기별</label
          >
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
          <label for="inputEmail3" class="col-2 col-form-label">업종별</label>
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
          <label for="inputEmail3" class="col-2 col-form-label">과목별</label>
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
          <label for="inputEmail3" class="col-2 col-form-label"
            >키워드 검색</label
          >
          <div class="col-9">
            <div class="mt-2">
              <div class="input-group input-group-sm">
                <div class="btn-group dropdown">
                  <select
                    class="form-select"
                    aria-label="Default select example"
                  >
                    <option selected>전체</option>
                    <option value="1">과정명</option>
                    <option value="2">내용</option>
                    <option value="3">해시태그</option>
                    <option value="4">강사명</option>
                  </select>
                </div>
                <input
                  type="text"
                  class="form-control ms-1 rounded"
                  placeholder="검색어를 입력해 주세요."
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
            v-for="(item, index) in paginatedList"
            :key="item.vno"
          >
            <div class="card mb-5" style="cursor: pointer">
              <img
                :src="item.thumbnail"
                class="card-img-top"
                alt="Card image"
              />
              <div class="card-body">
                <h5 class="card-title">{{ item.title }}</h5>
                <div class="d-flex justify-content-center align-items-center">
                  <!-- 수정된 부분 -->
                  <button
                    @click="openVideoPopup(item.videoUrl)"
                    class="btn btn-sm btn-primary mt-2"
                  >
                    시청하기
                  </button>
                  <router-link
                    :to="`/infoplaza/education/video/${item.vno}`"
                    class="btn btn-sm btn-primary mt-2 ms-2"
                    >상세보기</router-link
                  >
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="d-flex justify-content-center mt-4">
          <button
            class="btn btn-secondary"
            @click="prevPage"
            :disabled="currentPage === 1"
          >
            이전
          </button>
          <span class="mx-2">Page {{ currentPage }}</span>
          <button
            class="btn btn-secondary"
            @click="nextPage"
            :disabled="currentPage === totalPages"
          >
            다음
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import InfoPlazaHeader from '@/components/infoplaza/InfoPlazaHeader.vue';
import axios from 'axios';
import { ref, computed, onMounted } from 'vue';

const BASEURI = '/api/infoPlaza/education';
const totalList = ref([]); // 전체 데이터를 저장할 리스트
const currentPage = ref(1); // 현재 페이지 번호
const itemsPerPage = ref(12); // 한 페이지에 보여줄 데이터 개수

// 페이지에 맞는 데이터를 계산하는 computed
const paginatedList = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage.value;
  const end = start + itemsPerPage.value;
  return totalList.value.slice(start, end);
});

// 초기 화면 렌더링 시 불러올 초기 데이터 불러오기
const fetchList = async () => {
  try {
    console.log('TRYING......');
    // 전체 데이터 불러오기
    const response = await axios.get(
      'http://localhost:8080/api/infoPlaza/education/list'
    );
    if (response.status === 200) {
      console.log('데이터 조회 시작');
      totalList.value = response.data; // 조회된 데이터를 totalList에 저장
      console.log(totalList.value);
    } else {
      alert('데이터 조회 실패');
    }
  } catch (error) {
    alert('에러발생 :' + error);
  }
};
function openVideoPopup(videoUrl) {
  if (videoUrl) {
    window.open(videoUrl, '_blank', 'width=800,height=600');
  } else {
    alert('비디오 URL이 없습니다.');
  }
}
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

const selectedOptions = ref({
  사업주기: [],
  업종: [],
  과목: [],
});

// const submitOptions = async () => {
//   try {
//     const response = await axios.post(
//       'http://localhost:8080/api/infoPlaza/education/search',
//       {
//         selectedOptions: selectedOptions.value,
//       }
//     );
//     console.log('Response:', response.data);
//     // 추가적인 로직 (예: 성공 메시지 표시 등)
//   } catch (error) {
//     console.error('Error submitting options:', error);
//     // 에러 처리 로직
//   }
// };

// 총 페이지 수 계산
const totalPages = computed(() => {
  return Math.ceil(totalList.value.length / itemsPerPage.value);
});

// 다음 페이지로 이동
const nextPage = () => {
  if (currentPage.value < totalPages.value) {
    currentPage.value++;
  }
};

// 이전 페이지로 이동
const prevPage = () => {
  if (currentPage.value > 1) {
    currentPage.value--;
  }
};

// 페이지 로딩 시 데이터 호출
onMounted(() => {
  fetchList();
});
</script>

<style scoped>
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
