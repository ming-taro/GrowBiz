<template>
  <div>
    <CommunityHeader />
    <div class="container">
      <div class="d-flex justify-content-between fw-semibold mb-4 align-items-center"> <!-- align-items-center 추가 -->
        <h2>
        <span class="">{{ post.title }}</span></h2>
        <h4 class="mb-0"> <!-- mb-0 추가하여 아래 마진 제거 -->
          <span class="fw-light">조회수 {{ post.view }}</span>
      </h4>
      </div>
      <h4 class="fw-semibold mb-5 d-flex justify-content-between">
        <span>{{ post.userId }}</span>
        <span class="fw-light ms-auto">{{ post.createdAt }}</span>
      </h4>
      <hr/>
      <p class="text-m text-muted mb-10 fs-4" v-html="post.content"></p>
      <hr/>
      <div class="text-center gap-2 mb-5">
        <button type="button" class="btn btn-sm btn-neutral mx-1" @click="likePost(post.postId)">👍 추천 {{ post.recommend }}</button>
        <button type="button" class="btn btn-sm btn-neutral mx-1" @click="dislikePost(post.postId)">👎 비추천 {{ post.noRecommend }}</button>
      </div>
      <div class="text-center">
        <RouterLink :to="`/community/${category}`" class="btn btn-sm btn-neutral mb-5 mt-1">목록</RouterLink>
        <button type="button" class="btn btn-sm btn-primary ms-2 mb-5 mt-1" @click="editPost">수정</button>
        <button type="button" class="btn btn-sm btn-danger ms-2 mb-5 mt-1" @click="showDeleteModal">삭제</button>
      </div>

      <div class="list-group mt-5 mb-10">
        <h4 class="fw-semibold mb-5">댓글 {{ comments.length }}</h4>
        <div class="list-group-item py-3" v-for="comment in paginatedComments" :key="comment.commentId">
          <div class="d-flex flex-wrap w-100 justify-content-between py-2">
            <h4 class="pt-1">{{ comment.userId }}</h4>
            <button type="button" class="btn btn-sm btn-danger" @click="showDeleteCommentModal(comment.commentId)">삭제</button>
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
            <a class="page-link" href="#" @click.prevent="changePage(currentPage - 1)" :class="{ disabled: currentPage === 1 }">
              <i class="bi bi-chevron-left"></i>
            </a>
          </li>
          <li class="page-item" v-for="page in totalPages" :key="page">
            <a class="page-link" href="#" @click.prevent="changePage(page)" :class="{ active: currentPage === page }">{{ page }}</a>
          </li>
          <li class="page-item">
            <a class="page-link" href="#" @click.prevent="changePage(currentPage + 1)" :class="{ disabled: currentPage === totalPages }">
              <i class="bi bi-chevron-right"></i>
            </a>
          </li>
        </ul>
      </nav>
    </div>

    <!-- 게시글 삭제 확인 모달 -->
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

    <!-- 댓글 삭제 확인 모달 -->
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
import { ref, onMounted, computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import axios from 'axios';
import CommunityHeader from '@/components/community/CommunityHeader.vue';

const route = useRoute();
const post = ref({});
const category = ref('');
const router = useRouter();
const totalPages = ref(1);
const currentPage = ref(1);
const commentsPerPage = 5; // Number of comments per page
const isModalVisible = ref(false); // Post deletion modal state
const isCommentModalVisible = ref(false); // Comment deletion modal state
const newComment = ref('');
const comments = ref([]);
let commentToDelete = ref(null); // 삭제할 댓글 ID

onMounted(() => {
  fetchPost();
  fetchComments();
  category.value = route.params.category;
});

const fetchPost = async () => {
  const postId = route.params.postId;
  
  try {
    // 그 다음 게시글 데이터 가져오기
    const response = await axios.get(`http://localhost:8080/api/community/view/${postId}`);
    post.value = response.data; // 받아온 게시글 데이터 설정
  } catch (error) {
    console.error('Failed to fetch post:', error);
  }
};
// Fetch comments data
const fetchComments = async () => {
  const postId = route.params.postId;
  try {
    const response = await axios.get(`http://localhost:8080/api/community/comment/${postId}`);
    comments.value = response.data;
    calculateTotalPages(); // Update total pages after fetching comments
  } catch (error) {
    console.error('Failed to fetch comments:', error);
  }
};

// Calculate total pages for comments
const calculateTotalPages = () => {
  totalPages.value = Math.ceil(comments.value.length / commentsPerPage);
};

// Change page function
const changePage = (page) => {
  if (page < 1 || page > totalPages.value) return;
  currentPage.value = page;
};

// Comments to display on the current page
const paginatedComments = computed(() => {
  const start = (currentPage.value - 1) * commentsPerPage;
  return comments.value.slice(start, start + commentsPerPage);
});

const confirmDelete = async () => {
  const postId = route.params.postId;
  try {
    await axios.delete(`http://localhost:8080/api/community/view/${postId}`);
    router.push(`/community/${category.value}`);
  } catch (error) {
    console.error('Failed to delete post:', error);
    alert('Failed to delete post.');
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
    await fetchComments(); // Refresh comments after adding
  } catch (error) {
    console.error('Failed to add comment:', error);
    alert('Failed to add comment.');
  }
};

// Show comment deletion modal
const showDeleteCommentModal = (commentId) => {
  commentToDelete.value = commentId; // Store comment ID to delete
  isCommentModalVisible.value = true; // Show modal
};

// Hide comment deletion modal
const hideCommentDeleteModal = () => {
  isCommentModalVisible.value = false;
};

// Confirm comment deletion
const confirmCommentDelete = async () => {
  try {
    await axios.delete(`http://localhost:8080/api/community/comment/${commentToDelete.value}`);
    comments.value = comments.value.filter(comment => comment.commentId !== commentToDelete.value); // Remove from list
    calculateTotalPages(); // Update total pages after deleting
  } catch (error) {
    console.error('Failed to delete comment:', error);
    alert('Failed to delete comment.');
  } finally {
    hideCommentDeleteModal(); // Hide modal
  }
};

// 좋아요 추가
const likePost = async (postId) => {
  try {
    await axios.post(`http://localhost:8080/api/community/view/${postId}/like`);
    post.value.recommend += 1; // 로컬 상태 업데이트
  } catch (error) {
    console.error('Failed to like post:', error);
  }
};

// 싫어요 추가
const dislikePost = async (postId) => {
  try {
    await axios.post(`http://localhost:8080/api/community/view/${postId}/dislike`);
    post.value.noRecommend += 1; // 로컬 상태 업데이트
  } catch (error) {
    console.error('Failed to dislike post:', error);
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
