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

<div class="container">
    <div class="row mb-10">
      <ul
        class="nav nav-tabs custom justify-content-center"
        id="myTab"
        role="tablist"
      >
        <li class="nav-item">
          <RouterLink
            class="nav-link"
            :class="{ active: category === 'economy' }" 
            to="/news/economy"
            @mouseover="hoveredCategory = 'economy'" 
            @mouseleave="hoveredCategory = ''" 
            ><h4>경제</h4></RouterLink
          >
        </li>
        <li class="nav-item">
          <RouterLink
          class="nav-link"
          :class="{ active: category === 'distribution' }" 
          to="/community/distribution"
          @mouseover="hoveredCategory = 'distribution'"
          @mouseleave="hoveredCategory = ''"
          ><h4>소상공인</h4></RouterLink
        >
        </li>
        <li class="nav-item">
          <RouterLink
            class="nav-link"
            :class="{ active: category === 'fashion' }"
            to="/community/fashion"
            @mouseover="hoveredCategory = 'fashion'"
            @mouseleave="hoveredCategory = ''"
            ><h4>대출</h4></RouterLink
          >
        </li>
        <li class="nav-item">
          <RouterLink
            class="nav-link"
            :class="{ active: category === 'medical' }"
            to="/community/medical"
            @mouseover="hoveredCategory = 'medical'"
            @mouseleave="hoveredCategory = ''"
            ><h4>주식</h4></RouterLink
          >
        </li>
        
      </ul>
    </div>
</div>

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
        item.description.replace(/<[^>]+>/g, '').length > 100 // description에서 HTML 태그 제거 후 길이 체크
          ? item.description.replace(/<[^>]+>/g, '').substring(0, 100) + '...' // HTML 태그 제거 후 100자로 자르기
          : item.description.replace(/<[^>]+>/g, ''), // HTML 태그 제거
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
</style>
