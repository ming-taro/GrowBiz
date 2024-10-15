<template>

    <!-- 개업률, 폐업률, 유동인구 -->
    <div class="container mb-5">
        <div class="row">
            <div class="col-12 d-flex ms-8 align-items-center">

                <div class="col-3 text-center ms-8 me-10">
                    <img src="@/assets/img/report/popular.png" style="width:50px; height:50px;" alt="" class="mb-5">
                    <span class="h3"><br />선택하신 지역의<br /></span>
                    <span class="h3"> 근처 유동인구 <br /></span>
                    <span class="h3">상위 3개 역 정보입니다.</span>
                </div>

                <!-- 1등 카드 -->
                <div class="col-4 me-3">
                    <div class="card border-left-primary shadow h-100 py-2">
                        <div class="card-body d-flex flex-column justify-content-center align-items-center">
                            <div class="text-center">
                                <img src="@/assets/img/medals/first_place_medal.png"
                                    style="max-width: 60%; height: auto" alt="1등 메달" />
                            </div>
                            <div class="row no-gutters align-items-center justify-content-center">
                                <div class="col text-center">
                                    <div class="h3 mt-5 mb-2 font-weight-bold text-purple">{{ firstStation }}역</div>
                                    <div class="h4 mb-1 text-gray-300">
                                        <h4>{{ firstPeople.toLocaleString() }}명</h4>
                                    </div>
                                    <p>{{ getTodayDate() }} 기준</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- 2등, 3등 카드 -->
                <div class="col-3 d-flex flex-column justify-content-between">
                    <!-- 2등 카드 -->
                    <div class="card border-left-primary shadow py-2 mb-5">
                        <div class="card-body d-flex align-items-center">
                            <div class="text-left me-2">
                                <img src="@/assets/img/medals/second_place_medal.png"
                                    style="max-width: 60px; height: auto" alt="2등 메달" />
                            </div>
                            <div>
                                <div class="h4 font-weight-bold text-purple mb-1">{{ secondStation }}역</div>
                                <div class="h6 text-gray-300">{{ secondPeople.toLocaleString() }}명</div>
                            </div>
                        </div>
                    </div>

                    <!-- 3등 카드 -->
                    <div class="card border-left-primary shadow py-2">
                        <div class="card-body d-flex align-items-center">
                            <div class="text-left me-2">
                                <img src="@/assets/img/medals/third_place_medal.png"
                                    style="max-width: 60px; height: auto" alt="3등 메달" />
                            </div>
                            <div>
                                <div class="h4 font-weight-bold text-purple mb-1">{{ thirdStation }}역</div>
                                <div class="h6 text-gray-300">{{ thirdPeople.toLocaleString() }}명</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { onMounted, ref, defineProps } from 'vue';
import axios from 'axios';

const props = defineProps(["reportId"]);

const data = ref({});

// 역 데이터
const firstStation = ref('');
const secondStation = ref('');
const thirdStation = ref('');
const firstPeople = ref(0);
const secondPeople = ref(0);
const thirdPeople = ref(0);
const firstDate = ref('');
const secondDate = ref('');
const thirdDate = ref('');

const getTodayDate = () => {
    const today = new Date();

    const year = today.getFullYear();
    const month = String(today.getMonth() + 1).padStart(2, '0'); // 월은 0부터 시작하므로 +1을 해줘야 합니다.
    const day = String(today.getDate()).padStart(2, '0'); // 날짜도 두 자릿수로 포맷

    return `${year}-${month}-${day}`;
}

onMounted(async () => {
    // API 호출
    const response = await axios.get(`http://localhost:8080/api/report/${props.reportId}`);
    data.value = response.data;


    // 각 역 데이터 할당
    firstStation.value = data.value.top_3_nearby_stations[0].station_name;
    firstPeople.value = data.value.top_3_nearby_stations[0].people;
    firstDate.value = data.value.top_3_nearby_stations[0].date;

    secondStation.value = data.value.top_3_nearby_stations[1].station_name;
    secondPeople.value = data.value.top_3_nearby_stations[1].people;
    secondDate.value = data.value.top_3_nearby_stations[1].date;

    thirdStation.value = data.value.top_3_nearby_stations[2].station_name;
    thirdPeople.value = data.value.top_3_nearby_stations[2].people;
    thirdDate.value = data.value.top_3_nearby_stations[2].date;


});

</script>

<style scoped>
.card {
    overflow: hidden;
    /* 카드가 내부 내용을 벗어나지 않도록 설정 */
    border-radius: 0.35rem;
    /* 카드의 모서리 라운드 설정 */
}

.text-overlay {
    /* position: absolute; */
    z-index: 1;
    /* 텍스트가 이미지 위에 표시되도록 설정 */
    text-align: left;
    /* 왼쪽 정렬 */
    font-weight: 600;
}

.text-purple {
    color: #fca3b9;
}




.add_card {
    border: 1px solid #F6A8B8;
    /* 카드 테두리 색상 */
    border-radius: 10px;
    /* 둥근 모서리 */
    padding: 20px;
    /* 내부 여백 */
    text-align: center;
    /* 텍스트 가운데 정렬 */
    margin: 10px;
    /* 카드 간의 외부 여백 */
}
</style>