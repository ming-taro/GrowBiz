<template>
  <div>
    <InfoPlazaHeader />
    <div class="container">
      <div class="row align-items-center">
        <!-- 헤딩 -->
        <div class="col-md-6">
          <h1
            class="h3 position-relative pb-sm-2 pb-md-3 mb-5"
            style="z-index: 1021"
          >
            Best 인기 업종 - 전체
          </h1>
        </div>

        <!-- 필터링 -->
        <div class="row mb-14">
          <div class="col-1 d-flex justify-content-center align-items-center">
            <button
              class="btn btn-primary p-0 col-6"
              style="font-size: 20px"
              @click="resetFunction"
            >
              <i class="fa-solid fa-rotate-right"></i>
            </button>
          </div>
          <!-- 지역 검색(구) -->
          <div class="col-2">
            <select
              class="form-select round-corner"
              aria-label="Default select example"
              id="signgu-select"
              @change="
                onSignguChange;
                bringDataList;
              "
              ref="signguSelect"
            >
              <option value="전체" hidden>구 선택</option>
              <option value="전체">전체</option>
              <option value="동작구">동작구</option>
              <option value="금천구">금천구</option>
              <option value="용산구">용산구</option>
              <option value="송파구">송파구</option>
              <option value="종로구">종로구</option>
              <option value="동대문구">동대문구</option>
              <option value="서초구">서초구</option>
              <option value="구로구">구로구</option>
              <option value="영등포구">영등포구</option>
              <option value="노원구">노원구</option>
              <option value="중구">중구</option>
              <option value="강남구">강남구</option>
              <option value="강서구">강서구</option>
              <option value="마포구">마포구</option>
              <option value="성동구">성동구</option>
              <option value="양천구">양천구</option>
              <option value="광진구">광진구</option>
              <option value="강동구">강동구</option>
              <option value="서대문구">서대문구</option>
              <option value="강북구">강북구</option>
              <option value="중랑구">중랑구</option>
              <option value="관악구">관악구</option>
              <option value="은평구">은평구</option>
              <option value="도봉구">도봉구</option>
              <option value="성북구">성북구</option>
            </select>
          </div>

          <!-- 지역 검색(동) -->
          <div class="col-md-2">
            <select
              class="form-select round-corner"
              aria-label="Default select example"
              id="adstrd-select"
              :disabled="selectedSigngu === '전체'"
              @change="
                onDongChange;
                bringDataList;
              "
              ref="adstrdSelect"
            >
              <option selected disabled hidden>동 선택</option>
              <option value="전체">전체</option>
              <!-- <option
                v-for="dong in filteredDongs"
                :key="dong.value"
                :value="dong.value"
              >
                {{ dong.label }}
              </option> -->
            </select>
          </div>

          <!-- 서비스 업종 -->
          <div class="col-md-2">
            <select
              class="form-select round-corner"
              aria-label="Default select example"
              @change="
                onServiceChange;
                bringDataList;
              "
            >
              <option selected hidden>서비스 업종</option>
              <option value="전체">전체</option>
              <option value="수산물판매">수산물판매</option>
              <option value="일반의류">일반의류</option>
              <option value="컴퓨터및주변장치판매">컴퓨터및주변장치판매</option>
              <option value="반찬가게">반찬가게</option>
              <option value="시계및귀금속">시계및귀금속</option>
              <option value="가전제품">가전제품</option>
              <option value="청과상">청과상</option>
              <option value="육류판매">육류판매</option>
              <option value="일반의원">일반의원</option>
              <option value="조명용품">조명용품</option>
              <option value="한식음식점">한식음식점</option>
              <option value="운동경기용품">운동경기용품</option>
              <option value="화장품">화장품</option>
              <option value="일반교습학원">일반교습학원</option>
              <option value="의약품">의약품</option>
              <option value="문구">문구</option>
              <option value="커피-음료">커피-음료</option>
              <option value="미곡판매">미곡판매</option>
              <option value="외국어학원">외국어학원</option>
              <option value="슈퍼마켓">슈퍼마켓</option>
              <option value="편의점">편의점</option>
              <option value="치과의원">치과의원</option>
              <option value="의료기기">의료기기</option>
              <option value="양식음식점">양식음식점</option>
              <option value="신발">신발</option>
              <option value="전자상거래업">전자상거래업</option>
              <option value="완구">완구</option>
              <option value="화초">화초</option>
              <option value="호프-간이주점">호프-간이주점</option>
              <option value="일식음식점">일식음식점</option>
              <option value="가구">가구</option>
              <option value="안경">안경</option>
              <option value="가방">가방</option>
              <option value="중식음식점">중식음식점</option>
              <option value="미용실">미용실</option>
              <option value="핸드폰">핸드폰</option>
              <option value="분식전문점">분식전문점</option>
              <option value="제과점">제과점</option>
              <option value="자동차수리">자동차수리</option>
              <option value="피부관리실">피부관리실</option>
              <option value="패스트푸드점">패스트푸드점</option>
              <option value="서적">서적</option>
              <option value="인테리어">인테리어</option>
              <option value="한의원">한의원</option>
              <option value="스포츠 강습">스포츠 강습</option>
              <option value="섬유제품">섬유제품</option>
              <option value="부동산중개업">부동산중개업</option>
              <option value="예술학원">예술학원</option>
              <option value="여관">여관</option>
              <option value="스포츠클럽">스포츠클럽</option>
              <option value="자전거 및 기타운송장비">
                자전거 및 기타운송장비
              </option>
              <option value="노래방">노래방</option>
              <option value="치킨전문점">치킨전문점</option>
              <option value="PC방">PC방</option>
              <option value="철물점">철물점</option>
              <option value="골프연습장">골프연습장</option>
              <option value="자동차미용">자동차미용</option>
              <option value="당구장">당구장</option>
              <option value="세탁소">세탁소</option>
              <option value="애완동물">애완동물</option>
            </select>
          </div>

          <!-- 검색창 -->
          <div class="col-5">
            <div class="position-relative w-100 d-flex justify-content-md-end">
              <input
                type="search"
                class="form-control form-control-lg"
                placeholder="Search for products"
                aria-label="Search"
                style="
                  border: none;
                  border-bottom: 2px solid #ced4da;
                  border-radius: 0;
                "
              />
              <button
                type="button"
                class="btn btn-icon btn-ghost fs-lg text-bo border-0 position-absolute top-0 end-0 rounded-circle mt-1 me-1"
                aria-label="Search button"
              >
                <i class="fa-solid fa-magnifying-glass"></i>
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- 사업 아이템 리스트 -->
      <div class="row">
        <!-- 사업 아이템 리스트 본문 -->
        <div class="table-responsive">
          <table class="table table-hover table-sm table-nowrap">
            <thead>
              <tr>
                <th scope="col">
                  <div class="d-flex align-items-center gap-2 ps-1">
                    <div class="text-base">
                      <div class="form-check">
                        <input class="form-check-input" type="checkbox" />
                      </div>
                    </div>
                    <span>Handler</span>
                  </div>
                </th>
                <th scope="col">Currency</th>
                <th scope="col">Rate</th>
                <th scope="col">Amount</th>
                <th scope="col" class="d-none d-xl-table-cell">Date</th>
                <th scope="col" class="d-none d-xl-table-cell">Status</th>
                <th scope="col" class="d-none d-xl-table-cell">
                  Required Action
                </th>
                <th></th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>
                  <div class="d-flex align-items-center gap-3 ps-1">
                    <div class="text-base">
                      <div class="form-check">
                        <input class="form-check-input" type="checkbox" />
                      </div>
                    </div>
                    <div
                      class="d-none d-xl-inline-flex icon icon-shape w-rem-8 h-rem-8 rounded-circle text-sm bg-secondary bg-opacity-25 text-secondary"
                    >
                      <i class="bi bi-file-fill"></i>
                    </div>
                    <div>
                      <span class="d-block text-heading fw-bold"
                        >Bought BTC</span
                      >
                    </div>
                  </div>
                </td>
                <td class="text-xs">
                  BTC <i class="bi bi-arrow-right mx-2"></i> USDT
                </td>
                <td>1.23</td>
                <td>$1,300,000.00</td>
                <td class="d-none d-xl-table-cell">3 min ago</td>
                <td class="d-none d-xl-table-cell">
                  <span class="badge badge-lg badge-dot">
                    <i class="bg-success"></i>Active
                  </span>
                </td>
                <td class="d-none d-xl-table-cell">Needs your attention</td>
                <td class="text-end">
                  <button
                    type="button"
                    class="btn btn-sm btn-square btn-neutral w-rem-6 h-rem-6"
                  >
                    <i class="bi bi-three-dots"></i>
                  </button>
                </td>
              </tr>
              <tr>
                <td>
                  <div class="d-flex align-items-center gap-3 ps-1">
                    <div class="text-base">
                      <div class="form-check">
                        <input class="form-check-input" type="checkbox" />
                      </div>
                    </div>
                    <div
                      class="d-none d-xl-inline-flex icon icon-shape w-rem-8 h-rem-8 rounded-circle text-sm bg-secondary bg-opacity-25 text-secondary"
                    >
                      <i class="bi bi-file-fill"></i>
                    </div>
                    <div>
                      <span class="d-block text-heading fw-bold">Sold ADA</span>
                    </div>
                  </div>
                </td>
                <td class="text-xs">
                  ADA <i class="bi bi-arrow-right mx-2"></i> USDT
                </td>
                <td>1.23</td>
                <td>$1,300,000.00</td>
                <td class="d-none d-xl-table-cell">3 min ago</td>
                <td class="d-none d-xl-table-cell">
                  <span class="badge badge-lg badge-dot">
                    <i class="bg-success"></i>Active
                  </span>
                </td>
                <td class="d-none d-xl-table-cell">Needs your attention</td>
                <td class="text-end">
                  <button
                    type="button"
                    class="btn btn-sm btn-square btn-neutral w-rem-6 h-rem-6"
                  >
                    <i class="bi bi-three-dots"></i>
                  </button>
                </td>
              </tr>
              <tr>
                <td>
                  <div class="d-flex align-items-center gap-3 ps-1">
                    <div class="text-base">
                      <div class="form-check">
                        <input class="form-check-input" type="checkbox" />
                      </div>
                    </div>
                    <div
                      class="d-none d-xl-inline-flex icon icon-shape w-rem-8 h-rem-8 rounded-circle text-sm bg-secondary bg-opacity-25 text-secondary"
                    >
                      <i class="bi bi-file-fill"></i>
                    </div>
                    <div>
                      <span class="d-block text-heading fw-bold"
                        >Bought XRP</span
                      >
                    </div>
                  </div>
                </td>
                <td class="text-xs">
                  XRP <i class="bi bi-arrow-right mx-2"></i> USDT
                </td>
                <td>1.23</td>
                <td>$1,300,000.00</td>
                <td class="d-none d-xl-table-cell">3 min ago</td>
                <td class="d-none d-xl-table-cell">
                  <span class="badge badge-lg badge-dot">
                    <i class="bg-success"></i>Active
                  </span>
                </td>
                <td class="d-none d-xl-table-cell">Needs your attention</td>
                <td class="text-end">
                  <button
                    type="button"
                    class="btn btn-sm btn-square btn-neutral w-rem-6 h-rem-6"
                  >
                    <i class="bi bi-three-dots"></i>
                  </button>
                </td>
              </tr>
              <tr>
                <td>
                  <div class="d-flex align-items-center gap-3 ps-1">
                    <div class="text-base">
                      <div class="form-check">
                        <input class="form-check-input" type="checkbox" />
                      </div>
                    </div>
                    <div
                      class="d-none d-xl-inline-flex icon icon-shape w-rem-8 h-rem-8 rounded-circle text-sm bg-secondary bg-opacity-25 text-secondary"
                    >
                      <i class="bi bi-file-fill"></i>
                    </div>
                    <div>
                      <span class="d-block text-heading fw-bold"
                        >Robert Fox</span
                      >
                    </div>
                  </div>
                </td>
                <td class="text-xs">
                  BTC <i class="bi bi-arrow-right mx-2"></i> USDT
                </td>
                <td>1.23</td>
                <td>$1,300,000.00</td>
                <td class="d-none d-xl-table-cell">3 min ago</td>
                <td class="d-none d-xl-table-cell">
                  <span class="badge badge-lg badge-dot">
                    <i class="bg-success"></i>Active
                  </span>
                </td>
                <td class="d-none d-xl-table-cell">Needs your attention</td>
                <td class="text-end">
                  <button
                    type="button"
                    class="btn btn-sm btn-square btn-neutral w-rem-6 h-rem-6"
                  >
                    <i class="bi bi-three-dots"></i>
                  </button>
                </td>
              </tr>
              <tr>
                <td>
                  <div class="d-flex align-items-center gap-3 ps-1">
                    <div class="text-base">
                      <div class="form-check">
                        <input class="form-check-input" type="checkbox" />
                      </div>
                    </div>
                    <div
                      class="d-none d-xl-inline-flex icon icon-shape w-rem-8 h-rem-8 rounded-circle text-sm bg-secondary bg-opacity-25 text-secondary"
                    >
                      <i class="bi bi-file-fill"></i>
                    </div>
                    <div>
                      <span class="d-block text-heading fw-bold"
                        >Robert Fox</span
                      >
                    </div>
                  </div>
                </td>
                <td class="text-xs">
                  BTC <i class="bi bi-arrow-right mx-2"></i> USDT
                </td>
                <td>1.23</td>
                <td>$1,300,000.00</td>
                <td class="d-none d-xl-table-cell">3 min ago</td>
                <td class="d-none d-xl-table-cell">
                  <span class="badge badge-lg badge-dot">
                    <i class="bg-success"></i>Active
                  </span>
                </td>
                <td class="d-none d-xl-table-cell">Needs your attention</td>
                <td class="text-end">
                  <button
                    type="button"
                    class="btn btn-sm btn-square btn-neutral w-rem-6 h-rem-6"
                  >
                    <i class="bi bi-three-dots"></i>
                  </button>
                </td>
              </tr>
              <tr>
                <td>
                  <div class="d-flex align-items-center gap-3 ps-1">
                    <div class="text-base">
                      <div class="form-check">
                        <input class="form-check-input" type="checkbox" />
                      </div>
                    </div>
                    <div
                      class="d-none d-xl-inline-flex icon icon-shape w-rem-8 h-rem-8 rounded-circle text-sm bg-secondary bg-opacity-25 text-secondary"
                    >
                      <i class="bi bi-file-fill"></i>
                    </div>
                    <div>
                      <span class="d-block text-heading fw-bold"
                        >Robert Fox</span
                      >
                    </div>
                  </div>
                </td>
                <td class="text-xs">
                  BTC <i class="bi bi-arrow-right mx-2"></i> USDT
                </td>
                <td>1.23</td>
                <td>$1,300,000.00</td>
                <td class="d-none d-xl-table-cell">3 min ago</td>
                <td class="d-none d-xl-table-cell">
                  <span class="badge badge-lg badge-dot">
                    <i class="bg-success"></i>Active
                  </span>
                </td>
                <td class="d-none d-xl-table-cell">Needs your attention</td>
                <td class="text-end">
                  <button
                    type="button"
                    class="btn btn-sm btn-square btn-neutral w-rem-6 h-rem-6"
                  >
                    <i class="bi bi-three-dots"></i>
                  </button>
                </td>
              </tr>
              <tr>
                <td>
                  <div class="d-flex align-items-center gap-3 ps-1">
                    <div class="text-base">
                      <div class="form-check">
                        <input class="form-check-input" type="checkbox" />
                      </div>
                    </div>
                    <div
                      class="d-none d-xl-inline-flex icon icon-shape w-rem-8 h-rem-8 rounded-circle text-sm bg-secondary bg-opacity-25 text-secondary"
                    >
                      <i class="bi bi-file-fill"></i>
                    </div>
                    <div>
                      <span class="d-block text-heading fw-bold"
                        >Robert Fox</span
                      >
                    </div>
                  </div>
                </td>
                <td class="text-xs">
                  BTC <i class="bi bi-arrow-right mx-2"></i> USDT
                </td>
                <td>1.23</td>
                <td>$1,300,000.00</td>
                <td class="d-none d-xl-table-cell">3 min ago</td>
                <td class="d-none d-xl-table-cell">
                  <span class="badge badge-lg badge-dot">
                    <i class="bg-success"></i>Active
                  </span>
                </td>
                <td class="d-none d-xl-table-cell">Needs your attention</td>
                <td class="text-end">
                  <button
                    type="button"
                    class="btn btn-sm btn-square btn-neutral w-rem-6 h-rem-6"
                  >
                    <i class="bi bi-three-dots"></i>
                  </button>
                </td>
              </tr>
              <tr>
                <td>
                  <div class="d-flex align-items-center gap-3 ps-1">
                    <div class="text-base">
                      <div class="form-check">
                        <input class="form-check-input" type="checkbox" />
                      </div>
                    </div>
                    <div
                      class="d-none d-xl-inline-flex icon icon-shape w-rem-8 h-rem-8 rounded-circle text-sm bg-secondary bg-opacity-25 text-secondary"
                    >
                      <i class="bi bi-file-fill"></i>
                    </div>
                    <div>
                      <span class="d-block text-heading fw-bold"
                        >Robert Fox</span
                      >
                    </div>
                  </div>
                </td>
                <td class="text-xs">
                  BTC <i class="bi bi-arrow-right mx-2"></i> USDT
                </td>
                <td>1.23</td>
                <td>$1,300,000.00</td>
                <td class="d-none d-xl-table-cell">3 min ago</td>
                <td class="d-none d-xl-table-cell">
                  <span class="badge badge-lg badge-dot">
                    <i class="bg-success"></i>Active
                  </span>
                </td>
                <td class="d-none d-xl-table-cell">Needs your attention</td>
                <td class="text-end">
                  <button
                    type="button"
                    class="btn btn-sm btn-square btn-neutral w-rem-6 h-rem-6"
                  >
                    <i class="bi bi-three-dots"></i>
                  </button>
                </td>
              </tr>
              <tr>
                <td>
                  <div class="d-flex align-items-center gap-3 ps-1">
                    <div class="text-base">
                      <div class="form-check">
                        <input class="form-check-input" type="checkbox" />
                      </div>
                    </div>
                    <div
                      class="d-none d-xl-inline-flex icon icon-shape w-rem-8 h-rem-8 rounded-circle text-sm bg-secondary bg-opacity-25 text-secondary"
                    >
                      <i class="bi bi-file-fill"></i>
                    </div>
                    <div>
                      <span class="d-block text-heading fw-bold"
                        >Robert Fox</span
                      >
                    </div>
                  </div>
                </td>
                <td class="text-xs">
                  BTC <i class="bi bi-arrow-right mx-2"></i> USDT
                </td>
                <td>1.23</td>
                <td>$1,300,000.00</td>
                <td class="d-none d-xl-table-cell">3 min ago</td>
                <td class="d-none d-xl-table-cell">
                  <span class="badge badge-lg badge-dot">
                    <i class="bg-success"></i>Active
                  </span>
                </td>
                <td class="d-none d-xl-table-cell">Needs your attention</td>
                <td class="text-end">
                  <button
                    type="button"
                    class="btn btn-sm btn-square btn-neutral w-rem-6 h-rem-6"
                  >
                    <i class="bi bi-three-dots"></i>
                  </button>
                </td>
              </tr>
              <tr>
                <td>
                  <div class="d-flex align-items-center gap-3 ps-1">
                    <div class="text-base">
                      <div class="form-check">
                        <input class="form-check-input" type="checkbox" />
                      </div>
                    </div>
                    <div
                      class="d-none d-xl-inline-flex icon icon-shape w-rem-8 h-rem-8 rounded-circle text-sm bg-secondary bg-opacity-25 text-secondary"
                    >
                      <i class="bi bi-file-fill"></i>
                    </div>
                    <div>
                      <span class="d-block text-heading fw-bold"
                        >Robert Fox</span
                      >
                    </div>
                  </div>
                </td>
                <td class="text-xs">
                  BTC <i class="bi bi-arrow-right mx-2"></i> USDT
                </td>
                <td>1.23</td>
                <td>$1,300,000.00</td>
                <td class="d-none d-xl-table-cell">3 min ago</td>
                <td class="d-none d-xl-table-cell">
                  <span class="badge badge-lg badge-dot">
                    <i class="bg-success"></i>Active
                  </span>
                </td>
                <td class="d-none d-xl-table-cell">Needs your attention</td>
                <td class="text-end">
                  <button
                    type="button"
                    class="btn btn-sm btn-square btn-neutral w-rem-6 h-rem-6"
                  >
                    <i class="bi bi-three-dots"></i>
                  </button>
                </td>
              </tr>
              <tr>
                <td>
                  <div class="d-flex align-items-center gap-3 ps-1">
                    <div class="text-base">
                      <div class="form-check">
                        <input class="form-check-input" type="checkbox" />
                      </div>
                    </div>
                    <div
                      class="d-none d-xl-inline-flex icon icon-shape w-rem-8 h-rem-8 rounded-circle text-sm bg-secondary bg-opacity-25 text-secondary"
                    >
                      <i class="bi bi-file-fill"></i>
                    </div>
                    <div>
                      <span class="d-block text-heading fw-bold"
                        >Robert Fox</span
                      >
                    </div>
                  </div>
                </td>
                <td class="text-xs">
                  BTC <i class="bi bi-arrow-right mx-2"></i> USDT
                </td>
                <td>1.23</td>
                <td>$1,300,000.00</td>
                <td class="d-none d-xl-table-cell">3 min ago</td>
                <td class="d-none d-xl-table-cell">
                  <span class="badge badge-lg badge-dot">
                    <i class="bg-success"></i>Active
                  </span>
                </td>
                <td class="d-none d-xl-table-cell">Needs your attention</td>
                <td class="text-end">
                  <button
                    type="button"
                    class="btn btn-sm btn-square btn-neutral w-rem-6 h-rem-6"
                  >
                    <i class="bi bi-three-dots"></i>
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        <!-- 페이지네이션 -->
        <div class="py-4 px-6">
          <div class="row align-items-center justify-content-between">
            <div class="col-md-6 d-none d-md-block">
              <span class="text-muted text-sm"
                >Showing 10 items out of 250 results found</span
              >
            </div>
            <div class="col-md-auto">
              <nav aria-label="Page navigation example">
                <ul class="pagination pagination-spaced gap-1">
                  <li class="page-item">
                    <a class="page-link" href="#">
                      <i class="bi bi-chevron-left"></i>
                    </a>
                  </li>
                  <li class="page-item"><a class="page-link" href="#">1</a></li>
                  <li class="page-item"><a class="page-link" href="#">2</a></li>
                  <li class="page-item"><a class="page-link" href="#">3</a></li>
                  <li class="page-item"><a class="page-link" href="#">4</a></li>
                  <li class="page-item"><a class="page-link" href="#">5</a></li>
                  <li class="page-item">
                    <a class="page-link" href="#">
                      <i class="bi bi-chevron-right"></i>
                    </a>
                  </li>
                </ul>
              </nav>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import InfoPlazaHeader from '@/components/infoplaza/InfoPlazaHeader.vue';
import { ref, computed } from 'vue';
import axios from 'axios';

// '구' 필터링 변수
const selectedSigngu = ref('전체');
const selectedDong = ref('전체');
const selectedService = ref('전체');

const BASEURI = '/api/infoPlaza/businessItem';

// 필터링된 전체 데이터 리스트
const dataList = ref([]);

// 데이터 리스트 가져오는 함수
const bringDataList = async () => {
  try {
    // Best 인기 업종 - 전체
    const response = await axios.get(BASEURI + '/getFilteredList', {
      params: {
        gu: selectedSigngu.value,
        dong: selectedDong.value,
        service: selectedService.value,
      }, // 선택된 필터링 값을 쿼리 파라미터로 전송
    });
    if (response.status === 200) {
      dataList.value = response.data;
      console.log(dataList.value);
    } else {
      console.log('데이터 조회 실패');
    }
  } catch (error) {
    console.log('에러발생 :' + error);
  }
};
// // Computed property to filter '동' based on selected '구'
// const filteredDongs = computed(() => {
//   return selectedSigngu.value === 'all'
//     ? []
//     : dongs.filter((dong) => dong.signguId === selectedSigngu.value);
// });

// '구' 필터링 시, '구' 값 저장
const onSignguChange = (event) => {
  selectedSigngu.value = event.target.value;
};

// '동' 필터링 시, '동' 값 저장
const onDongChange = (event) => {
  selectedDong.value = event.target.value;
};

// '동' 필터링 시, '동' 값 저장
const onServiceChange = (event) => {
  selectedService.value = event.target.value;
};

bringDataList();
</script>

<style scoped>
.round-corner {
  border-radius: 20px;
}
</style>
