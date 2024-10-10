<template>
  <div>
    <InfoPlazaHeader />
    <!-- <div class="d-flex justify-content-center align-items-center mb-10">
      <ul class="pagination pagination-spaced gap-1 mb-0">
        <li class="page-item">
          <a class="page-link" href="#" @click.prevent="changeDate(-1)">
            <i class="bi bi-chevron-left"></i>
          </a>
        </li>
      </ul>
      <h2 class="mx-3 mb-0">{{ formattedDate }}</h2>
      <ul class="pagination pagination-spaced gap-1 mb-0">
        <li class="page-item">
          <a class="page-link" href="#" @click.prevent="changeDate(1)">
            <i class="bi bi-chevron-right"></i>
          </a>
        </li>
      </ul>
    </div> -->

    <div class="container_news">
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
import { ref, computed, watchEffect, onMounted } from 'vue'; // watchEffect 추가
import InfoPlazaHeader from '@/components/infoplaza/InfoPlazaHeader.vue';
import axios from 'axios';

const newsList = ref([]);
const currentDate = ref(new Date());

// 날짜 형식 포맷 함수
const formattedDate = computed(() => {
  return currentDate.value.toLocaleDateString('ko-KR', {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
  });
});

// 날짜 변경 함수
// function changeDate(direction) {
//   // direction이 -1이면 이전 날, 1이면 다음 날
//   currentDate.value.setDate(currentDate.value.getDate() + direction);

//   // 날짜 변경 직후, currentDate의 값을 사용하여 뉴스를 다시 조회
//   const newFormattedDate = currentDate.value.toLocaleDateString('ko-KR', {
//     year: 'numeric',
//     month: '2-digit',
//     day: '2-digit',
//   });

//   getNews('주식', newFormattedDate); // 변경된 날짜로 조회
// }

// 뉴스 API 요청 함수
async function getNews(query, date) {
  try {
    const response = await axios.get('/api/news', {
      params: {
        query: query,
        startDate: date.replace(/\./g, ''), // "YYYY.MM.DD" 형식을 "YYYYMMDD"로 변환
        endDate: date.replace(/\./g, ''),
      },
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
  getNews('주식', formattedDate.value); // 초기 로드 시 오늘 날짜로 뉴스 불러옴
});
</script>

<style>
.container_news {
  margin: 0px 355px;
}
.img-fluid {
  width: 200px; /* 원하는 가로 크기 */
  height: 200px; /* 원하는 세로 크기 */
  object-fit: cover; /* 이미지 비율을 유지하면서 영역을 채움 */
}
</style>
