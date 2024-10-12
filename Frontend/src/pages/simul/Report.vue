<template>
  <div>
    <!-- 헤더 -->
    <Result v-if="report != null" v-bind:simulationResponseId=report.simulationResponseId />
    <!-- <Result /> -->

    <div class="container mw-screen-xl">
      <!-- 추천 위치 -->
      <Location v-if="location != null" v-bind:location=location />
    </div>

    <!-- 그래프 -->
    <Bar />

    <!-- 교육정보 -->
    <div class="container mw-screen-xl">
      <Education />
    </div>
    <!-- 대출 -->
    <div style="background-color: #f6f4f9; padding: 20px">
      <!-- 배경색과 패딩 추가 -->
      <Loan />
    </div>
  </div>
</template>

<script setup>
import Result from '@/components/report/Result.vue';
import Location from '@/components/report/Location.vue';
import Bar from '@/components/report/Bar.vue';
import Education from '@/components/report/Education.vue';
import Loan from '@/components/report/Loan.vue';
import { onMounted, ref } from 'vue';
import { fetchReportById } from '@/services/ReportAPI';
import { findLocation } from '@/services/SimulationAPI';

const report = ref(null);
const location = ref(null);

const storeLocation = async () => {
  const id = report.value.simulationResponseId;
  location.value = await findLocation(id);
}

const storeReport = async () => {
  let query = window.location.search;
  let param = new URLSearchParams(query);
  let reportId = param.get('id');

  console.log("리포트 아이디:", reportId);
  
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
