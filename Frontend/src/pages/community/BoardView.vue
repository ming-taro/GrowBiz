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
      <button type="button" class="btn btn-sm btn-primary ms-2 mb-5 mt-1" @click="editPost">수정</button> <!-- 수정 버튼 추가 -->
      <button type="button" class="btn btn-sm btn-danger ms-2 mb-5 mt-1" @click="showDeleteModal">삭제</button>
    </div>
      
    <div class="list-group mt-5 mb-10">
      <h4 class="fw-semibold mb-5">댓글 {{ comments.length }}</h4>
      <div class="list-group-item py-3" v-for="comment in comments" :key="comment.commentId">
        <div class="d-flex flex-wrap w-100 justify-content-between py-2">
          <h4 class="pt-1">{{ comment.userId }}</h4>
          <button type="button" class="btn btn-sm btn-danger" @click="deleteComment(comment.commentId)">삭제</button>
        </div>
        <p class="font-weight-normal fs-4 text-body py-2 pt-0">{{ comment.content }}</p>
        <small class="text-muted">{{ comment.createdAt }}</small>
      </div>
    </div>
    
    <!-- 댓글 추가 섹션 -->
    <div class="mt-4 mb-10">
      <h5 class="fw-semibold mb-3">댓글 작성</h5>
      <div class="input-group mb-3">
        <input type="text" class="form-control" placeholder="댓글을 입력하세요." v-model="newComment" />
        <button class="btn btn-primary" @click="addComment">추가</button>
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

    <!-- 삭제 확인 모달 -->
  <div v-if="isModalVisible" class="modal show" tabindex="-1" aria-modal="true" style="display: block;">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">삭제 확인</h5>
            <button type="button" class="btn-close" @click="hideDeleteModal"></button>
          </div>
          <div class="modal-body">
            정말로 이 게시글을 삭제하시겠습니까?
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" @click="hideDeleteModal">취소</button>
            <button type="button" class="btn btn-danger" @click="confirmDelete">삭제</button>
          </div>
        </div>
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
const totalPages = ref(5); // 페이지네이션
const isModalVisible = ref(false); // 모달 표시 상태
const newComment = ref(''); // 새로운 댓글 내용
const comments = ref([]); 

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
  } catch (error) {
    console.error('댓글을 가져오는 데 실패했습니다:', error);
  }
};

const confirmDelete = async () => {
  const postId = route.params.postId; 
  try {
    await axios.delete(`http://localhost:8080/api/community/view/${postId}`);
    router.push(`/community/${category.value}`); 
  } catch (error) {
    console.error('게시글 삭제 실패:', error);
    alert('게시글 삭제에 실패했습니다.');
  } finally {
    hideDeleteModal(); // 모달 숨기기
  }
};

// 모달을 여는 함수
const showDeleteModal = () => {
  isModalVisible.value = true;
};

// 모달을 닫는 함수
const hideDeleteModal = () => {
  isModalVisible.value = false;
};



const editPost = () => {
  // 게시글 ID를 세션 스토리지에 저장
  sessionStorage.setItem('editPostId', route.params.postId);
  router.push(`/community/${category.value}/edit`);
};


const addComment = async () => {
  const postId = route.params.postId; // 현재 게시글 ID
  try {
    const response = await axios.post(`http://localhost:8080/api/community/comment`, {
      postId: postId, // 게시글 ID
      userId: 'user34', // 사용자 ID는 로그인된 사용자로 설정해야 합니다.
      content: newComment.value // 댓글 내용
    });
    comments.value.push(response.data); // 새 댓글을 댓글 목록에 추가
    newComment.value = ''; // 입력 필드 비우기
    await fetchComments(); // 새로운 댓글 추가 후 댓글 목록을 다시 가져옴

  } catch (error) {
    console.error('댓글 추가 실패:', error);
    alert('댓글 추가에 실패했습니다.');
  }
};

// 댓글 삭제 함수
const deleteComment = async (commentId) => {
  const postId = route.params.postId; // 현재 게시글 ID
  try {
    await axios.delete(`http://localhost:8080/api/community/comment/${commentId}`); // 댓글 삭제 API 호출
    comments.value = comments.value.filter(comment => comment.commentId !== commentId); // 댓글 목록에서 삭제
  } catch (error) {
    console.error('댓글 삭제 실패:', error);
    alert('댓글 삭제에 실패했습니다.');
  }
};

</script>

<style scoped>
.modal {
  display: block; /* 모달을 항상 표시 */
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5); /* 배경을 어둡게 처리 */
  z-index: 1050; /* Bootstrap 모달 기본 z-index */
}
</style>
