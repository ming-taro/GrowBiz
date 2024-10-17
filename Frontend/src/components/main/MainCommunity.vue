<template>
<div class="mb-10">
    <div class="container">
    <h2 style="font-weight: bold" class="mb-5">커뮤니티</h2>
    </div>
    <BoardList :posts="posts" category="food" :showPagination="false" :showTabs="false" :showSearch="false" :showCreateButton="false" />
</div>
</template>

<script setup>
import BoardList from '@/pages/community/BoardList.vue';
import { ref, onMounted } from 'vue';
import axios from 'axios';

const posts = ref([]); // 게시글을 저장할 reactive 변수
const latestPosts = ref([]); // 최신 게시글을 저장할 reactive 변수

onMounted(async () => {
  const category = 'food'; // 기본 카테고리를 'food'로 설정
    try {
        const response = await axios.get(`http://localhost:8080/api/community/${category}`); // API 호출
        posts.value = response.data; // 받은 데이터를 posts에 저장
        // 최신 5개 게시글만 필터링하여 필요한 형태로 변환
        
    } catch (error) {
        console.error('게시글을 불러오는 데 실패했습니다.', error);
    }
});
</script>

<style></style>
