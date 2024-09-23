<template>
  <div class="container">
    <!-- 탭 메뉴 -->
    <InfoPlazaHeader />
    <router-view></router-view>
  </div>
</template>

<script setup>
import InfoPlazaHeader from './InfoPlazaHeader.vue';
</script>
