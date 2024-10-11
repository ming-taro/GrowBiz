<template>
  <div>
    <MypageHeader />
    <div class="container">
      <div class="row">
        <ul
          class="nav nav-tabs custom justify-content-center"
          id="myTab"
          role="tablist"
        >
          <li class="nav-item">
            <router-link class="nav-link" aria-current="page" to="mypageupdate"
              ><h4>개인정보</h4></router-link
            >
          </li>
          <li class="nav-item">
            <router-link
              class="nav-link active"
              aria-current="page"
              to="mypagereport"
              ><h4>마이리포트 확인</h4></router-link
            >
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup>
import MypageHeader from '@/components/mypage/MypageHeader.vue';
</script>

<style>
.btn-primary {
  margin: 0px 0px 0px 20px;
}
.btn-cls {
  display: flex;
  width: 18%;
  padding: 0.5% 0% 0% 20%;
}
.div-input {
  width: 40%;
}

.h1-title {
  margin: 10px 0px;
}
</style>
