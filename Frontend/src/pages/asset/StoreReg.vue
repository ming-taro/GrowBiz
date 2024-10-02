<template>
  <div>
    <AssetHeader />
    <div class="container mw-screen-lg">
      <div class="mb-5">
        <h2 class="title">내 가게 등록</h2>
      </div>
      <div style="display: flex">
        <div style="width: 60%">
          <div class="mb-8">
            <div class="d-flex mb-3 align-items-end">
              <h3 class="fw-bolder me-3">가게 정보</h3>
              <p>등록할 가게 주소를 입력해 주세요.</p>
            </div>

            <div class="d-inline-flex align-items-center btn-store">
              <input
                type="text"
                class="form-control me-2 mb-3"
                placeholder="도로명, 지번, 건물명 검색"
              />
            </div>
            <button class="btn btn-primary">주소검색</button>
            <div style="width: 61.7%">
              <input type="text" class="form-control" placeholder="상세주소" />
            </div>
          </div>
        </div>
        <div style="width: 40%">asd</div>
      </div>
      <!-- <div class="mb-8">
        <div class="d-flex mb-3 align-items-end">
          <h3 class="fw-bolder me-3">초기 정보</h3>
          <p>가게 권리금 및 투자액을 입력해 주세요.</p>
        </div>
        <div class="d-flex">
          <div class="col-sm-2 me-8">
            <h6 class="mb-2">권리금</h6>
            <input type="text" class="form-control me-2 mb-3" />
          </div>
          <div class="col-sm-2">
            <h6 class="mb-2">총 투자액</h6>
            <input type="text" class="form-control me-2 mb-3" />
          </div>
        </div>
      </div>
      <div class="mb-8">
        <div class="d-flex mb-3 align-items-end">
          <h3 class="fw-bolder me-3">매출 정보</h3>
          <p>가게 월 매출 정보와 마진율을 입력해 주세요.</p>
        </div>

        <div class="d-flex">
          <div class="col-sm-2 me-8">
            <h6 class="mb-2">마진율</h6>
            <input type="text" class="form-control me-2 mb-3" />
          </div>
          <div class="col-sm-2 me-8">
            <h6 class="mb-2">손익 분기점</h6>
            <input type="text" class="form-control me-2 mb-3" />
          </div>
        </div>
      </div>
      <div class="mb-8">
        <div class="d-flex mb-3 align-items-end">
          <h3 class="fw-bolder me-3">경비</h3>
          <p>가게 공과금 및 기타 비용을 입력해 주세요.</p>
        </div>

        <div class="d-flex">
          <div class="col-sm-2 me-8">
            <h6 class="mb-2">입점 비용</h6>
            <input type="text" class="form-control me-2 mb-3" />
          </div>
          <div class="col-sm-2 me-8">
            <h6 class="mb-2">월 인건비</h6>
            <input type="text" class="form-control me-2 mb-3" />
          </div>
          <div class="col-sm-2 me-8">
            <h6 class="mb-2">공과 비용</h6>
            <input type="text" class="form-control me-2 mb-3" />
          </div>
          <div class="col-sm-2 me-8">
            <h6 class="mb-2">기타 비용</h6>
            <input type="text" class="form-control me-2 mb-3" />
          </div>
        </div>
      </div> -->
      <div class="mb-8">
        <div class="d-flex mb-3 align-items-end">
          <h3 class="fw-bolder me-3">종합 정보</h3>
          <p>상위 입력값을 바탕으로 계산된 정보를 보여드립니다.</p>
        </div>
        <div class="d-flex gap-8">
          <div class="">
            <h5 class="mb-2">매출 이익</h5>
            <input type="text" class="form-control me-2 mb-3" />
          </div>
          <div class="">
            <h5 class="mb-2">경비합계</h5>
            <input type="text" class="form-control me-2 mb-3" />
          </div>
          <div class="">
            <h5 class="mb-2">월수익</h5>
            <input type="text" class="form-control me-2 mb-3" />
          </div>
          <div class="">
            <h5 class="mb-2">권리금 회수기간</h5>
            <input type="text" class="form-control me-2 mb-3" />
          </div>
        </div>
      </div>
      <div class="d-flex justify-content-center">
        <button class="btn btn-primary streg-btn">등록하기</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import AssetHeader from '@/components/asset/AssetHeader.vue';
</script>

<style>
.streg-con {
  padding: 0px 150px 0px 150px;
}
.streg-h3 {
  text-align: center;
  margin-bottom: 30px;
}
.col-sm-4 {
  display: inline-flex; /* 인라인 플렉스 박스 */
  align-items: center; /* 수직 정렬 */
}

.straeg-p {
  margin-bottom: 10px;
}
p {
  font-weight: 300;
}

.streg-btn {
  width: 20%;
}
.btn-store {
  width: 49%;
}
</style>
