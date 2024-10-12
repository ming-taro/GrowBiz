<template>
  <div v-if="totalList.length">
    <div class="d-flex align-items-center justify-content-between mb-5">
      <h3>교육정보</h3>
      <router-link to="/infoplaza/education" class="text-primary fw-bold">
        더보기 &gt;
      </router-link>
    </div>

    <div class="row">
      <div
        class="col-6"
        v-for="(item, index) in totalList.slice(0, 2)"
        :key="item.vno"
      >
        <div
          class="card mb-5 hover-card"
          style="cursor: pointer"
          @click="goToDetail(item.vno)"
        >
          <div class="image-container">
            <img :src="item.thumbnail" class="card-img-top" alt="Card image" />
            <div class="overlay">
              <h5 class="card-title m-3">{{ item.title }}</h5>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';

const BASEURI = '/api/infoPlaza/education';

const router = useRouter();

const totalList = ref([]); // 전체 데이터를 저장할 리스트

// 초기 화면 렌더링 시 불러올 초기 데이터 불러오기
const fetchList = async () => {
  try {
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
// 상세 페이지로 이동하는 함수
const goToDetail = (vno) => {
  router.push(`/infoplaza/education/video/${vno}`); // vno를 사용하여 라우팅
};
// 페이지 로딩 시 데이터 호출
onMounted(() => {
  fetchList();
});
</script>

<style scoped>
.card {
  height: 200px; /* 카드의 고정된 높이 */
  overflow: hidden;
}

.image-container {
  position: relative;
  height: 100%; /* 카드 높이에 맞춤 */
  overflow: hidden; /* 자식 요소가 컨테이너를 넘어가지 않도록 설정 */
}

.card-img-top {
  height: 100%;
  object-fit: cover; /* 이미지 비율 유지하면서 꽉 차게 설정 */
}

.overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5); /* 불투명한 검은색 배경 */
  display: flex;
  align-items: center; /* 수직 중앙 정렬 */
  justify-content: center; /* 수평 중앙 정렬 */

  font-size: 1.2rem; /* 제목 크기 */
  text-align: center; /* 제목 중앙 정렬 */
  opacity: 0; /* 초기 투명도 설정 */
  transition: opacity 0.3s; /* 호버 시 투명도 전환 효과 */
}
.card-title {
  color: white; /* 제목 색상 */
}

.card:hover .overlay {
  opacity: 1; /* 호버 시 불투명하게 변경 */
}
</style>
