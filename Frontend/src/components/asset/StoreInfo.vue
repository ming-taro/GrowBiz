<template lang="">
  <div>
    <div style="position: relative; overflow: hidden">
      <div class="d-flex justify-content-between gap-2">
        <div style="display: flex; width: 60%">
          <h2 class="title mb-2">내 가게</h2>
          <div style="margin: 1% 0% 0% 1%" id="disable">
            해당 내용은 견본 데이터 입니다. 회원님의 가게를 등록해 보세요.
          </div>
        </div>
        <div class="d-flex align-items-center gap-2">
          <button
            type="button"
            @click="goToUpdate"
            class="btn btn-sm btn-neutral mb-3"
          >
            수정
          </button>
          <button
            type="button"
            class="btn btn-sm btn-primary mb-3"
            @click="goToStoreReg"
          >
            가게 등록
          </button>
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
                  :src="'/src/assets/img/upload/' + store.imageUrl"
                  class="card-img-top rounded"
                  style="width: 546px; height: 307px; object-fit: cover"
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
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { useAuthStore } from '@/stores/auth';
import { useRouter } from 'vue-router';
import { ref, onMounted } from 'vue';

const authStore = useAuthStore();

const mno = authStore.state.mno;

let id = mno;

export default {
  name: 'StoreInfo',
  setup() {
    const router = useRouter();

    const store = ref({});
    const amount = ref();
    const total = ref();

    const fetchStoreData = async () => {
      if (id == '') {
        id = 0;
      }

      try {
        let response = await axios.get(`/api/kmap/member/${id}`);

        console.log(response.data);

        disable.style.display = '';
        if (response.data.length == 0) {
          const disable = document.getElementById('disable');
          id = '1234';
        } else {
          id = mno;
          disable.style.display = 'none';
        }

        response = await axios.get(`/api/kmap/member/${id}`);

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

        console.log(store.value);
      } catch (error) {
        console.error('데이터를 가져오는 중 오류 발생:', error);
      }
    };

    const formatMoney = (amount) => {
      if (amount === null || amount === undefined) {
        return '-'; // 값이 없을 때 기본값 설정
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

    // const formatRate = (rate) => {
    //   return rate * 100 + '%';
    // };

    const goToStoreReg = () => {
      if (mno == '') {
        router.push('/login');
      } else {
        router.push('/asset/storereg');
      }
    };

    const goToUpdate = () => {
      if (mno == '') {
        router.push('login');
      } else if (id == '1234') {
        router.push('/asset/storereg');
      } else {
        router.push('/asset/storeupdate');
      }
    };

    // 페이지 로딩 시 로그인 상태 확인하는 함수
    const checkUserId = () => {
      const blur_overlay = document.getElementById('blur-overlay');
      const blur = document.getElementById('blur');
      const blur_text = document.getElementById('blur-text');

      blur_text.style.display = 'none';

      if (mno == '') {
        blur_text.style.display = '';
        blur_overlay.classList.add('blur-overlay');
        blur.classList.add('blur');
        blur_text.classList.add('blur-text');
      }
    };

    onMounted(() => {
      checkUserId(); // 페이지가 로드될 때 checkUserId 함수 호출
      fetchStoreData(); // 페이지가 로드될 때 데이터 가져오기
    });

    return {
      store,
      formatMoney,
      amount,
      total,
      // formatRate,
      checkUserId,
      goToStoreReg,
      goToUpdate,
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
