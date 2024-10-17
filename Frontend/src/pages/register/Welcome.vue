<template>
  <div class="animation-container">
    <img
      src="@/assets/img/register/Welcome.jpg"
      alt="Background Image"
      class="background-image"
    />
    <div class="overlay">
      <div class="content">
        <h1 class="ls-tight fw-bolder display-6 text-white mb-5">
          회원가입이 완료되었습니다!
        </h1>
        <p class="text-white text-opacity-75">
          회원님을 위한 다양한 컨텐츠가 준비되어 있습니다. <br />
          로그인하시고 자영업자 키우기에서 다양한 컨텐츠를 즐겨보세요.
        </p>

        <a
          href="/login"
          class="btn fw-bold btn-sm btn-secondary bg-hover border-0 rounded-pill w-100 w-lg-auto mt-4 mb-lg-0"
          style="background-color: #fcd752"
          >로그인하러 가기</a
        >
      </div>
    </div>
  </div>
</template>

<script setup>
let particles = [];
const colors = ['#82E024', '#F5CB21', '#BAE3E7', '#FCA3B9'];

function pop() {
  for (let i = 0; i < 150; i++) {
    const p = document.createElement('div');
    p.x = window.innerWidth * 0.5;
    p.y = -Math.random() * window.innerHeight * 0.3;
    p.vel = {
      x: (Math.random() - 0.5) * 10,
      y: Math.random() * -20 - 15,
    };
    p.mass = Math.random() * 0.2 + 0.8;
    particles.push(p);
    p.style.transform = `translate(${p.x}px, ${p.y}px)`;
    const size = Math.random() * 15 + 5;
    p.style.width = size + 'px';
    p.style.height = size + 'px';
    p.style.position = 'absolute';
    p.style.background = colors[Math.floor(Math.random() * colors.length)];
    p.style.zIndex = 2;
    document.body.appendChild(p);
  }
}

function render() {
  for (let i = particles.length - 1; i >= 0; i--) {
    const p = particles[i];
    p.style.transform = `translate3d(${p.x}px, ${p.y}px, 1px)`;

    p.x += p.vel.x;
    p.y += p.vel.y;

    p.vel.y += 0.5 * p.mass;
    if (p.y > window.innerHeight * 2) {
      p.remove();
      particles.splice(i, 1);
    }
  }
  requestAnimationFrame(render);
}

pop();
window.setTimeout(render, 700);
</script>

<style scoped>
.animation-container {
  position: relative;
  width: 100%;
  height: 712px;
  overflow: hidden;
}

.background-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.7);
  z-index: 1;
  display: flex;
  justify-content: center; /* 중앙 정렬 */
  align-items: center; /* 세로 중앙 정렬 */
}

.content {
  text-align: center; /* 텍스트 중앙 정렬 */
}

.btn {
  display: inline-block;
  padding: 10px 20px;
  background-color: #6c757d;
  color: white;
  border: none;
  cursor: pointer;
  font-size: 16px;
  border-radius: 4px;
}

.btn-secondary {
  background-color: #6c757d;
}

.particule {
  position: absolute;
  border-radius: 50%;
  box-shadow: 1px 1px 4px #eb6383;
  z-index: 2;
}
</style>
