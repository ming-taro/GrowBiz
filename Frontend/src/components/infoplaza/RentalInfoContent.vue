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
const selectedTown = ref('화양동');
const districts = ref([]);
const towns = ref([]);
let markers = [];
let infowindow;
let clusterer;

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
  loadKakaoMap(mapContainer.value);
  await fetchDistinctDistricts(); // 중복 제거된 구 가져오기
});

// Load Kakao Map
const loadKakaoMap = (container) => {
  const script = document.createElement('script');
  script.src = import.meta.env.VITE_KAKAO_API_URL;
  document.head.appendChild(script);

  script.onload = () => {
    window.kakao.maps.load(() => {
      const options = {
        center: new window.kakao.maps.LatLng(37.5465421, 127.0713152), // 광진구 화양동
        level: 4, // Zoom level
        maxLevel: 6, // Maximum zoom level
      };

      kakaoMap = new window.kakao.maps.Map(container, options); // Create map instance

      // Marker Clusterer 설정
      clusterer = new kakao.maps.MarkerClusterer({
        map: kakaoMap,
        averageCenter: true,
        minLevel: 5,
      });

      // 줌 변경 이벤트 리스너 등록
      kakao.maps.event.addListener(kakaoMap, 'zoom_changed', () => {
        const level = kakaoMap.getLevel();
        // 오버레이가 존재한다면 닫기
        if (infowindow) {
          infowindow.setMap(null); // 현재 열려있는 오버레이 닫기
          infowindow = null; // infowindow 초기화
        }
        if (level < 5) {
          clusterer.setMap(null); // 클러스터러 비활성화
          markers.forEach((marker) => marker.setMap(kakaoMap)); // 개별 마커 표시
        } else {
          clusterer.setMap(kakaoMap); // 클러스터러 활성화
          clusterer.addMarkers(markers); // 마커들을 클러스터러에 추가
        }
      });
    });
  };
};

// 구 이름 중복 제거해서 가져오기
const fetchDistinctDistricts = async () => {
  try {
    // 1. 기본값 미리 설정
    districts.value = [{ guName: '광진구' }];
    selectedDistrict.value = '광진구';
    towns.value = [{ dongName: '광장동' }];
    selectedTown.value = '광장동';

    // 2. 비동기적으로 데이터 불러오기
    const response = await axios.get(
      'http://localhost:8080/api/property/gu-names'
    );
    districts.value = response.data;

    await fetchTowns(selectedDistrict.value); // 동 데이터 불러오기
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
      fetchLocation();
    }
  } catch (error) {
    console.error('Error fetching towns:', error);
  }
};

// Fetch location data for the selected town and move the map
const fetchLocation = async () => {
  try {
    // Update map center to the new coordinates
    const position = new window.kakao.maps.LatLng(37.517342, 127.037213);
    kakaoMap.setCenter(position); // Move the map center
    // 주소로 좌표 검색
    const geocoder = new window.kakao.maps.services.Geocoder();
    const address = currentLocation.value; // 현재 선택된 지역을 가져옵니다.

    removeMarkers(); // 이전 마커 제거

    // 이전 마커 삭제
    if (infowindow) {
      infowindow.setMap(null); // 기존 인포윈도우 닫기
    }

    geocoder.addressSearch(address, function (result, status) {
      if (status === window.kakao.maps.services.Status.OK) {
        const coords = new window.kakao.maps.LatLng(result[0].y, result[0].x);
        // 지도의 중심을 결과값으로 받은 위치로 이동
        kakaoMap.setCenter(coords);
      }
    });

    fetchDongCode(); // 동 코드 가져오기
  } catch (error) {
    console.error('Error fetching location:', error);
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

// 동 이름으로 동 코드 가져오기 -> 매물 정보 가져오기
const fetchDongCode = async () => {
  try {
    const response = await axios.get(
      `http://localhost:8080/api/property/dong-code?dongName=${selectedTown.value}`
    );

    if (response.status === 200) {
      const dongCode = response.data; // 동 코드를 가져옵니다.
      if (dongCode) {
        fetchPropertyDetails(dongCode); // 동 코드로 매물 세부 정보 가져오기 호출
      } else {
        showInfoWindow('해당 지역의 매물 정보가 없습니다.');
      }
    }
  } catch (error) {
    // 500 에러가 발생하지 않도록 처리
    console.error('동 코드를 가져오는 중 오류 발생:', error.message);
    // 이 부분은 이제 실행되지 않을 것입니다.
  }
};

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

// 매물 정보 가져오기 및 마커 표시
const fetchPropertyDetails = async (dongCode) => {
  try {
    const response = await axios.get(
      `http://localhost:8080/api/property/list?dongCode=${dongCode}`
    );
    propertys.value = response.data; // 매물 정보를 저장
    // 이전 마커 삭제
    removeMarkers();
    console.log(propertys);
    // 매물 정보로 마커 표시
    propertys.value.forEach((property) => {
      // atclSfeCn가 있는 경우에만 마커 추가
      if (property.atclSfeCn) {
        const position = new window.kakao.maps.LatLng(
          property.laCrd,
          property.loCrd
        );
        const marker = new window.kakao.maps.Marker({
          map: kakaoMap,
          position,
        });

        // 마커 클릭 시 매물 정보 표시
        window.kakao.maps.event.addListener(marker, 'click', () => {
          if (infowindow) {
            infowindow.setMap(null); // 현재 열려있는 오버레이 닫기
            infowindow = null; // infowindow 초기화
          }

          const imageContent = property.imageData
            ? `<img src="${property.imageData}" alt="Property Image" />`
            : `<img src="/src/assets/img/infoplaza/house.png" alt="Property Image" class="none-img" />`; // 이미지가 없을 경우 기본 이미지

          var content = `<div class="customoverlay">
                  ${imageContent}
                  <button class="close-overlay" onclick="closeOverlay()">x</button>
                  <h5 title="${property.atclSfeCn}">${property.atclSfeCn}</h5>
                  <p>${property.dealKindCdNm} | ${property.ctgryCd2Nm}</p>
                  <p>${property.mdiatBzestNm} ${property.mdiatBzestRepTelno}</p>
                </div>`;
          // 새로운 커스텀 오버레이를 생성합니다
          infowindow = new kakao.maps.CustomOverlay({
            map: kakaoMap,
            position: position,
            content: content,
            yAnchor: 1, // 오버레이의 위치 조정
          });

          window.closeOverlay = () => {
            if (infowindow) {
              infowindow.setMap(null); // 현재 열려있는 오버레이 닫기
              infowindow = null; // infowindow 초기화
            }
          };
        });

        markers.push(marker); // 마커 배열에 저장
      }
    });
  } catch (error) {
    console.error('매물 정보를 가져오는 중 오류 발생:', error);
  }
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
.customoverlay .close-overlay {
  position: absolute;
  top: 10px;
  right: 10px;
  background-color: white;
  color: black;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  z-index: 10; /* 버튼이 오버레이 내부에서 가장 위에 표시되도록 설정 */
}
</style>
