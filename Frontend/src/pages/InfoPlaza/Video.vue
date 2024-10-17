<template>
  <InfoPlazaHeader />
  <div class="container mw-screen-xl">
    <div
      class="position-relative mb-8 d-flex align-items-end justify-content-center"
    >
      <h2 class="fw-bold m-0">영상 정보</h2>
      <button
        @click="goBack"
        class="btn btn-sm btn-link position-absolute end-0 mt-6"
      >
        뒤로가기
      </button>
    </div>
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
              <span v-html="formattedCategories"></span>
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
            <button
              @click="openVideoPopup(video.videoUrl)"
              class="btn btn-primary mt-2"
            >
              시청하기
            </button>
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
    <div class="d-flex flex-wrap ms-5 gap-2">
      <button
        v-for="hashtag in formattedHashtags"
        :key="hashtag"
        class="btn btn-secondary btn-sm"
        @click="goToCategory(hashtag.slice(1))"
        style="border-radius: 20px"
      >
        {{ hashtag }}
      </button>
    </div>
  </div>
</template>

<script setup>
import { useRoute, useRouter } from 'vue-router'; // Import the router
import { ref, onMounted, computed } from 'vue';
import InfoPlazaHeader from '@/components/infoplaza/InfoPlazaHeader.vue';
import axios from 'axios';

const formattedCategories = computed(() => {
  if (!video.value.category) return '';
  return video.value.category
    .split(/\s+/)
    .map(
      (word) =>
        `<span class="category-link" onclick="window.goToCategory('${word.replace(
          /[,.]$/,
          ''
        )}')">${word}</span>`
    )
    .join(' ');
});

const formattedHashtags = computed(() => {
  if (!video.value.category) return [];
  return video.value.category
    .split(/\s+/)
    .map((word) => '#' + word.replace(/[,.]$/, '').trim())
    .filter((tag) => tag.length > 1);
});

// goToCategory 함수를 script 내부로 이동
const goToCategory = (category) => {
  router.push({
    name: 'CategoryList',
    params: { category: category },
  });
};

window.goToCategory = (category) => {
  router.push({
    name: 'CategoryList',
    params: { category: category },
  });
};

const props = defineProps({
  vno: {
    type: String,
    required: true,
  },
});

const router = useRouter();
const video = ref({});

function openVideoPopup(videoUrl) {
  if (videoUrl) {
    window.open(videoUrl, '_blank', 'width=800,height=600');
  } else {
    alert('비디오 URL이 없습니다.');
  }
}

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
