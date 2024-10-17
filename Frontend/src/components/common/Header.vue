<template>
  <header>
    <div class="contaier">
      <div
        class="mx-2 mx-lg-auto position-relative z-2 px-lg-3 py-0 rounded-3 rounded-lg-pill bg-white"
        style="width: 80%"
      >
        <nav class="navbar navbar-expand-lg navbar-black p-0" id="navbar">
          <div class="container px-sm-0">
            <a class="navbar-brand d-inline-block" href="/"
              ><img src="@/assets/img/logos/logo-gom.png" class="" alt="..." />
            </a>
            <button
              class="navbar-toggler"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#navbarCollapse"
              aria-controls="navbarCollapse"
              aria-expanded="false"
              aria-label="Toggle navigation"
            >
              <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarCollapse">
              <ul class="navbar-nav gap-2 mx-lg-auto">
                <li class="nav-item flex-item header-info-container">
                  <a class="fw-bold nav-link rounded-pill" href="/simul">
                    시뮬레이션
                  </a>
                  <!-- <div class="header-info-dropdown">
                    <RouterLink to="/simul"><span>시작하기</span></RouterLink>
                    <RouterLink to="/simul/report"
                      ><span>결과보기</span></RouterLink
                    > 
                  </div> -->
                </li>

                <li class="nav-item">
                  <a class="fw-bold nav-link rounded-pill" href="/asset"
                    >가게관리</a
                  >
                </li>
                <li class="nav-item flex-item header-info-container">
                  <a
                    class="fw-bold nav-link rounded-pill"
                    href="/community/food"
                  >
                    커뮤니티
                  </a>
                  <div class="header-info-dropdown">
                    <RouterLink to="/community/food"
                      ><span>음식/음료</span></RouterLink
                    >
                    <RouterLink to="/community/distribution"
                      ><span>유통</span></RouterLink
                    >
                    <RouterLink to="/community/fashion"
                      ><span>패션/뷰티</span></RouterLink
                    >
                    <RouterLink to="/community/medical"
                      ><span>의료</span></RouterLink
                    >
                    <RouterLink to="/community/leisure"
                      ><span>여가/오락</span></RouterLink
                    >
                  </div>
                </li>
                <li class="nav-item flex-item header-info-container">
                  <a
                    class="fw-bold nav-link rounded-pill"
                    href="/infoPlaza/industry"
                  >
                    정보광장
                  </a>
                  <div class="header-info-dropdown">
                    <RouterLink to="/infoPlaza/industry"
                      ><span>인기업종</span></RouterLink
                    >
                    <RouterLink to="/infoPlaza/floatpopular"
                      ><span>상권정보</span></RouterLink
                    >
                    <RouterLink to="/infoPlaza/education"
                      ><span>교육정보</span></RouterLink
                    >
                    <RouterLink to="/infoPlaza/personalCreditLoan"
                      ><span>대출정보</span></RouterLink
                    >
                    <RouterLink to="/infoPlaza/news/economy"
                      ><span>뉴스</span></RouterLink
                    >
                  </div>
                </li>
                <li class="nav-item">
                  <a class="fw-bold nav-link rounded-pill" href="/mypageInfo">
                    마이페이지
                  </a>
                </li>
              </ul>
              <div
                class="navbar-nav align-items-lg-center justify-content-end gap-2 ms-lg-4 w-lg-64"
              >
                <a
                  v-if="!authStore.isLogin"
                  href="/register"
                  class="btn fw-bold btn-sm btn-secondary bg-hover border-0 rounded-pill w-100 w-lg-auto mb-4 mb-lg-0"
                  >회원가입</a
                >
                <!-- 로그인/로그아웃 버튼 -->
                <a
                  v-if="!authStore.isLogin"
                  class="fw-bold nav-item nav-link rounded-pill d-none d-lg-block"
                  href="/login"
                  >로그인</a
                >
                <a
                  v-else
                  @click="logout"
                  class="btn fw-bold btn-sm btn-secondary bg-hover rounded-pill"
                  href="#"
                  >로그아웃</a
                >
              </div>
            </div>
          </div>
        </nav>
      </div>
    </div>
  </header>
</template>

<script setup>
import { useAuthStore } from '@/stores/auth';
import { onMounted } from 'vue';

const authStore = useAuthStore();

const logout = (event) => {
  event.preventDefault(); // 기본 동작(페이지 리로딩) 막기
  console.log('logout'); // 로그아웃 클릭 로그 확인
  authStore.logout();
  window.location.href = '/login'; // 로그아웃 후 리디렉션
};

onMounted(() => {
  const headerInfoContainers = document.querySelectorAll(
    '.header-info-container'
  );

  headerInfoContainers.forEach((container) => {
    container.addEventListener('mouseover', () => {
      container.querySelector('.header-info-dropdown').classList.add('show');
    });

    container.addEventListener('mouseleave', () => {
      container.querySelector('.header-info-dropdown').classList.remove('show');
    });
  });
});
</script>

<style>
.header-info-container {
  position: relative;
  flex: 1; /* Ensure it takes up available space */
}

.header-info-title {
  cursor: pointer;
  font-size: small;
}

.header-info-dropdown {
  display: block;
  position: absolute;
  top: 100%;
  left: 0;
  background-color: white;
  border-radius: 20px;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-height: 0;
  overflow: hidden;
  opacity: 0;
  transition: max-height 0.3s ease, opacity 0.3s ease;
}

.header-info-dropdown.show {
  max-height: 500px;
  opacity: 1;
}

.header-info-dropdown span {
  display: block;
  margin: 10px;
  font-size: small;
  cursor: pointer;
  text-align: center;
  color: black;
}

.header-info-dropdown span:hover {
  background-color: #f0f0f0;
  border-radius: 25px;
  font-size: small;
  font-weight: bold;
}

/* Ensure the link text doesn't wrap */
.nav-link {
  white-space: nowrap;
}
</style>
