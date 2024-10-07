<template>
  <div>
    <CommunityHeader />
    <div class="container"> 
      <h3 class="fw-semibold mb-5">{{ post.title }}</h3>
      <p class="text-m text-muted mb-5">{{ post.content }}</p>
      <div class="text-center gap-2 mb-5">
        <button type="button" class="btn btn-sm btn-neutral mx-1">👍 추천</button>
        <button type="button" class="btn btn-sm btn-neutral mx-1">👎 비추천</button>
      </div>
      <RouterLink :to="`/community/${category}`" class="btn btn-sm btn-neutral mb-5 mt-1">목록</RouterLink>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import axios from 'axios';
import CommunityHeader from '@/components/community/CommunityHeader.vue';

const route = useRoute();
const post = ref({});
const category = ref('');

onMounted(() => {
  fetchPost();
  category.value = route.params.category;  // URL의 category 값을 가져옵니다.
});
const fetchPost = async () => {
  const postId = route.params.postId;
  try {
    const response = await axios.get(`http://localhost:8080/api/community/view/${postId}`);
    post.value = response.data;
  } catch (error) {
    console.error('게시글을 가져오는 데 실패했습니다:', error);
  }
};

</script>

<style scoped>
/* 스타일 추가 */
</style>
