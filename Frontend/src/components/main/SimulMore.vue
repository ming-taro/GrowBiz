<template>
  <div class="container">
    <div class="row justify-content-center mb-10">
      <!-- Row to contain cards -->
      <div class="col-5">
        <div class="card none_border ms-10">
          <div class="d-flex">
            <img
              src="@/assets/img/report/cafe2.png"
              class="rounded card-img-left"
              alt="Card image"
            />
            <div class="card-body">
              <h3 class="mb-3">동작구 카페</h3>
              <div class="d-flex justify-content-between">
                <h5 class="mb-1 fw-medium">보증금</h5>
                <h4 class="mb-0">2억</h4>
              </div>
              <div class="d-flex justify-content-between">
                <h5 class="mb-0 fw-medium">월세</h5>
                <h4 class="mb-0">550만</h4>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="col-5">
        <div class="card none_border ms-10">
          <div class="d-flex">
            <img
              src="@/assets/img/report/cafe1.png"
              class="rounded card-img-left"
              alt="Card image"
            />
            <div class="card-body ">
              <h3 class="mb-3">강남구 카페</h3>
              <div class="d-flex justify-content-between">
                <h5 class="mb-1 fw-medium">보증금</h5>
                <h4 class="mb-0">1억</h4>
              </div>
              <div class="d-flex justify-content-between">
                <h5 class="mb-0 fw-medium">월세</h5>
                <h4 class="mb-0">900만</h4>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="col-2 d-flex align-items-center justify-content-center pe-5">
        <a href="/simul/report">
          <button type="button" class="btn btn-sm btn-primary p-5">
            더 많은 리포트<br /> 보러가기 >
          </button>
        </a>
      </div>
    </div>
  </div>
</template>

<script setup>
</script>

<style scoped>
.card-img-left {
  height: 150px; /* 원하는 높이로 조정 */
  width: 250px; /* 원하는 너비로 조정 (필요에 따라 변경) */
  object-fit: cover; /* 이미지 비율 유지하면서 잘리도록 설정 */
}
.none_border {
  border: none;
  box-shadow: none;
}
</style>
