<template>
  <div>
    <div class="title-sm">
      <div class="custom-line" />
      추천 위치
      <div class="custom-line" />
    </div>
    <div class="row">
      <div class="col-7">
        <div id="map" style="height: 400px"></div>
      </div>
      <div class="col-5 d-flex justify-content-center align-content-center">
        <div style="display: flex; flex-direction: column; overflow: auto; height: 400px">
          <div v-for="(plno, index) in props.plno_list" v-bind:key="index">
            <Property v-bind:plno="plno"/>
            <hr />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, defineProps } from 'vue';
import { findLocationByAddress } from '@/services/simulation/LocationAPI';
import Property from '@/components/report/Property.vue'

const props = defineProps(["location", "plno_list"]);

const setLocation = async () => {
  const location = props.location ? await findLocationByAddress(props.location) : await findLocationByAddress("광진구 군자동");
  const script = document.createElement('script');
  script.src = import.meta.env.VITE_KAKAO_API_URL;
  script.onload = () => {
    kakao.maps.load(() => {
      var container = document.getElementById('map');
      var options = {
        center: new kakao.maps.LatLng(location.y, location.x),
        level: 5,
      };

      var map = new kakao.maps.Map(container, options);
    });
  };
  document.head.appendChild(script);
}

onMounted(async() => {
  await setLocation();
})
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
</style>