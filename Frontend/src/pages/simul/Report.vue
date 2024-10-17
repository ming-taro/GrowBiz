<template>
  <div v-if="report">
    <!-- 헤더 -->
    <Result v-if="report != null" v-bind:simulation_response_id=report.simulation_response_id
      :brand_name=report.brand_name />


    <!-- 추천브랜드 및 그래프 -->
    <Bar v-bind:report=report />

    <AddBrand v-bind:reportId=reportId />


    <div style="background-color: #f6f4f9; padding-bottom: 20px">
      <AvgCard v-bind:report=report></AvgCard>
    </div>

    <!-- 추천 위치 -->
    <div class="container mw-screen-xl mb-8">
      <Location v-if="location != null" v-bind:location=location :plno_list=getPropertyId() />
    </div>

    <!-- 대출 -->
    <div style="background-color: #f6f4f9; padding: 20px" class="mb-8 pt-8 pb-5">
      <!-- 배경색과 패딩 추가 -->
      <Loan v-bind:report=report />
    </div>

    <!-- 유동인구-->
    <div class="mb-8">
      <Result3 v-bind:reportId=reportId />
    </div>


    <!-- 교육정보 -->
    <div style="background-color: #f6f4f9;" class="pt-5 pb-5">
      <Education />
    </div>

  </div>
</template>

<script setup>
import Result from '@/components/report/Result.vue';
import Location from '@/components/report/Location.vue';
import Bar from '@/components/report/Bar.vue';
import Education from '@/components/report/Education.vue';
import Loan from '@/components/report/Loan.vue';
import AvgCard from '@/components/report/AvgCard.vue';
import Result3 from '@/components/report/Result3.vue';
import AddBrand from '@/components/report/AddBrand.vue';

import { onMounted, ref } from 'vue';
import { fetchReportById } from '@/services/simulation/ReportAPI';
import { findLocation } from '@/services/simulation/SimulationAPI';

const report = ref(null);

const location = ref(null);
const reportId = ref("670a117bf2faf8abef449573");

const getPropertyId = () => {
  const data = report.value.top_property_listings;
  let propertyId = [];

  for (let index = 0; index < data.length; index++) {
    propertyId.push(data[index].property_id);
  }
  return propertyId;
}

const storeLocation = async () => {
  const id = report.value.simulation_response_id;
  location.value = await findLocation(id);
}

const storeReport = async () => {
  let query = window.location.search;
  let param = new URLSearchParams(query);
  // let reportId = param.get('id');
  reportId.value = param.get('id');
  report.value = await fetchReportById(reportId.value);
}

onMounted(async () => {
  await storeReport();
  await storeLocation();
});
</script>

<style>
.title {
  font-size: 25px;
  font-weight: bold;
}
</style>