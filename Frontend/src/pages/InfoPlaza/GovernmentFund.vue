<template>
  <div>
    <InfoPlazaHeader />
    <div class="container mw-screen-xl">
      <!-- Best 금리상품 title-->
      <div class="d-flex justify-content-center align-items-center">
        <div class="row">
          <div class="d-flex align-items-center mb-6">
            <img
              src="@/assets/img/infoplaza/thumbsUp.png"
              alt=""
              style="height: auto; max-height: 30px"
            />
            <h2 class="ms-2" style="font-weight: 700">BEST 금리 상품</h2>
          </div>
        </div>
      </div>
      <div class="card mb-10 p-4" style="background-color: #f6f4f9">
        <!-- Best 금리상품 내용-->
        <div class="row">
          <!-- 카드 여러 개 -->
          <div class="col-xl-3" v-for="(item, index) in best4List" :key="index">
            <a href="#">
              <div class="card card-xl-stretch h-100">
                <div
                  class="card-body pt-5 d-flex flex-column justify-content-between"
                >
                  <div>
                    <div class="d-flex flex-stack flex-wrap">
                      <span
                        class="fs-3 text-gray-500 pe-2"
                        style="font-weight: 500"
                      >
                        {{ item.loanProductName }}
                      </span>
                    </div>
                    <div class="carousel-inner pt-6">
                      <div class="carousel-item active">
                        <div class="carousel-wrapper">
                          <div class="d-flex flex-column flex-grow-1">
                            <!-- 콘텐츠 추가 가능 -->
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <!-- 금리 -->
                  <div
                    class="d-flex justify-content-end align-items-end ms-auto"
                  >
                    <p class="fs-6 text-gray-600 mb-1">금리</p>
                    <p class="h2 fw-bold mb-0 ms-2">
                      {{ item.totalInterestRate }}
                    </p>
                  </div>
                </div>
              </div>
            </a>
          </div>
        </div>
      </div>

      <div class="row mb-4 d-flex justify-content-end">
        <!-- d-flex 및 justify-content-end 추가 -->
        <!-- 필터링 및 검색 -->
        <div class="col-5 d-flex">
          <!-- col-auto 사용 -->
          <!-- 대출 구분 -->
          <div class="col-4">
            <select
              class="form-select round-corner"
              aria-label="Default select example"
              @change="onCategoryChange"
            >
              <option selected disabled hidden>구분</option>
              <option value="전체">전체</option>
              <option value="직접대출">직접대출</option>
              <option value="대리대출">대리대출</option>
            </select>
          </div>
          <!-- 검색창 -->
          <div class="col-8">
            <div class="h-100">
              <form class="h-100 form-group">
                <div class="h-100 input-group input-group-sm">
                  <input
                    type="text"
                    class="rounded form-control ms-1"
                    placeholder="검색어를 입력해 주세요."
                  />
                  <span class="ms-1 rounded input-group-text">
                    <i class="bi bi-search"></i>
                  </span>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>

      <div class="row">
        <div class="col-1">
          <PersonalLoanHeader class="" />
        </div>
        <!-- 대출 상품 내용 -->
        <div class="col-xl-11 ps-7">
          <!-- 대출 상품 카드 내용 -->
          <div class="row">
            <!-- 카드 1개 -->
            <div class="col-xl-4">
              <div class="card card-xl-stretch mb-5 mb-xl-8">
                <div class="card-body pt-5">
                  <div
                    id="kt_stats_widget_8_carousel"
                    class="carousel carousel-custom carousel-stretch slide"
                    data-bs-ride="carousel"
                    data-bs-interval="8000"
                  >
                    <div style="width: 25%">
                      <img
                        :src="'/images/banklogo/' + '㈜우리카드' + '.png'"
                        alt=""
                        style="width: 100px"
                      />
                    </div>
                    <div class="d-flex flex-stack flex-wrap">
                      <span class="fs-3 text-gray-500 fw-bolder pe-2 pt-4">{{
                        dataList[0].loanProductName
                      }}</span>
                    </div>
                    <div class="carousel-inner pt-6">
                      <div class="carousel-item active">
                        <div class="carousel-wrapper">
                          <div
                            class="d-flex flex-column justify-content-between flex-grow-1"
                          >
                            <!-- 첫 번째 행: 신청기간 마감 -->
                            <div
                              class="d-flex justify-content-between align-items-center"
                            >
                              <p class="fs-5">신청기간</p>
                              <p class="fs-5 fw-bolder">
                                {{ dataList[0].applicationPeriod }}
                              </p>
                            </div>

                            <!-- 두 번째 행: 구분 -->
                            <div
                              class="d-flex justify-content-between align-items-center"
                            >
                              <p class="fs-5">구분</p>
                              <p class="fs-5 fw-bolder">
                                {{ dataList[0].category }}
                              </p>
                            </div>

                            <!-- 세 번째 행: 금리 -->
                            <div
                              class="d-flex justify-content-between align-items-center"
                            >
                              <p class="fs-5 0">금리</p>
                              <p class="fs-5 fw-bolder">
                                {{ dataList[0].totalInterestRate }}
                              </p>
                            </div>
                          </div>

                          <!-- Info (상세 보기 버튼) -->
                          <div class="d-flex justify-content-end pt-4">
                            <RouterLink
                              to="/infoPlaza/personalLoan/loanDetail"
                              class="btn btn-light btn-sm btn-color-muted fs-7 fw-bolder px-5"
                              >상세 보기</RouterLink
                            >
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <!-- 카드 1개끝 -->
            <!-- 카드 1개 -->
            <div class="col-xl-4">
              <div class="card card-xl-stretch mb-5 mb-xl-8">
                <div class="card-body pt-5">
                  <div
                    id="kt_stats_widget_8_carousel"
                    class="carousel carousel-custom carousel-stretch slide"
                    data-bs-ride="carousel"
                    data-bs-interval="8000"
                  >
                    <div style="width: 25%">
                      <img src="@/assets/img/banklogo/국민은행.png" alt="" />
                    </div>
                    <div class="d-flex flex-stack flex-wrap">
                      <span class="fs-3 text-gray-500 fw-bolder pe-2 pt-4"
                        >혁신성장촉진자금</span
                      >
                    </div>
                    <div class="carousel-inner pt-6">
                      <div class="carousel-item active">
                        <div class="carousel-wrapper">
                          <div
                            class="d-flex flex-column justify-content-between flex-grow-1"
                          >
                            <!-- 첫 번째 행: 신청기간 마감 -->
                            <div
                              class="d-flex justify-content-between align-items-center"
                            >
                              <p class="fs-5">신청기간</p>
                              <p class="fs-5 fw-bolder">마감됨</p>
                            </div>

                            <!-- 두 번째 행: 구분 -->
                            <div
                              class="d-flex justify-content-between align-items-center"
                            >
                              <p class="fs-5">구분</p>
                              <p class="fs-5 fw-bolder">
                                성장기반자금/직접대출
                              </p>
                            </div>

                            <!-- 세 번째 행: 금리 -->
                            <div
                              class="d-flex justify-content-between align-items-center"
                            >
                              <p class="fs-5 0">금리</p>
                              <p class="fs-5 fw-bolder">3.83%</p>
                            </div>
                          </div>

                          <!-- Info (상세 보기 버튼) -->
                          <div class="d-flex justify-content-end pt-4">
                            <a
                              href="#"
                              class="btn btn-light btn-sm btn-color-muted fs-7 fw-bolder px-5"
                              >상세 보기</a
                            >
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <!-- 카드 1개끝 -->
            <!-- 카드 1개 -->
            <div class="col-xl-4">
              <div class="card card-xl-stretch mb-5 mb-xl-8">
                <div class="card-body pt-5">
                  <div
                    id="kt_stats_widget_8_carousel"
                    class="carousel carousel-custom carousel-stretch slide"
                    data-bs-ride="carousel"
                    data-bs-interval="8000"
                  >
                    <div style="width: 25%">
                      <img src="@/assets/img/banklogo/국민은행.png" alt="" />
                    </div>
                    <div class="d-flex flex-stack flex-wrap">
                      <span class="fs-3 text-gray-500 fw-bolder pe-2 pt-4"
                        >혁신성장촉진자금</span
                      >
                    </div>
                    <div class="carousel-inner pt-6">
                      <div class="carousel-item active">
                        <div class="carousel-wrapper">
                          <div
                            class="d-flex flex-column justify-content-between flex-grow-1"
                          >
                            <!-- 첫 번째 행: 신청기간 마감 -->
                            <div
                              class="d-flex justify-content-between align-items-center"
                            >
                              <p class="fs-5">신청기간</p>
                              <p class="fs-5 fw-bolder">마감됨</p>
                            </div>

                            <!-- 두 번째 행: 구분 -->
                            <div
                              class="d-flex justify-content-between align-items-center"
                            >
                              <p class="fs-5">구분</p>
                              <p class="fs-5 fw-bolder">
                                성장기반자금/직접대출
                              </p>
                            </div>

                            <!-- 세 번째 행: 금리 -->
                            <div
                              class="d-flex justify-content-between align-items-center"
                            >
                              <p class="fs-5 0">금리</p>
                              <p class="fs-5 fw-bolder">3.83%</p>
                            </div>
                          </div>

                          <!-- Info (상세 보기 버튼) -->
                          <div class="d-flex justify-content-end pt-4">
                            <a
                              href="#"
                              class="btn btn-light btn-sm btn-color-muted fs-7 fw-bolder px-5"
                              >상세 보기</a
                            >
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <!-- 카드 1개끝 -->
            <!-- 카드 1개 -->
            <div class="col-xl-4">
              <div class="card card-xl-stretch mb-5 mb-xl-8">
                <div class="card-body pt-5">
                  <div
                    id="kt_stats_widget_8_carousel"
                    class="carousel carousel-custom carousel-stretch slide"
                    data-bs-ride="carousel"
                    data-bs-interval="8000"
                  >
                    <div style="width: 25%">
                      <img src="@/assets/img/banklogo/국민은행.png" alt="" />
                    </div>
                    <div class="d-flex flex-stack flex-wrap">
                      <span class="fs-3 text-gray-500 fw-bolder pe-2 pt-4"
                        >혁신성장촉진자금</span
                      >
                    </div>
                    <div class="carousel-inner pt-6">
                      <div class="carousel-item active">
                        <div class="carousel-wrapper">
                          <div
                            class="d-flex flex-column justify-content-between flex-grow-1"
                          >
                            <!-- 첫 번째 행: 신청기간 마감 -->
                            <div
                              class="d-flex justify-content-between align-items-center"
                            >
                              <p class="fs-5">신청기간</p>
                              <p class="fs-5 fw-bolder">마감됨</p>
                            </div>

                            <!-- 두 번째 행: 구분 -->
                            <div
                              class="d-flex justify-content-between align-items-center"
                            >
                              <p class="fs-5">구분</p>
                              <p class="fs-5 fw-bolder">
                                성장기반자금/직접대출
                              </p>
                            </div>

                            <!-- 세 번째 행: 금리 -->
                            <div
                              class="d-flex justify-content-between align-items-center"
                            >
                              <p class="fs-5 0">금리</p>
                              <p class="fs-5 fw-bolder">3.83%</p>
                            </div>
                          </div>

                          <!-- Info (상세 보기 버튼) -->
                          <div class="d-flex justify-content-end pt-4">
                            <a
                              href="#"
                              class="btn btn-light btn-sm btn-color-muted fs-7 fw-bolder px-5"
                              >상세 보기</a
                            >
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <!-- 카드 1개끝 -->
            <!-- 카드 1개 -->
            <div class="col-xl-4">
              <div class="card card-xl-stretch mb-5 mb-xl-8">
                <div class="card-body pt-5">
                  <div
                    id="kt_stats_widget_8_carousel"
                    class="carousel carousel-custom carousel-stretch slide"
                    data-bs-ride="carousel"
                    data-bs-interval="8000"
                  >
                    <div style="width: 25%">
                      <img src="@/assets/img/banklogo/국민은행.png" alt="" />
                    </div>
                    <div class="d-flex flex-stack flex-wrap">
                      <span class="fs-3 text-gray-500 fw-bolder pe-2 pt-4"
                        >혁신성장촉진자금</span
                      >
                    </div>
                    <div class="carousel-inner pt-6">
                      <div class="carousel-item active">
                        <div class="carousel-wrapper">
                          <div
                            class="d-flex flex-column justify-content-between flex-grow-1"
                          >
                            <!-- 첫 번째 행: 신청기간 마감 -->
                            <div
                              class="d-flex justify-content-between align-items-center"
                            >
                              <p class="fs-5">신청기간</p>
                              <p class="fs-5 fw-bolder">마감됨</p>
                            </div>

                            <!-- 두 번째 행: 구분 -->
                            <div
                              class="d-flex justify-content-between align-items-center"
                            >
                              <p class="fs-5">구분</p>
                              <p class="fs-5 fw-bolder">
                                성장기반자금/직접대출
                              </p>
                            </div>

                            <!-- 세 번째 행: 금리 -->
                            <div
                              class="d-flex justify-content-between align-items-center"
                            >
                              <p class="fs-5 0">금리</p>
                              <p class="fs-5 fw-bolder">3.83%</p>
                            </div>
                          </div>

                          <!-- Info (상세 보기 버튼) -->
                          <div class="d-flex justify-content-end pt-4">
                            <a
                              href="#"
                              class="btn btn-light btn-sm btn-color-muted fs-7 fw-bolder px-5"
                              >상세 보기</a
                            >
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <!-- 카드 1개끝 -->
            <!-- 카드 1개 -->
            <div class="col-xl-4">
              <div class="card card-xl-stretch mb-5 mb-xl-8">
                <div class="card-body pt-5">
                  <div
                    id="kt_stats_widget_8_carousel"
                    class="carousel carousel-custom carousel-stretch slide"
                    data-bs-ride="carousel"
                    data-bs-interval="8000"
                  >
                    <div style="width: 25%">
                      <img src="@/assets/img/banklogo/국민은행.png" alt="" />
                    </div>
                    <div class="d-flex flex-stack flex-wrap">
                      <span class="fs-3 text-gray-500 fw-bolder pe-2 pt-4"
                        >혁신성장촉진자금</span
                      >
                    </div>
                    <div class="carousel-inner pt-6">
                      <div class="carousel-item active">
                        <div class="carousel-wrapper">
                          <div
                            class="d-flex flex-column justify-content-between flex-grow-1"
                          >
                            <!-- 첫 번째 행: 신청기간 마감 -->
                            <div
                              class="d-flex justify-content-between align-items-center"
                            >
                              <p class="fs-5">신청기간</p>
                              <p class="fs-5 fw-bolder">마감됨</p>
                            </div>

                            <!-- 두 번째 행: 구분 -->
                            <div
                              class="d-flex justify-content-between align-items-center"
                            >
                              <p class="fs-5">구분</p>
                              <p class="fs-5 fw-bolder">
                                성장기반자금/직접대출
                              </p>
                            </div>

                            <!-- 세 번째 행: 금리 -->
                            <div
                              class="d-flex justify-content-between align-items-center"
                            >
                              <p class="fs-5 0">금리</p>
                              <p class="fs-5 fw-bolder">3.83%</p>
                            </div>
                          </div>

                          <!-- Info (상세 보기 버튼) -->
                          <div class="d-flex justify-content-end pt-4">
                            <a
                              href="#"
                              class="btn btn-light btn-sm btn-color-muted fs-7 fw-bolder px-5"
                              >상세 보기</a
                            >
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <!-- 카드 1개끝 -->
            <!-- 카드 1개 -->
            <div class="col-xl-4">
              <div class="card card-xl-stretch mb-5 mb-xl-8">
                <div class="card-body pt-5">
                  <div
                    id="kt_stats_widget_8_carousel"
                    class="carousel carousel-custom carousel-stretch slide"
                    data-bs-ride="carousel"
                    data-bs-interval="8000"
                  >
                    <div style="width: 25%">
                      <img src="@/assets/img/banklogo/국민은행.png" alt="" />
                    </div>
                    <div class="d-flex flex-stack flex-wrap">
                      <span class="fs-3 text-gray-500 fw-bolder pe-2 pt-4"
                        >혁신성장촉진자금</span
                      >
                    </div>
                    <div class="carousel-inner pt-6">
                      <div class="carousel-item active">
                        <div class="carousel-wrapper">
                          <div
                            class="d-flex flex-column justify-content-between flex-grow-1"
                          >
                            <!-- 첫 번째 행: 신청기간 마감 -->
                            <div
                              class="d-flex justify-content-between align-items-center"
                            >
                              <p class="fs-5">신청기간</p>
                              <p class="fs-5 fw-bolder">마감됨</p>
                            </div>

                            <!-- 두 번째 행: 구분 -->
                            <div
                              class="d-flex justify-content-between align-items-center"
                            >
                              <p class="fs-5">구분</p>
                              <p class="fs-5 fw-bolder">
                                성장기반자금/직접대출
                              </p>
                            </div>

                            <!-- 세 번째 행: 금리 -->
                            <div
                              class="d-flex justify-content-between align-items-center"
                            >
                              <p class="fs-5 0">금리</p>
                              <p class="fs-5 fw-bolder">3.83%</p>
                            </div>
                          </div>

                          <!-- Info (상세 보기 버튼) -->
                          <div class="d-flex justify-content-end pt-4">
                            <a
                              href="#"
                              class="btn btn-light btn-sm btn-color-muted fs-7 fw-bolder px-5"
                              >상세 보기</a
                            >
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <!-- 카드 1개끝 -->
            <!-- 카드 1개 -->
            <div class="col-xl-4">
              <div class="card card-xl-stretch mb-5 mb-xl-8">
                <div class="card-body pt-5">
                  <div
                    id="kt_stats_widget_8_carousel"
                    class="carousel carousel-custom carousel-stretch slide"
                    data-bs-ride="carousel"
                    data-bs-interval="8000"
                  >
                    <div style="width: 25%">
                      <img src="@/assets/img/banklogo/국민은행.png" alt="" />
                    </div>
                    <div class="d-flex flex-stack flex-wrap">
                      <span class="fs-3 text-gray-500 fw-bolder pe-2 pt-4"
                        >혁신성장촉진자금</span
                      >
                    </div>
                    <div class="carousel-inner pt-6">
                      <div class="carousel-item active">
                        <div class="carousel-wrapper">
                          <div
                            class="d-flex flex-column justify-content-between flex-grow-1"
                          >
                            <!-- 첫 번째 행: 신청기간 마감 -->
                            <div
                              class="d-flex justify-content-between align-items-center"
                            >
                              <p class="fs-5">신청기간</p>
                              <p class="fs-5 fw-bolder">마감됨</p>
                            </div>

                            <!-- 두 번째 행: 구분 -->
                            <div
                              class="d-flex justify-content-between align-items-center"
                            >
                              <p class="fs-5">구분</p>
                              <p class="fs-5 fw-bolder">
                                성장기반자금/직접대출
                              </p>
                            </div>

                            <!-- 세 번째 행: 금리 -->
                            <div
                              class="d-flex justify-content-between align-items-center"
                            >
                              <p class="fs-5 0">금리</p>
                              <p class="fs-5 fw-bolder">3.83%</p>
                            </div>
                          </div>

                          <!-- Info (상세 보기 버튼) -->
                          <div class="d-flex justify-content-end pt-4">
                            <a
                              href="#"
                              class="btn btn-light btn-sm btn-color-muted fs-7 fw-bolder px-5"
                              >상세 보기</a
                            >
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <!-- 카드 1개끝 -->
            <!-- 카드 1개 -->
            <div class="col-xl-4">
              <div class="card card-xl-stretch mb-5 mb-xl-8">
                <div class="card-body pt-5">
                  <div
                    id="kt_stats_widget_8_carousel"
                    class="carousel carousel-custom carousel-stretch slide"
                    data-bs-ride="carousel"
                    data-bs-interval="8000"
                  >
                    <div style="width: 25%">
                      <img src="@/assets/img/banklogo/국민은행.png" alt="" />
                    </div>
                    <div class="d-flex flex-stack flex-wrap">
                      <span class="fs-3 text-gray-500 fw-bolder pe-2 pt-4"
                        >혁신성장촉진자금</span
                      >
                    </div>
                    <div class="carousel-inner pt-6">
                      <div class="carousel-item active">
                        <div class="carousel-wrapper">
                          <div
                            class="d-flex flex-column justify-content-between flex-grow-1"
                          >
                            <!-- 첫 번째 행: 신청기간 마감 -->
                            <div
                              class="d-flex justify-content-between align-items-center"
                            >
                              <p class="fs-5">신청기간</p>
                              <p class="fs-5 fw-bolder">마감됨</p>
                            </div>

                            <!-- 두 번째 행: 구분 -->
                            <div
                              class="d-flex justify-content-between align-items-center"
                            >
                              <p class="fs-5">구분</p>
                              <p class="fs-5 fw-bolder">
                                성장기반자금/직접대출
                              </p>
                            </div>

                            <!-- 세 번째 행: 금리 -->
                            <div
                              class="d-flex justify-content-between align-items-center"
                            >
                              <p class="fs-5 0">금리</p>
                              <p class="fs-5 fw-bolder">3.83%</p>
                            </div>
                          </div>

                          <!-- Info (상세 보기 버튼) -->
                          <div class="d-flex justify-content-end pt-4">
                            <a
                              href="#"
                              class="btn btn-light btn-sm btn-color-muted fs-7 fw-bolder px-5"
                              >상세 보기</a
                            >
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <!-- 카드 1개끝 -->
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>
import InfoPlazaHeader from '@/components/infoplaza/InfoPlazaHeader.vue';
import PersonalLoanHeader from '@/components/infoplaza/PersonalLoanHeader.vue';
import { ref } from 'vue';
import axios from 'axios';

const selectedCategory = ref('전체');
const dataList = ref([]);
const best4List = ref([]);

const BASEURI = '/api/infoPlaza/loan';

// 데이터 리스트 가져오는 함수
const bringLoanList = async () => {
  try {
    // Best 인기 업종 - 전체
    const response = await axios.get(BASEURI + '/getFilteredList', {
      params: {
        category: selectedCategory.value,
      }, // 선택된 필터링 값을 쿼리 파라미터로 전송
    });
    if (response.status === 200) {
      dataList.value = response.data;
      console.log(dataList.value);
    } else {
      console.log('데이터 조회 실패');
    }
  } catch (error) {
    console.log('에러발생 :' + error);
  }
};

// 데이터 리스트 가져오는 함수
const bringBest4List = async () => {
  try {
    // Best 인기 업종 - 전체
    const response = await axios.get(BASEURI + '/getBest4', {
      params: {
        category: selectedCategory.value,
      }, // 선택된 필터링 값을 쿼리 파라미터로 전송
    });
    if (response.status === 200) {
      best4List.value = response.data;
      console.log(best4List.value);
    } else {
      console.log('데이터 조회 실패');
    }
  } catch (error) {
    console.log('에러발생 :' + error);
  }
};

const onCategoryChange = (event) => {
  selectedCategory.value = event.target.value;
  bringLoanList();
};

bringBest4List();
bringLoanList();
</script>

<style scoped>
.row.d-flex {
  display: flex;
  flex-wrap: wrap;
}

.card-link {
  width: 100%;
}

.card {
  display: flex;
  flex-direction: column;
  height: 100%;
}
</style>
