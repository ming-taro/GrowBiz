<template>
  <div v-if="property != null" class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">상세 정보</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"
          @click="handleClose"></button>
      </div>
      <div class="modal-body content">
        <div class="title">
          {{ property.atclSfeCn }}
        </div>
        <div class="mainblue price fw-bolder">
          {{ property.dealKindCdNm }} | {{ formatPrice(property.bscTnthWuntAmt) }} | {{
            formatPrice(property.addTnthWuntAmt) }}
        </div>
        <div class="property-image">
          <img :src="property.imageData ? property.imageData : defaultImage" alt=""
            style="width: 100%; height: 100%; object-fit: cover;" />
        </div>

        <div class="property-info">
          <div class="info-row">
            <div class="info-label">주소</div>
            <div class="info-value">{{ property.addr || "-" }}</div>
          </div>
          <div class="info-row">
            <div class="info-label">공급/전용면적</div>
            <div class="info-value">{{ property.area1 || "-" }} / {{ property.area2 || "-" }}㎡</div>
          </div>
          <div class="info-row">
            <div class="info-label">층</div>
            <div class="info-value">1층</div>
          </div>
          <div class="info-row">
            <div class="info-label">방향</div>
            <div class="info-value">{{ property.drcCd || "-" }}</div>
          </div>

          <div class="info-row">
            <div class="info-label">관리비</div>
            <div class="info-value">{{ formatManagementFee(property.mmMcost) || "-" }}</div>
          </div>

          <div class="info-row">
            <div class="info-label">난방 정보</div>
            <div class="info-value">{{ String(property.heatingInfo) !== 'null' ? property.heatingInfo : "-" }}</div>
          </div>

          <div class="info-row">
            <div class="info-label">건축물 용도</div>
            <div class="info-value">{{ property.bldUsageCd || "-" }}</div>
          </div>

          <div class="info-row">
            <div class="info-label">총 주차대수</div>
            <div class="info-value">{{ property.parkCcnt || "-" }} 대</div>
          </div>

          <div class="info-row">
            <div class="info-label">상세 설명</div>
            <div class="info-value">{{ property.dtlDesc || "-" }}</div>
          </div>
        </div>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-primary" data-bs-dismiss="modal" @click="handleClose">닫기</button>
      </div>
    </div>
  </div>
</template>
<script setup>
import { onMounted, defineProps, ref } from 'vue';
import defaultImage from '@/assets/img/report/default-property.jpg';

const property = ref(null);
const props = defineProps(['property', 'closeModal']);

const handleClose = () => {
  props.closeModal();
};

const formatManagementFee = (amount) => {
  const formattedAmount = new Intl.NumberFormat().format(amount);  // 천 단위 구분
  return `월 ${formattedAmount}원`;
}

const formatPrice = (value) => {
  if (value >= 10000) {
    const eok = Math.floor(value / 10000);
    const man = value % 10000;

    if (man === 0) {
      return eok.toLocaleString() + '억';
    } else {
      return eok.toLocaleString() + '억 ' + man.toLocaleString() + '만원';
    }
  } else {
    return value.toLocaleString() + '만원';
  }
}

onMounted(() => {
  property.value = props.property;
})
</script>
<style scoped>
.modal-content {
  height: 90vh;
}

.content {
  max-height: 80%;
  overflow-y: auto;
}

.title {
  font-size: 20px;
  padding: 10px;
}

.property-image {
  width: 100%;
  height: auto;
  border-radius: 10px;
  padding: 10px;
  box-sizing: border-box;
  overflow: hidden;
}

.price {
  font-size: 20px;
  padding: 10px;
}

.mainblue {
  color: #6184c6;
}

.property-info {
  display: flex;
  flex-direction: column;
  gap: 10px;
  /* 각 줄 사이의 간격 */
  padding: 10px;
  font-size: 16px;
}

.info-row {
  display: flex;
  justify-content: space-between;
  /* 좌우 정렬 */
  align-items: center;
  /* 수직 정렬 */
}

.info-label {
  font-weight: bold;
  width: 120px;
  /* 라벨의 고정 너비 */
  white-space: nowrap;
}

.info-value {
  flex: 1;
  /* 값이 라벨 옆에서 자동 확장됨 */
  text-align: left;
}
</style>