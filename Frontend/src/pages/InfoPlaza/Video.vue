<template>
  <InfoPlazaHeader />
  <div class="container mw-screen-xl">
    <button @click="goBack" class="btn ms-3">뒤로가기</button>
    <div class="card m-3">
      <div class="row g-0">
        <div class="col-md-4">
          <img
            :src="video.thumbnail"
            class="img-fluid rounded-start m-3"
            alt="..."
          />
        </div>
        <div class="col-md-8">
          <div class="card-body m-3">
            <h6 class="card-title mb-2" style="color: #6184c6">
              {{ video.category }}
            </h6>
            <h3 class="card-title mb-0">
              {{ video.title }}
            </h3>

            <p class="card-text mt-2 me-5" style="max-width: 90%">
              {{ video.briefIntroduction }}
            </p>
            <p class="card-text">
              <small class="text-body-secondary">{{ video.eduTime }}</small>
            </p>
          </div>
        </div>
      </div>
    </div>
    <div class="introduce">
      <h3 class="ms-5 mb-2 mt-10" style="font-weight: 600">영상 세부사항</h3>
      <hr />
      <h4 class="ms-5 mb-2 mt-4">학습 목표</h4>
      <p class="ms-5 mt-3 mb-2" style="width: 75%">
        {{ video.learningGoal }}
      </p>
      <h4 class="ms-5 mb-2 mt-4">상세 소개</h4>
      <p class="ms-5 mt-3 mb-2" style="width: 75%">
        {{ video.content }}
      </p>
    </div>
    <hr />
    <!-- Nav pills -->
    <ul class="nav nav-pills ms-5">
      <li class="nav-item">
        <a href="#" class="nav-link active">Active</a>
      </li>
      <li class="nav-item">
        <a href="#" class="nav-link">Link</a>
      </li>
      <li class="nav-item">
        <a href="#" class="nav-link">Link</a>
      </li>
      <li class="nav-item">
        <a href="#" class="nav-link disabled" tabindex="-1" aria-disabled="true"
          >Disabled</a
        >
      </li>
    </ul>
  </div>
</template>

<script setup>
import { useRoute, useRouter } from 'vue-router'; // Import the router
import { ref, onMounted } from 'vue';
import InfoPlazaHeader from '@/components/infoplaza/InfoPlazaHeader.vue';
import axios from 'axios';

const props = defineProps({
  vno: {
    type: String,
    required: true,
  },
});

const router = useRouter();
const video = ref({});

const fetchVideo = async (vno) => {
  try {
    const response = await axios.get(
      `http://localhost:8080/api/infoPlaza/education/video/${vno}`
    );
    if (response.status === 200) {
      video.value = response.data; // 받아온 데이터를 video에 저장
    } else {
      alert('비디오 정보를 불러오지 못했습니다.');
    }
  } catch (error) {
    alert('에러 발생: ' + error);
  }
};
onMounted(() => {
  fetchVideo(props.vno);
});

// Function for navigating back

function goBack() {
  router.go(-1); // Navigate to the previous page
}
</script>

<style>
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
</style>
