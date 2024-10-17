<template>
  <!-- <div>
    <div id="map" style="width: 400px; height: 400px"></div>
  </div> -->
</template>

<!-- <script>
import axios from 'axios';

const id = '1234';

export default {
  data() {
    return {
      map: null,
      address: '', // 초기 주소를 설정할 수 있습니다.
      geocoder: null, // Geocoder 추가
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
    },
    async fetchAddress() {
      try {
        const response = await axios.get(`/api/kmap/member/${id}`); // ID에 해당하는 주소를 가져옴
        this.address = response.data; // 응답 데이터에서 주소를 가져와서 설정

        console.log(response.data);

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
            });

            // 동 이름을 서버에서 가져옴
            this.fetchDongName(address);
          } else {
            alert('주소를 찾을 수 없습니다.');
          }
        });
      } catch (error) {
        console.error('Error:', error);
        alert('주소 검색 중 오류가 발생했습니다.');
      }
    },
    async fetchDongName(address) {
      try {
        const response = await axios.get(`/api/kmap/address/${address}`);
        const dongName = response.data;
        if (dongName) {
          console.log(dongName);
          this.getNearbyInfo(address);
        } else {
          alert('동 이름을 찾을 수 없습니다.');
        }
      } catch (error) {
        console.error('Error:', error);
        alert('동 이름을 가져오는 중 오류가 발생했습니다.');
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
        });

        // 편의점 마커 표시
        convenienceStores.forEach((store) => {
          new kakao.maps.Marker({
            position: new kakao.maps.LatLng(store.y, store.x),
            map: this.map,
          });
        });

        // 지도 중심 이동
        // alert('지도 중심 이동');
        // this.map.setCenter(new kakao.maps.LatLng(center.y, center.x));
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
</script> -->
