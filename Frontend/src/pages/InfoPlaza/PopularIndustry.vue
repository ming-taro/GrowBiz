<template>
  <div>
    <InfoPlazaHeader />
    <div class="container mw-screen-xl">
      <div class="row justify-content-center">
        <div class="col-xl-3 col-md-6">
          <div
            class="card border-left-primary h-100 position-relative"
            style="border: 0"
          >
            <div
              class="card-body d-flex flex-column justify-content-center align-items-center"
            >
              <img
                src="@/assets/img/medals/leaf.png"
                style="max-width: 70%; height: auto"
                alt="..."
              />
              <div class="mt-5 d-flex flex-column text-overlay">
                <h1>BEST</h1>
                <h2>인기 업종</h2>
              </div>
            </div>
          </div>
        </div>

        <!-- 1등 카드 -->
        <div class="col-xl-3 col-md-6">
          <div class="card border-left-primary shadow h-100 py-2">
            <div
              class="card-body d-flex flex-column justify-content-center align-items-center"
            >
              <div class="text-center">
                <img
                  src="@/assets/img/medals/first_place_medal.png"
                  style="max-width: 60%; height: auto"
                  alt="..."
                />
              </div>
              <div
                class="row no-gutters align-items-center justify-content-center"
              >
                <div class="col text-center">
                  <div class="h3 mt-5 mb-2 font-weight-bold text-purple">
                    {{ best3Data[0].svcIndutyCdNm }}
                  </div>
                  <div class="h4 mb-1 text-gray-300">
                    <h4>
                      {{ best3Data[0].signguCdNm }}
                      {{ best3Data[0].adstrdCdNm }}
                    </h4>
                  </div>
                  <p>
                    {{ best3Data[0].trdarSeCdNm }}
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- 2등, 3등 카드 -->
        <div class="col-xl-3 col-md-6 d-flex flex-column">
          <!-- 2등 카드 -->
          <div
            class="card border-left-primary shadow py-2 mb-2"
            style="flex: 1"
          >
            <div class="card-body d-flex align-items-center">
              <div class="text-left me-2">
                <img
                  src="@/assets/img/medals/second_place_medal.png"
                  style="max-width: 60px; height: auto"
                  alt="2nd place medal"
                />
              </div>
              <div class="ml-3">
                <div class="h4 font-weight-bold text-purple mb-1">
                  {{ best3Data[1].svcIndutyCdNm }}
                </div>
                <div class="h6 text-gray-300">
                  {{ best3Data[1].signguCdNm }} {{ best3Data[1].adstrdCdNm }}
                </div>
                <p class="text-gray-300">{{ best3Data[1].trdarSeCdNm }}</p>
              </div>
            </div>
          </div>

          <!-- 3등 카드 -->
          <div class="card border-left-primary shadow py-2" style="flex: 1">
            <div class="card-body d-flex align-items-center">
              <div class="text-left me-2">
                <img
                  src="@/assets/img/medals/third_place_medal.png"
                  style="max-width: 60px; height: auto"
                  alt="3rd place medal"
                />
              </div>
              <div class="ml-3">
                <div class="h4 font-weight-bold text-purple mb-1">
                  {{ best3Data[2].svcIndutyCdNm }}
                </div>
                <div class="h6 text-gray-300">
                  {{ best3Data[2].signguCdNm }} {{ best3Data[2].adstrdCdNm }}
                </div>
                <p class="text-gray-300">{{ best3Data[1].trdarSeCdNm }}</p>
              </div>
            </div>
          </div>
        </div>

        <!-- 필터링 카드 -->
        <div class="col-xl-3 col-md-6">
          <div class="card border-0 shadow h-100 py-4 text-center">
            <div
              class="card-body d-flex flex-column justify-content-center align-items-center"
            >
              <form @submit.prevent="fetchAgeData">
                <!-- 연령대 필터링 -->
                <label
                  for="ageFilter"
                  class="fw-bold mt-5"
                  style="font-size: 1.25rem"
                  >연령대</label
                >
                <div class="d-flex flex-wrap justify-content-center mt-2">
                  <div class="form-check form-check-inline mb-2">
                    <input
                      type="radio"
                      class="form-check-input"
                      id="ageAll"
                      value="전체"
                      name="age"
                      v-model="selectedAge"
                    />
                    <label class="form-check-label" for="ageAll">전체</label>
                  </div>
                  <div class="form-check form-check-inline mb-2">
                    <input
                      type="radio"
                      class="form-check-input"
                      id="age10"
                      value="10대"
                      name="age"
                      v-model="selectedAge"
                    />
                    <label class="form-check-label" for="age10">10대</label>
                  </div>
                  <div class="form-check form-check-inline mb-2">
                    <input
                      type="radio"
                      class="form-check-input"
                      id="age20"
                      value="20대"
                      name="age"
                      v-model="selectedAge"
                    />
                    <label class="form-check-label" for="age20">20대</label>
                  </div>
                  <div class="form-check form-check-inline mb-2">
                    <input
                      type="radio"
                      class="form-check-input"
                      id="age30"
                      value="30대"
                      name="age"
                      v-model="selectedAge"
                    />
                    <label class="form-check-label" for="age30">30대</label>
                  </div>
                  <div class="form-check form-check-inline mb-2">
                    <input
                      type="radio"
                      class="form-check-input"
                      id="age40"
                      value="40대"
                      name="age"
                      v-model="selectedAge"
                    />
                    <label class="form-check-label" for="age40">40대</label>
                  </div>
                  <div class="form-check form-check-inline mb-2">
                    <input
                      type="radio"
                      class="form-check-input"
                      id="age50"
                      value="50대"
                      name="age"
                      v-model="selectedAge"
                    />
                    <label class="form-check-label" for="age50">50대</label>
                  </div>
                  <div class="form-check form-check-inline mb-2">
                    <input
                      type="radio"
                      class="form-check-input"
                      id="age60"
                      value="60대 이상"
                      name="age"
                      v-model="selectedAge"
                    />
                    <label class="form-check-label" for="age60"
                      >60대 이상</label
                    >
                  </div>
                </div>

                <!-- 검색창 -->
                <div class="col-12 d-flex justify-content-center mt-4">
                  <button type="submit" class="btn btn-primary mb-4">
                    검색하기
                  </button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>

      <div class="row mt-20" style="display: flex; align-items: start">
        <div
          class="row"
          style="display: flex; justify-content: center; align-items: start"
        >
          <!-- Best 인기 업종 -전체 -->
          <div class="col-4">
            <!--begin::List widget 7-->
            <div class="card card-flush h-md-100">
              <!--begin::Header-->
              <div class="card-header py-7">
                <!--begin::Statistics-->
                <div class="m-0">
                  <!--begin::Heading-->
                  <div class="d-flex align-items-center mb-2">
                    <!--begin::Title-->
                    <span class="fs-2hx fw-bold text-gray-800 lh-1 ls-n2">
                      Best 인기 업종 - 전체
                    </span>
                    <!--end::Title-->
                    <router-link
                      to="/infoPlaza/industry/totalTrendingBusinessItems"
                      class="ms-auto"
                      style="font-size: 13px"
                    >
                      <i class="fa-solid fa-arrow-up-right-from-square"></i>
                      더보기
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
              <div class="card-body pt-0">
                <!--begin::Items-->
                <div class="mb-0">
                  <div
                    v-for="(item, index) in best5"
                    :key="item.stdrTrdarSvc"
                    class=""
                  >
                    <div class="d-flex flex-stack mt-3">
                      <!--begin::Section-->
                      <div
                        class="d-flex align-items-center me-5"
                        style="flex-grow: 1"
                      >
                        <!--begin::Symbol-->
                        <div class="symbol symbol-30px me-5 col-2">
                          <img
                            :src="
                              '/images/businessItem/' +
                              item.svcIndutyCdNm +
                              '.png'
                            "
                            alt=""
                            style="width: 30px"
                          />
                        </div>
                        <!--end::Symbol-->
                        <!--begin::Content-->
                        <div class="me-auto col-7">
                          <!--begin::Title-->
                          <p style="color: gray; font-size: 0.6rem">
                            {{ item.trdarSeCdNm }}
                          </p>
                          <span style="color: black; font-size: 1rem">{{
                            item.svcIndutyCdNm
                          }}</span>
                          <!--end::Desc-->
                        </div>
                        <!--end::Content-->
                      </div>
                      <!--end::Section-->
                      <!--begin::Wrapper-->
                      <div class="d-flex align-items-center col-5">
                        <!--begin::Number-->
                        <span class="text-gray-800 fw-bold fs-6 me-3">{{
                          item.signguCdNm
                        }}</span>
                        <!--end::Number-->
                        <!--begin::Info-->
                        <div class="d-flex flex-center">
                          <!--begin::label-->
                          <span class="badge badge-light-success fs-base">
                            <i class="fa-solid fa-angle-up"></i> 4 점포
                          </span>
                          <!--end::label-->
                        </div>
                        <!--end::Info-->
                      </div>
                      <!--end::Wrapper-->
                    </div>

                    <!--end::Item-->
                    <!--begin::Separator-->
                    <hr v-if="index < best5.length - 1" />
                  </div>

                  <!--end::Item-->
                </div>
                <!--end::Items-->
              </div>
              <!--end::Body-->
            </div>
            <!--end::List widget 7-->
          </div>

          <!-- Best 인기 업종 - My 위치 -->
          <div class="col-4">
            <!--begin::List widget 7-->
            <div class="card card-flush h-md-100">
              <!--begin::Header-->
              <div class="card-header py-7">
                <!--begin::Statistics-->
                <div class="m-0">
                  <!--begin::Heading-->
                  <div class="d-flex align-items-center mb-2">
                    <!--begin::Title-->
                    <span class="fs-2hx fw-bold text-gray-800 lh-1 ls-n2">
                      Best 인기 업종 - My 위치
                    </span>
                    <router-link
                      to="/infoPlaza/industry/mylocationTrending"
                      class="ms-auto"
                      style="font-size: 13px"
                    >
                      <i class="fa-solid fa-arrow-up-right-from-square"></i>
                      더보기
                    </router-link>
                    <!--end::Title-->
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
              <div class="card-body pt-0">
                <!--begin::Items-->
                <div class="mb-0">
                  <!--begin::Item-->
                  <div class="d-flex flex-stack mt-3">
                    <!--begin::Section-->
                    <div
                      class="d-flex align-items-center me-5"
                      style="flex-grow: 1"
                    >
                      <!--begin::Symbol-->
                      <div class="symbol symbol-30px me-5">
                        <span class="symbol-label">
                          <i class="ki-duotone ki-magnifier fs-3 text-gray-600">
                            <!-- 아이콘 사진 넣는 곳 -->
                            <i class="fa-solid fa-bowl-food"></i>
                          </i>
                        </span>
                      </div>
                      <!--end::Symbol-->
                      <!--begin::Content-->
                      <div class="me-auto">
                        <!--begin::Title-->
                        <p style="color: gray; font-size: 0.6rem">서대문역</p>
                        <span style="color: black; font-size: 1rem"
                          >한식음식점</span
                        >
                        <!--end::Desc-->
                      </div>
                      <!--end::Content-->
                    </div>
                    <!--end::Section-->
                    <!--begin::Wrapper-->
                    <div class="d-flex align-items-center">
                      <!--begin::Number-->
                      <span class="text-gray-800 fw-bold fs-6 me-3">124%</span>
                      <!--end::Number-->
                      <!--begin::Info-->
                      <div class="d-flex flex-center">
                        <!--begin::label-->
                        <span class="badge badge-light-success fs-base">
                          <i class="fa-solid fa-angle-up"></i> 4 점포
                        </span>
                        <!--end::label-->
                      </div>
                      <!--end::Info-->
                    </div>
                    <!--end::Wrapper-->
                  </div>
                  <!--end::Item-->
                  <!--begin::Separator-->
                  <hr />
                  <!--end::Separator-->
                  <!--begin::Item-->
                  <div class="d-flex flex-stack mt-3">
                    <!--begin::Section-->
                    <div
                      class="d-flex align-items-center me-5"
                      style="flex-grow: 1"
                    >
                      <!--begin::Symbol-->
                      <div class="symbol symbol-30px me-5">
                        <span class="symbol-label">
                          <i class="ki-duotone ki-magnifier fs-3 text-gray-600">
                            <!-- 아이콘 사진 넣는 곳 -->
                            <i class="fa-solid fa-bowl-food"></i>
                          </i>
                        </span>
                      </div>
                      <!--end::Symbol-->
                      <!--begin::Content-->
                      <div class="me-auto">
                        <!--begin::Title-->
                        <p style="color: gray; font-size: 0.6rem">서대문역</p>
                        <span style="color: black; font-size: 1rem"
                          >한식음식점</span
                        >
                        <!--end::Desc-->
                      </div>
                      <!--end::Content-->
                    </div>
                    <!--end::Section-->
                    <!--begin::Wrapper-->
                    <div class="d-flex align-items-center">
                      <!--begin::Number-->
                      <span class="text-gray-800 fw-bold fs-6 me-3">124%</span>
                      <!--end::Number-->
                      <!--begin::Info-->
                      <div class="d-flex flex-center">
                        <!--begin::label-->
                        <span class="badge badge-light-success fs-base">
                          <i class="fa-solid fa-angle-up"></i> 4 점포
                        </span>
                        <!--end::label-->
                      </div>
                      <!--end::Info-->
                    </div>
                    <!--end::Wrapper-->
                  </div>
                  <!--end::Item-->
                  <!--begin::Separator-->
                  <hr />
                  <!--end::Separator-->
                  <!--begin::Item-->
                  <div class="d-flex flex-stack mt-3">
                    <!--begin::Section-->
                    <div
                      class="d-flex align-items-center me-5"
                      style="flex-grow: 1"
                    >
                      <!--begin::Symbol-->
                      <div class="symbol symbol-30px me-5">
                        <span class="symbol-label">
                          <i class="ki-duotone ki-magnifier fs-3 text-gray-600">
                            <!-- 아이콘 사진 넣는 곳 -->
                            <i class="fa-solid fa-bowl-food"></i>
                          </i>
                        </span>
                      </div>
                      <!--end::Symbol-->
                      <!--begin::Content-->
                      <div class="me-auto">
                        <!--begin::Title-->
                        <p style="color: gray; font-size: 0.6rem">서대문역</p>
                        <span style="color: black; font-size: 1rem"
                          >한식음식점</span
                        >
                        <!--end::Desc-->
                      </div>
                      <!--end::Content-->
                    </div>
                    <!--end::Section-->
                    <!--begin::Wrapper-->
                    <div class="d-flex align-items-center">
                      <!--begin::Number-->
                      <span class="text-gray-800 fw-bold fs-6 me-3">124%</span>
                      <!--end::Number-->
                      <!--begin::Info-->
                      <div class="d-flex flex-center">
                        <!--begin::label-->
                        <span class="badge badge-light-success fs-base">
                          <i class="fa-solid fa-angle-up"></i> 4 점포
                        </span>
                        <!--end::label-->
                      </div>
                      <!--end::Info-->
                    </div>
                    <!--end::Wrapper-->
                  </div>
                  <!--end::Item-->
                  <!--begin::Separator-->
                  <hr />
                  <!--end::Separator-->
                  <!--begin::Item-->
                  <div class="d-flex flex-stack mt-3">
                    <!--begin::Section-->
                    <div
                      class="d-flex align-items-center me-5"
                      style="flex-grow: 1"
                    >
                      <!--begin::Symbol-->
                      <div class="symbol symbol-30px me-5">
                        <span class="symbol-label">
                          <i class="ki-duotone ki-magnifier fs-3 text-gray-600">
                            <!-- 아이콘 사진 넣는 곳 -->
                            <i class="fa-solid fa-bowl-food"></i>
                          </i>
                        </span>
                      </div>
                      <!--end::Symbol-->
                      <!--begin::Content-->
                      <div class="me-auto">
                        <!--begin::Title-->
                        <p style="color: gray; font-size: 0.6rem">서대문역</p>
                        <span style="color: black; font-size: 1rem"
                          >한식음식점</span
                        >
                        <!--end::Desc-->
                      </div>
                      <!--end::Content-->
                    </div>
                    <!--end::Section-->
                    <!--begin::Wrapper-->
                    <div class="d-flex align-items-center">
                      <!--begin::Number-->
                      <span class="text-gray-800 fw-bold fs-6 me-3">124%</span>
                      <!--end::Number-->
                      <!--begin::Info-->
                      <div class="d-flex flex-center">
                        <!--begin::label-->
                        <span class="badge badge-light-success fs-base">
                          <i class="fa-solid fa-angle-up"></i> 4 점포
                        </span>
                        <!--end::label-->
                      </div>
                      <!--end::Info-->
                    </div>
                    <!--end::Wrapper-->
                  </div>
                  <!--end::Item-->
                  <!--begin::Separator-->
                  <hr />
                  <!--end::Separator-->
                  <!--begin::Item-->
                  <div class="d-flex flex-stack mt-3">
                    <!--begin::Section-->
                    <div
                      class="d-flex align-items-center me-5"
                      style="flex-grow: 1"
                    >
                      <!--begin::Symbol-->
                      <div class="symbol symbol-30px me-5">
                        <span class="symbol-label">
                          <i class="ki-duotone ki-magnifier fs-3 text-gray-600">
                            <!-- 아이콘 사진 넣는 곳 -->
                            <i class="fa-solid fa-bowl-food"></i>
                          </i>
                        </span>
                      </div>
                      <!--end::Symbol-->
                      <!--begin::Content-->
                      <div class="me-auto">
                        <!--begin::Title-->
                        <p style="color: gray; font-size: 0.6rem">서대문역</p>
                        <span style="color: black; font-size: 1rem"
                          >한식음식점</span
                        >
                        <!--end::Desc-->
                      </div>
                      <!--end::Content-->
                    </div>
                    <!--end::Section-->
                    <!--begin::Wrapper-->
                    <div class="d-flex align-items-center">
                      <!--begin::Number-->
                      <span class="text-gray-800 fw-bold fs-6 me-3">124%</span>
                      <!--end::Number-->
                      <!--begin::Info-->
                      <div class="d-flex flex-center">
                        <!--begin::label-->
                        <span class="badge badge-light-success fs-base">
                          <i class="fa-solid fa-angle-up"></i> 4 점포
                        </span>
                        <!--end::label-->
                      </div>
                      <!--end::Info-->
                    </div>
                    <!--end::Wrapper-->
                  </div>
                  <!--end::Item-->
                </div>
                <!--end::Items-->
              </div>
              <!--end::Body-->
            </div>
            <!--end::List widget 7-->
          </div>

          <!-- 최근 폐업률 순위 -->
          <div class="col-4">
            <!--begin::List widget 7-->
            <div class="card card-flush h-md-100">
              <!--begin::Header-->
              <div class="card-header py-7">
                <!--begin::Statistics-->
                <div class="m-0">
                  <!--begin::Heading-->
                  <div class="d-flex align-items-center mb-2">
                    <!--begin::Title-->
                    <span class="fs-2hx fw-bold text-gray-800 lh-1 ls-n2">
                      최근 폐업률 순위
                    </span>
                    <!--end::Title-->
                    <router-link
                      to="/infoPlaza/industry/totalTrendingBusinessItems"
                      class="ms-auto"
                      style="font-size: 13px"
                    >
                      <i class="fa-solid fa-arrow-up-right-from-square"></i>
                      더보기
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
              <div class="card-body pt-0">
                <!--begin::Items-->
                <div class="mb-0">
                  <div
                    v-for="(item, index) in worst5"
                    :key="item.stdrTrdarSvc"
                    class=""
                  >
                    <div class="d-flex flex-stack mt-3">
                      <!--begin::Section-->
                      <div
                        class="d-flex align-items-center me-5"
                        style="flex-grow: 1"
                      >
                        <!--begin::Symbol-->
                        <div class="symbol symbol-30px me-5 col-2">
                          <img
                            :src="
                              '/images/businessItem/' +
                              item.svcIndutyCdNm +
                              '.png'
                            "
                            alt=""
                            style="width: 30px"
                          />
                        </div>
                        <!--end::Symbol-->
                        <!--begin::Content-->
                        <div class="me-auto col-7">
                          <!--begin::Title-->
                          <p style="color: gray; font-size: 0.6rem">
                            {{ item.trdarSeCdNm }}
                          </p>
                          <span style="color: black; font-size: 1rem">{{
                            item.svcIndutyCdNm
                          }}</span>
                          <!--end::Desc-->
                        </div>
                        <!--end::Content-->
                      </div>
                      <!--end::Section-->
                      <!--begin::Wrapper-->
                      <div class="d-flex align-items-center col-5">
                        <!--begin::Number-->
                        <span class="text-gray-800 fw-bold fs-6 me-3">{{
                          item.clsbizRt
                        }}</span>
                        <!--end::Number-->
                        <!--begin::Info-->
                        <div class="d-flex flex-center">
                          <!--begin::label-->
                          <span class="badge badge-light-danger fs-base">
                            <i class="fa-solid fa-angle-down"></i> 4 점포
                          </span>
                          <!--end::label-->
                        </div>
                        <!--end::Info-->
                      </div>
                      <!--end::Wrapper-->
                    </div>

                    <!--end::Item-->
                    <!--begin::Separator-->
                    <hr v-if="index < best5.length - 1" />
                  </div>

                  <!--end::Item-->
                </div>
                <!--end::Items-->
              </div>
              <!--end::Body-->
            </div>
            <!--end::List widget 7-->
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import InfoPlazaHeader from '@/components/infoplaza/InfoPlazaHeader.vue';
import axios from 'axios';
import { ref, reactive } from 'vue';

const BASEURI = '/api/infoPlaza/businessItem';
const best5 = ref([]);
const worst5 = ref([]);
const selectedAge = ref('전체');
const best3Data = ref([
  {
    adstrdCdNm: '노량진1동',
    agrde10SelngAmt: null,
    agrde20SelngAmt: null,
    agrde30SelngAmt: null,
    agrde40SelngAmt: null,
    agrde50SelngAmt: null,
    agrde60AboveSelngAmt: null,
    fmlSelngAmt: null,
    img: null,
    mdwkSelngAmt: null,
    mlSelngAmt: null,
    signguCdNm: '동작구',
    stdrTrdarSvc: null,
    stdrYyquCd: null,
    svcIndutyCdNm: '수산물판매',
    thsmonSelngAmt: null,
    trdarSeCdNm: '노량진역(노량진)',
    wkendSelngAmt: null,
  },
  {
    stdrTrdarSvc: null,
    stdrYyquCd: null,
    trdarSeCdNm: '가산디지털단지',
    svcIndutyCdNm: '일반의류',
    thsmonSelngAmt: null,
    agrde10SelngAmt: null,
    agrde20SelngAmt: null,
    agrde30SelngAmt: null,
    agrde40SelngAmt: null,
    agrde50SelngAmt: null,
    agrde60AboveSelngAmt: null,
    fmlSelngAmt: null,
    img: null,
    mdwkSelngAmt: null,
    mlSelngAmt: null,
  },
  {
    stdrTrdarSvc: null,
    stdrYyquCd: null,
    trdarSeCdNm: '용산전자상가(용산역)',
    svcIndutyCdNm: '컴퓨터및주변장치판매',
    thsmonSelngAmt: null,
    agrde10SelngAmt: null,
    agrde20SelngAmt: null,
    agrde30SelngAmt: null,
    agrde40SelngAmt: null,
    agrde50SelngAmt: null,
    agrde60AboveSelngAmt: null,
    fmlSelngAmt: null,
    img: null,
    mdwkSelngAmt: null,
    mlSelngAmt: null,
  },
]);

// 초기 화면 렌더링 시 불러올 초기 데이터 불러오기
const fetchTodoList = async () => {
  try {
    // Best 인기 업종 - 전체
    const response = await axios.get(BASEURI + '/getTotal5');
    console.log(response);
    if (response.status === 200) {
      best5.value = response.data;
    } else {
      console.log('데이터 조회 실패');
    }
  } catch (error) {
    console.log('에러발생 :' + error);
  }
  try {
    // 최근 폐업률 순위
    const response = await axios.get(BASEURI + '/getRate5');
    if (response.status === 200) {
      worst5.value = response.data;
    } else {
      console.log('데이터 조회 실패');
    }
  } catch (error) {
    console.log('에러발생 :' + error);
  }
};
// 연령대 카테고리 데이터 최신화
const fetchAgeData = async () => {
  try {
    const response = await axios.get(BASEURI + '/getBest3', {
      params: { age: selectedAge.value }, // 선택된 연령대 값을 쿼리 파라미터로 전송
    });
    best3Data.value = response.data;
    console.log(response.data);
    console.log('!!!');
    console.log(best3Data.value);

    console.log(best3Data.value[0].svcIndutyCdNm);
  } catch (error) {
    console.error('Error fetching age data:', error);
  }
};

fetchTodoList();
</script>

<style scoped>
.badge-light-success {
  background-color: #d4edda !important; /* 밝은 녹색 배경색 */
  color: #155724 !important; /* 진한 녹색 텍스트 */
}
.badge-light-danger {
  background-color: rgba(220, 53, 69, 0.1); /* 연한 빨간색 배경 */
  color: #dc3545; /* 빨간색 텍스트 */
}
.card {
  overflow: hidden; /* 카드가 내부 내용을 벗어나지 않도록 설정 */
  border-radius: 0.35rem; /* 카드의 모서리 라운드 설정 */
}

.text-overlay {
  /* position: absolute; */
  z-index: 1; /* 텍스트가 이미지 위에 표시되도록 설정 */
  text-align: left; /* 왼쪽 정렬 */
  font-weight: 600;
}
.text-purple {
  color: #fca3b9;
}
</style>
