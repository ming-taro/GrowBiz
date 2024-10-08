<template>
  <div>
    <CommunityHeader />
    <BoardList :posts="posts" :category="route.params.category" />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import CommunityHeader from '@/components/community/CommunityHeader.vue';
import BoardList from '@/pages/community/BoardList.vue';
import axios from 'axios';

const route = useRoute();
const posts = ref([]);

onMounted(async () => {
  const category = route.params.category; // URL에서 카테고리 가져오기
  try {
    const response = await axios.get(`http://localhost:8080/api/community/${category}`); // API 호출
    posts.value = response.data; // 받은 데이터를 posts에 저장
  } catch (error) {
    console.error('게시글을 불러오는 데 실패했습니다.', error);
  }
});
</script>

<style scoped>
</style>
