<template>
  <div>
    <CommunityHeader />
    <div class="container"> 
      <h2 class="fw-semibold mb-5">{{ post.title }}</h2>
      <h4 class="fw-semibold mb-5 d-flex justify-content-between">
        <span>{{ post.userId }}</span>
        <span class="fw-light ms-auto">{{ post.createdAt }}</span>
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
        <button type="button" class="btn btn-sm btn-primary ms-2 mb-5 mt-1" @click="editPost">수정</button>
        <button type="button" class="btn btn-sm btn-danger ms-2 mb-5 mt-1" @click="showDeleteModal">삭제</button>
      </div>

      <div class="list-group mt-5 mb-10">
        <h4 class="fw-semibold mb-5">댓글 {{ comments.length }}</h4>
        <div class="list-group-item py-3" v-for="comment in comments" :key="comment.commentId">
          <div class="d-flex flex-wrap w-100 justify-content-between py-2">
            <h4 class="pt-1">{{ comment.userId }}</h4>
            <button type="button" class="btn btn-sm btn-danger" @click="showDeleteCommentModal(comment.commentId)">삭제</button> <!-- 댓글 삭제 버튼 -->
          </div>
          <p class="font-weight-normal fs-4 text-body py-2 pt-0">{{ comment.content }}</p>
          <small class="text-muted">{{ comment.createdAt }}</small>
        </div>
      </div>

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

    <!-- 삭제 확인 모달 -->
    <div v-if="isCommentModalVisible" class="modal show" tabindex="-1" aria-modal="true" style="display: block;">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">삭제 확인</h5>
            <button type="button" class="btn-close" @click="hideCommentDeleteModal"></button>
          </div>
          <div class="modal-body">
            정말로 이 댓글을 삭제하시겠습니까?
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" @click="hideCommentDeleteModal">취소</button>
            <button type="button" class="btn btn-danger" @click="confirmCommentDelete">삭제</button>
          </div>
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
const router = useRouter();
const totalPages = ref(5);
const isModalVisible = ref(false); // 게시글 삭제 모달 상태
const isCommentModalVisible = ref(false); // 댓글 삭제 모달 상태
const newComment = ref('');
const comments = ref([]);
let commentToDelete = ref(null); // 삭제할 댓글 ID 저장

onMounted(() => {
  fetchPost();
  fetchComments();
  category.value = route.params.category;
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
    comments.value = response.data;
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
    hideDeleteModal();
  }
};

const showDeleteModal = () => {
  isModalVisible.value = true;
};

const hideDeleteModal = () => {
  isModalVisible.value = false;
};

const editPost = () => {
  sessionStorage.setItem('editPostId', route.params.postId);
  router.push(`/community/${category.value}/edit`);
};

const addComment = async () => {
  const postId = route.params.postId;
  try {
    const response = await axios.post(`http://localhost:8080/api/community/comment`, {
      postId: postId,
      userId: 'user34',
      content: newComment.value
    });
    comments.value.push(response.data);
    newComment.value = '';
    await fetchComments();
  } catch (error) {
    console.error('댓글 추가 실패:', error);
    alert('댓글 추가에 실패했습니다.');
  }
};

// 댓글 삭제 모달 표시
const showDeleteCommentModal = (commentId) => {
  commentToDelete.value = commentId; // 삭제할 댓글 ID 저장
  isCommentModalVisible.value = true; // 모달 표시
};

// 댓글 삭제 모달 숨기기
const hideCommentDeleteModal = () => {
  isCommentModalVisible.value = false;
};

// 댓글 삭제 확인
const confirmCommentDelete = async () => {
  try {
    await axios.delete(`http://localhost:8080/api/community/comment/${commentToDelete.value}`);
    comments.value = comments.value.filter(comment => comment.commentId !== commentToDelete.value); // 댓글 목록에서 삭제
  } catch (error) {
    console.error('댓글 삭제 실패:', error);
    alert('댓글 삭제에 실패했습니다.');
  } finally {
    hideCommentDeleteModal(); // 모달 숨기기
  }
};
</script>

<style scoped>
.modal {
  display: block;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: 1050;
}
</style>
