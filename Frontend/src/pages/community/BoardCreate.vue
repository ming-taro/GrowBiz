<template>
  <div>
    <CommunityHeader />
    <div class="container">
      <div class="flex-fill overflow-y-lg-auto scrollbar bg-body rounded-top-4 rounded-top-start-lg-4 rounded-top-end-lg-0 border-top border-lg shadow-2">
        <main class="container-fluid px-6 pb-10">
          <div class="row align-items-center g-3 mt-6">
            <div class="col-md-12 col-xl-12">
              <input 
                type="text" 
                v-model="postTitle" 
                class="form-control"
                placeholder="제목을 입력하세요." 
              />
            </div>
          </div>
          <hr class="my-6" />
          <div class="row align-items-center g-3">
            <label class="visually-hidden">내용</label>
            <div class="col-md-12 col-xl-12">
              <Editor v-model="postContent" />
            </div>
          </div>
          <hr class="my-6" />
          <div class="d-flex justify-content-end gap-2">
            <RouterLink :to="`/community/${category}`" class="btn btn-sm btn-neutral">취소</RouterLink>            
            <button type="button" class="btn btn-sm btn-primary" @click="submitPost">
              {{ isEditMode ? '수정' : '등록' }}
            </button>
          </div>
        </main>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import axios from 'axios';
import Editor from '@/components/editor/Editor.vue'; 
import CommunityHeader from '@/components/community/CommunityHeader.vue';
import { useAuthStore } from '@/stores/auth'; // Import your auth store

const postTitle = ref('');
const postContent = ref('');
const route = useRoute();
const router = useRouter();
const category = route.params.category; // URL에서 category를 가져옴

const postId = sessionStorage.getItem('editPostId') || null; // postId가 없으면 null로 초기화
const isEditMode = ref(!!postId); // postId가 있으면 수정 모드로 설정

const authStore = useAuthStore();
const userId = authStore.name; // Assuming you have a userId property in your auth store


const submitPost = async () => {
  if (postTitle.value.trim() && postContent.value.trim()) {
    try {
      if (isEditMode.value) {
        // 수정 모드일 때 PUT 요청
        const response = await axios.put(`http://localhost:8080/api/community/${category}/edit`, {
          postId: postId,
          title: postTitle.value,
          content: postContent.value,
          userId: userId 
        });
      } else {
        // 생성 모드일 때 POST 요청
        const response = await axios.post(`http://localhost:8080/api/community/${category}/create`, {
          title: postTitle.value,
          content: postContent.value,
          userId: userId 
        });
      }

      resetFields();
      router.push(`/community/${category}`); // 글 작성 또는 수정 후 해당 카테고리로 이동
    } catch (error) {
      console.error('글 처리 중 오류 발생:', error);
    }
  } else {
    alert('제목과 내용을 입력해주세요.');
  }
};

const resetFields = () => {
  postTitle.value = '';
  postContent.value = '';
};

// onMounted 시점에서 postId가 null인 경우 새 글 작성으로 처리
onMounted(async () => {
  if (isEditMode.value) {
    try {
      const response = await axios.get(`http://localhost:8080/api/community/view/${postId}`);
      postTitle.value = response.data.title;
      postContent.value = response.data.content;
    } catch (error) {
      console.error('게시글 불러오기 중 오류 발생:', error);
    }
  } else {
    // 수정 모드가 아닐 경우 필드를 초기화합니다.
    resetFields(); // 새 글 작성 시 필드 초기화
  }
});
</script>

<style scoped>
</style>
