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
            <button type="button" class="btn btn-sm btn-primary" @click="submitPost">등록</button>
          </div>
        </main>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRoute, useRouter } from 'vue-router'; // Router 가져오기
import Editor from '@/components/editor/Editor.vue';
import axios from 'axios';
import CommunityHeader from '@/components/community/CommunityHeader.vue';

// Reactive properties for title and content
const postTitle = ref('');
const postContent = ref('');
const route = useRoute(); // 라우트 객체를 사용하여 URL에서 카테고리 값을 가져옴
const router = useRouter(); // 라우터 인스턴스 가져오기
const category = route.params.category; // 카테고리 매개변수 가져오기

const submitPost = async () => {
  if (postTitle.value.trim() && postContent.value.trim()) {

      // HTML 태그 처리
      const cleanContent = postContent.value
      .replace(/<\/?p[^>]*>/g, '\n')  // <p> 태그를 줄바꿈으로 대체
      .replace(/<\/?div[^>]*>/g, '\n') // <div> 태그를 줄바꿈으로 대체 (필요시)
      .replace(/<br\s*\/?>/g, '\n');   // <br> 태그를 줄바꿈으로 대체

    try {
      const response = await axios.post(`http://localhost:8080/api/community/${category}/create`, {
        title: postTitle.value,
        content: cleanText,
        category: category,
        userId: '김수현'
      });

      alert('글이 성공적으로 작성되었습니다.');
      resetFields();

      router.push(`/community/${category}`); // 글 작성 후 해당 카테고리로 이동
    } catch (error) {
      console.error('글 작성 중 오류 발생:', error);
      alert('글 작성 중 오류가 발생했습니다.');
    }
  } else {
    alert('제목과 내용을 입력해주세요.');
  }
};

// Method to reset input fields
const resetFields = () => {
  postTitle.value = '';
  postContent.value = '';
};
</script>

<style scoped>
</style>
