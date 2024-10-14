<template>
  <div class="container">
    <div class="row mb-10" v-if="showTabs">
      <ul
        class="nav nav-tabs custom justify-content-center"
        id="myTab"
        role="tablist"
      >
        <li class="nav-item">
          <RouterLink
            class="nav-link"
            :class="{ active: category === 'food' }" 
            to="/community/food"
            @mouseover="hoveredCategory = 'food'" 
            @mouseleave="hoveredCategory = ''" 
            ><h4>음식/음료</h4></RouterLink
          >
        </li>
        <li class="nav-item">
          <RouterLink
          class="nav-link"
          :class="{ active: category === 'distribution' }" 
          to="/community/distribution"
          @mouseover="hoveredCategory = 'distribution'"
          @mouseleave="hoveredCategory = ''"
          ><h4>유통</h4></RouterLink
        >
        </li>
        <li class="nav-item">
          <RouterLink
            class="nav-link"
            :class="{ active: category === 'fashion' }"
            to="/community/fashion"
            @mouseover="hoveredCategory = 'fashion'"
            @mouseleave="hoveredCategory = ''"
            ><h4>패션/뷰티</h4></RouterLink
          >
        </li>
        <li class="nav-item">
          <RouterLink
            class="nav-link"
            :class="{ active: category === 'medical' }"
            to="/community/medical"
            @mouseover="hoveredCategory = 'medical'"
            @mouseleave="hoveredCategory = ''"
            ><h4>의료</h4></RouterLink
          >
        </li>
        <li class="nav-item">
          <RouterLink
          class="nav-link"
          :class="{ active: category === 'leisure' }"
          to="/community/leisure"
          @mouseover="hoveredCategory = 'leisure'"
          @mouseleave="hoveredCategory = ''"
          ><h4>여가/오락</h4></RouterLink
        >
        </li>
      </ul>
    </div>
    <!-- 검색 기능 -->
    <div v-if="showSearch" class="row mb-10 justify-content-center">
      <div class="col-8">
        <div class="d-flex align-items-center mt-2">
          <form class="form-group flex-grow-1 me-2" @submit.prevent="searchPosts">
            <div class="input-group input-group-sm">
              <div class="btn-group dropdown">
                <select v-model="filterType" class="form-select" aria-label="Default select example">
                  <option value="all" selected>전체</option>
                  <option value="user">작성자</option>
                  <option value="title">제목</option>
                  <option value="content">내용</option>
                </select>
              </div>
              <input
                type="text"
                v-model="searchKeyword"
                class="rounded form-control ms-1"
                placeholder="검색어를 입력해 주세요."
              />
              <button type="submit" class="ms-1 rounded input-group-text">
                <i class="bi bi-search"></i>
              </button>
            </div>
          </form>

          <!-- 작성 버튼 추가 -->
          <div v-if="showCreateButton && loggedInUserId" class="ms-2"> <!-- 로그인한 ID가 있을 때만 보이도록 설정 -->
            <button type="button" @click="createPost" class="btn btn-sm btn-primary">글작성</button>
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
      <div v-if="showPagination" class="py-4 px-6 mt-3">
        <div
          class="row align-items-center justify-content-center text-center"
        >
          <div class="col-md-12 d-flex flex-column align-items-center">
            <!-- Pagination -->
            <nav aria-label="Page navigation example">
              <ul class="pagination pagination-spaced gap-1">
                <!-- First Page Button -->
                <li class="page-item"
                  :class="{ disabled: currentPage === 1 }">
                  <a
                    class="page-link"
                    href="#"
                    @click.prevent="changePage(1)"
                  >
                    <i class="fa-solid fa-angles-left"></i>
                  </a>
                </li>
                <!-- Previous Page Button -->
                <li
                  class="page-item"
                  :class="{ disabled: currentPage === 1 }"
                >
                  <a
                    class="page-link"
                    href="#"
                    @click.prevent="changePage(currentPage - 1)"
                  >
                    <i class="fa-solid fa-angle-left"></i>
                  </a>
                </li>
                <!-- Ellipsis -->
                <li v-if="currentPage >= 7" class="page-item disabled">
                  <span class="page-link">...</span>
                </li>
                <!-- Page Numbers -->
                <li
                  v-for="page in totalPages"
                  :key="page"
                  class="page-item"
                  :class="{ active: currentPage === page }"
                >
                  <a
                    class="page-link"
                    href="#"
                    @click.prevent="changePage(page)"
                  >
                    {{ page }}
                  </a>
                </li>
                <!-- Ellipsis -->
                <li
                  v-if="currentPage <= totalPages - 10"
                  class="page-item disabled"
                >
                  <span class="page-link">...</span>
                </li>
                <!-- Next Page Button -->
                <li
                  class="page-item"
                  :class="{ disabled: currentPage === totalPages }"
                >
                  <a
                    class="page-link"
                    href="#"
                    @click.prevent="changePage(currentPage + 1)"
                  >
                    <i class="fa-solid fa-angle-right"></i>
                  </a>
                </li>
                <!-- Last Page Button -->
                <li
                  class="page-item"
                  :class="{ disabled: currentPage === totalPages }"
                >
                  <a
                    class="page-link"
                    href="#"
                    @click.prevent="changePage(totalPages)"
                  >
                    <i class="fa-solid fa-angles-right"></i>
                  </a>
                </li>
              </ul>
            </nav>
          </div>
        </div>
      </div>
    </div>
</div>
</template>


<script setup>
import { ref, watch, computed } from 'vue'; // computed 추가
import { defineProps } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router'; // useRouter 추가
import { useAuthStore } from '@/stores/auth'; // Import your auth store

const auth = useAuthStore();
const loggedInUserId = computed(() => auth.name);


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
  showTabs: {
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

const searchKeyword = ref(''); // 검색어 저장
const filterType = ref('all'); // 필터 타입 저장

const paginatedPosts = computed(() => {
  const start = (currentPage.value - 1) * postsPerPage.value;
  const end = start + postsPerPage.value;
  return posts.value.slice(start, end); // 현재 페이지에 해당하는 게시글 반환
});

// 검색 기능 추가
const searchPosts = async () => {
  try {
    const response = await axios.get(`http://localhost:8080/api/community/${props.category}/search`, {
      params: {
        keyword: searchKeyword.value,
        filterType: filterType.value
      }
    });
    posts.value = response.data;
    totalPages.value = Math.ceil(posts.value.length / postsPerPage.value);
    currentPage.value = 1; // 검색 시 페이지를 1로 초기화
  } catch (error) {
    console.error("Error searching posts:", error);
  }
};


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
  currentPage.value = 1; // 카테고리 변경 시 페이지를 1로 초기화
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

/* 타이틀 부분 글자 크기 조정 */
.table thead th {
  font-size: 16px; /* 원하는 크기로 조정 */
  font-weight: bold; /* 글자 두께 조정 */
  padding-top: 12px;
  padding-bottom: 12px;
}
.table tbody td {
  font-size: 14px; /* 원하는 크기로 조정 */
  font-weight: light; /* 글자 두께 조정 */
  padding-top: 12px;
  padding-bottom: 12px;
}

/* nav 아래 hr 같은 선 제거 */
.nav {
  border-bottom: none !important;
}

/* li 간격을 늘리기 위한 스타일 */
.nav-item {
  margin: 0 30px; /* li 요소 간의 좌우 간격을 15px로 설정 */
}
/* 활성화된 탭 스타일 */
.nav-link.active {
  background-color: transparent !important; /* 배경 투명 */
  border-bottom: 2px solid #007bff !important; /* 파란색 밑줄 */
  border-radius: 0 !important; /* 테두리 둥글게 하지 않음 */
  border-width: 0;
}

.nav-link.active h4 {
  color: #0056b3 !important; /* 파란색 텍스트 */
}

/* 비활성화된 탭 스타일 */
.nav-link {
  color: #555 !important; /* 약간 어두운 회색 텍스트 */
  border-width: 0;
}

.nav-link:hover h4 {
  color: #007bff !important; /* 호버 시 파란색 */
  text-decoration: none !important; /* 호버 시 밑줄 제거 */
}


/* 모든 <a> 태그 색상 변경 */
  a {
    color: #6184c6; /* 변경하고 싶은 기본 링크 색상 */
    font-weight: 500;
    text-decoration: none; /* 밑줄 제거 */
  }
  
  
</style>
