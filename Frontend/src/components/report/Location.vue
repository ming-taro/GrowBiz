<template>
  <div class="">
    <div class="title">추천 위치</div>
    <span class="row">
      <div class="col-6" style="width: 60%">
        <div id="map" style="height: 400px"></div>
      </div>
      <div class="col-6 p-5" style="background-color: white; width: 40%">
        <div class="d-flex flex-stack flex-wrap">
          <span class="fs-3 text-gray-500 fw-bolder pe-2 pt-4"
            >신한 넥스텔</span
          >
        </div>
        <div class="carousel-inner pt-6">
          <div class="carousel-item active">
            <div class="carousel-wrapper">
              <div
                class="d-flex flex-column justify-content-between flex-grow-1"
              >
                <!-- 첫 번째 행: 신청기간 마감 -->
                <div class="d-flex justify-content-between align-items-center">
                  <p class="fs-5">신청기간</p>
                  <p class="fs-5 fw-bolder">마감됨</p>
                </div>

                <!-- 두 번째 행: 구분 -->
                <div class="d-flex justify-content-between align-items-center">
                  <p class="fs-5">구분</p>
                  <p class="fs-5 fw-bolder">성장기반자금/직접대출</p>
                </div>

                <!-- 세 번째 행: 금리 -->
                <div class="d-flex justify-content-between align-items-center">
                  <p class="fs-5 0">금리</p>
                  <p class="fs-5 fw-bolder">3.83%</p>
                </div>
              </div>
            </div>
          </div>
        </div>
        <hr />
        <div class="d-flex flex-stack flex-wrap">
          <span class="fs-3 text-gray-500 fw-bolder pe-2 pt-4"
            >신한 넥스텔</span
          >
        </div>
        <div class="carousel-inner pt-6">
          <div class="carousel-item active">
            <div class="carousel-wrapper">
              <div
                class="d-flex flex-column justify-content-between flex-grow-1"
              >
                <!-- 첫 번째 행: 신청기간 마감 -->
                <div class="d-flex justify-content-between align-items-center">
                  <p class="fs-5">신청기간</p>
                  <p class="fs-5 fw-bolder">마감됨</p>
                </div>

                <!-- 두 번째 행: 구분 -->
                <div class="d-flex justify-content-between align-items-center">
                  <p class="fs-5">구분</p>
                  <p class="fs-5 fw-bolder">성장기반자금/직접대출</p>
                </div>

                <!-- 세 번째 행: 금리 -->
                <div class="d-flex justify-content-between align-items-center">
                  <p class="fs-5 0">금리</p>
                  <p class="fs-5 fw-bolder">3.83%</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </span>
  </div>
</template>

<script>
export default {
  mounted() {
    const script = document.createElement('script');
    script.src =
      '//dapi.kakao.com/v2/maps/sdk.js?appkey=09118387dc78b55b2c58f3876095c5d2&autoload=false';
    script.onload = () => {
      kakao.maps.load(() => {
        var container = document.getElementById('map');
        var options = {
          center: new kakao.maps.LatLng(33.450701, 126.570667),
          level: 3,
        };

        var map = new kakao.maps.Map(container, options);
      });
    };
    document.head.appendChild(script);
  },
};
</script>

<style scoped>
.container {
  padding: 0px 80px 15px 80px;
}

.title {
  margin: -14px 0px -14px 0px;
  position: relative;
  top: -18px;
  font-size: 25px;
  font-weight: bold;
}
</style>
