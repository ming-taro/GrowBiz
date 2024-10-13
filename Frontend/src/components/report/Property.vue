<template lang="">
  <div
    class="d-flex justify-content-between m-4 align-items-stretch"
    style="height: 50%"
  >
    <!-- 왼쪽 텍스트 -->
    <div
      class="d-flex flex-column justify-content-between"
      style="width: 60%"
    >
      <div>
        <h2 class="fw-bolder">신한넥스텔</h2>
        <h4 class="mainblue mt-1">매매 9,800 ~ 2억 1,000 원</h4>
        <div class="align-content-center">
          <h6 class="mt-2" style="font-weight: 300">
            오피스텔·280세대·총1동
          </h6>
          <h6 style="font-weight: 300">
            1998.10.26·36.49㎡ ~ 103.66㎡
          </h6>
        </div>
      </div>
      <h5 class="mt-auto align-content-end">
        매매 9 | 전세 0 | 월세 14
      </h5>
    </div>

    <!-- 오른쪽 이미지 -->
    <div class="d-flex align-items-end" style="width: 36%">
      <img
        src="../../assets/img/report/sapmle.jpg"
        alt=""
        style="width: 100%; height: auto"
      />
    </div>
  </div>
</template>
<script setup>
import { onMounted, defineProps } from 'vue';

const props = defineProps(["plno"]);

onMounted(() => {
  console.log(props.plno);
})
</script>
<style lang="">
  
</style>