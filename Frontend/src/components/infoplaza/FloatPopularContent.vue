<template>
  <div>
    <div class="row">
      <CommercialHeader class="ms-10 me-5 col-1" />
      <div v-if="showLocationInfo" class="col-3 me-5 mt-3 p-0">
        <div class="mb-10">
          <h4 class="mb-3">현위치</h4>
          <div class="mb-5">
            <div class="card-body card_padding d-flex gap-3">
              <i class="bi bi-geo-alt h-rem-7"></i>
              <span class="d-inline text-muted">{{ currentLocation }}</span>
            </div>
          </div>
        </div>
        <div>
          <h4 class="mb-3">지역 선택</h4>
          <div class="card-body card_padding d-flex gap-3">
            <select
              class="d-inline text-muted dropdown-item w-100 city-select"
              id="city"
              v-model="selectedCity"
              @change="updateDistricts"
            >
              <option
                v-for="city in cities"
                :key="city.name"
                :value="city.name"
              >
                {{ city.name }}
              </option>
            </select>
            <select
              class="text-muted dropdown-item"
              id="district"
              v-model="selectedDistrict"
              @change="updateTowns"
              :disabled="!districts.length"
            >
              <option
                v-for="district in districts"
                :key="district.guName"
                :value="district.guName"
              >
                {{ district.guName }}
              </option>
            </select>
            <select
              class="text-muted dropdown-item"
              id="town"
              v-model="selectedTown"
              @change="fetchLocation"
              :disabled="!towns.length"
            >
              <option
                v-for="town in towns"
                :key="town.dongName"
                :value="town.dongName"
              >
                {{ town.dongName }}
              </option>
            </select>
          </div>
        </div>
      </div>
      <div class="col-6 ms-10" ref="mapContainer" style="height: 70vh"></div>
    </div>
  </div>
</template>

<script setup>
import CommercialHeader from '@/components/infoplaza/CommercialHeader.vue';
import { onMounted, ref, computed } from 'vue';
import axios from 'axios';

const mapContainer = ref(null);
const propertys = ref([]);
let kakaoMap; // Declare a variable to hold the map instance
const selectedCity = ref('서울특별시');
const selectedDistrict = ref('광진구');
const selectedTown = ref('광장동');
const districts = ref([]);
const towns = ref([]);
let markers = [];
let infowindow;

// Prop to control the visibility of location info
const props = defineProps({
  showLocationInfo: {
    type: Boolean,
    default: true,
  },
});

// 초기 데이터 설정
const cities = [
  { name: '서울특별시' },
  // 추가 도시 및 구 데이터...
];


onMounted(async () => {
  try {
    await loadKakaoMap();
    if (kakaoMap) {
      await fetchDistinctDistricts();
      fetchLocation();
    }
  } catch (error) {
    console.error("Error loading Kakao Map: ", error);
  }
});



const loadKakaoMap = () => {
  return new Promise((resolve, reject) => {
    if (window.kakao && window.kakao.maps) {
      const options = {
        center: new window.kakao.maps.LatLng(37.5465421, 127.0713152),
        level: 5,
        maxLevel: 7
      };
      kakaoMap = new window.kakao.maps.Map(mapContainer.value, options);
      resolve(kakaoMap);
    } else {
      const script = document.createElement('script');
      script.src = `${import.meta.env.VITE_KAKAO_API_URL}&v=${new Date().getTime()}`;
      document.head.appendChild(script);
      script.onload = () => {
        if (window.kakao && window.kakao.maps) {
          window.kakao.maps.load(() => {
            const options = {
              center: new window.kakao.maps.LatLng(37.5465421, 127.0713152),
              level: 5,
              maxLevel: 7
            };
            kakaoMap = new window.kakao.maps.Map(mapContainer.value, options);
            resolve(kakaoMap);
          });
        } else {
          reject(new Error('Kakao Maps API failed to load'));
        }
      };
      script.onerror = () => {
        reject(new Error('Kakao Maps API script failed to load'));
      };
    }
  });
};



const fetchDistinctDistricts = async () => {
  try {
    // 1. 기본값 미리 설정
    districts.value = [{ guName: '광진구' }];
    selectedDistrict.value = '광진구';
    towns.value = [{ dongName: '광장동' }];
    selectedTown.value = '광장동'; // 초기화

    // 2. 비동기적으로 데이터 불러오기
    const response = await axios.get(
      'http://localhost:8080/api/property/gu-names'
    );
    districts.value = response.data;

    // 3. 첫 번째 데이터를 선택
    if (districts.value.length) {
      await fetchTowns(selectedDistrict.value); // 동 데이터 불러오기
    }
  } catch (error) {
    console.error('Error fetching distinct district names:', error);
  }
};

// 동 이름 업데이트 함수
const fetchTowns = async (guName) => {
  try {
    const response = await axios.get(
      `http://localhost:8080/api/property/dong-names?guName=${guName}`
    );
    towns.value = response.data; // 동 이름 리스트를 towns에 저장
    if (towns.value.length) {
      selectedTown.value = towns.value[0].dongName; // 첫 번째 동 이름 선택
      // fetchLocation 호출을 여기로 이동
      fetchLocation(); // 동 업데이트 후에 위치를 가져옴
    }
  } catch (error) {
    console.error('Error fetching towns:', error);
  }
};

const fetchLocation = async () => {
  try {
    if (!window.kakao || !window.kakao.maps || !window.kakao.maps.services) {
      console.error('Kakao Maps services not loaded yet.');
      return;
    }
    const geocoder = new window.kakao.maps.services.Geocoder();
    const address = `${selectedCity.value} ${selectedDistrict.value} ${selectedTown.value}`; // 주소를 직접 설정

    removeMarkers(); // 기존 마커 제거
    let dongNames = []; // 동 이름을 저장할 배열

    // 중심 좌표 가져오기
    geocoder.addressSearch(address, async function (result, status) {
      if (status === window.kakao.maps.services.Status.OK) {
        const centerCoords = new window.kakao.maps.LatLng(
          result[0].y,
          result[0].x
        );
        // 지도 중심 이동
        kakaoMap.setCenter(centerCoords);

        // 반경 1km 범위 내 좌표들 계산
        const radius = 0.009009; // 1km 대략적인 위도/경도 변환 값

        const positions = [
          { lat: centerCoords.getLat() + radius, lng: centerCoords.getLng() }, // 북쪽 1km
          { lat: centerCoords.getLat() - radius, lng: centerCoords.getLng() }, // 남쪽 1km
          { lat: centerCoords.getLat(), lng: centerCoords.getLng() + radius }, // 동쪽 1km
          { lat: centerCoords.getLat(), lng: centerCoords.getLng() - radius }, // 서쪽 1km
        ];

        // 각 좌표에 대한 동 이름을 가져오기
        dongNames = await Promise.all(
          positions.map(async (pos) => {
            return new Promise((resolve, reject) => {
              const coords = new window.kakao.maps.LatLng(pos.lat, pos.lng);
              geocoder.coord2Address(
                coords.getLng(),
                coords.getLat(),
                function (result, status) {
                  if (status === window.kakao.maps.services.Status.OK) {
                    const dongName = result[0].address.region_3depth_name; // 동 이름 추출
                    resolve(dongName); // 동 이름 반환
                  } else {
                    reject('Error fetching dong name'); // 실패 시 reject 호출
                  }
                }
              );
            });
          })
        );

        // 중복된 동 이름 제거
        dongNames = [...new Set(dongNames)];

        const cleanedDongNames = dongNames.map((name) => name.slice(0, -1)); // 마지막 글자 제거

        // 동 이름 배열을 서버로 전송하는 함수 호출
        sendDongNamesToServer(cleanedDongNames);
      }
    });
  } catch (error) {
    console.error('Error fetching location:', error);
  }
};

// 동 이름 배열을 서버로 전송하는 함수
const sendDongNamesToServer = async (dongNames) => {
  try {
    const response = await axios.post(
      'http://localhost:8080/api/property/float-popular',
      {
        dongNames: dongNames,
        yearQuarter: '20242',
      },
      {
        headers: {
          'Content-Type': 'application/json',
        },
      }
    );
    const populationData = response.data; // 서버로부터 받은 인구 데이터
    displayMarkers(populationData); // 마커 표시 함수 호출
  } catch (error) {
    console.error('Error sending dong names to server:', error);
  }
};

const displayMarkers = (populationData) => {
  const geocoder = new window.kakao.maps.services.Geocoder();
  const markerMap = new Map(); // 동 이름을 키로 하여 인구 수를 값으로 저장

  // 각 동에 대한 인구 수를 정리
  populationData.forEach((data) => {
    const { totFlpopCo, adstrdCdNm } = data;

    // 기존에 마커가 있다면 인구 수 비교 후 갱신
    if (markerMap.has(adstrdCdNm)) {
      const existingData = markerMap.get(adstrdCdNm);
      if (existingData.totFlpopCo < totFlpopCo) {
        markerMap.set(adstrdCdNm, data); // 인구수가 많은 데이터로 갱신
      }
    } else {
      markerMap.set(adstrdCdNm, data); // 새로운 동 데이터 추가
    }
  });

  // 저장된 동 이름에 대해 마커 표시
  markerMap.forEach((data) => {
    const { adstrdCdNm, totFlpopCo } = data;

    geocoder.addressSearch(adstrdCdNm, (result, status) => {
      if (status === window.kakao.maps.services.Status.OK) {
        const coords = new window.kakao.maps.LatLng(result[0].y, result[0].x);
        const markerColor = getMarkerColor(totFlpopCo); // 인구수에 따른 마커 색상 결정

        const marker = new window.kakao.maps.Marker({
          map: kakaoMap,
          position: coords,
          title: adstrdCdNm,
          image: new window.kakao.maps.MarkerImage(
            `/src/assets/img/infoplaza/marker_${markerColor}.png`,
            new window.kakao.maps.Size(50, 50)
          ),
        });
        // 인구 수 포맷팅
        const formattedPopulation = totFlpopCo.toLocaleString();
        // 커스텀 오버레이 내용 생성
        const overlayContent = `
          <div class="customoverlay" style="width: 170px; padding-left:15px">
            <div>
              <h5>${adstrdCdNm}</h5>
              <p>인구 수: ${formattedPopulation}명</p>
            </div>
          </div>
        `;

        const customOverlay = new window.kakao.maps.CustomOverlay({
          position: coords,
          content: overlayContent,
          yAnchor: 1.5,
          zIndex: 3
        });

        // 마커에 마우스 이벤트 추가
        window.kakao.maps.event.addListener(marker, 'mouseover', function() {
          customOverlay.setMap(kakaoMap);
        });

        window.kakao.maps.event.addListener(marker, 'mouseout', function() {
          customOverlay.setMap(null);
        });

        // 마커 배열에 저장
        markers.push(marker);
      } else {
        console.log(`주소 검색 실패: ${adstrdCdNm}`);
      }
    });
  });
};

// 인구수에 따라 마커 색상 결정하는 함수
const getMarkerColor = (totFlpopCo) => {
  if (totFlpopCo > 7000000) {
    return 'red'; // 인구수 많을 때
  } else if (totFlpopCo > 5000000) {
    return 'blue'; // 중간
  } else if (totFlpopCo > 3000000) {
    return 'green'; // 중간
  } else {
    return 'gray'; // 적을 때
  }
};

// 구 업데이트 후 동 업데이트
const updateTowns = async () => {
  await fetchTowns(selectedDistrict.value); // Pass the selected district (guName) to fetch towns
  fetchLocation(); // 동 업데이트 후에 위치를 가져옴
};

// 현재 위치 텍스트 computed 속성
const currentLocation = computed(() => {
  let location = selectedCity.value || ''; // 기본적으로 도시 이름
  if (selectedDistrict.value) {
    location += ` ${selectedDistrict.value}`; // 구 이름 추가
  }
  if (selectedTown.value) {
    location += ` ${selectedTown.value}`; // 동 이름 추가
  }
  return location.trim(); // 최종 위치 반환
});

// 인포윈도우를 띄우는 함수
const showInfoWindow = (message) => {
  let content = `<div class = "info-window label" id="info-window"><span class="left"></span><span class="center">${message}</span><span class="right"></span></div>`;
  // 커스텀 오버레이를 생성합니다
  infowindow = new kakao.maps.CustomOverlay({
    position: kakaoMap.getCenter(),
    content: content,
  });

  // 커스텀 오버레이를 지도에 표시합니다
  infowindow.setMap(kakaoMap);
};

// 이전에 생성된 마커 제거하는 함수
const removeMarkers = () => {
  markers.forEach((marker) => marker.setMap(null)); // 마커 제거
  markers = []; // 마커 배열 초기화
};
</script>

<style>
.card_padding {
  padding-top: 3px;
  padding-bottom: 5px;
  padding-left: 0px;
  border: none;
  box-shadow: none; /* Remove shadow */
  border-bottom: 0.7px solid #d9d9d9; /* Add bottom line */
  border-radius: 0; /* Remove rounded corners */
}

.pe-100 {
  padding-right: 100px;
}

.city-select {
  width: 200px; /* 원하는 너비로 조정 */
}
/* CSS 스타일 추가 */
.info-window {
  padding: 10px;
  border-radius: 5px;
  background-color: white;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
}

.info-window strong {
  font-size: 16px;
  color: #333;
}

.customoverlay {
  width: 300px; /* 고정 너비 설정 */
  height: auto; /* 높이를 자동으로 설정하여 내용에 맞게 조정 */
  max-height: 400px; /* 최대 높이 설정 (예: 400px) */
  overflow: hidden; /* 내용이 넘칠 경우 숨김 처리 */
  background-color: #fff; /* 배경색 */
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2); /* 그림자 */
  border-radius: 8px; /* 둥근 모서리 */
  padding: 10px; /* 패딩 */
  display: flex; /* Flexbox 사용 */
  flex-direction: column; /* 세로 방향 유지 */
}

.customoverlay img {
  width: 100%; /* 너비를 100%로 설정하여 div에 맞춤 */
  height: auto; /* 자동 높이 설정 */
  max-height: 150px; /* 최대 높이 설정 (예: 150px) */
  object-fit: fill; /* 이미지 비율 유지하며 잘리도록 설정 */
  border-radius: 5px; /* 둥근 모서리 */
  margin-bottom: 10px; /* 이미지와 텍스트 간의 공간 유지 */
}

.customoverlay .none-img {
  width: 100%; /* 너비를 100%로 설정하여 div에 맞춤 */
  height: auto; /* 자동 높이 설정 */
  max-height: 150px; /* 최대 높이 설정 (예: 150px) */
  object-fit: contain; /* 이미지 비율 유지하며 잘리도록 설정 */
  border-radius: 5px; /* 둥근 모서리 */
  margin-bottom: 10px; /* 이미지와 텍스트 간의 공간 유지 */
}

.customoverlay h5,
p {
  margin: 0; /* 기본 여백 제거 */
  overflow-wrap: break-word; /* 단어가 넘어가면 줄바꿈 */
  white-space: normal; /* 기본 줄바꿈 처리 */
  text-align: left; /* 텍스트 정렬 */
}
</style>
