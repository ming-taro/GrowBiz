<template>
  <div>
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
.main-overlay {
  position: absolute;
  top: 55%;
  left: 34%;
  transform: translateX(-50%);
  width: 18%;
  background-color: rgba(255, 255, 255);
  border-radius: 50px;
  z-index: 1;
  box-sizing: border-box;
  box-shadow: 0px 4px 5px rgba(0, 0, 0, 0.2);
  overflow: hidden; /* 부모 요소에 overflow를 hidden으로 설정 */
}

.start-btn {
  width: 100%; /* 버튼 이미지의 너비를 100%로 설정 */
  transition: opacity 0.3s; /* 부드러운 전환 효과 */
}

.main-overlay:hover .start-btn {
  content: url('../../assets/img/main/startbtn-hover.png'); /* 호버 시 이미지 변경 */
}
</style>
