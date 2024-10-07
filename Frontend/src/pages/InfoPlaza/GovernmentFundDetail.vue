<template>
  <div>
    <InfoPlazaHeader />
    <div class="container mw-screen-xl">
      <div class="row">
        <div class="col-1">
          <PersonalLoanHeader class="" />
        </div>
        <div class="col-11">
          <div class="row">
            <div class="">
              <!-- Product details-->
              <div class="offset-xl-1">
                <div class="d-none d-md-block" style="margin-top: -90px"></div>
                <div class="position-md-sticky top-0 ps-md-4 ps-lg-5 ps-xl-0">
                  <div
                    class="d-none d-md-block"
                    style="padding-top: 90px"
                  ></div>
                  <h1 class="d-none d-md-inline-block pb-1 mb-2">
                    {{ data.loanProductName }}
                  </h1>
                  <hr />
                  <div class="row">
                    <div
                      class="col-4 d-flex align-items-center justify-content-center"
                    >
                      <span>
                        <i
                          class="fa-solid fa-calendar-days"
                          style="font-size: 50px"
                        ></i>
                      </span>
                      <span class="text ms-3">
                        <span style="color: gray">신청기간</span> <br />
                        <strong>{{ data.applicationPeriod }}</strong>
                      </span>
                    </div>
                    <div
                      class="col-4 d-flex align-items-center justify-content-center"
                    >
                      <span>
                        <i
                          class="fa-solid fa-coins"
                          style="font-size: 50px"
                        ></i>
                      </span>
                      <span class="text ms-3">
                        <span style="color: gray">금리</span> <br />
                        <strong style="color: brown">{{
                          data.totalInterestRate
                        }}</strong>
                      </span>
                    </div>
                    <div
                      class="col-4 d-flex align-items-center justify-content-center"
                    >
                      <span>
                        <i
                          class="fa-solid fa-won-sign"
                          style="font-size: 50px"
                        ></i>
                      </span>
                      <span class="text ms-3">
                        <span style="color: gray">가산금리</span> <br />
                        <strong style="color: brown">{{
                          data.additionalInterestRate
                        }}</strong>
                      </span>
                    </div>
                  </div>

                  <hr />
                  <h3>상품 안내</h3>

                  <div v-html="formattedDescription"></div>
                  <hr />
                </div>
              </div>
            </div>
            <!-- <div class="col-6">
          <h2>대출 계산기</h2>
        </div> -->
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>
import InfoPlazaHeader from '@/components/infoplaza/InfoPlazaHeader.vue';
import PersonalLoanHeader from '@/components/infoplaza/PersonalLoanHeader.vue';
import { useRoute } from 'vue-router';
import { ref, computed } from 'vue';
import axios from 'axios';

const route = useRoute();

const productName = ref('');
productName.value = route.params.productName;
console.log(productName.value);
const BASEURI = '/api/infoPlaza/loan';

const data = ref();

// 데이터 리스트 가져오는 함수
const bringDataList = async () => {
  try {
    // Best 인기 업종 - 전체
    const response = await axios.get(BASEURI + '/getDetailItem', {
      params: {
        productName: productName.value,
      }, // 선택된 필터링 값을 쿼리 파라미터로 전송
    });
    if (response.status === 200) {
      data.value = response.data;
    } else {
      console.log('데이터 조회 실패');
    }
  } catch (error) {
    console.log('에러발생 :' + error);
  }
};

// Computed property to modify the description
const formattedDescription = computed(() => {
  // <h2>를 <h3>로 변경하고 <hr> 추가
  console.log(
    data.value.description
      .replace(/<h2>/g, '<hr><h3>')
      .replace(/<\/h2>/g, '</h3><br>')
      .replace(/<h3>/g, '<br><h4>')
  );

  if (data.value) {
    return data.value.description
      .replace(/<h3>/g, '<br><h4>')
      .replace(/<h2>/g, '<hr><h3>')
      .replace(/<\/h2>/g, '</h3><br>');
  }
  return '';
});

bringDataList();
</script>

<style></style>
