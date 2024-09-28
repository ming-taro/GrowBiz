<template>
  <div>
    <div class="title">추천 위치</div>
    <div class="row">
      <div class="col-7">
        <div id="map" style="height: 400px"></div>
      </div>
      <div
        class="col-5 d-flex justify-content-center align-content-center"
        style="background-color: white"
      >
        <div style="display: flex; flex-direction: column; height: 95%">
          <div
            class="d-flex justify-content-between m-4 align-items-stretch"
            style="height: 50%"
          >
            <!-- 왼쪽 텍스트 -->
            <div
              class="d-flex flex-column justify-content-between"
              style="width: 60%"
            >
              <div>
                <h2 class="fw-bolder">신한넥스텔</h2>
                <h4 class="mainblue mt-1">매매 9,800 ~ 2억 1,000 원</h4>
                <div class="align-content-center">
                  <h6 class="mt-2" style="font-weight: 300">
                    오피스텔·280세대·총1동
                  </h6>
                  <h6 style="font-weight: 300">
                    1998.10.26·36.49㎡ ~ 103.66㎡
                  </h6>
                </div>
              </div>
              <h5 class="mt-auto align-content-end">
                매매 9 | 전세 0 | 월세 14
              </h5>
            </div>

            <!-- 오른쪽 이미지 -->
            <div class="d-flex align-items-end" style="width: 36%">
              <img
                src="../../assets/img/report/sapmle.jpg"
                alt=""
                style="width: 100%; height: auto"
              />
            </div>
          </div>

          <hr />
          <!-- 가로선 추가 -->

          <div
            class="d-flex justify-content-between mt-0 m-4 align-items-stretch"
            style="height: 50%"
          >
            <!-- 왼쪽 텍스트 -->
            <div
              class="d-flex flex-column justify-content-between"
              style="width: 60%"
            >
              <div>
                <h2 class="fw-bolder">신한넥스텔</h2>
                <h4 class="mainblue mt-1">매매 9,800 ~ 2억 1,000</h4>
                <div class="align-content-center">
                  <h6 class="mt-2" style="font-weight: 300">
                    오피스텔·280세대·총1동
                  </h6>
                  <h6 style="font-weight: 300">
                    1998.10.26·36.49㎡ ~ 103.66㎡
                  </h6>
                </div>
              </div>
              <h5 class="mt-auto align-content-end">
                매매 9 | 전세 0 | 월세 14
              </h5>
            </div>

            <!-- 오른쪽 이미지 -->
            <div class="d-flex align-items-end" style="width: 36%">
              <img
                src="../../assets/img/report/sapmle.jpg"
                alt=""
                style="width: 100%; height: auto"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
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
.mainblue {
  color: #6184c6;
}
.weight {
  font-weight: 100;
}
</style>
