<template>
  <div>
    <MainHeader />

    <div class="main-pd">
      <MainSimul />
      <SimulMore />
      <MainMyStore />
      <MainCommunity />
      <MainInfoPlaza />
    </div>
</div>
</template>

<script setup>
import MainHeader from '@/components/main/MainHeader.vue';
import MainSimul from '@/components/main/MainSimul.vue';
import MainMyStore from '@/components/main/MainMyStore.vue';
import MainCommunity from '@/components/main/MainCommunity.vue';
import MainInfoPlaza from '@/components/main/MainInfoPlaza.vue';
import SimulMore from '@/components/main/SimulMore.vue';
</script>


<style scoped>
.main-pd{
  padding-left: 180px;
  padding-right: 180px;
}
</style>