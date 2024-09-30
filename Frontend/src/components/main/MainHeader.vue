<template>
  <div>
    <img src="../../assets/img/main/Main.png" alt="" />
    <a href="/simul">
      <img
        src="../../assets/img/main/STARTBTN.png"
        alt=""
        class="main-overlay"
      />
    </a>
  </div>
</template>

<style>
.main-overlay {
  position: absolute;
  top: 57%;
  left: 35%;
  transform: translateX(-50%);
  width: 18%;
  background-color: rgba(255, 255, 255);
  border-radius: 50px;
  z-index: 1;
  box-sizing: border-box;
}
</style>
