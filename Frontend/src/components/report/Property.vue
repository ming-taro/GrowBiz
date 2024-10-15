<template lang="">
  <div
    class="d-flex justify-content-between m-3 align-items-stretch"
    v-if="property != null"
    style="cursor: pointer;"
    @click="clickDetail"
  >
  <!-- @click="moveMapCenter" -->
    <!-- 왼쪽 텍스트 -->
    <div
      style="width: 60%; height: 100%"
    >
      <div class="title fw-semibold">
        {{ property.atclSfeCn }}
      </div>
      <div class="mainblue price fw-bolder">
        {{ property.dealKindCdNm }} | {{ formatPrice(property.bscTnthWuntAmt) }} | {{ formatPrice(property.addTnthWuntAmt) }}
      </div>
      <div style="font-weight: 300">
        {{ property.area1 }}㎡ / {{ property.area2 }}㎡
      </div>
      <div style="font-weight: 300">
        {{ property.mdiatBzestNm }}
      </div>
    </div>

    <!-- 오른쪽 이미지 -->
    <div style="width: 30%; height: 100%; border-radius: 10px; overflow: hidden;">
      <img
        :src="property.imageData ? property.imageData : defaultImage"
        alt=""
        style="width: 100%; height: 100%; object-fit: cover;"
      />
    </div>
  </div>
  <hr v-if="property != null" style="border: 1px solid #ccc; margin-top: 10px;"/>
</template>

<script setup>
import { onMounted, defineProps, defineEmits, ref } from 'vue';
import { fetchPropertyById } from '@/services/simulation/PropertyAPI';
import defaultImage from '@/assets/img/report/default-property.jpg';

const props = defineProps(["plno", "map"]);
const property = ref(null);
const emit = defineEmits(['property-clicked']);

const clickDetail = () => {
  moveMapCenter();
  emit('property-clicked', props.plno);  // 클릭한 plno를 부모로 전달
};

const moveMapCenter = () => {
  const newLatLng = new kakao.maps.LatLng(property.value.laCrd, property.value.loCrd);
  props.map.setCenter(newLatLng);
}

const setMarker = (lat, lon) => {
  // var imageSrc = "https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/markerStar.png"; 
  var imageSrc = new URL('@/assets/img/report/map-marker.png', import.meta.url).href
  var imageSize = new kakao.maps.Size(40, 40);
  var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize);

  var marker = new kakao.maps.Marker({
    map: props.map,
    position: new kakao.maps.LatLng(lat, lon),
    image: markerImage
  });
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

onMounted(async () => {
  property.value = await fetchPropertyById(props.plno);
  setMarker(property.value.laCrd, property.value.loCrd);
})
</script>
<style scoped>
.title {
  font-size: 15px;
  white-space: nowrap;
  /* 줄 바꿈 없이 한 줄로 표시 */
  overflow: hidden;
  /* 넘치는 텍스트 숨기기 */
  text-overflow: ellipsis;
  /* 넘치는 부분을 "..."으로 표시 */
  max-width: 100%;
  /* 너비 제한 */
}

.price {
  font-size: 20px;
}

.mainblue {
  color: #6184c6;
}
</style>