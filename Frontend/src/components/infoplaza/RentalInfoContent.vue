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
                        <!-- 서울 선택 -->
                        <select
                            class="d-inline text-muted dropdown-item w-100 city-select"
                            id="city"
                            v-model="selectedCity"
                            @change="updateDistricts"
                        >
                            <option v-for="city in cities" :key="city.name" :value="city.name">{{ city.name }}</option>
                        </select>
                        <!-- 구 선택 -->
                        <select
                            class="text-muted dropdown-item"
                            id="district"
                            v-model="selectedDistrict"
                            @change="updateTowns"
                            :disabled="!districts.length"
                        >
                            <option v-for="district in districts" :key="district.name" :value="district.name">{{ district.name }}</option>
                        </select>
                        <!-- 동 선택 -->
                        <select
                            class="text-muted dropdown-item"
                            id="town"
                            v-model="selectedTown"
                            :disabled="!towns.length"
                        >
                            <option v-for="town in towns" :key="town" :value="town">{{ town }}</option>
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

// Prop to control the visibility of location info
const props = defineProps({
    showLocationInfo: {
        type: Boolean,
        default: true,
    },
});

// 초기 데이터 설정
const cities = [
    { name: '서울특별시', districts: [
        { name: '강남구', towns: ['역삼동', '삼성동', '신사동'] },
        { name: '강동구', towns: ['명일동', '천호동', '암사동'] },
        { name: '종로구', towns: ['청운효자동', '신문로1가', '삼청동'] },
        { name: '광진구', towns: ['화양동', '군자동'] }
    ]}
    // 추가 도시 및 구 데이터...
];

const selectedCity = ref('서울특별시');
const selectedDistrict = ref('강남구');
const selectedTown = ref('역삼동');
const districts = ref([]);
const towns = ref([]);

onMounted(async () => {
    loadKakaoMap(mapContainer.value);
    updateDistricts(); // Initialize districts based on selected city
    updateTowns(); // Initialize towns based on selected district
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
                center: new window.kakao.maps.LatLng(33.450701, 126.570667), // Center coordinates
                level: 3, // Zoom level
                maxLevel: 5, // Maximum zoom level
            };

            new window.kakao.maps.Map(container, options); // Create map instance
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

// 구 업데이트 함수
const updateDistricts = () => {
    const city = cities.find(city => city.name === selectedCity.value);
    districts.value = city ? city.districts : [];
    selectedDistrict.value = districts.value.length ? districts.value[0].name : ''; // Set first district as selected
    selectedTown.value = ''; // Reset town selection
    updateTowns(); // Update towns based on selected district
};

// 동 업데이트 함수
const updateTowns = () => {
    const district = districts.value.find(district => district.name === selectedDistrict.value);
    towns.value = district ? district.towns : [];
    selectedTown.value = towns.value.length ? towns.value[0] : ''; // Set first town as selected
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
