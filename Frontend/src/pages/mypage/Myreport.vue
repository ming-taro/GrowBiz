<template>
  <div class="app">
    <MypageHeader />

    <div class="container">
      <div class="row pt-sm-2 pt-lg-0 mt-3">
        <!-- Sidebar (offcanvas on sreens < 992px)-->
        <aside class="col-lg-3 mt-3">
          <div class="position-lg-sticky top-0">
            <div class="d-none d-lg-block"></div>
            <div class="offcanvas-lg offcanvas-start" id="sidebarAccount">
              <button class="btn-close position-absolute top-0 end-0 mt-3 me-3 d-lg-none" type="button"
                data-bs-dismiss="offcanvas" data-bs-target="#sidebarAccount"></button>
              <div class="offcanvas-body">
                <div class="pb-2 pb-lg-0 mb-4 mb-lg-5">
                  <img class="d-block rounded-circle mb-2" :src="profileImageUrl" width="80" alt="Isabella Bocouse" />
                  <h4 class="h4 mb-1 fw-bold">{{ member.name }}</h4>
                  <p class="fs-sm text-muted mb-0">{{ member.email }}</p>
                  <nav class="nav flex-column pb-2 pb-lg-4 mb-3">
                    <h4 class="fs-xs fw-medium text-muted text-uppercase pb-1 mb-2 mt-10">
                      Account
                    </h4>
                    <RouterLink class="nav-link fw-semibold py-2 px-0" to="/mypageInfo#myInfo"><i
                        class="fa-regular fa-user me-3"></i> 내
                      정보</RouterLink><a class="nav-link fw-semibold py-2 px-0" href="#edit-section"><i
                        class="fa-regular fa-pen-to-square me-3"></i>회원정보
                      수정</a><a class="nav-link fw-semibold py-2 px-0" href="account-billing.html"><i
                        class="fa-regular fa-folder-open me-3"></i>마이리포트</a>
                  </nav>
                  <nav class="nav flex-column">
                    <a class="nav-link fw-semibold py-2 px-0" href="account-signin.html" @click="logout"><i
                        class="fa-solid fa-right-from-bracket me-3"></i>로그아웃</a>
                  </nav>
                </div>
              </div>
            </div>
          </div>
        </aside>
        <!-- Page content-->
        <div class="col-lg-9 pt-1 pb-2 pb-sm-4">
          <h1 class="h2" id="myInfo">My 리포트</h1>

          <div class="table-responsive">
            <table class="table table-nowrap table-flush">
              <thead>
                <tr>
                  <th scope="col">
                    <div class="d-flex align-items-center gap-2 ps-1">
                      <div class="text-base">
                        <div class="form-check">
                          <input class="form-check-input" type="checkbox" />
                        </div>
                      </div>
                      <span>
                        <h4>브랜드</h4>
                      </span>
                    </div>
                  </th>
                  <th scope="col">
                    <h4>자본</h4>
                  </th>
                  <th scope="col">
                    <h4>업종</h4>
                  </th>
                  <th scope="col">
                    <h4>추천위치</h4>
                  </th>
                  <th scope="col">
                    <h4>날짜</h4>
                  </th>
                  <th></th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="report in reports" :key="report.reportId" @click=showReport(report.reportId)
                  style="cursor: pointer">
                  <td>
                    <div class=" d-flex align-items-center gap-3 ps-1">
                      <div class="text-base">
                        <div class="form-check">
                          <input class="form-check-input" type="checkbox" />
                        </div>
                      </div>
                      <div
                        class="icon icon-shape w-rem-10 h-rem-10 rounded-circle text-sm bg-primary bg-opacity-25 text-tertiary">
                        <i class="bi bi-file-fill"></i>
                      </div>
                      <div>
                        <span class="d-block text-heading fw-bold">
                          {{ report.brandName }}
                        </span>
                      </div>
                    </div>
                  </td>
                  <td>
                    <a class="text-current">{{ report.capital }}</a>
                  </td>
                  <td>{{ report.category }}</td>
                  <td>{{ report.location }}</td>
                  <td>{{ formatCreatedDate(report.createdAt) }}</td>
                  <td class="text-end">
                    <div class="dropdown">
                      <a class="text-muted" href="#" role="button" data-bs-toggle="dropdown" aria-haspopup="true"
                        aria-expanded="false">
                        <i class="bi bi-three-dots-vertical"></i>
                      </a>
                      <div class="dropdown-menu dropdown-menu-end">
                        <a href="#!" class="dropdown-item">Action</a>
                        <a href="#!" class="dropdown-item">Another action</a>
                        <a href="#!" class="dropdown-item">Something else here</a>
                      </div>
                    </div>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import MypageHeader from '@/components/mypage/MypageHeader.vue';
import { useAuthStore } from '@/stores/auth';
import { useRouter } from 'vue-router';
import { ref, computed, onMounted } from 'vue';
import axios from 'axios';
import { findAllReports } from '@/services/simulation/ReportAPI';
import { fetchResponseById } from '@/services/simulation/SimulationAPI';

const authStore = useAuthStore();
const router = useRouter();

// 회원 정보를 저장할 변수 선언
const member = ref({
  img: null,
  id: '',
  mno: '',
  name: '',
  email: '',
  phone: '',
  goalAmount: 0,
  message: '',
  mno: '', // 회원 고유번호 (mno) 추가
  gender: '',
});

// 프로필 이미지 URL을 동적으로 설정하는 computed 속성
const profileImageUrl = computed(() => {
  return authStore.id
    ? `http://localhost:8080/api/member/${authStore.id}/avatar`
    : 'src/assets/img/people/img-1.jpg'; // 기본 이미지 경로
});

// API로부터 회원 데이터를 가져오는 함수
const getMemberData = async () => {
  try {
    // authStore.mno로 회원 고유번호를 사용하여 API 요청
    const response = await axios.get(
      `http://localhost:8080/api/member/${authStore.id}`
    );
    member.value = response.data; // 응답 데이터를 member에 저장
  } catch (error) {
    console.error('회원 정보를 불러오는 중 오류가 발생했습니다.', error);
  }
};

const answers = ref([]);
const reports = ref([]);

const formatCreatedDate = (createdAt) => {
  const inputDate = new Date(createdAt);

  const formattedDate = inputDate.toLocaleDateString('ko-KR', {
    year: 'numeric',
    month: 'numeric',
    day: 'numeric'
  });

  const result = formattedDate.replace(/(\d{4})\.\s(\d{1,2})\.\s(\d{1,2})/, "$1년 $2월 $3일").replace(/\.$/, ''); // 마지막 점 제거;

  return result;
}

const showReport = (reportId) => {
  location.href = `/simul/report?id=${reportId}`; // 리포트 페이지로 이동
}

const fetchResponse = async (responseId) => {
  return await fetchResponseById(responseId);
}

const formatPrice = (value) => {
  if (value >= 10000) {
    const eok = Math.floor(value / 10000);
    const man = value % 10000;

    if (man === 0) {
      return new Intl.NumberFormat().format(eok) + '억';
    } else {
      return new Intl.NumberFormat().format(eok) + '억 ' + new Intl.NumberFormat().format(man) + '만원';
    }
  } else {
    return new Intl.NumberFormat().format(value) + '만원';
  }
}

onMounted(async () => {
  reports.value = await findAllReports(authStore.id);

  for (let index = 0; index < reports.value.length; index++) {
    const response = await fetchResponse(reports.value[index].simulationResponseId);
    reports.value[index]["category"] = response[3].subcategories;
    reports.value[index]["location"] = response[0].district + " " + response[0].neighborhoods;
    reports.value[index]["capital"] = formatPrice(response[4].text);
  }

  console.log(reports.value);
  getMemberData();
})
</script>

<style scoped>
.app {
  background-color: rgb(246, 249, 252);
  min-height: 100vh;
  /* 최소 높이를 100vh로 설정하여 화면을 다 채우도록 함 */
}

.card {
  box-shadow: 0 1px 10px rgba(0, 0, 0, 0.1);
  /* 얇은 그림자 */
}

.page-loading {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 100%;
  -webkit-transition: all 0.4s 0.2s ease-in-out;
  transition: all 0.4s 0.2s ease-in-out;
  background-color: #fff;
  opacity: 0;
  visibility: hidden;
  z-index: 9999;
}

.dark-mode .page-loading {
  background-color: #121519;
}

.page-loading.active {
  opacity: 1;
  visibility: visible;
}

.page-loading-inner {
  position: absolute;
  top: 50%;
  left: 0;
  width: 100%;
  text-align: center;
  -webkit-transform: translateY(-50%);
  transform: translateY(-50%);
  -webkit-transition: opacity 0.2s ease-in-out;
  transition: opacity 0.2s ease-in-out;
  opacity: 0;
}

.page-loading.active>.page-loading-inner {
  opacity: 1;
}

.page-loading-inner>span {
  display: block;
  font-family: 'Inter', sans-serif;
  font-size: 1rem;
  font-weight: normal;
  color: #6f788b;
}

.dark-mode .page-loading-inner>span {
  color: #fff;
  opacity: 0.6;
}

.page-spinner {
  display: inline-block;
  width: 2.75rem;
  height: 2.75rem;
  margin-bottom: 0.75rem;
  vertical-align: text-bottom;
  background-color: #d7dde2;
  border-radius: 50%;
  opacity: 0;
  -webkit-animation: spinner 0.75s linear infinite;
  animation: spinner 0.75s linear infinite;
}

.dark-mode .page-spinner {
  background-color: rgba(255, 255, 255, 0.25);
}

@-webkit-keyframes spinner {
  0% {
    -webkit-transform: scale(0);
    transform: scale(0);
  }

  50% {
    opacity: 1;
    -webkit-transform: none;
    transform: none;
  }
}

@keyframes spinner {
  0% {
    -webkit-transform: scale(0);
    transform: scale(0);
  }

  50% {
    opacity: 1;
    -webkit-transform: none;
    transform: none;
  }
}

.custom-line {
  width: 100%;
  /* 선의 길이 설정 */
  height: 1px;
  /* 선의 굵기 설정 */
  background-color: #6184c6;
  /* 선의 색상 설정 */
  margin: 0px 0;
  /* 원하는 여백 설정 */
}

.btn-custom {
  display: block;

  margin: 0 auto;
  /* 화면 가운데 정렬 */
  width: 100%;
  /* 버튼을 가로로 길게 설정 */
  max-width: 200px;
  /* 최대 너비 설정 */
  padding: 10px 0;
  /* 버튼 세로 크기 조절 */
}

.table {
  border-collapse: collapse;
  /* 경계선 제거 */
}

.table td,
.table th {
  border: none;
  /* 셀 경계선 제거 */
}
</style>
