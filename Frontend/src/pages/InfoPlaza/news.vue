<template>
  <div>
    <InfoPlazaHeader />

    <div class="container">
      <div class="row mb-10">
        <ul class="nav nav-tabs custom justify-content-center" id="myTab" role="tablist">
          <li class="nav-item">
            <RouterLink
              class="nav-link"
              :class="{ active: category === '경제' || hoveredCategory === 'economy' }"
              to="/infoplaza/news/economy"
              @mouseover="hoveredCategory = 'economy'"
              @mouseleave="hoveredCategory = ''"
            >
              <h4>경제</h4>
            </RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink
              class="nav-link"
              :class="{ active: category === '소상공인' || hoveredCategory === 'smallowner' }"
              to="/infoplaza/news/smallowner"
              @mouseover="hoveredCategory = 'smallowner'"
              @mouseleave="hoveredCategory = ''"
            >
              <h4>소상공인</h4>
            </RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink
              class="nav-link"
              :class="{ active: category === '대출' || hoveredCategory === 'loan' }"
              to="/infoplaza/news/loan"
              @mouseover="hoveredCategory = 'loan'"
              @mouseleave="hoveredCategory = ''"
            >
              <h4>대출</h4>
            </RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink
              class="nav-link"
              :class="{ active: category === '주식' || hoveredCategory === 'stock' }"
              to="/infoplaza/news/stock"
              @mouseover="hoveredCategory = 'stock'"
              @mouseleave="hoveredCategory = ''"
            >
              <h4>주식</h4>
            </RouterLink>
          </li>
        </ul>
      </div>
    </div>

    <div v-if="loading" class="loading-container text-center"> 
      <img src="@/assets/img/common/loading.jpg" alt="Loading..." class="loading-image" />
      <span>데이터 불러오는 중...</span>
    </div>

    <div class="container_news" v-else>
      <div v-for="news in newsList" :key="news.link" class="col-12 mb-3">
        <div class="card">
          <div class="row g-0">
            <div class="col-md-4">
              <a :href="news.link">
                <img
                  :src="news.thumbnail || 'https://via.placeholder.com/150'"
                  class="img-fluid rounded-start"
                  alt="news.title"
                />
              </a>
            </div>
            <div class="col-md-8">
              <div class="card-body">
                <a :href="news.link" class="text-decoration-none text-dark">
                  <h5 class="card-title" v-html="news.title"></h5>
                </a>
                <p class="card-text">{{ news.shortContent }}</p>
                <p class="card-text">
                  <small class="text-muted">{{ news.date }}</small>
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watchEffect, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import InfoPlazaHeader from '@/components/infoplaza/InfoPlazaHeader.vue';
import axios from 'axios';

const newsList = ref([]);
const currentDate = ref(new Date());
const category = ref('');
const hoveredCategory = ref('');
const loading = ref(true); // 로딩 상태 관리
const cachedNews = ref({}); // 캐시된 뉴스 데이터

const categoryMap = {
  economy: '경제',
  smallowner: '소상공인',
  loan: '대출',
  stock: '주식',
};

const route = useRoute();

const formattedDate = computed(() => {
  return currentDate.value.toLocaleDateString('ko-KR', {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
  });
});

async function getNews(query, date) {
  loading.value = true; // 요청 시작 시 로딩 상태 설정

  // 캐시된 데이터가 있는지 확인
  if (cachedNews[query]) {
    newsList.value = cachedNews[query];
    loading.value = false; // 로딩 상태 해제
    return;
  }

  try {
    const response = await axios.get('/api/news', {
      params: {
        query: query,
        startDate: date.replace(/\./g, ''),
        endDate: date.replace(/\./g, ''),
      },
    });

    const newsData = response.data.news;

    newsList.value = newsData.map((item) => ({
      title: item.title.replace(/<[^>]+>/g, ''),
      link: item.link,
      shortContent:
        item.description.replace(/<[^>]+>/g, '').length > 100
          ? item.description.replace(/<[^>]+>/g, '').substring(0, 100) + '...'
          : item.description.replace(/<[^>]+>/g, ''),
      thumbnail: item.thumbnail || 'https://via.placeholder.com/150',
      date: new Date().toLocaleDateString(),
    }));

    // 요청 성공 시 캐시에 저장
    cachedNews[query] = newsList.value;
  } catch (error) {
    console.error('뉴스 검색 중 오류 발생:', error);
  } finally {
    loading.value = false; // 요청 완료 후 로딩 상태 해제
  }
}

watchEffect(() => {
  const routeCategory = route.params.category;
  category.value = categoryMap[routeCategory] || '경제';
  
  getNews(category.value, formattedDate.value);
});

onMounted(() => {
  getNews(category.value, formattedDate.value);
});
</script>

<style scoped>
.container_news {
  margin: 0px 355px;
}
.img-fluid {
  width: 200px;
  height: 200px;
  object-fit: cover;
}

.nav {
  border-bottom: none !important;
}

.nav-item {
  margin: 0 30px;
}

.nav-link.active {
  background-color: transparent !important;
  border-bottom: 2px solid #007bff !important;
  border-radius: 0 !important;
  border-width: 0;
}

.nav-link.active h4 {
  color: #0056b3 !important;
}

.nav-link {
  color: #555 !important;
  border-width: 0;
}

.nav-link:hover h4 {
  color: #007bff !important;
  text-decoration: none !important;
}
.loading-image {
  width: 50px; /* 적절한 크기로 변경 */
  height: 50px; /* 비율에 맞게 높이 자동 조정 */
  margin-bottom: 20px; /* 이미지와 텍스트 간격 조정 */
}
.loading-container {
  display: flex;
  flex-direction: column;
  align-items: center; /* 수직 중앙 정렬 */
  justify-content: top; /* 수평 중앙 정렬 */
  height: calc(100vh - 100px); /* 헤더 높이를 고려한 조정 (80px는 필요에 따라 변경) */
  margin-top: 100px; /* 적절한 마진을 추가하여 아래로 내리기 */
}


</style>
