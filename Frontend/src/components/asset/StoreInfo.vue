<template lang="">
  <div>
    <div style="position: relative; overflow: hidden">
      <div class="d-flex justify-content-between gap-2">
        <div>
          <h2 class="title mb-2">내 가게</h2>
        </div>
        <div class="d-flex align-items-center gap-2">
          <button type="button" class="btn btn-sm btn-neutral mb-3 mt-3">
            수정
          </button>
          <router-link to="/asset/storereg"
            ><button
              type="button"
              class="btn btn-sm btn-primary mb-3 mt-3 ms-0"
            >
              가게 등록
            </button>
          </router-link>
        </div>
      </div>

      <div id="blur-text">로그인 후 이용하실 수 있습니다.</div>
      <div class="row g-3 g-xl-6" id="blur">
        <div id="blur-overlay"></div>
        <div class="col-xl-6 col-sm-6 d-flex">
          <!-- 왼쪽 카드의 부모 -->
          <div class="card image-card w-100 d-flex flex-column">
            <!-- 카드가 세로로 늘어날 수 있도록 설정 -->
            <div class="card-body pb-5 flex-grow-1">
              <div class="d-flex justify-content-between align-items-center">
                <img
                  src="https://www.jumpoline.com/_file/jumpo/jumpoline_202406121654211156.jpg"
                  class="card-img-top rounded"
                />
              </div>
            </div>
          </div>
        </div>

        <div class="col-xl-6 col-sm-6 d-flex">
          <!-- 오른쪽 카드의 부모 -->
          <div class="card w-100 d-flex flex-column">
            <!-- 카드가 세로로 늘어날 수 있도록 설정 -->
            <div class="card-body pb-5 flex-grow-1">
              <div class="">
                <div class="d-block stretched-link h4 mb-2 fw-bold fs-1">
                  {{ store.storeName }}
                </div>
                <div class="d-block stretched-link h5 mb-2 fs-3">
                  {{ store.location }}
                </div>
                <div class="d-flex justify-content-between gap-4">
                  <div class="">
                    <span class="d-block text-sm text-heading fw-bold"
                      >권리금</span
                    >
                    <span class="d-block text-sm text-heading fw-bold"
                      >총 투자액</span
                    >
                    <span class="d-block text-sm text-heading fw-bold"
                      >월매출</span
                    >
                    <span class="d-block text-sm text-heading fw-bold"
                      >마진율</span
                    >
                    <span class="d-block text-sm text-heading fw-bold"
                      >매출이익</span
                    >
                    <span class="d-block text-sm text-heading fw-bold"
                      >경비 합계</span
                    >
                    <span class="d-block text-sm text-heading fw-bold"
                      >월수익</span
                    >
                    <span class="d-block text-sm text-heading fw-bold"
                      >권리금 회수기간</span
                    >
                  </div>
                  <div class="text-end">
                    <span class="d-block text-sm text-heading fw-bold">{{
                      formatMoney(store.keyMoney)
                    }}</span>
                    <span class="d-block text-sm text-heading fw-bold">{{
                      formatMoney(store.totalInvestment)
                    }}</span>
                    <span class="d-block text-sm text-heading fw-bold">{{
                      formatMoney(store.monthlySales)
                    }}</span>
                    <span class="d-block text-sm text-heading fw-bold">{{
                      formatRate(store.marginRate)
                    }}</span>
                    <span class="d-block text-sm text-heading fw-bold">{{
                      formatMoney(store.salesProfit)
                    }}</span>
                    <span class="d-block text-sm text-heading fw-bold">{{
                      formatMoney(store.totalExpenses)
                    }}</span>
                    <span class="d-block text-sm text-heading fw-bold">{{
                      formatMoney(store.monthlyProfit)
                    }}</span>
                    <span class="d-block text-sm text-heading fw-bold"
                      >{{ store.depositRecoveryPeriod }}개월</span
                    >
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { useAuthStore } from '@/stores/auth';

const authStore = useAuthStore();

const mno = authStore.state.mno;

export default {
  name: 'StoreInfo',
  setup() {
    const store = {
      stNo: 1,
      apNo: 'AP12345',
      userId: 'user01',
      storeName: 'CU 성남점',
      location: '경기남부 성남시 수정구 태평동 1층',
      keyMoney: 50000000,
      totalInvestment: 105000000,
      monthlySales: 20000000,
      marginRate: 0.25,
      salesProfit: 5000000,
      monthlyProfit: 3000000,
      storeEntryFee: 1000000,
      totalExpenses: 15000000,
      depositRecoveryPeriod: 12,
      breakEvenPoint: 20,
    };

    const formatMoney = (amount) => {
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

    const formatRate = (rate) => {
      return rate * 100 + '%';
    };

    // 페이지 로딩 시 로그인 상태 확인하는 함수
    const checkUserId = () => {
      const blur_overlay = document.getElementById('blur-overlay');
      const blur = document.getElementById('blur');
      const blur_text = document.getElementById('blur-text');

      blur_text.style.display = 'none';

      if (mno == undefined) {
        blur_text.style.display = '';
        blur_overlay.classList.add('blur-overlay');
        blur.classList.add('blur');
        blur_text.classList.add('blur-text');
      }
    };

    return {
      store,
      formatMoney,
      formatRate,
      checkUserId,
    };
  },
  mounted() {
    this.checkUserId(); // 페이지가 로드될 때 checkUserId 함수 호출
  },
};
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

.blur {
  width: 100%;
  height: 100%;
  background-image: url('your-image-url.jpg');
  background-size: cover;
  filter: blur(5px);
  top: 0;
  left: 0;
  z-index: 1;
}

.blur-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(128, 128, 128, 0.5);
  z-index: 2;
}

.blur-text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 3;
  color: black;
  font-size: 20px;
  font-weight: bold;
}
</style>
