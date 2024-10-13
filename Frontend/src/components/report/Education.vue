<template>
  <div class="">
    <div class="title">교육 정보</div>
    <div class="con-card">
      <!-- Row to contain 4 cards in a single row -->
      <div class="row">
        <div class="col-3">
          <div class="card">
            <img
                src="@/assets/img/report/edu_1.png"
                class="card-img-top"
                alt="Card image"
              />
              <div class="card-body">
              <h5 class="card-title">초보 창업자들은 왜 프랜차이즈를 선택하는가?
              </h5>
              <p class="card-text fs-sm mb-3">
                프랜차이즈 창업에 대한 이해
              </p>
              <a href="/infoplaza/education/video/1252" class="btn btn-sm btn-primary"
                >상세보기</a>
            </div>
          </div>
        </div>

        <div class="col-3">
          <div class="card">
            <img
                src="@/assets/img/report/edu_2.png"
                class="card-img-top"
                alt="Card image"
              />
            <div class="card-body">
              <h5 class="card-title">매출 상승의 비결, '온라인 고객 관리'</h5>
              <p class="card-text fs-sm mb-3">
                소비 심리에 대한 이해
              </p>
              <a href="/infoplaza/education/video/1198" class="btn btn-sm btn-primary">상세보기</a>
            </div>
          </div>
        </div>

        <div class="col-3">
          <div class="card">
            <img
                src="@/assets/img/report/edu_3.png"
                class="card-img-top"
                alt="Card image"
              />
            <div class="card-body">
              <h5 class="card-title">대박 나는 가게는 입구부터 다릅니다! (1)
              </h5>
              <p class="card-text fs-sm mb-3">
                매장 공간 디자인의 이해
              </p>
              <a href="/infoplaza/education/video/1335" class="btn btn-sm btn-primary">상세보기</a>
            </div>
          </div>
        </div>

        <div class="col-3">
          <div class="card">
            <img
                src="@/assets/img/report/edu_4.png"
                class="card-img-top"
                alt="Card image"
              />
            <div class="card-body">
              <h5 class="card-title">직장을 포기하고, 부캐로 창업하다!</h5>
              <p class="card-text fs-sm mb-3">
                캐릭터 디자인의 이해
              </p>
              <a href="/infoplaza/education/video/1198" class="btn btn-sm btn-primary">상세보기</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import imgSrc from '@/assets/img/people/img-12.jpg'; // 이미지 파일을 import

export default {
  data() {
    return {
      card: {
        title: '여기 적힌 글은',
        text: 'script에서 때려넣은 글임',
        imgSrc: imgSrc, // import한 이미지를 사용
        imgAlt: 'Card image',
        link: '#',
      },
    };
  },
};
</script>

<style>
.container {
  padding: 0px 80px;
}

.title {
  padding: 5px 0px;
}
</style>
