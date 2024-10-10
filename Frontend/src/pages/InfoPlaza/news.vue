<template>
  <div>
    <InfoPlazaHeader />
    <div class="container">
      <div class="d-flex justify-content-center align-items-center mb-10">
        <ul class="pagination pagination-spaced gap-1 mb-0">
          <li class="page-item">
            <a class="page-link" href="#"><i class="bi bi-chevron-left"></i></a>
          </li>
        </ul>
        <h2 class="mx-3 mb-0">{{ formattedDate }}</h2>
        <ul class="pagination pagination-spaced gap-1 mb-0">
          <li class="page-item">
            <a class="page-link" href="#"
              ><i class="bi bi-chevron-right"></i
            ></a>
          </li>
        </ul>
      </div>

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
import { ref, onMounted } from 'vue';
import InfoPlazaHeader from '@/components/infoplaza/InfoPlazaHeader.vue';
import axios from 'axios';

const newsList = ref([]);
const formattedDate = ref(new Date().toLocaleDateString());

async function getNews(query) {
  try {
    const response = await axios.get('/api/news', {
      params: { query: query },
    });

    // 받아온 데이터를 newsList에 추가
    const newsData = response.data.news;

    // 각 뉴스마다 고유한 thumbnail을 사용하도록 수정
    newsList.value = newsData.map((item) => ({
      title: item.title.replace(/<[^>]+>/g, ''), // HTML 태그 제거
      link: item.link,
      shortContent:
        item.description.length > 100
          ? item.description.substring(0, 100) + '...'
          : item.description, // 짧게 자르기
      thumbnail: item.thumbnail || 'https://via.placeholder.com/150', // 각 뉴스 항목의 개별 thumbnail 값 사용
      date: new Date().toLocaleDateString(), // 임의의 날짜로 설정
    }));
  } catch (error) {
    console.error('뉴스 검색 중 오류 발생:', error);
  }
}

onMounted(() => {
  const searchQuery = '주식'; // 예시 키워드
  getNews(searchQuery);
});
</script>

<style>
.img-fluid {
  width: 250px;
  height: 250px;
}
</style>
