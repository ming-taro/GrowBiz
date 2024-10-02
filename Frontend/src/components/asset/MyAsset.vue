<template>
  <div>
    <div class="title">추천 위치</div>
    <div class="row">
      <div class="wid-half">
        <div id="map" style="height: 400px"></div>
      </div>
      <div class="wid-half">
        <MyGraph />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  mounted() {
    const script = document.createElement('script');
    script.src =
      '//dapi.kakao.com/v2/maps/sdk.js?appkey=09118387dc78b55b2c58f3876095c5d2&autoload=false';
    script.onload = () => {
      kakao.maps.load(() => {
        var container = document.getElementById('map');
        var options = {
          center: new kakao.maps.LatLng(33.450701, 126.570667),
          level: 3,
        };

        var map = new kakao.maps.Map(container, options);
      });
    };
    document.head.appendChild(script);
  },
};
</script>

<script setup>
import MyGraph from '@/components/asset/MyGraph.vue';
</script>

<style scoped>
.container {
  padding: 0px 80px 15px 80px;
}

.title {
  margin: -14px 0px -14px 0px;
  position: relative;
  top: -18px;
  font-size: 25px;
  font-weight: bold;
}
.mainblue {
  color: #6184c6;
}
.weight {
  font-weight: 100;
}
.wid-half {
  width: 50%;
}
</style>
