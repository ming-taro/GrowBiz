<template>
  <div>
    <div id="map" style="width: 400px; height: 400px"></div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      map: null,
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
        kakao.maps.load(this.loadMap);
      };
      document.head.appendChild(script);
    },
    loadMap() {
      const container = document.getElementById('map');
      const options = {
        center: new kakao.maps.LatLng(37.566826, 126.9786567),
        level: 5,
      };
      this.map = new kakao.maps.Map(container, options);
      this.getNearbyInfo('가락2동');
    },
    async getNearbyInfo(dongName) {
      try {
        const response = await axios.get(`/api/neighborhoods/${dongName}`);
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
        console.error('Error fetching nearby info:', error);
      }
    },
  },
};
</script>
