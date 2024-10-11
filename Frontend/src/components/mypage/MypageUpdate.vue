<template>
  <MypageHeader />
  <Mypage />
  <div class="container mw-screen-sm">
    <div>
      <h2 class="mb-8 mt-10">개인정보 설정</h2>
      <div class="custom-line mb-10" />
      <h4 class="mb-6">닉네임 변경</h4>

      <div class="row mb-4">
        <label for="inputEmail3" class="col-sm-3 col-form-label"
          >새 닉네임</label
        >
        <div class="col-sm-9">
          <input type="text" class="form-control" />
        </div>
      </div>

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
          >새 비밀번호</label
        >
        <div class="col-sm-9">
          <input type="text" class="form-control" />
        </div>
      </div>
      <div class="row mb-3">
        <label for="inputEmail3" class="col-sm-3 col-form-label"
          >새 비밀번호 확인</label
        >
        <div class="col-sm-9">
          <input type="text" class="form-control" />
        </div>
      </div>

      <button
        type="submit"
        class="btn btn-primary rounded-pill btn-custom mt-10"
      >
        저장하기
      </button>
    </div>
  </div>
</template>

<script setup>
import Mypage from '@/pages/mypage/Update.vue';
import MypageHeader from '@/components/mypage/MypageHeader.vue';
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
</style>
