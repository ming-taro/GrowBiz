<template>
  <!--begin::List widget 7-->
  <div class="card card-flush">
    <!--begin::Header-->
    <div class="card-header p-5 ps-6">
      <!--begin::Statistics-->
      <div class="m-0">
        <!--begin::Heading-->
        <div class="d-flex align-items-center">
          <!--begin::Title-->
          <span class="fs-2hx fw-bold text-gray-800 lh-1 ls-n2">
            Best 인기 업종 - 전체
          </span>
          <router-link
            to="/infoPlaza/industry/portionTrendingBusinessItems"
            class="ms-auto text-primary fw-bold"
          >
            더보기 &gt;
          </router-link>
        </div>
        <!--end::Heading-->
      </div>
      <!--end::Statistics-->
      <!--begin::Toolbar-->
      <div class="card-toolbar"></div>
      <!--end::Toolbar-->
    </div>
    <!--end::Header-->
    <!--begin::Body-->
    <div class="card-body pe-6 ps-6 pb-3 pt-1">
      <!--begin::Items-->
      <div class="mb-0">
        <!--begin::Item-->
        <div v-for="(item, index) in best5" :key="index">
          <div class="d-flex flex-stack mt-0">
            <!--begin::Section-->
            <div class="d-flex align-items-center me-5" style="flex-grow: 1">
              <div class="symbol symbol-30px me-5 col-2">
                <img
                  :src="'/images/businessItem/' + item.svcIndutyCdNm + '.png'"
                  alt=""
                  style="width: 30px"
                />
              </div>
              <!--begin::Content-->
              <div class="p-3">
                <!--begin::Title-->
                <p style="color: black; font-size: 1rem">
                  {{ item.svcIndutyCdNm }}
                </p>
                <!--end::Desc-->
              </div>
              <!--end::Content-->
            </div>
            <!--end::Section-->
            <!--begin::Wrapper-->
            <div class="d-flex align-items-center">
              <!--begin::Number-->
              <span
                class="text-gray-800 fw-bold fs-6 me-3 col-3 text-center"
                :class="{
                  'text-success': item.rankChange.startsWith('+'),
                  'text-danger':
                    item.rankChange.startsWith('-') &&
                    !/^-\s*$/.test(item.rankChange),
                }"
              >
                {{ item.rankChange == '-' ? '―' : item.rankChange }}
              </span>
              <!--end::Number-->
              <!--begin::Info-->
              <div class="d-flex flex-center">
                <span v-if="item.opbizStorCo > 0">
                  <span class="badge badge-light-success fs-base text-center">
                    <i class="fa-solid fa-angle-up"></i>
                    {{ item.opbizStorCo }} 점포
                  </span>
                </span>
                <span v-else>
                  <span class="badge badge-light-middle fs-base text-center">
                    {{ item.opbizStorCo }} 점포
                  </span>
                </span>
              </div>
              <!--end::Info-->
            </div>
            <!--end::Wrapper-->
          </div>
          <!--end::Item-->
          <!--begin::Separator-->
          <hr v-if="index < best5.length - 1" class="m-0" />
        </div>

        <!--end::Separator-->
      </div>
      <!--end::Items-->
    </div>
    <!--end::Body-->
  </div>
  <!--end::List widget 7-->
</template>
<script setup>
import axios from 'axios';
import { ref } from 'vue';

const BASEURI = '/api/infoPlaza/businessItem';

const best5 = ref([]);

const fetchTodoList = async () => {
  try {
    // Best 인기 업종 - 전체
    const response = await axios.get(BASEURI + '/getTotal5');
    if (response.status === 200) {
      best5.value = response.data;
    } else {
      console.log('데이터 조회 실패');
    }
  } catch (error) {
    console.log('에러발생 :' + error);
  }
};
fetchTodoList();
</script>
<style>
.badge-light-success {
  background-color: #d4edda !important; /* 밝은 녹색 배경색 */
  color: #155724 !important; /* 진한 녹색 텍스트 */
}
</style>
