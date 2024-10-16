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
                    :src="profileImageUrl"
                    width="80"
                    alt="Isabella Bocouse"
                  />
                  <h4 class="h4 mb-1 fw-bold">{{ member.name }}</h4>
                  <p class="fs-sm text-muted mb-0">{{ member.email }}</p>
                  <nav class="nav flex-column pb-2 pb-lg-4 mb-3">
                    <h4
                      class="fs-xs fw-medium text-muted text-uppercase pb-1 mb-2 mt-10"
                    >
                      Account
                    </h4>
                    <RouterLink
                      class="nav-link fw-semibold py-2 px-0"
                      to="/mypageInfo#myInfo"
                      ><i class="fa-regular fa-user me-3"></i> 내
                      정보</RouterLink
                    ><a
                      class="nav-link fw-semibold py-2 px-0"
                      href="#edit-section"
                      ><i class="fa-regular fa-pen-to-square me-3"></i>회원정보
                      수정</a
                    ><RouterLink
                      class="nav-link fw-semibold py-2 px-0"
                      to="/mypage/myreport"
                      ><i class="fa-regular fa-folder-open me-3"></i
                      >마이리포트</RouterLink
                    >
                  </nav>
                  <nav class="nav flex-column">
                    <a
                      class="nav-link fw-semibold py-2 px-0"
                      href="account-signin.html"
                      @click="logout"
                      ><i class="fa-solid fa-right-from-bracket me-3"></i
                      >로그아웃</a
                    >
                  </nav>
                </div>
              </div>
            </div>
          </div>
        </aside>
        <!-- Page content-->
        <div class="col-lg-9 pt-1 pb-2 pb-sm-4">
          <h1 class="h2" id="myInfo">내 정보</h1>
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
                    :src="profileImageUrl"
                    width="100"
                    alt="Isabella Bocouse"
                  />
                  <div class="pt-3 pt-sm-0 ps-sm-3">
                    <h3 class="h4 mb-2 fw-bold">{{ member.name }}</h3>
                    <div
                      class="text-muted fw-medium d-flex flex-wrap flex-sm-nowrap align-iteems-center"
                    >
                      <div class="d-flex align-items-center me-3">
                        <i class="fa-regular fa-envelope me-1"></i
                        >{{ member.email }}
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
                    목표 월매출 달성<strong class="ms-2"
                      >{{ saleRate }}%</strong
                    >
                  </div>
                  <div class="progress" style="height: 5px">
                    <div
                      class="progress-bar"
                      role="progressbar"
                      :style="{ width: `${saleRate}%` }"
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
                          <span v-if="member.phone">{{ member.phone }}</span>
                          <span v-else class="text-muted"
                            >번호를 등록하세요.</span
                          >
                        </td>
                      </tr>

                      <tr>
                        <td class="border-0 text-muted py-1 px-0 fs-6">
                          월 매출액
                        </td>
                        <td class="border-0 text-dark fw-medium py-1 ps-3 fs-6">
                          ₩ {{ formattedSaleAmount }}
                        </td>
                      </tr>
                      <tr>
                        <td class="border-0 text-muted py-1 px-0 fs-6">
                          상태 메세지
                        </td>
                        <td
                          class="border-0 text-muted fw-medium py-1 ps-3 fs-6"
                        >
                          <span v-if="member.message">{{
                            member.message
                          }}</span>
                          <span v-else>상태 메세지를 등록하세요.</span>
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
                    :style="`width: 80px; height: 80px; background-image: url(${computedImageUrl}); background-size: cover; background-position: center;`"
                  >
                    <span
                      class="d-block text-light text-center lh-1 pb-1"
                      style="background-color: rgba(0, 0, 0, 0.5)"
                    >
                      <i class="fa-solid fa-camera"></i>
                    </span>
                  </a>

                  <div class="dropdown-menu my-1">
                    <input
                      type="file"
                      @change="handleFileUpload"
                      accept="image/png, image/jpeg"
                    />
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
                  <input
                    class="form-control"
                    type="text"
                    id="fn"
                    v-model="memberEdit.name"
                  />
                </div>

                <div class="col-sm-6">
                  <label class="form-label" for="email">이메일 주소</label>
                  <input
                    class="form-control"
                    type="email"
                    id="email"
                    v-model="memberEdit.email"
                  />
                </div>
                <div class="col-sm-6">
                  <label class="form-label" for="phone"
                    >연락처 <span class="text-muted">(선택)</span></label
                  >
                  <input
                    class="form-control"
                    type="tel"
                    placeholder="010-xxxx-xxxx"
                    v-model="memberEdit.phone"
                  />
                </div>
                <div class="col-sm-6">
                  <label class="form-label" for="goal"
                    >목표 월 매출액
                    <span class="text-muted">(선택)</span></label
                  >
                  <input
                    class="form-control"
                    type="text"
                    v-model="formattedGoalAmount"
                    @input="updateGoalAmount($event.target.value)"
                  />
                </div>
                <div class="col-12">
                  <label class="form-label" for="bio"
                    >상태 메세지 <span class="text-muted">(선택)</span></label
                  >
                  <textarea
                    class="form-control"
                    rows="5"
                    v-model="memberEdit.message"
                    placeholder="상태 메세지를 입력하세요."
                  ></textarea>
                </div>
                <div class="col-12 d-flex justify-content-end pt-3">
                  <button
                    class="btn btn-dark"
                    type="button"
                    @click="resetMemberEdit"
                  >
                    취소하기
                  </button>
                  <button
                    class="btn btn-primary ms-3"
                    type="button"
                    @click="saveProfile"
                  >
                    저장하기
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
                      v-model="oldPassword"
                    />
                  </div>
                </div>
                <div class="col-sm-6"></div>
                <div class="col-sm-6">
                  <label class="form-label" for="new-pass"
                    >새로운 비밀번호</label
                  >
                  <div class="password-toggle">
                    <input
                      class="form-control"
                      type="password"
                      v-model="newPassword1"
                    />
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
                      v-model="newPassword2"
                    />
                  </div>
                </div>
              </div>
              <div
                class="alert alert-info d-flex my-3 my-sm-4"
                v-if="authStore.alertMessage"
              >
                <i class="ai-circle-info fs-xl me-2"></i>
                <p class="mb-0">
                  {{ authStore.alertMessage }}
                </p>
              </div>
              <div class="d-flex justify-content-end pt-3">
                <button
                  class="btn btn-dark"
                  type="button"
                  @click="resetPasswordFields"
                >
                  취소하기
                </button>
                <button
                  class="btn btn-primary ms-3"
                  type="button"
                  @click="changePassword"
                >
                  저장하기
                </button>
              </div>
            </div>
          </section>

          <h1 class="h2 mt-10">계정 삭제</h1>
          <section class="card border-0 py-1 p-md-2 p-xl-3 p-xxl-4 mb-4 mt-3">
            <div class="card-body">
              <span class="text me-3">
                <h4>주의할 점</h4>
                <br />
                <p>계정을 삭제하면 모든 데이터가 손실됩니다.</p>
              </span>
              <span class="d-flex justify-content-end pt-3">
                <button
                  class="btn btn-danger ms-3"
                  type="button"
                  @click="deleteAccount"
                >
                  계정 삭제하기
                </button>
              </span>
            </div>
          </section>
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

const authStore = useAuthStore();
const router = useRouter();

if (!authStore.isLogin) {
  router.push('/login');
}

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
const memberEdit = ref({
  img: null,
  id: authStore.id,
  mno: authStore.mno,
  name: '',
  email: '',
  phone: '',
  goalAmount: 0,
  message: '',
  gender: '남자',
});

const oldPassword = ref('');
const newPassword1 = ref('');
const newPassword2 = ref('');

// 프로필 이미지 URL을 동적으로 설정하는 computed 속성
const profileImageUrl = computed(() => {
  return authStore.id
    ? `http://localhost:8080/api/member/${authStore.id}/avatar`
    : 'src/assets/img/people/img-1.jpg'; // 기본 이미지 경로
});

// computed로 이미지 URL 결정
const computedImageUrl = computed(() => {
  return memberEdit.value.img || profileImageUrl.value; // 업로드한 이미지가 있으면 그 이미지, 없으면 기본 이미지
});

// API로부터 회원 데이터를 가져오는 함수
const getMemberData = async () => {
  try {
    // authStore.mno로 회원 고유번호를 사용하여 API 요청
    const response = await axios.get(
      `http://localhost:8080/api/member/${authStore.id}`
    );
    member.value = response.data; // 응답 데이터를 member에 저장
    memberEdit.value = response.data;
    memberEdit.value = { ...response.data };
  } catch (error) {
    console.error('회원 정보를 불러오는 중 오류가 발생했습니다.', error);
  }
};

// 파일 업로드 핸들러
const handleFileUpload = (event) => {
  const file = event.target.files[0]; // 선택된 파일
  if (file) {
    memberEdit.value.img = URL.createObjectURL(file); // 이미지 미리보기

    memberEdit.value.avatarFile = file; // 파일 객체 저장
  } else {
    console.error('No file selected or file is invalid.');
  }
};
// const goToMyPage = () => {
//   router.push('MypageInfo');
// };

// 프로필 저장 함수
const saveProfile = async () => {
  const formData = new FormData();
  formData.append('mno', authStore.mno);
  formData.append('id', authStore.id);
  formData.append('name', memberEdit.value.name);
  formData.append('email', memberEdit.value.email);
  formData.append('phone', memberEdit.value.phone);
  formData.append('goalAmount', memberEdit.value.goalAmount);
  formData.append('message', memberEdit.value.message);
  formData.append('gender', '남자'); // gender 추가
  formData.append('avatar', memberEdit.value.avatarFile); // 파일 추가

  const confirmUpdate = window.confirm('정말 수정하시겠습니까?');
  try {
    if (confirmUpdate) {
      // ID를 가져오는 부분은 사용자의 고유 ID로 수정해야 합니다.
      const id = authStore.id; // 예시로 회원 고유 번호를 사용
      const response = await axios.put(
        `http://localhost:8080/api/member/${id}`,
        formData,
        {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        }
      );
      window.location.reload();
    }
  } catch (error) {
    console.error('Error updating profile:', error);
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
    authStore
      .changePassword(passwordInfo)
      .then(() => {
        // 비밀번호 변경이 성공했을 때, 입력 필드 초기화
        oldPassword.value = '';
        newPassword1.value = '';
        newPassword2.value = '';
      })
      .catch((error) => {});
  } else {
    // 조건을 만족하지 않는 경우의 알림 메시지
    if (!oldPassword.value) {
      authStore.alertMessage = '현재 비밀번호를 입력해주세요.';
    } else if (!newPassword1.value || !newPassword2.value) {
      authStore.alertMessage = '새 비밀번호를 입력해주세요.';
    } else if (newPassword1.value !== newPassword2.value) {
      authStore.alertMessage = '새 비밀번호가 일치하지 않습니다.';
    }
  }
};
// 버튼 클릭 시 memberEdit 값을 member 값으로 초기화하는 메서드
const resetMemberEdit = () => {
  memberEdit.value = { ...member.value }; // member 값을 memberEdit으로 복사
};
// 비밀번호 입력 필드를 초기화하는 메서드
const resetPasswordFields = () => {
  oldPassword.value = '';
  newPassword1.value = '';
  newPassword2.value = '';
};
const logout = (event) => {
  event.preventDefault(); // 기본 동작(페이지 리로딩) 막기
  console.log('logout'); // 로그아웃 클릭 로그 확인
  authStore.logout();
  router.push('/');
};
const deleteAccount = async () => {
  try {
    const response = await axios.delete(
      `http://localhost:8080/api/member/${authStore.id}`
    );
    // 성공적으로 삭제된 경우의 처리
    console.log('Account deleted:', response.data);
    alert('계정이 성공적으로 삭제되었습니다.');
    router.push('/');

    // 추가적인 후속 작업 (예: 로그아웃, 페이지 리디렉션 등)
  } catch (error) {
    console.error('Error deleting account:', error);
    if (error.response) {
      alert(`계정 삭제에 실패했습니다: ${error.response.data}`);
    } else {
      alert('네트워크 오류 또는 요청 오류 발생');
    }
  }
};

const saleAmount = ref(0);

const fetchSaleAmount = async () => {
  try {
    const mno = authStore.mno;

    const id = mno;

    // 첫 번째 API 호출
    const response = await axios.get(`/api/kmap/member/${id}`);

    // 서비스 산업 코드 이름 가져오기
    const svcIndutyCdNm = response.data.svcIndutyCdNm;

    console.log(response);
    // 두 번째 API 호출
    const sumResponse = await axios.get(`/api/chart/sum/${svcIndutyCdNm}`);
    // saleAmount 값 설정

    if (svcIndutyCdNm == 0) {
      saleAmount.value = 0;
    } else {
      saleAmount.value = sumResponse.data.amount;
    }

    console.log(saleAmount.value); // saleAmount 값 확인
  } catch (error) {
    console.error('API 요청 중 오류 발생:', error);
  }
};

// 반점으로 구분된 문자열을 반환하는 computed 속성
const formattedSaleAmount = computed(() => {
  return saleAmount.value.toLocaleString(); // 숫자를 반점으로 구분된 문자열로 변환
});

const formattedGoalAmount = computed(() => {
  return memberEdit.value.goalAmount.toLocaleString(); // 숫자를 반점으로 구분된 문자열로 변환
});

const updateGoalAmount = (value) => {
  // 숫자가 아닌 경우에는 빈 문자열로 설정
  const numberValue = value.replace(/[^0-9]/g, ''); // 숫자만 남기기
  memberEdit.value.goalAmount = numberValue ? parseInt(numberValue, 10) : 0; // 변환하여 저장
};

// saleRate를 computed로 정의
const saleRate = computed(() => {
  // goalAmount가 0이 아닐 때만 계산
  return memberEdit.value.goalAmount > 0
    ? (saleAmount.value / memberEdit.value.goalAmount).toFixed(2)
    : '0.00';
});

// 호출 순서에 맞게 함수 실행
const loadData = async () => {
  await getMemberData(); // 회원 데이터 가져오기
  await fetchSaleAmount(); // 판매 금액 가져오기
};

// loadData 호출
loadData();
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
