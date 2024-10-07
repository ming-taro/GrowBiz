<template>
  <!-- 좌측 정책자금 / 국민은행 구분 탭 -->
  <div class="">
    <div class="list-group list-group-flush gap-2">
      <div class="text-center">
        <h4>개인</h4>
      </div>
      <div
        class="col-12 list-group-item gap-3 text-center p-2 bg-body-secondary-hover"
      >
        <div class="icon flex-none">
          <div class="icon flex-none">
            <img
              src="@/assets/img/infoplaza/popular.png"
              class="w-rem-8 h-rem-8"
              alt="..."
            />
          </div>
        </div>
        <div class="align-items-center flex-fill">
          <div>
            <RouterLink
              to="/infoPlaza/personalCreditLoan"
              class="stretched-link text-heading text-sm fw-bold"
              >개인신용</RouterLink
            >
          </div>
        </div>
      </div>
      <div
        class="list-group-item gap-3 text-center p-2 bg-body-secondary-hover"
      >
        <div class="icon flex-none">
          <img
            src="@/assets/img/infoplaza/storeinfo.png"
            class="w-rem-8 h-rem-8"
            alt="..."
          />
        </div>
        <div class="align-items-center flex-fill">
          <div>
            <RouterLink
              to="/infoPlaza/jeonseLoan"
              class="stretched-link text-heading text-sm fw-bold"
              >전세자금</RouterLink
            >
          </div>
        </div>
      </div>
      <div
        class="mb-10 list-group-item gap-3 p-2 text-center bg-body-secondary-hover"
      >
        <div class="icon flex-none">
          <img
            src="@/assets/img/infoplaza/add_business.png"
            class="w-rem-8 h-rem-8"
            alt="..."
          />
        </div>
        <div class="align-items-center flex-fill">
          <div>
            <RouterLink
              to="/infoPlaza/mortgageLoan"
              class="stretched-link text-heading text-sm fw-bold"
              >주택담보</RouterLink
            >
          </div>
        </div>
      </div>

      <div class="text-center">
        <h4>기업</h4>
      </div>
      <div
        class="list-group-item gap-3 text-center p-2 bg-body-secondary-hover"
      >
        <div class="icon flex-none">
          <div class="icon flex-none">
            <img
              src="@/assets/img/infoplaza/popular.png"
              class="w-rem-8 h-rem-8"
              alt="..."
            />
          </div>
        </div>
        <div class="align-items-center flex-fill">
          <div>
            <RouterLink
              to="/infoPlaza/governmentFund"
              class="stretched-link text-heading text-sm fw-bold"
              >정책자금</RouterLink
            >
          </div>
        </div>
      </div>
      <div
        class="list-group-item gap-3 text-center p-2 bg-body-secondary-hover"
      >
        <div class="icon flex-none">
          <div class="icon flex-none">
            <img
              src="@/assets/img/infoplaza/popular.png"
              class="w-rem-8 h-rem-8"
              alt="..."
            />
          </div>
        </div>
        <div class="align-items-center flex-fill">
          <div>
            <RouterLink
              to="/infoPlaza/KBLoan"
              class="stretched-link text-heading text-sm fw-bold"
              >국민은행</RouterLink
            >
          </div>
        </div>
      </div>
      <br />
    </div>
  </div>
  <!-- <ul class="nav nav-underline nav-fill">
    <li class="nav-item">
      <router-link
        class="nav-link active"
        aria-current="page"
        to="/infoPlaza/personalLoan"
        style="font-size: 18px"
        >개인</router-link
      >
    </li>
    <li class="nav-item">
      <router-link
        class="nav-link"
        aria-current="page"
        to="/infoPlaza/enterpriseLoan"
        style="font-size: 18px"
        >기업</router-link
      >
    </li>
  </ul> -->
</template>
