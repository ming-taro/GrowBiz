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
              <p>등록할 가게 주소와 사진을 등록해 주세요.</p>
            </div>

            <div class="d-inline-flex align-items-center">
              <input
                v-model="address"
                type="text"
                class="form-control me-2 mb-3"
                placeholder="도로명, 지번, 건물명 검색"
                readonly
              />
              <button
                class="btn btn-primary me-2 mb-3"
                style="width: 115px"
                @click="openDaumPostcode"
              >
                주소검색
              </button>
            </div>
            <div style="width: 70.7%">
              <input
                v-model="detailAddress"
                type="text"
                class="form-control"
                placeholder="상세주소"
              />
            </div>
          </div>
        </div>
        <!-- 사진 업로드 섹션 -->
        <div style="width: 40%">
          <div class="photo-area" @click="triggerFileInput">
            <img :src="imageUrl" alt="미리보기" class="photo-preview" />
          </div>
          <input
            type="file"
            ref="fileInput"
            @change="onFileChange"
            style="display: none"
          />
        </div>
      </div>

      <!-- 종합 정보 섹션 -->
      <div class="mb-8">
        <div class="d-flex mb-3 align-items-end">
          <h3 class="fw-bolder me-3">지출 정보</h3>
          <p>상위 입력값을 바탕으로 계산된 정보를 보여드립니다.</p>
        </div>
        <div class="d-flex gap-8">
          <div class="">
            <h5 class="mb-2">월세</h5>
            <input v-model="rent" type="text" class="form-control me-2 mb-3" />
          </div>
          <div class="">
            <h5 class="mb-2">공과금</h5>
            <input
              v-model="utilityExpenses"
              type="text"
              class="form-control me-2 mb-3"
            />
          </div>
          <div class="">
            <h5 class="mb-2">인건비</h5>
            <input
              v-model="laborCost"
              type="text"
              class="form-control me-2 mb-3"
            />
          </div>
          <div class="">
            <h5 class="mb-2">기타비용</h5>
            <input
              v-model="otherExpenses"
              type="text"
              class="form-control me-2 mb-3"
            />
          </div>
        </div>
      </div>
    </div>

    <AssetReg />

    <!-- 등록하기 버튼 -->
    <div class="d-flex justify-content-center">
      <button class="btn btn-primary streg-btn" @click="submitForm">
        등록하기
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import AssetHeader from '@/components/asset/AssetHeader.vue';
import AssetReg from '@/pages/asset/AssetReg.vue';
import defaultImage from '@/assets/img/infoplaza/house.png';

// 라우터 사용
const router = useRouter();

// 데이터 관련 변수들
const imageUrl = ref(defaultImage);
const fileInput = ref(null); // 파일 입력 필드를 참조하는 ref
const address = ref(''); // 주소 저장
const detailAddress = ref(''); // 상세 주소 저장
const rent = ref(''); // 월세
const utilityExpenses = ref(''); // 공과금
const laborCost = ref(''); // 인건비
const otherExpenses = ref(''); // 기타비용

// 파일 선택을 트리거하는 함수
const triggerFileInput = () => {
  fileInput.value.click();
};

// 파일 변경 시 호출되는 함수
const onFileChange = (event) => {
  const file = event.target.files[0];
  if (file) {
    imageUrl.value = URL.createObjectURL(file); // 미리보기용 이미지 URL 생성
  }
};

// Daum 우편번호 검색 창 열기
const openDaumPostcode = () => {
  new daum.Postcode({
    oncomplete: function (data) {
      address.value = data.address; // 주소 저장
    },
  }).open();
};

// 등록하기 버튼을 눌렀을 때 실행되는 함수
const submitForm = () => {
  const formData = {
    address: address.value,
    detailAddress: detailAddress.value,
    rent: rent.value,
    utilityExpenses: utilityExpenses.value,
    laborCost: laborCost.value,
    otherExpenses: otherExpenses.value,
    imageUrl: imageUrl.value,
  };

  // InfoAgree 페이지로 데이터를 넘기면서 이동 (query 사용)
  router.push({
    name: 'InfoAgree',
    query: formData, // 데이터를 query로 전달
  });
};
</script>

<style scoped>
.streg-con {
  padding: 0px 150px 0px 150px;
}
.streg-h3 {
  text-align: center;
  margin-bottom: 30px;
}
.col-sm-4 {
  display: inline-flex;
  align-items: center;
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

.photo-area {
  width: 100%;
  aspect-ratio: 1 / 1; /* 정사각형 비율 */
  border: solid;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer; /* 클릭 가능하도록 포인터 표시 */
}

.photo-preview {
  width: 100%;
  height: 100%;
  object-fit: cover; /* 이미지를 영역에 맞춰서 자르거나 맞춤 */
  aspect-ratio: 1 / 1; /* 이미지를 정사각형 비율로 맞춤 */
}
</style>
