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

          <!-- 업종 선택 섹션 -->
          <div class="option">
            <select
              class="form-select round-corner"
              @change="onStoreChange"
              v-model="selectedStore"
            >
              <option value="" selected disabled>업종을 선택해 주세요</option>
              <option
                v-for="(store, index) in storeList"
                :key="index"
                :value="store"
              >
                {{ store }}
              </option>
            </select>
          </div>
        </div>

        <!-- 사진 업로드 섹션 -->
        <div style="width: 40%">
          <div class="photo-area" @click="triggerFileInput">
            <img
              :src="imageUrl"
              alt="미리보기"
              class="photo-preview"
              v-if="imageUrl"
              id="image"
            />
            <p v-else>이미지를 선택하세요</p>
          </div>
          <input
            type="file"
            ref="fileInput"
            @change="onFileChange"
            style="display: none"
          />
        </div>
      </div>

      <!-- 지출 정보 섹션 -->
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
        수정하기
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';
import AssetHeader from '@/components/asset/AssetHeader.vue';
import AssetReg from '@/pages/asset/AssetReg.vue';
import defaultImage from '@/assets/img/infoplaza/house.png';
import { useAuthStore } from '@/stores/auth';

const imageFile = ref(null); // 선택된 파일을 저장
const authStore = useAuthStore();
const mno = authStore.state.mno; // 사용자 번호

// 데이터 관련 변수들
const imageUrl = ref('house.png');
const fileInput = ref(null); // 파일 입력 필드를 참조하는 ref
const address = ref('');
const detailAddress = ref('');
const rent = ref('');
const utilityExpenses = ref('');
const laborCost = ref('');
const otherExpenses = ref('');
const storeList = ref([]); // 서버에서 가져온 업종 리스트
const selectedStore = ref(''); // 선택된 업종

// 파일 선택을 트리거하는 함수
const triggerFileInput = () => {
  fileInput.value.click();
};

// 파일 변경 시 호출되는 함수
const onFileChange = (event) => {
  const file = event.target.files[0];

  if (file) {
    imageFile.value = file;
    imageUrl.value = URL.createObjectURL(file); // 선택된 파일의 미리보기 URL 설정
  }
};

// Daum 우편번호 검색 창 열기
const openDaumPostcode = () => {
  if (window.daum) {
    new daum.Postcode({
      oncomplete: function (data) {
        address.value = data.address;
      },
    }).open();
  }
};

// Daum 우편번호 API 스크립트를 동적으로 로드
onMounted(() => {
  const script = document.createElement('script');
  script.src =
    'https://t1.daumcdn.net/mapjsapi/bundle/postcode/prod/postcode.v2.js';

  document.body.appendChild(script);
});

// 서버에서 가게 정보를 가져오는 함수
const fetchStoreData = async () => {
  try {
    const id = mno;

    const response = await axios.get(`/api/kmap/member/${id}`); // 사용자 가게 정보 불러오기
    const data = response.data;

    // 가져온 데이터를 폼에 기본값으로 채움
    address.value = data.address;
    detailAddress.value = data.detailAddress;
    rent.value = data.rent;
    utilityExpenses.value = data.utilityExpenses;
    laborCost.value = data.laborCost;
    otherExpenses.value = data.otherExpenses;
    selectedStore.value = data.svcIndutyCdNm;

    if (data.imageUrl == null) {
      imageUrl.value = defaultImage;
    } else {
      imageUrl.value = '/src/assets/img/upload/' + data.imageUrl;
    }

    // 이미지가 없을 경우 기본 이미지 사용
  } catch (error) {
    console.error('가게 정보를 불러오는 중 오류 발생:', error);
  }
};

// 서버에서 업종 리스트를 가져오는 함수
const fetchStoreList = async () => {
  try {
    const response = await axios.get('/api/store/list');
    storeList.value = response.data; // 업종 리스트 저장
  } catch (error) {
    console.error('업종 목록을 불러오는 중 오류가 발생했습니다.', error);
  }
};

// 폼 데이터를 서버로 전송하는 함수
const router = useRouter();

const submitForm = () => {
  const formDataToSend = new FormData();
  formDataToSend.append('address', address.value);
  formDataToSend.append('id', mno);
  formDataToSend.append('detailAddress', detailAddress.value);
  formDataToSend.append('rent', rent.value);
  formDataToSend.append('utilityExpenses', utilityExpenses.value);
  formDataToSend.append('laborCost', laborCost.value);
  formDataToSend.append('otherExpenses', otherExpenses.value);
  formDataToSend.append('svcIndutyCdNm', selectedStore.value); // 선택된 업종 추가

  // 이미지 파일 추가
  if (imageFile.value == null) {
    const fileName = imageUrl.value.match(/[^/]+$/)[0];
    console.log('Using existing image file name:', fileName);
    formDataToSend.append('existingImage', fileName);
  } else {
    console.log(imageFile.value);
    formDataToSend.append('image', imageFile.value); // 선택된 파일 추가
  }

  // 서버로 데이터를 전송
  axios
    .post('/api/store/insert', formDataToSend, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    })
    .then(() => {
      // 성공 시 다음 페이지로 이동
      router.push({ name: 'AssetFin' });
    })
    .catch((error) => {
      console.error('데이터 전송 오류:', error);
    });
};

// 페이지가 로드될 때 업종 목록 및 가게 정보 가져오기
onMounted(() => {
  fetchStoreList();
  fetchStoreData();
});
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

.option {
  width: 70.6%;
}
</style>
