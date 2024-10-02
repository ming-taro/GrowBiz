<template>
  <div class="main-container">
    <!-- 부모 요소에 클래스 추가 -->
    <img src="../../assets/img/main/Main.png" alt="" />
    <a href="/simul">
      <div class="main-overlay">
        <img
          src="../../assets/img/main/STARTBTN.png"
          alt=""
          class="start-btn"
        />
      </div>
    </a>
  </div>
</template>

<style>
.main-container {
  position: relative; /* 부모 요소에 relative 추가 */
}

.main-overlay {
  position: absolute;
  top: 82%; /* 원하는 위치로 조정 */
  left: 34%; /* 중앙 정렬 */
  transform: translate(-50%, -50%); /* 수직 및 수평 중앙 정렬 */
  width: 18%; /* 버튼 오버레이의 너비 설정 */
  border-radius: 50px;
  z-index: 1;
  box-sizing: border-box;
  box-shadow: 0px 4px 5px rgba(0, 0, 0, 0.2);
}

.start-btn {
  width: 100%; /* 버튼 이미지의 너비를 100%로 설정 */
  transition: opacity 0.3s; /* 부드러운 전환 효과 */
}

.main-overlay:hover .start-btn {
  content: url('../../assets/img/main/startbtn-hover.png'); /* 호버 시 이미지 변경 */
}
</style>
