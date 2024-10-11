<template>
  <MypageHeader />
  <Mypage />
  <div class="container mw-screen-sm">
    <div class="card m-3 mt-10">
      <div class="row g-0">
        <div class="col-md-4">
          <img
            src="@/assets/img/report/clothes.png"
            class="img-fluid rounded-start m-3"
            alt="..."
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
          >현재 비밀번호</label
        >
        <div class="col-sm-9">
          <input type="text" class="form-control" />
        </div>
      </div>
      <div class="row mb-3">
        <label for="inputEmail3" class="col-sm-3 col-form-label"
          >새로운 비밀번호</label
        >
        <div class="col-sm-9">
          <input type="text" class="form-control" />
        </div>
      </div>
      <div class="row mb-3">
        <label for="inputEmail3" class="col-sm-3 col-form-label"
          >새로운 비밀번호 확인</label
        >
        <div class="col-sm-9">
          <input type="text" class="form-control" />
        </div>
      </div>

      <button
        type="submit"
        class="btn btn-primary rounded-pill btn-custom mt-10"
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

onMounted(async () => {
  await authStore.load(); // store에서 데이터를 로드
});
</script>

<style>
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

.card {
  max-height: 150px;
}
</style>
