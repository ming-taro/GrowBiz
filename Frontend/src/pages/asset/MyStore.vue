<template lang="">
  <AssetHeader />
  <div class="container mw-screen-xl">
    <StoreInfo class="mb-12" />
    <MyGraph class="mb-12" />
    <MyAsset class="mb-5" />
  </div>
</template>

<script>
import StoreInfo from '@/components/asset/StoreInfo.vue';
import MyAsset from '@/components/asset/MyAsset.vue';
import MyGraph from '@/components/asset/MyGraph.vue';
import AssetHeader from '@/components/asset/AssetHeader.vue';

export default {
  name: 'MyStore',
  components: {
    StoreInfo,
    MyAsset,
    MyGraph,
    AssetHeader,
  },
  setup() {
    return {};
  },
};
</script>

<style scoped>
.text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 2; /* 텍스트가 blur된 div 위에 표시되도록 z-index를 높임 */
  color: black;
  font-size: 20px;
  font-weight: bold;
}
</style>
