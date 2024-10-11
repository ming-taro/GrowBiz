<template>
  <div>
    <div class="container mw-screen-lg">
      <div class="row">
        <ul
          class="nav nav-tabs custom justify-content-center"
          id="myTab"
          role="tablist"
        >
          <li class="nav-item">
            <router-link
              class="nav-link active"
              aria-current="page"
              to="mypageupdate"
              ><h4>개인정보 수정</h4></router-link
            >
          </li>
          <li class="nav-item">
            <router-link class="nav-link" aria-current="page" to="mypagereport"
              ><h4>마이리포트 확인</h4></router-link
            >
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<!-- <style scope>
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
.row.d-flex {
  display: flex;
  flex-wrap: wrap;
}

.custom-line {
  width: 100%; /* 선의 길이 설정 */
  height: 1px; /* 선의 굵기 설정 */
  background-color: #6184c6; /* 선의 색상 설정 */
  margin: 0px 0; /* 원하는 여백 설정 */
}
</style> -->
