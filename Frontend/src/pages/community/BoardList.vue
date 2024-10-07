<template>
  <div class="container">
    <div v-if="posts.length === 0">게시글이 없습니다.</div>
    <div v-else>
      <div class="table-responsive">
        <table class="table table-nowrap text-center">
          <thead>
            <tr>
              <th scope="col">번호</th>
              <th scope="col">제목</th>
              <th scope="col">작성자</th>
              <th scope="col">조회</th>
              <th scope="col">추천</th>
              <th scope="col">작성일</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="post in posts" :key="post.originalPostId">
              <td>{{ post.postId }}</td>
              <td>
                <a :href="`/community/${category}/view/` + post.originalPostId">{{ post.title }}</a>
              </td>
              <td>{{ post.userId }}</td>
              <td>{{ post.view }}</td>
              <td>{{ post.recommend }}</td>
              <td>{{ post.createdAt }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>


<script setup>
import { ref, watch } from 'vue';
import { defineProps } from 'vue';
import axios from 'axios';

const props = defineProps({
  category: {
    type: String,
    required: true
  }
});

const posts = ref([]);

const fetchPostsByCategory = async (category) => {
  try {
    const response = await axios.get(`http://localhost:8080/api/community/${category}`);
    posts.value = response.data; // 받아온 게시글 목록 설정
    console.log(posts.value);
  } catch (error) {
    console.error("Error fetching posts:", error);
  }
};

// 카테고리 prop이 변경될 때마다 게시글 목록을 다시 가져옴
watch(() => props.category, (newCategory) => {
  fetchPostsByCategory(newCategory);
});

// 페이지 로드 시 기본 카테고리 게시글을 가져옴
fetchPostsByCategory(props.category);
</script>

<style scoped>
</style>
