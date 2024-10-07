<template>
  <div>
    <CommunityHeader />
    <div class="container"> 
      <h2 class="fw-semibold mb-5">{{ post.title }}</h2>
      <h4 class="fw-semibold mb-5 d-flex justify-content-between">
        <span>{{ post.userId }}</span>
        <span class="fw-light ms-auto">{{ post.createdAt }}</span> <!-- 오른쪽으로 밀기 -->
      </h4>
      <hr/>
      <p class="text-m text-muted mb-5 fs-4" v-html="post.content"></p>
      <hr/>
      <div class="text-center gap-2 mb-5">
        <button type="button" class="btn btn-sm btn-neutral mx-1">👍 추천</button>
        <button type="button" class="btn btn-sm btn-neutral mx-1">👎 비추천</button>
      </div>
      <div class="text-center">
      <RouterLink :to="`/community/${category}`" class="btn btn-sm btn-neutral mb-5 mt-1">목록</RouterLink>
      <button type="button" class="btn btn-sm btn-danger ms-2 mb-5 mt-1" @click="deletePost">삭제</button> <!-- 삭제 버튼 추가 -->
    </div>
      
    <div class="list-group mt-5 mb-5">
      <h4 class="fw-semibold mb-5">댓글 {{ comments.length }}</h4>
      <div class="list-group-item py-3" v-for="comment in comments" :key="comment.commentId">
        <div class="d-flex flex-wrap w-100 justify-content-between py-2">
          <h6>{{ comment.userId }}</h6>
        </div>
        <p class="fs-sm font-weight-normal text-body py-2">{{ comment.content }}</p>
        <small class="text-muted">{{ comment.createdAt }}</small>
      </div>
    </div>

      <nav aria-label="Page navigation example">
        <ul class="pagination justify-content-center pagination-spaced gap-1">
          <li class="page-item">
            <a class="page-link" href="#">
              <i class="bi bi-chevron-left"></i>
            </a>
          </li>
          <li class="page-item" v-for="page in totalPages" :key="page">
            <a class="page-link" href="#">{{ page }}</a>
          </li>
          <li class="page-item">
            <a class="page-link" href="#">
              <i class="bi bi-chevron-right"></i>
            </a>
          </li>
        </ul>
      </nav>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import axios from 'axios';
import CommunityHeader from '@/components/community/CommunityHeader.vue';

const route = useRoute();
const post = ref({});
const category = ref('');
const router = useRouter(); // useRouter 추가

onMounted(() => {
  fetchPost();
  fetchComments(); // 댓글 가져오기
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


const fetchComments = async () => {
  const postId = route.params.postId;
  try {
    const response = await axios.get(`http://localhost:8080/api/community/comment/${postId}`);
    comments.value = response.data; // 댓글 데이터를 comments 배열에 저장
    console.log(comments);
  } catch (error) {
    console.error('댓글을 가져오는 데 실패했습니다:', error);
  }
};

const deletePost = async () => {
  const postId = route.params.postId; // 삭제할 게시글의 ID 가져오기
  try {
    await axios.delete(`http://localhost:8080/api/community/view/${postId}`);
    alert('게시글이 삭제되었습니다.');
    router.push(`/community/${category.value}`); // category.value로 변경
  } catch (error) {
    console.error('게시글 삭제 실패:', error);
    alert('게시글 삭제에 실패했습니다.');
  }
};




const comments = ref([
  { author: '작성자1', content: '댓글댓글댓글댓글댓글...', date: '2014-01-23' },
  { author: '작성자2', content: '댓글댓글댓글댓글...', date: '2015-01-25' },
  { author: '작성자3', content: '댓글댓글댓글댓글...', date: '2017-03-23' },
]);

const totalPages = ref(5); // 페이지네이션
</script>

<style scoped>
/* 스타일 추가 */
</style>
