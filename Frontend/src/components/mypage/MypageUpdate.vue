<template>
  <MypageHeader />
  <div class="container">
    <div class="row pt-sm-2 pt-lg-0 mt-3">
      <!-- Sidebar (offcanvas on sreens < 992px)-->
      <aside class="col-lg-3">
        <div class="position-lg-sticky top-0">
          <div class="d-none d-lg-block"></div>
          <div class="offcanvas-lg offcanvas-start" id="sidebarAccount">
            <button
              class="btn-close position-absolute top-0 end-0 mt-3 me-3 d-lg-none"
              type="button"
              data-bs-dismiss="offcanvas"
              data-bs-target="#sidebarAccount"
            ></button>
            <div class="offcanvas-body">
              <div class="pb-2 pb-lg-0 mb-4 mb-lg-5">
                <img
                  class="d-block rounded-circle mb-2"
                  src="@/assets/img/people/img-1.jpg"
                  width="80"
                  alt="Isabella Bocouse"
                />
                <h4 class="h4 mb-1 fw-bold">최종현</h4>
                <p class="fs-sm text-muted mb-0">wwhdgus112@example.com</p>
                <nav class="nav flex-column pb-2 pb-lg-4 mb-3">
                  <h4
                    class="fs-xs fw-medium text-muted text-uppercase pb-1 mb-2 mt-10"
                  >
                    Account
                  </h4>
                  <a
                    class="nav-link fw-semibold py-2 px-0 active"
                    href="account-overview.html"
                    ><i class="fa-regular fa-user me-3"></i> 내 정보</a
                  ><a
                    class="nav-link fw-semibold py-2 px-0"
                    href="account-settings.html"
                    ><i class="fa-regular fa-pen-to-square me-3"></i>회원정보
                    수정</a
                  ><a
                    class="nav-link fw-semibold py-2 px-0"
                    href="account-billing.html"
                    ><i class="fa-regular fa-folder-open me-3"></i>마이리포트</a
                  >
                </nav>
                <nav class="nav flex-column">
                  <a
                    class="nav-link fw-semibold py-2 px-0"
                    href="account-signin.html"
                    ><i class="fa-solid fa-right-from-bracket me-3"></i>Sign
                    out</a
                  >
                </nav>
              </div>
            </div>
          </div>
        </div>
      </aside>
      <!-- Page content-->
      <div class="col-lg-9 pt-1 pb-2 pb-sm-4">
        <h1 class="h2">내 정보</h1>
        <!-- Basic info-->
        <section class="card mt-3">
          <div class="card-body">
            <div
              class="d-flex align-items-center mt-sm-n1 pb-4 mb-0 mb-lg-1 mb-xl-3"
            >
              <i class="fa-solid fa-id-card me-3" style="font-size: 25px"></i>
              <h2 class="h4 mb-0">기본 정보</h2>
              <a
                class="btn btn-sm btn-secondary ms-auto"
                href="account-settings.html"
                ><i class="fa-solid fa-user-pen me-3"></i>Edit info</a
              >
            </div>
            <div class="d-md-flex align-items-center">
              <div class="d-sm-flex align-items-center">
                <img
                  class="d-block rounded-circle mb-2"
                  src="@/assets/img/people/img-1.jpg"
                  width="100"
                  alt="Isabella Bocouse"
                />
                <div class="pt-3 pt-sm-0 ps-sm-3">
                  <h3 class="h4 mb-2 fw-bold">최종현</h3>
                  <div
                    class="text-muted fw-medium d-flex flex-wrap flex-sm-nowrap align-iteems-center"
                  >
                    <div class="d-flex align-items-center me-3">
                      <i class="fa-regular fa-envelope me-1"></i
                      >email@example.com
                    </div>
                    <div class="d-flex align-items-center text-nowrap">
                      <i class="fa-solid fa-location-dot me-1"></i>KOR
                    </div>
                  </div>
                </div>
              </div>
              <div
                class="w-100 pt-3 pt-md-0 ms-md-auto"
                style="max-width: 212px"
              >
                <div class="d-flex justify-content-between fs-sm pb-1 mb-2">
                  목표 월매출 달성<strong class="ms-2">62%</strong>
                </div>
                <div class="progress" style="height: 5px">
                  <div
                    class="progress-bar"
                    role="progressbar"
                    style="width: 62%"
                    aria-valuenow="62"
                    aria-valuemin="0"
                    aria-valuemax="100"
                  ></div>
                </div>
              </div>
            </div>
            <div class="row py-4 mb-2 mb-sm-3">
              <div class="col-md-6 mb-4 mb-md-0">
                <table class="table table-borderless mb-0">
                  <tbody>
                    <tr>
                      <td class="border-0 text-muted py-1 px-0 fs-6">번호</td>
                      <td class="border-0 text-dark fw-medium py-1 ps-3 fs-6">
                        010-5294-4460
                      </td>
                    </tr>

                    <tr>
                      <td class="border-0 text-muted py-1 px-0 fs-6">매출액</td>
                      <td class="border-0 text-dark fw-medium py-1 ps-3 fs-6">
                        100,000,000 ₩
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </section>
      </div>
    </div>
  </div>
  <Mypage />
  <div class="container mw-screen-sm">
    <div class="card m-3 mt-10">
      <div class="row g-0">
        <div class="col-md-4">
          <img
            src="@/assets/img/people/img-1.jpg"
            class="img-fluid rounded-start m-3"
            alt="..."
            style="width: 130px"
          />
        </div>
        <div class="col-md-8">
          <div
            class="card-body d-flex flex-column justify-content-center"
            style="height: 150px"
          >
            <!-- 카드 높이를 설정 -->
            <p class="card-text">
              <small class="text-body-secondary mb-2">{{
                authStore.state.id
              }}</small>
            </p>

            <h3 class="card-title mb-0">{{ authStore.state.name }}</h3>

            <p class="card-text me-5" style="max-width: 90%">
              {{ authStore.state.email }}
            </p>
            <h6 class="card-title mt-4" style="color: #6184c6">
              <span> 프로필 사진 변경하기</span>
            </h6>
          </div>
        </div>
      </div>
    </div>
    <div>
      <h3 class="mb-5 mt-10">개인정보 변경</h3>
      <div class="custom-line mb-5" />
      <h4 class="mb-6">닉네임 변경</h4>

      <div class="row mb-4">
        <label for="inputNickname" class="col-sm-3 col-form-label"
          >새로운 닉네임</label
        >
        <div class="col-sm-9">
          <input type="text" class="form-control" v-model="newNickname" />
        </div>
      </div>

      <button
        type="submit"
        class="btn btn-primary rounded-pill btn-custom mt-10"
        @click="changeNickname"
        :disabled="!newNickname"
      >
        닉네임 변경하기
      </button>

      <h4 class="mb-6 mt-6">비밀번호 변경</h4>

      <div class="row mb-3">
        <label for="inputEmail3" class="col-sm-3 col-form-label"
          >현재 비밀번호를 입력하세요.</label
        >
        <div class="col-sm-9">
          <input type="text" class="form-control" v-model="oldPassword" />
        </div>
      </div>
      <div class="row mb-3">
        <label for="inputEmail3" class="col-sm-3 col-form-label"
          >새로운 비밀번호를 입력하세요.</label
        >
        <div class="col-sm-9">
          <input type="password" class="form-control" v-model="newPassword1" />
        </div>
      </div>
      <div class="row mb-3">
        <label for="inputEmail3" class="col-sm-3 col-form-label"
          >새로운 비밀번호 확인를 입력하세요.</label
        >
        <div class="col-sm-9">
          <input type="password" class="form-control" v-model="newPassword2" />
        </div>
      </div>

      <button
        type="submit"
        class="btn btn-primary rounded-pill btn-custom mt-10"
        @click="changePassword"
      >
        비밀번호 변경하기
      </button>
    </div>
  </div>
</template>

<script setup>
import Mypage from '@/pages/mypage/Update.vue';
import MypageHeader from '@/components/mypage/MypageHeader.vue';
import { useAuthStore } from '@/stores/auth';
import { ref, onMounted } from 'vue';

const authStore = useAuthStore();
const newNickname = ref('');
const oldPassword = ref('');
const newPassword1 = ref('');
const newPassword2 = ref('');

const changeNickname = () => {
  if (newNickname.value) {
    const memberInfo = {
      id: authStore.state.id, // 기존의 ID 값을 가져오기
      password: authStore.state.password, // 기존의 비밀번호 값을 가져오기
      name: newNickname.value,
      email: authStore.state.email, // 기존의 이메일 값을 가져오기
    };
    authStore.changeProfileName(memberInfo);
    alert('닉네임이 변경되었습니다');
  } else {
    alert('닉네임을 입력해주세요.');
  }
};
const changePassword = () => {
  // oldPassword, newPassword1, newPassword2가 모두 존재하고 newPassword1과 newPassword2가 같을 때
  if (
    oldPassword.value &&
    newPassword1.value &&
    newPassword2.value &&
    newPassword1.value === newPassword2.value
  ) {
    const passwordInfo = {
      id: authStore.state.id,
      oldPassword: oldPassword.value,
      newPassword: newPassword1.value,
    };

    // 비밀번호 변경 로직 호출
    authStore.changePassword(passwordInfo);
  } else {
    // 조건을 만족하지 않는 경우의 알림 메시지
    if (!oldPassword.value) {
      alert('현재 비밀번호를 입력해주세요.');
    } else if (!newPassword1.value || !newPassword2.value) {
      alert('새 비밀번호를 입력해주세요.');
    } else if (newPassword1.value !== newPassword2.value) {
      alert('새 비밀번호가 일치하지 않습니다.');
    }
  }
};
</script>

<style scoped>
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
.page-loading.active > .page-loading-inner {
  opacity: 1;
}
.page-loading-inner > span {
  display: block;
  font-family: 'Inter', sans-serif;
  font-size: 1rem;
  font-weight: normal;
  color: #6f788b;
}
.dark-mode .page-loading-inner > span {
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
  width: 100%; /* 선의 길이 설정 */
  height: 1px; /* 선의 굵기 설정 */
  background-color: #6184c6; /* 선의 색상 설정 */
  margin: 0px 0; /* 원하는 여백 설정 */
}

.btn-custom {
  display: block;

  margin: 0 auto; /* 화면 가운데 정렬 */
  width: 100%; /* 버튼을 가로로 길게 설정 */
  max-width: 200px; /* 최대 너비 설정 */
  padding: 10px 0; /* 버튼 세로 크기 조절 */
}

.table {
  border-collapse: collapse; /* 경계선 제거 */
}

.table td,
.table th {
  border: none; /* 셀 경계선 제거 */
}
</style>
