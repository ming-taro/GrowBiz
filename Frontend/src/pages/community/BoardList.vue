<template>
  <div class="container">
    <!-- 검색 기능 -->
    <div v-if="showSearch" class="row mb-10 justify-content-center  ">
      <div class="col-8">
        <div class="d-flex justify-content-between align-items-center mt-2">
          <form class="form-group flex-grow-1 me-2">
            <div class="input-group input-group-sm">
              <div class="btn-group dropdown">
                <select class="form-select" aria-label="Default select example">
                  <option selected>전체</option>
                  <option value="1">작성자</option>
                  <option value="2">제목</option>
                  <option value="3">내용</option>
                </select>
              </div>
              <input
                type="text"
                class="rounded form-control ms-1"
                placeholder="검색어를 입력해 주세요."
              />
              <span class="ms-1 rounded input-group-text">
                <i class="bi bi-search"></i>
              </span>
            </div>
          </form>
          </div>

          <!-- 작성 버튼 추가 -->
          <div v-if="showCreateButton" class="ms-auto">
            <div>
              <button type="button" @click="createPost" class="btn btn-sm btn-primary mb-5">글작성</button>
          </div>
          </div>
        </div>
      </div>
      <div class="border-top">
      <div class="table-responsive mb-5">
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
            <tr v-for="post in paginatedPosts" :key="post.originalPostId">
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
      
      <!-- 페이지네이션 기능 -->
      <div v-if="showPagination" class="py-4 px-6 d-flex justify-content-center">
        <nav aria-label="Page navigation example">
          <ul class="pagination pagination-spaced gap-1">
            <li class="page-item" :class="{ disabled: currentPage === 1 }">
              <a class="page-link" @click="changePage(currentPage - 1)" href="#"><</a>
            </li>
            <li class="page-item" v-for="page in totalPages" :key="page" :class="{ active: currentPage === page }">
              <a class="page-link" @click="changePage(page)" href="#">{{ page }}</a>
            </li>
            <li class="page-item" :class="{ disabled: currentPage === totalPages }">
              <a class="page-link" @click="changePage(currentPage + 1)" href="#">></a>
            </li>
          </ul>
        </nav>
      </div>
    </div>
</div>
</template>


<script setup>
import { ref, watch, computed } from 'vue'; // computed 추가
import { defineProps } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router'; // useRouter 추가

const router = useRouter(); // router 정의

const props = defineProps({
  posts: {
    type: Array,
    required: true
  },
  category: {
    type: String,
    required: true
  },
  showPagination: {
    type: Boolean,
    default: true
  },
  showSearch: {
    type: Boolean,
    default: true
  },
  showCreateButton: {
    type: Boolean,
    default: true
  }
});

const posts = ref([]);
const currentPage = ref(1); // 현재 페이지
const postsPerPage = ref(8); // 페이지당 게시글 수
const totalPages = ref(0); // 전체 페이지 수

const paginatedPosts = computed(() => {
  const start = (currentPage.value - 1) * postsPerPage.value;
  const end = start + postsPerPage.value;
  return posts.value.slice(start, end); // 현재 페이지에 해당하는 게시글 반환
});

const fetchPostsByCategory = async (category) => {
  try {
    const response = await axios.get(`http://localhost:8080/api/community/${category}`);
    posts.value = response.data; // 받아온 게시글 목록 설정
    totalPages.value = Math.ceil(posts.value.length / postsPerPage.value); // 전체 페이지 수 계산
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

// 페이지 변경 함수
const changePage = (page) => {
  if (page < 1 || page > totalPages.value) return; // 유효하지 않은 페이지 수는 무시
  currentPage.value = page; // 현재 페이지 업데이트
};


// 글 작성 버튼의 경우 세션 스토리지를 비우고 글 작성 페이지로 이동
const createPost = () => {
  sessionStorage.removeItem('editPostId'); // 세션 스토리지 비우기
  router.push(`/community/${props.category}/create`); // 새로운 게시글 작성 페이지로 이동
};
</script>

<style scoped>
</style>
