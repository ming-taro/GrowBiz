<template>
  <div>
    <!-- 헤더 -->
    <Result v-if="report != null" v-bind:simulation_response_id=report.simulation_response_id
      :brand_name=report.brand_name />


    <!-- 그래프 -->
    <Bar />

    <div style="background-color: #f6f4f9;" class="pt-7 pb-7">
      <AvgCard></AvgCard>
    </div>

    <!-- 추천 위치 -->
    <div class="container mw-screen-xl mb-8 mt-8">
      <Location v-if="location != null" v-bind:location=location :plno_list=report.plno_list />
    </div>

    <!-- 그래프 및 유동인구-->
    <div class="">
      <Result3></Result3>
    </div>

    <!-- 대출 -->
    <div>
      <!-- 배경색과 패딩 추가 -->
      <Loan />
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

import { onMounted, ref } from 'vue';
import { fetchReportById } from '@/services/simulation/ReportAPI';
import { findLocation } from '@/services/simulation/SimulationAPI';

const report = ref(null);
const location = ref(null);

const storeLocation = async () => {
  const id = report.value.simulation_response_id;
  location.value = await findLocation(id);
}

const storeReport = async () => {
  let query = window.location.search;
  let param = new URLSearchParams(query);
  let reportId = param.get('id');
  report.value = await fetchReportById(reportId);
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