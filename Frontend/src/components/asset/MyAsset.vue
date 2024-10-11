<template>
  <div>
    <div class="title">추천 위치</div>
    <div class="row">
      <div class="wid-half">
        <div id="map" style="height: 400px"></div>
      </div>
      <div class="wid-half">
        <MyMapGraph />
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

import { useAuthStore } from '@/stores/auth'; // Import your auth store

const authStore = useAuthStore();

const mno = authStore.state.mno;

export default {
  data() {
    return {
      map: null,
      address: '', // 초기 주소를 설정할 수 있습니다.
      geocoder: null, // Geocoder 추가
      markerImage: 'null', // 커스텀 마커 이미지
    };
  },
  mounted() {
    this.loadKakaoMapsScript();
  },
  methods: {
    loadKakaoMapsScript() {
      const script = document.createElement('script');
      script.src = import.meta.env.VITE_KAKAO_API_URL;
      script.onload = () => {
        kakao.maps.load(() => {
          this.initMap();
          this.geocoder = new kakao.maps.services.Geocoder(); // Geocoder 초기화
          this.fetchAddress(); // 초기 주소를 가져오는 함수 호출
        });
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

      // 여기서 마커 이미지를 생성
      const imageSrc = 'src/assets/img/mystore/marker.jpg';
      const imageSize = new kakao.maps.Size(100, 90); // 마커 이미지의 크기
      this.markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize);
    },
    async fetchAddress() {
      const id = '';

      if (mno == undefined) {
        id = '1234';
      } else {
        id = mno;
      }
      try {
        const response = await axios.get(`/api/kmap/member/${id}`); // ID에 해당하는 주소를 가져옴
        this.address = response.data.address; // 응답 데이터에서 주소를 가져와서 설정

        this.searchAddress(); // 주소를 사용하여 검색 실행
      } catch (error) {
        console.error('Error fetching address:', error);
        alert('주소를 가져오는 중 오류가 발생했습니다.');
      }
    },
    async searchAddress() {
      try {
        const address = this.address;
        if (!address) {
          alert('주소를 입력하세요.');
          return;
        }

        // 입력된 주소에 마커를 표시
        this.geocoder.addressSearch(address, (result, status) => {
          if (status === kakao.maps.services.Status.OK) {
            const coords = new kakao.maps.LatLng(result[0].y, result[0].x);

            // 지도 중심을 주소의 좌표로 이동
            this.map.setCenter(coords);

            // 입력된 주소에 마커 표시
            new kakao.maps.Marker({
              map: this.map,
              position: coords,
              image: this.markerImage, // 커스텀 마커 이미지 적용
            });

            // 동 이름을 서버에서 가져옴
            this.getNearbyInfo(address);
          } else {
            alert('주소를 찾을 수 없습니다.');
          }
        });
      } catch (error) {
        console.error('Error:', error);
        alert('주소 검색 중 오류가 발생했습니다.');
      }
    },
    async getNearbyInfo(address) {
      try {
        const response = await axios.get(`/api/kmap/nearby/${address}`);
        const { center, nearbyDongs, convenienceStores } = response.data;

        // 중심 마커 표시
        new kakao.maps.Marker({
          position: new kakao.maps.LatLng(center.y, center.x),
          map: this.map,
          image: this.markerImage, // 커스텀 마커 이미지 적용
        });

        // 편의점 마커 표시
        convenienceStores.forEach((store) => {
          new kakao.maps.Marker({
            position: new kakao.maps.LatLng(store.y, store.x),
            map: this.map,
          });
        });
      } catch (error) {
        console.error(
          'Error:',
          error.response ? error.response.data : error.message
        );
        alert(
          '주변 정보 검색 중 오류가 발생했습니다: ' +
            (error.response ? error.response.data.message : error.message)
        );
      }
    },
  },
};
</script>

<script setup>
import MyMapGraph from '@/components/asset/MyMapGraph.vue';
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
