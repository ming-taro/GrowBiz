<template>
  <div class="">
    <div class="title">추천 위치</div>
    <span class="row">
      <div class="col-6" style="width: 60%">
        <div id="map" style="height: 400px"></div>
      </div>
      <div
        class="col-6"
        style="background-color: white; width: 40%; display: flex"
      >
        <div style="width: 70%">
          <div style="height: 50%">
            <h4>신한넥스텔</h4>
            <h5>매매 9,800 ~ 2억 1000</h5>
            오피스텔·280세대·총1동
            <br />
            1998.10.26·36.49㎡ ~ 103.66㎡
            <h5>매매9 | 전세0 | 월세14</h5>
          </div>
          <div style="height: 50%">
            <h4>신한넥스텔</h4>
            <h5>매매 9,800 ~ 2억 1000</h5>
          </div>
        </div>
        <div style="width: 30%">
          <div style="height: 50%">
            <img src="../../assets/img/report/sapmle.jpg" alt="" />
          </div>
          <div style="height: 50%">
            <img src="../../assets/img/report/sapmle.jpg" alt="" />
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
