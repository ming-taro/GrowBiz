<template>
  <div>
    <InfoPlazaHeader />
    <div class="container mw-screen-xl">
      <div class="row">
        <!-- 데이터가 있을 때만 렌더링 -->
        <div v-if="data">
          <!-- Product details-->
          <div class="offset-xl-1">
            <h1>{{ data.productName }}</h1>
            <hr />
            <div class="row">
              <div class="col-4 d-flex align-items-center justify-content-center">
                <span>
                  <i class="fa-solid fa-calendar-days" style="font-size: 50px"></i>
                </span>
                <span class="text ms-3">
                  <span style="color: gray">신청기간</span> <br />
                  <strong>{{ data.applicationPeriod }}</strong>
                </span>
              </div>
              <div class="col-4 d-flex align-items-center justify-content-center">
                <span>
                  <i class="fa-solid fa-coins" style="font-size: 50px"></i>
                </span>
                <span class="text ms-3">
                  <span style="color: gray">금리</span> <br />
                  <strong style="color: brown">{{ data.totalInterestRate }}</strong>
                </span>
              </div>
              <div class="col-4 d-flex align-items-center justify-content-center">
                <span>
                  <i class="fa-solid fa-won-sign" style="font-size: 50px"></i>
                </span>
                <span class="text ms-3">
                  <span style="color: gray">가산금리</span> <br />
                  <strong style="color: brown">{{ data.additionalInterestRate }}</strong>
                </span>
              </div>
            </div>
            <hr />
            <h3>상품 안내</h3>
            <hr />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>
import InfoPlazaHeader from '@/components/infoplaza/InfoPlazaHeader.vue';
import { useRoute } from 'vue-router';
import { ref, computed, onMounted } from 'vue';
import axios from 'axios';

const route = useRoute();
const data = ref(null); // 초기화
const loanKey = route.params.loanKey;

const bringDataList = async() => {
  try {
    const response = await axios.get(`http://localhost:8080/infoPlaza/loan/getKBLoan/${loanKey}`);
    data.value = response.data;
    console.log(data.value);
  } catch (error) {
    console.error('Failed to select:', error);
  }
};

onMounted(async () => {
  bringDataList();
});

</script>

<style></style>
