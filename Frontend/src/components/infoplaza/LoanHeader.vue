<template>
  <ul
    class="nav nav-tabs custom justify-content-center"
    id="myTab"
    role="tablist"
  >
    <li class="nav-item">
      <RouterLink class="nav-link active" to="/infoPlaza/personalCreditLoan"
        ><h4>개인신용</h4></RouterLink
      >
    </li>
    <li class="nav-item">
      <RouterLink class="nav-link" to="/infoPlaza/jeonseLoan"
        ><h4>전세자금</h4></RouterLink
      >
    </li>
    <li class="nav-item">
      <RouterLink class="nav-link" to="/infoPlaza/mortgageLoan"
        ><h4>주택담보</h4></RouterLink
      >
    </li>
    <li class="nav-item">
      <RouterLink class="nav-link" to="/infoPlaza/governmentFund"
        ><h4>정책자금</h4></RouterLink
      >
    </li>
    <li class="nav-item">
      <RouterLink class="nav-link" to="/infoPlaza/KBLoan"
        ><h4>국민은행</h4></RouterLink
      >
    </li>
  </ul>
</template>

<style scoped>
/* nav 아래 hr 같은 선 제거 */
.nav {
  border-bottom: none !important;
}

/* li 간격을 늘리기 위한 스타일 */
.nav-item {
  margin: 0 30px; /* li 요소 간의 좌우 간격을 15px로 설정 */
}
/* 활성화된 탭 스타일 */
.nav-link.active {
  background-color: transparent !important; /* 배경 투명 */
  border-bottom: 2px solid #007bff !important; /* 파란색 밑줄 */
  border-radius: 0 !important; /* 테두리 둥글게 하지 않음 */
  border-width: 0;
}

.nav-link.active h4 {
  color: #0056b3 !important; /* 파란색 텍스트 */
}

/* 비활성화된 탭 스타일 */
.nav-link {
  color: #555 !important; /* 약간 어두운 회색 텍스트 */
  border-width: 0;
}

.nav-link:hover h4 {
  color: #007bff !important; /* 호버 시 파란색 */
  text-decoration: none !important; /* 호버 시 밑줄 제거 */
}
</style>
