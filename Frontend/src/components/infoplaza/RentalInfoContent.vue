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
                            <option v-for="city in cities" :key="city.name" :value="city.name">{{ city.name }}</option>
                        </select>
                        <select
                            class="text-muted dropdown-item"
                            id="district"
                            v-model="selectedDistrict"
                            @change="updateTowns"
                            :disabled="!districts.length"
                        >
                            <option v-for="district in districts" :key="district.guName" :value="district.guName">{{ district.guName }}</option>
                        </select>
                        <select
                            class="text-muted dropdown-item"
                            id="town"
                            v-model="selectedTown"
                            @change="fetchLocation"
                            :disabled="!towns.length"
                        >
                            <option v-for="town in towns" :key="town.dongName" :value="town.dongName">{{ town.dongName }}</option>
                        </select>
                    </div>
                </div>
            </div>
            <div class="col-6 ms-10" ref="mapContainer" style="height: 70vh;"></div>
        </div>

        <h4>매물 목록</h4>
        <ul>
            <li v-for="property in propertys" :key="property.plno">
                {{ property.atclSfeCn }} - {{ property.bscTnthWuntAmt }} 원
            </li>
        </ul>
    </div>
</template>

<script setup>
import CommercialHeader from '@/components/infoplaza/CommercialHeader.vue';
import { onMounted, ref, computed } from 'vue';
import axios from 'axios';

const mapContainer = ref(null);
const propertys = ref([]);
let kakaoMap; // Declare a variable to hold the map instance

// Prop to control the visibility of location info
const props = defineProps({
    showLocationInfo: {
        type: Boolean,
        default: true,
    },
});

// 초기 데이터 설정
const cities = [
    { name: '서울특별시' }
    // 추가 도시 및 구 데이터...
];

const selectedCity = ref('서울특별시');
const selectedDistrict = ref('강남구');
const selectedTown = ref('개포1동');
const districts = ref([]);
const towns = ref([]);
let markers = [];
let infowindow;



onMounted(async () => {
    loadKakaoMap(mapContainer.value);
    await fetchDistinctDistricts(); // 중복 제거된 구 가져오기
    
});

// Load Kakao Map
const loadKakaoMap = (container) => {
    const script = document.createElement('script');
    script.src = `https://dapi.kakao.com/v2/maps/sdk.js?appkey=09118387dc78b55b2c58f3876095c5d2&autoload=false&libraries=services`;
    document.head.appendChild(script);

    script.onload = () => {
        window.kakao.maps.load(() => {
            const options = {
                center: new window.kakao.maps.LatLng(37.4827409, 127.055737), // 강남구 개포1동
                level: 4, // Zoom level
                maxLevel: 10, // Maximum zoom level
            };

            kakaoMap = new window.kakao.maps.Map(container, options); // Create map instance
        });
    };
};


// 구 이름 중복 제거해서 가져오기
const fetchDistinctDistricts = async () => {
    try {
        // 1. 기본값 미리 설정
        districts.value = [{ guName: '강남구' }];
        selectedDistrict.value = '강남구';
        towns.value = [{ dongName: '개포1동' }];
        selectedTown.value = '개포1동';
        
        // 2. 비동기적으로 데이터 불러오기
        const response = await axios.get('http://localhost:8080/api/property/gu-names');
        districts.value = response.data;

        // 3. 첫 번째 데이터를 선택 (데이터가 로드된 후에도 유지)
        if (districts.value.length) {
            selectedDistrict.value = districts.value[0].guName; // 첫 번째 구 선택
            await fetchTowns(selectedDistrict.value); // 동 데이터 불러오기
        }
    } catch (error) {
        console.error('Error fetching distinct district names:', error);
    }
};

// 동 이름 업데이트 함수
const fetchTowns = async (guName) => {
    try {
        const response = await axios.get(`http://localhost:8080/api/property/dong-names?guName=${guName}`);
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
        
        // 이전 마커 삭제
        removeMarkers();

        geocoder.addressSearch(address, function(result, status) {
            if (status === window.kakao.maps.services.Status.OK) {
                const coords = new window.kakao.maps.LatLng(result[0].y, result[0].x);

                // 마커 표시
                const marker = new window.kakao.maps.Marker({
                    map: kakaoMap,
                    position: coords
                });


                // 새로운 마커를 배열에 추가
                markers.push(marker); // <-- 이 줄 추가

                // 이전 인포윈도우 닫기
                if (infowindow) {
                    infowindow.close(); // 이전 인포윈도우 닫기
                }

                // 인포윈도우에 현재 위치 정보 표시
                infowindow = new window.kakao.maps.InfoWindow({
                    content: `<div style="width:150px;text-align:center;padding:6px 0;">${address}</div>`
                });
                infowindow.open(kakaoMap, marker);

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
    console.log('Current Location:', location); // 디버그 로그
    return location.trim(); // 최종 위치 반환
});

// 동 이름으로 동 코드 가져오기
const fetchDongCode = async () => {
    try {
        const response = await axios.get(`http://localhost:8080/api/property/dong-code?dongName=${selectedTown.value}`);
        
        if (response.status === 200) {
            const dongCode = response.data; // 동 코드를 가져옵니다.
            if (dongCode) {
                console.log('동 코드:', dongCode); // 동 코드가 있을 경우 출력
            } else {
                console.log('동 코드가 없습니다.'); // 동 코드가 없을 경우 메시지 출력
            }
        }
    } catch (error) {
        // 500 에러가 발생하지 않도록 처리
        console.error('동 코드를 가져오는 중 오류 발생:', error.message);
        // 이 부분은 이제 실행되지 않을 것입니다.
    }
};

// 이전에 생성된 마커 제거하는 함수
const removeMarkers = () => {
    markers.forEach(marker => marker.setMap(null)); // 마커 제거
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
    border-bottom: 0.7px solid #D9D9D9; /* Add bottom line */
    border-radius: 0; /* Remove rounded corners */
}

.pe-100 {
    padding-right: 100px;
}

.city-select {
    width: 200px; /* 원하는 너비로 조정 */
}
</style>
