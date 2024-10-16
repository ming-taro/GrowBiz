<template lang="">
  <div class="container mb-10">
    <div style="display: flex; align-items: flex-end" class="mb-5">
      <h2 style="font-weight: bold">가게관리</h2>
      <p style="margin-left: 20px">회원님의 자산 현황을 확인해 보세요.</p>
    </div>
    <div class="row">
      <div class="row" style="width: 66%">
        <div class="col-xl-6 col-sm-6 d-flex">
          <div class="card image-card w-100 d-flex flex-column">
            <div class="card-body pb-5 flex-grow-1 mt-3">
              <div class="d-flex justify-content-between align-items-center">
                <img
                  :src="'/src/assets/img/upload/' + store.imageUrl"
                  class="card-img-top rounded p-2"
                  style="width: 546px; height: 307px; object-fit: cover"
                />
              </div>
            </div>
          </div>
        </div>

        <div class="col-xl-6 col-sm-6 d-flex">
          <div class="card w-100 d-flex flex-column">
            <div class="card-body pb-5 flex-grow-1 mt-5">
              <div class="">
                <div class="d-block stretched-link h4 mb-2 fw-bold fs-1">
                  {{ store.svcIndutyCdNm }}
                </div>
                <div class="d-block stretched-link h5 mb-2 fs-3">
                  {{ store.address }}&nbsp;{{ store.detailAddress }}
                </div>
                <div class="d-flex justify-content-between gap-4">
                  <div class="">
                    <span class="d-block text-sm text-heading fw-bold"
                      >월매출</span
                    >
                    <span class="d-block text-sm text-heading fw-bold"
                      >월세</span
                    >
                    <span class="d-block text-sm text-heading fw-bold"
                      >공과금</span
                    >
                    <span class="d-block text-sm text-heading fw-bold"
                      >인건비</span
                    >
                    <span class="d-block text-sm text-heading fw-bold"
                      >기타비용</span
                    >
                    <span class="d-block text-sm text-heading fw-bold"
                      >순이익</span
                    >
                  </div>
                  <div class="text-end">
                    <span class="d-block text-sm text-heading fw-bold">{{
                      formatMoney(amount)
                    }}</span>
                    <span class="d-block text-sm text-heading fw-bold">{{
                      formatMoney(store.rent)
                    }}</span>
                    <span class="d-block text-sm text-heading fw-bold">{{
                      formatMoney(store.utilityExpenses)
                    }}</span>
                    <span class="d-block text-sm text-heading fw-bold">{{
                      formatMoney(store.laborCost)
                    }}</span>
                    <span class="d-block text-sm text-heading fw-bold">{{
                      formatMoney(store.otherExpenses)
                    }}</span>
                    <span class="d-block text-sm text-heading fw-bold">{{
                      formatMoney(total)
                    }}</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="col-4">
        <StoreGraph />
      </div>
    </div>
  </div>
</template>

<script setup>
import StoreGraph from '@/components/main/StoreGraph.vue';
import axios from 'axios';
import { useAuthStore } from '@/stores/auth';
import { useRouter } from 'vue-router';
import { ref, onMounted } from 'vue';

const authStore = useAuthStore();
const mno = authStore.state.mno;
const router = useRouter();

const store = ref({});
const amount = ref();
const total = ref();

const fetchStoreData = async () => {
  try {
    var id = '1234';

    let response = await axios.get(`/api/kmap/member/${id}`);

    const svcIndutyCdNm = response.data.svcIndutyCdNm;

    const sum = await axios.get(`/api/chart/sum/${svcIndutyCdNm}`);

    amount.value = sum.data.amount;
    store.value = response.data;

    total.value =
      amount.value -
      (store.value.rent +
        store.value.utilityExpenses +
        store.value.laborCost +
        store.value.otherExpenses);

    if (store.value.imageUrl == null) {
      store.value.imageUrl = 'house.png';
    }
  } catch (error) {
    console.error('데이터를 가져오는 중 오류 발생:', error);
  }
};

const formatMoney = (amount) => {
  if (amount === null || amount === undefined) {
    return '-';
  }

  const 억 = Math.floor(amount / 100000000);
  const 만 = Math.floor((amount % 100000000) / 10000);

  let result = '';
  if (억 > 0) {
    result += `${억}억`;
  }
  if (만 > 0) {
    result += `${만}만`;
  }

  return result || amount.toString();
};

const goToStoreReg = () => {
  if (mno == undefined) {
    router.push('/login');
  } else {
    router.push('/asset/storereg');
  }
};

const goToUpdate = () => {
  if (mno == undefined) {
    router.push('/asset/storereg');
  } else {
    router.push('/asset/storeupdate');
  }
};

onMounted(() => {
  fetchStoreData();
});
</script>

<style scoped>
.card.image-card {
  margin: 0;
  /* 카드의 마진을 0으로 설정 */
  padding: 0;
  /* 카드의 패딩을 0으로 설정 */
}

.card.image-card .card-body {
  padding: 0 !important;
  /* 카드 본문 내부의 패딩을 0으로 설정 (강제 적용) */
}
</style>
