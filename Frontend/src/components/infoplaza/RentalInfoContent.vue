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

onMounted(async () => {
    loadKakaoMap(mapContainer.value);
    await fetchDistinctDistricts(); // 중복 제거된 구 가져오기
    await fetchPropertyListings(); // Fetch property listings after loading the map
});

// Load Kakao Map
const loadKakaoMap = (container) => {
    const script = document.createElement('script');
    script.src = `https://dapi.kakao.com/v2/maps/sdk.js?appkey=09118387dc78b55b2c58f3876095c5d2&autoload=false`;
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

// Fetch property listings
const fetchPropertyListings = async () => {
    try {
        const response = await axios.get('http://localhost:8080/api/property/116');
        propertys.value = response.data; // Store the fetched data in propertys ref
        console.log(propertys.value);
    } catch (error) {
        console.error('Error fetching property listings:', error);
    }
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
        const response = await axios.get(`http://localhost:8080/api/property/location?dongName=${selectedTown.value}`);
        const { latitude, longitude } = response.data; // Destructure the response to get latitude and longitude

        // Update map center to the new coordinates
        const position = new window.kakao.maps.LatLng(latitude, longitude);
        kakaoMap.setCenter(position); // Move the map center
    } catch (error) {
        console.error('Error fetching location:', error);
    }
};

// 구 업데이트 후 동 업데이트
const updateTowns = async () => {
    await fetchTowns(selectedDistrict.value); // Pass the selected district (guName) to fetch towns
};

// 현재 위치 텍스트 computed 속성
const currentLocation = computed(() => {
    let location = selectedCity.value; // 기본적으로 도시 이름
    if (selectedDistrict.value) {
        location += ` ${selectedDistrict.value}`; // 구 이름 추가
    }
    if (selectedTown.value) {
        location += ` ${selectedTown.value}`; // 동 이름 추가
    }
    return location; // 최종 위치 반환
});
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
