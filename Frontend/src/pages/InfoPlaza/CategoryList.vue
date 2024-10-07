<template>
  <InfoPlazaHeader />
  <div class="container mw-screen-xl">
    <div class="category-container">
      <div class="vertical-line me-3"></div>
      <div class="category-content ms-3">
        <p class="" style="color: #6184c6">카테고리</p>
        <h2>{{ category }}</h2>
      </div>
    </div>
    <div class="cards mt-10">
      <div class="d-flex justify-content-between align-items-center mb-5">
        <h3 style="font-weight: 600">영상 목록</h3>
        <div class="d-flex">
          <button @click="goBack" class="btn btn-sm btn-link me-2">
            뒤로가기
          </button>
          <router-link to="/infoplaza/education" class="btn btn-sm btn-link">
            전체 목록
          </router-link>
        </div>
      </div>
      <div v-if="loading">로딩 중...</div>
      <!-- Row to contain 4 cards in a single row -->
      <div class="row">
        <div
          class="col-3"
          v-for="(item, index) in paginatedList"
          :key="item.vno"
        >
          <div class="card mb-5" style="cursor: pointer">
            <img :src="item.thumbnail" class="card-img-top" alt="Card image" />
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
                  >상세보기</router-link
                >
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="d-flex justify-content-center align-items-center mt-4">
        <button
          class="btn btn-link"
          @click="prevPage"
          :disabled="currentPage === 1"
        >
          < 이전
        </button>
        <span class="mx-3">{{ currentPage }} / {{ totalPages }}</span>
        <button
          class="btn btn-link"
          @click="nextPage"
          :disabled="currentPage === totalPages"
        >
          다음 >
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import { useRoute } from 'vue-router';
import InfoPlazaHeader from '@/components/infoplaza/InfoPlazaHeader.vue';
import axios from 'axios';

const route = useRoute();
const category = ref('');

const loading = ref(true);

const totalList = ref([]); // 전체 데이터를 저장할 리스트
const currentPage = ref(1); // 현재 페이지 번호
const itemsPerPage = ref(12); // 한 페이지에 보여줄 데이터 개수

const totalPages = computed(() =>
  Math.ceil(totalList.value.length / itemsPerPage.value)
);
const prevPage = () => {
  if (currentPage.value > 1) {
    currentPage.value--;
  }
};
const nextPage = () => {
  if (currentPage.value < totalPages.value) {
    currentPage.value++;
  }
};

// 페이지에 맞는 데이터를 계산하는 computed
const paginatedList = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage.value;
  const end = start + itemsPerPage.value;
  return totalList.value.slice(start, end);
});

const load = async (category) => {
  try {
    const url = new URL('http://localhost:8080/api/infoPlaza/education/search');
    url.searchParams.append('option', category);

    console.log('요청 URL:', url.toString());

    const response = await axios.get(url.toString());
    console.log('전체 응답 데이터:', response.data);

    if (response.status === 200) {
      if (response.data.content) {
        totalList.value = response.data.content;
      } else {
        totalList.value = response.data;
      }
      console.log('설정된 totalList:', totalList.value);
    } else {
      console.error('데이터 조회 실패:', response.status);
    }
  } catch (error) {
    console.error('데이터 불러오기 실패:', error);
    totalList.value = [];
  } finally {
    loading.value = false;
  }
};

onMounted(() => {
  category.value = route.params.category;
  load(category.value);
});

function openVideoPopup(videoUrl) {
  if (videoUrl) {
    window.open(videoUrl, '_blank', 'width=800,height=600');
  } else {
    alert('비디오 URL이 없습니다.');
  }
}

function goBack() {
  router.go(-1);
}
</script>

<style scoped>
.video-item {
  margin-bottom: 20px;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
}

.category-container {
  display: flex;
  align-items: stretch;
}

.vertical-line {
  width: 6px;
  background-color: #6184c6; /* 원하는 색상으로 변경하세요 */
  margin-right: 10px;
}

.category-content {
  display: flex;
  flex-direction: column;
  justify-content: center;
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
