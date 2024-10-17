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
                      href="#edit-section"
                      ><i class="fa-regular fa-pen-to-square me-3"></i>회원정보
                      수정</a
                    ><a
                      class="nav-link fw-semibold py-2 px-0"
                      href="account-billing.html"
                      ><i class="fa-regular fa-folder-open me-3"></i
                      >마이리포트</a
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
                <a class="btn btn-sm btn-primary ms-auto" href="#edit-section"
                  ><i class="fa-solid fa-user-pen me-3"></i>수정하기</a
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
                        <td class="border-0 text-muted py-1 px-0 fs-6">
                          매출액
                        </td>
                        <td class="border-0 text-dark fw-medium py-1 ps-3 fs-6">
                          100,000,000 ₩
                        </td>
                      </tr>
                      <tr>
                        <td class="border-0 text-muted py-1 px-0 fs-6">
                          상태 메세지
                        </td>
                        <td
                          class="border-0 text-muted fw-medium py-1 ps-3 fs-6"
                        >
                          우리 동네 일등 음식점 가자!!
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
          </section>

          <!-- Basic info-->
          <h1 class="h2 mt-10" id="edit-section">회원정보 수정</h1>
          <section class="card mt-3">
            <div class="card-body">
              <div class="d-flex align-items-center">
                <div class="dropdown">
                  <a
                    class="d-flex flex-column justify-content-end position-relative overflow-hidden rounded-circle bg-size-cover bg-position-center flex-shrink-0"
                    href="#"
                    data-bs-toggle="dropdown"
                    aria-expanded="false"
                    style="
                      width: 80px;
                      height: 80px;
                      background-image: url(/src/assets/img/people/img-1.jpg);
                      background-size: cover; /* 이미지가 배경에 꽉 차도록 */
                      background-position: center; /* 이미지가 가운데에 오도록 */
                    "
                  >
                    <span
                      class="d-block text-light text-center lh-1 pb-1"
                      style="background-color: rgba(0, 0, 0, 0.5)"
                    >
                      <i class="fa-solid fa-camera"></i>
                    </span>
                  </a>

                  <div class="dropdown-menu my-1">
                    <a class="dropdown-item fw-normal" href="#"
                      ><i class="ai-camera fs-base opacity-70 me-2"></i>이미지
                      업로드하기</a
                    ><a class="dropdown-item text-danger fw-normal" href="#"
                      ><i class="ai-trash fs-base me-2"></i>이미지 삭제하기</a
                    >
                  </div>
                </div>
                <div class="ps-3">
                  <h3 class="h6 mb-1">프로필 사진</h3>
                  <p class="fs-6 text-muted mb-0">
                    PNG 또는 JPG, 가로 및 세로 크기가 1000px을 넘기지 않게
                    하십시오.
                  </p>
                </div>
              </div>
              <div class="row g-3 g-sm-4 mt-0 mt-lg-2">
                <div class="col-sm-6">
                  <label class="form-label" for="fn">닉네임</label>
                  <input class="form-control" type="text" id="fn" />
                </div>

                <div class="col-sm-6">
                  <label class="form-label" for="email">이메일 주소</label>
                  <input class="form-control" type="email" id="email" />
                </div>
                <div class="col-sm-6">
                  <label class="form-label" for="phone">
                    연락처 <span class="text-muted">(optional)</span>
                  </label>
                  <input
                    class="form-control"
                    type="tel"
                    data-format='{"numericOnly": true, "delimiters": ["-"], "blocks": [3, 4, 4]}'
                    placeholder="010-xxxx-xxxx"
                    id="phone"
                  />
                </div>
                <div class="col-sm-6">
                  <label class="form-label" for="phone"
                    >목표 매출액
                    <span class="text-muted">(optional)</span></label
                  >
                  <input class="form-control" type="number" id="phone" />
                </div>
                <div class="col-12">
                  <label class="form-label" for="bio">상태 메세지</label>
                  <textarea
                    class="form-control"
                    rows="5"
                    placeholder="상태 메세지를 입력하세요."
                    id="bio"
                  ></textarea>
                </div>
                <div
                  class="col-12 d-sm-flex align-items-center pt-sm-2 pt-md-3"
                >
                  <div class="form-label text-muted mb-2 mb-sm-0 me-sm-4">
                    Gender:
                  </div>
                  <div class="form-check form-check-inline mb-0">
                    <input
                      class="form-check-input"
                      type="radio"
                      name="gender"
                      value="Male"
                      id="male"
                    />
                    <label class="form-check-label" for="male">남자</label>
                  </div>
                  <div class="form-check form-check-inline mb-0">
                    <input
                      class="form-check-input"
                      type="radio"
                      name="gender"
                      value="Female"
                      checked
                      id="female"
                    />
                    <label class="form-check-label" for="female">여자</label>
                  </div>
                </div>

                <div class="col-12 d-flex justify-content-end pt-3">
                  <button class="btn btn-dark" type="button">Cancel</button>
                  <button class="btn btn-primary ms-3" type="button">
                    Save changes
                  </button>
                </div>
              </div>
            </div>
          </section>
          <h1 class="h2 mt-10">비밀번호 수정</h1>
          <!-- Password-->
          <section class="card border-0 py-1 p-md-2 p-xl-3 p-xxl-4 mb-4 mt-3">
            <div class="card-body">
              <div class="row align-items-center g-3 g-sm-4 pb-3">
                <div class="col-sm-6">
                  <label class="form-label" for="current-pass"
                    >현재 비밀번호</label
                  >
                  <div class="password-toggle">
                    <input
                      class="form-control"
                      type="password"
                      value="hidden@password"
                      id="current-pass"
                    />
                    <label
                      class="password-toggle-btn"
                      aria-label="Show/hide password"
                    >
                    </label>
                  </div>
                </div>
                <div class="col-sm-6"></div>
                <div class="col-sm-6">
                  <label class="form-label" for="new-pass"
                    >새로운 비밀번호</label
                  >
                  <div class="password-toggle">
                    <input class="form-control" type="password" id="new-pass" />
                    <label
                      class="password-toggle-btn"
                      aria-label="Show/hide password"
                    >
                    </label>
                  </div>
                </div>
                <div class="col-sm-6">
                  <label class="form-label" for="confirm-pass"
                    >새로운 비밀번호 확인</label
                  >
                  <div class="password-toggle">
                    <input
                      class="form-control"
                      type="password"
                      id="confirm-pass"
                    />
                    <label
                      class="password-toggle-btn"
                      aria-label="Show/hide password"
                    >
                    </label>
                  </div>
                </div>
              </div>
              <div class="alert alert-info d-flex my-3 my-sm-4">
                <i class="ai-circle-info fs-xl me-2"></i>
                <p class="mb-0">
                  Password must be minimum 8 characters long - the more, the
                  better.
                </p>
              </div>
              <div class="d-flex justify-content-end pt-3">
                <button class="btn btn-dark" type="button">Cancel</button>
                <button class="btn btn-primary ms-3" type="button">
                  Save changes
                </button>
              </div>
            </div>
          </section>
        </div>
      </div>
    </div>
  </div>

  <div class="container mw-screen-sm">
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
.app {
  background-color: rgb(246, 249, 252);
  min-height: 100vh; /* 최소 높이를 100vh로 설정하여 화면을 다 채우도록 함 */
}
.card {
  box-shadow: 0 1px 10px rgba(0, 0, 0, 0.1); /* 얇은 그림자 */
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
