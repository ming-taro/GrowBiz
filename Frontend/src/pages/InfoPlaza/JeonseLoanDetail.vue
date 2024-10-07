<template>
  <div>
    <InfoPlazaHeader />
    <div class="container mw-screen-xl">
      <div class="row">
        <div class="">
          <div class="offset-xl-1">
            <div class="d-none d-md-block" style="margin-top: -90px"></div>
            <div class="position-md-sticky top-0 ps-md-4 ps-lg-5 ps-xl-0">
              <div class="d-none d-md-block" style="padding-top: 90px"></div>

              <div class="d-flex align-items-center">
                <div class="d-flex align-items-center me-7">
                  <img
                    :src="'/images/banklogo/' + data.korCoNm + '.png'"
                    alt=""
                    style="width: 50px"
                  />
                </div>
                <div class="d-flex align-items-center">
                  <div class="text-left">
                    <span class="fs-2 text-gray-500 fw-bolder d-block">
                      {{ data.finPrdtNm }}
                    </span>
                  </div>
                </div>
              </div>

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
                    <strong
                      >{{ formatDate(data.dclsStrtDay) }} ~
                      {{ formatEndDate(data.dclsEndDay) }}</strong
                    >
                  </span>
                </div>
                <div
                  class="col-4 d-flex align-items-center justify-content-center"
                >
                  <span>
                    <i class="fa-solid fa-coins" style="font-size: 50px"></i>
                  </span>
                  <span class="text ms-3">
                    <span style="color: gray">유형</span> <br />
                    <strong>{{ data.lendRateTypeNm }}</strong>
                  </span>
                </div>
                <div
                  class="col-4 d-flex align-items-center justify-content-center"
                >
                  <span>
                    <i class="fa-solid fa-won-sign" style="font-size: 50px"></i>
                  </span>
                  <span class="text ms-3">
                    <span style="color: gray">금리</span> <br />
                    <strong style="color: brown"
                      >{{ data.lendRateMin }} ~ {{ data.lendRateMax }} %</strong
                    >
                  </span>
                </div>
              </div>

              <hr />
            </div>
          </div>
        </div>
        <!-- <div class="col-6">
            <h2>대출 계산기</h2>
          </div> -->
      </div>
      <div class="row">
        <div class="col-1">
          <PersonalLoanHeader class="" />
        </div>
        <div class="col-11">
          <div class="content-box">
            <h3>1. 주요 내용</h3>
            <div class="content-item">
              <span class="label fw-bold">회사명</span
              ><span class="colon">: </span>
              <span class="value">{{ data.korCoNm }}</span>
            </div>
            <div class="content-item">
              <span class="label fw-bold">상환방식유형</span
              ><span class="colon">: </span>
              <span class="value">{{ data.rpayTypeNm }}</span>
            </div>
            <div class="content-item">
              <span class="label fw-bold">평균 금리</span
              ><span class="colon">: </span>
              <span class="value">{{ data.lendRateAvg }} %</span>
            </div>
            <div class="content-item">
              <span class="label fw-bold">대출 한도</span
              ><span class="colon">: </span>
              <span class="value">{{ data.loanLmt }}</span>
            </div>

            <br />
            <h3>2. 대출 부대 비용</h3>
            <div class="content-item">
              <span class="label fw-bold">대출 부대 비용</span
              ><span class="colon">: </span>
              <span class="value">{{ data.loanInciExpn }}</span>
            </div>

            <br />
            <h3>3. 중도상환 수수료</h3>
            <div class="content-item">
              <span class="label fw-bold">중도상환 수수료</span
              ><span class="colon">: </span>
              <span class="value">{{ data.erlyRpayFee }}</span>
            </div>
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

const id = ref('');
id.value = route.params.id;
const BASEURI = '/api/infoPlaza/loan';

const data = ref();

// 데이터 리스트 가져오는 함수
const bringDataList = async () => {
  try {
    // Best 인기 업종 - 전체
    const response = await axios.get(BASEURI + '/getDetailItemJeonse', {
      params: {
        id: id.value,
      }, // 선택된 필터링 값을 쿼리 파라미터로 전송
    });
    if (response.status === 200) {
      data.value = response.data;
      console.log(data.value);
    } else {
      console.log('데이터 조회 실패');
    }
  } catch (error) {
    console.log('에러발생 :' + error);
  }
};

// 날짜 형식 변환
const formatDate = (date) => {
  const dateString = String(date);
  if (dateString.length !== 8) {
    return dateString;
  }

  const year = dateString.substring(0, 4);
  const month = dateString.substring(4, 6);
  const day = dateString.substring(6, 8);

  return `${year.substring(2)}/${month}/${day}`;
};

// dclsEndDay가 null일 경우를 처리하는 함수
const formatEndDate = (date) => {
  if (date === null) {
    return '';
  }
  return formatDate(date);
};

bringDataList();
</script>

<style scoped>
.content-box {
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
  background-color: #f9f9f9;
}
.content-item {
  display: flex;
  margin-bottom: 8px;
}
.label {
  min-width: 120px; /* Ensure labels align properly */
  color: #333;
}
.value {
  color: #555;
}
.colon {
  padding-right: 5px; /* Optional additional spacing */
}
</style>
