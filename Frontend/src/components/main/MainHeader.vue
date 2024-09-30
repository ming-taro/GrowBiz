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
  top: 55%;
  left: 34%;
  transform: translateX(-50%);
  width: 18%;
  background-color: rgba(255, 255, 255);
  border-radius: 50px;
  z-index: 1;
  box-sizing: border-box;
  box-shadow: 0px 4px 5px rgba(0, 0, 0, 0.2);
}
</style>
