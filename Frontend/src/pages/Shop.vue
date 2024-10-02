<template>
  <div>
    <input v-model="address" placeholder="주소를 입력하세요" />
    <button @click="searchAddress">검색</button>
    <div id="map" style="width: 400px; height: 400px"></div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      map: null,
      address: '',
    };
  },
  mounted() {
    this.loadKakaoMapsScript();
  },
  methods: {
    loadKakaoMapsScript() {
      const script = document.createElement('script');
      script.src = `//dapi.kakao.com/v2/maps/sdk.js?appkey=09118387dc78b55b2c58f3876095c5d2&autoload=false`;
      script.onload = () => {
        kakao.maps.load(this.initMap);
      };
      document.head.appendChild(script);
    },
    initMap() {
      const container = document.getElementById('map');
      const options = {
        center: new kakao.maps.LatLng(37.566826, 126.9786567),
        level: 5,
      };
      this.map = new kakao.maps.Map(container, options);
    },
    async searchAddress() {
      try {
        const address = this.address;
        alert(address);
        const response = await axios.get(`/api/kmap/address/${address}`);
        const dongName = response.data;
        if (dongName) {
          console.log(dongName);
          this.getNearbyInfo(dongName);
        } else {
          alert('동 이름을 찾을 수 없습니다.');
        }
      } catch (error) {
        console.error('Error:', error);
        alert('주소 검색 중 오류가 발생했습니다.');
      }
    },
    async getNearbyInfo(dongName) {
      try {
        const response = await axios.get(`/api/kmap/${dongName}`);
        const { center, nearbyDongs, convenienceStores } = response.data;

        // 중심 마커 표시
        new kakao.maps.Marker({
          position: new kakao.maps.LatLng(center.y, center.x),
          map: this.map,
        });

        // 편의점 마커 표시
        convenienceStores.forEach((store) => {
          new kakao.maps.Marker({
            position: new kakao.maps.LatLng(store.y, store.x),
            map: this.map,
          });
        });

        // 지도 중심 이동
        this.map.setCenter(new kakao.maps.LatLng(center.y, center.x));
      } catch (error) {
        console.error(
          'Error:',
          error.response ? error.response.data : error.message
        );
        alert(
          '주소 검색 중 오류가 발생했습니다: ' +
            (error.response ? error.response.data.message : error.message)
        );
      }
    },
  },
};
</script>
