<template>
  <div>
    <InfoPlazaHeader />
    <div class="container mw-screen-xl">
      <form class="form-horizontal card">
        <div class="col-12 d-flex justify-content-center mt-4">
          <h4>검색 옵션</h4>
        </div>
        <div class="row m-3">
          <!-- 사업주기별 -->
          <label for="inputEmail3" class="col-2 col-form-label"
            >사업주기별</label
          >
          <div class="col-9">
            <div class="mt-2">
              <div class="form-check form-check-inline">
                <input
                  type="checkbox"
                  class="form-check-input"
                  id="cycleCheck1"
                  onclick="toggleAll(this)"
                />
                <label class="form-check-label" for="cycleCheck1">전체</label>
              </div>
              <div class="form-check form-check-inline">
                <input
                  type="checkbox"
                  class="form-check-input"
                  id="cycleCheck2"
                />
                <label class="form-check-label" for="cycleCheck2">창업</label>
              </div>
              <div class="form-check form-check-inline">
                <input
                  type="checkbox"
                  class="form-check-input"
                  id="cycleCheck3"
                />
                <label class="form-check-label" for="cycleCheck3">성장</label>
              </div>
              <div class="form-check form-check-inline">
                <input
                  type="checkbox"
                  class="form-check-input"
                  id="cycleCheck4"
                />
                <label class="form-check-label" for="cycleCheck4"
                  >폐업, 재기</label
                >
              </div>
            </div>
          </div>

          <!-- 업종별 -->
          <label for="inputEmail3" class="col-2 col-form-label">업종별</label>
          <div class="col-9">
            <div class="mt-2">
              <div class="form-check form-check-inline">
                <input
                  type="checkbox"
                  class="form-check-input"
                  id="industryCheck1"
                />
                <label class="form-check-label" for="industryCheck1"
                  >전체</label
                >
              </div>
              <div class="form-check form-check-inline">
                <input
                  type="checkbox"
                  class="form-check-input"
                  id="industryCheck2"
                />
                <label class="form-check-label" for="industryCheck2"
                  >업종무관</label
                >
              </div>
              <div class="form-check form-check-inline">
                <input
                  type="checkbox"
                  class="form-check-input"
                  id="industryCheck3"
                />
                <label class="form-check-label" for="industryCheck3"
                  >제조업</label
                >
              </div>
              <div class="form-check form-check-inline">
                <input
                  type="checkbox"
                  class="form-check-input"
                  id="industryCheck4"
                />
                <label class="form-check-label" for="industryCheck4"
                  >도소매업</label
                >
              </div>
              <div class="form-check form-check-inline">
                <input
                  type="checkbox"
                  class="form-check-input"
                  id="industryCheck5"
                />
                <label class="form-check-label" for="industryCheck5"
                  >음식점업</label
                >
              </div>
              <div class="form-check form-check-inline">
                <input
                  type="checkbox"
                  class="form-check-input"
                  id="industryCheck6"
                />
                <label class="form-check-label" for="industryCheck6"
                  >서비스업</label
                >
              </div>
              <div class="form-check form-check-inline">
                <input
                  type="checkbox"
                  class="form-check-input"
                  id="industryCheck7"
                />
                <label class="form-check-label" for="industryCheck7"
                  >숙박업</label
                >
              </div>
            </div>
          </div>

          <!-- 과목별 -->
          <label for="inputEmail3" class="col-2 col-form-label">과목별</label>
          <div class="col-9">
            <div class="mt-2">
              <div class="form-check form-check-inline">
                <input
                  type="checkbox"
                  class="form-check-input"
                  id="subjectCheck1"
                />
                <label class="form-check-label" for="subjectCheck1">전체</label>
              </div>
              <div class="form-check form-check-inline">
                <input
                  type="checkbox"
                  class="form-check-input"
                  id="subjectCheck2"
                />
                <label class="form-check-label" for="subjectCheck2"
                  >마케팅</label
                >
              </div>
              <div class="form-check form-check-inline">
                <input
                  type="checkbox"
                  class="form-check-input"
                  id="subjectCheck3"
                />
                <label class="form-check-label" for="subjectCheck3"
                  >사업장 운영</label
                >
              </div>
              <div class="form-check form-check-inline">
                <input
                  type="checkbox"
                  class="form-check-input"
                  id="subjectCheck4"
                />
                <label class="form-check-label" for="subjectCheck4"
                  >노무&세무&법</label
                >
              </div>
              <div class="form-check form-check-inline">
                <input
                  type="checkbox"
                  class="form-check-input"
                  id="subjectCheck5"
                />
                <label class="form-check-label" for="subjectCheck5"
                  >수출입</label
                >
              </div>
              <div class="form-check form-check-inline">
                <input
                  type="checkbox"
                  class="form-check-input"
                  id="subjectCheck6"
                />
                <label class="form-check-label" for="subjectCheck6"
                  >지원사업</label
                >
              </div>
              <div class="form-check form-check-inline">
                <input
                  type="checkbox"
                  class="form-check-input"
                  id="subjectCheck7"
                />
                <label class="form-check-label" for="subjectCheck7"
                  >기업가정신</label
                >
              </div>
              <div class="form-check form-check-inline">
                <input
                  type="checkbox"
                  class="form-check-input"
                  id="subjectCheck8"
                />
                <label class="form-check-label" for="subjectCheck8">교양</label>
              </div>
            </div>
          </div>
          <label for="inputEmail3" class="col-2 col-form-label"
            >키워드 검색</label
          >

          <div class="col-9">
            <div class="mt-2">
              <form class="form-group">
                <div class="input-group input-group-sm">
                  <div class="btn-group dropdown">
                    <select
                      class="form-select"
                      aria-label="Default select example"
                    >
                      <option selected>전체</option>
                      <option value="1">과정명</option>
                      <option value="2">내용</option>
                      <option value="3">해시태그</option>
                      <option value="3">강사명</option>
                    </select>
                  </div>
                  <input
                    type="text"
                    class="form-control ms-1 rounded"
                    placeholder="검색어를 입력해 주세요."
                  />
                </div>
              </form>
            </div>
          </div>
          <div class="col-12 d-flex justify-content-center mt-4">
            <button type="submit" class="btn btn-primary mb-4">검색하기</button>
          </div>
        </div>
      </form>

      <div class="cards">
        <h3 class="mb-5" style="font-weight: 600">영상 목록</h3>
        <!-- Row to contain 4 cards in a single row -->
        <div class="row">
          <div
            class="col-3"
            v-for="(item, index) in paginatedList"
            :key="item.vno"
          >
            <div class="card" style="cursor: pointer">
              <img
                :src="item.thumbnail"
                class="card-img-top"
                alt="Card image"
              />
              <div class="card-body">
                <h5 class="card-title">{{ item.title }}</h5>

                <div class="d-flex align-items-center">
                  <button @click="openVideoPopup(item.videoUrl)" class="btn btn-sm btn-primary mt-2">시청하기</button>
                  <router-link
                    :to="`/infoplaza/education/video/${item.vno}`"
                    class="btn btn-sm btn-primary mt-2 ms-2"
                    >상세보기</router-link
                  >
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="d-flex justify-content-center mt-4">
          <button
            class="btn btn-secondary"
            @click="prevPage"
            :disabled="currentPage === 1"
          >
            이전
          </button>
          <span class="mx-2">Page {{ currentPage }}</span>
          <button
            class="btn btn-secondary"
            @click="nextPage"
            :disabled="currentPage === totalPages"
          >
            다음
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import InfoPlazaHeader from "@/components/infoplaza/InfoPlazaHeader.vue";
import axios from "axios";
import { ref, computed, onMounted } from "vue";

// // 개별 체크박스 상태 관리
// const checkAll = ref(false);
// const checkboxes = ref({
//   창업: false,
//   성장: false,
//   "폐업, 재기": false,
// });

// // 체크박스 토글 함수
// function toggleAll(source) {
//   checkAll.value = source.checked;
//   Object.keys(checkboxes.value).forEach((key) => {
//     checkboxes.value[key] = checkAll.value;
//   });
// }

// // 개별 체크박스가 변경될 때 '전체' 체크박스 상태도 업데이트
// function toggleIndividual() {
//   checkAll.value = Object.values(checkboxes.value).every((value) => value);
// }

const BASEURI = "/infoPlaza/education";
const totalList = ref([]); // 전체 데이터를 저장할 리스트
const currentPage = ref(1); // 현재 페이지 번호
const itemsPerPage = ref(12); // 한 페이지에 보여줄 데이터 개수

// 페이지에 맞는 데이터를 계산하는 computed
const paginatedList = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage.value;
  const end = start + itemsPerPage.value;
  return totalList.value.slice(start, end);
});

// 초기 화면 렌더링 시 불러올 초기 데이터 불러오기
const fetchList = async () => {
  try {
    console.log("TRYING......");
    // 전체 데이터 불러오기
    const response = await axios.get(
      "http://localhost:8080/api/infoPlaza/education/list"
    );
    if (response.status === 200) {
      console.log("데이터 조회 시작");
      totalList.value = response.data; // 조회된 데이터를 totalList에 저장
      console.log(totalList.value);
    } else {
      alert("데이터 조회 실패");
    }
  } catch (error) {
    alert("에러발생 :" + error);
  }
};
function openVideoPopup(videoUrl) {
  if (videoUrl) {
    window.open(videoUrl, "_blank", "width=800,height=600");
  } else {
    alert("비디오 URL이 없습니다.");
  }
}

// 총 페이지 수 계산
const totalPages = computed(() => {
  return Math.ceil(totalList.value.length / itemsPerPage.value);
});

// 다음 페이지로 이동
const nextPage = () => {
  if (currentPage.value < totalPages.value) {
    currentPage.value++;
  }
};

// 이전 페이지로 이동
const prevPage = () => {
  if (currentPage.value > 1) {
    currentPage.value--;
  }
};

// 페이지 로딩 시 데이터 호출
onMounted(() => {
  fetchList();
});
</script>

<style scoped>
.form-horizontal {
  margin: 20px;
}
.cards {
  margin: 60px 0px;
}
.container {
  padding: 0px 80px 0px 80px;
}
.col-form-label {
  font-weight: 500;
}
</style>
