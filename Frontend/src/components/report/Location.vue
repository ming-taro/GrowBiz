<template>
  <div>
    <div class="title-sm mt-5 mb-2 title-location">
      <div class="custom-line"></div> <!-- Change here -->
      <span class="title">추천 위치</span>
      <div class="custom-line"></div> <!-- Change here -->
    </div>
    <div class="row">
      <div class="col-7">
        <div id="map" style="height: 400px"></div>
      </div>
      <div class="col-5 d-flex justify-content-center align-content-center">

        <div style="display: flex; flex-direction: column; overflow: auto; height: 400px" class="scrollBar">
          <div v-if="plno_list" class="pl-3 pr-3 pe-5" style="font-size: 20px">
            조회 결과 {{ props.plno_list.length }}건
            <hr />
          </div>

          <div v-for="(plno, index) in props.plno_list" v-bind:key="index" class="pe-5">
            <Property v-bind:plno="plno" :map="map" @property-clicked="handlePropertyClick(plno)" @click="openModal" />
          </div>
        </div>
      </div>
    </div>

    <div v-if="isModalOpen" class="modal fade show" style="display: block;" tabindex="-1"
      aria-labelledby="exampleModalLabel">
      <PropertyDetail :property=property :closeModal=closeModal />
    </div>
  </div>
</template>

<script setup>
import { onMounted, defineProps, ref } from 'vue';
import { findLocationByAddress } from '@/services/simulation/LocationAPI';
import Property from '@/components/report/Property.vue'
import { fetchPropertyById } from '@/services/simulation/PropertyAPI';
import PropertyDetail from '@/components/report/PropertyDetail.vue';

const props = defineProps(["location", "plno_list"]);
const map = ref(null);

const isModalOpen = ref(false);
const selectedPropertyIndex = ref(null);
const property = ref(null);

const openModal = () => {
  isModalOpen.value = true;
};

const closeModal = () => {
  isModalOpen.value = false;
};

const handlePropertyClick = async (plno) => {
  selectedPropertyIndex.value = plno;
  property.value = await fetchPropertyById(plno);
  openModal();
};

const setLocation = async () => {
  const location = props.location ? await findLocationByAddress(props.location) : await findLocationByAddress("광진구 군자동");
  // const location = { y: 37.49606, x: 127.040995 }; // 임시 위치 -> 위의 데이터로 교체 필요
  const script = document.createElement('script');
  script.src = import.meta.env.VITE_KAKAO_API_URL;
  script.onload = () => {
    kakao.maps.load(() => {
      var container = document.getElementById('map');
      var options = {
        center: new kakao.maps.LatLng(location.y, location.x),
        level: 5,
      };

      map.value = new kakao.maps.Map(container, options);
    });
  };
  document.head.appendChild(script);
}

onMounted(async () => {
  await setLocation();
  console.log(props.plno_list);
})
</script>

<style scoped>
.container {
  padding: 0px 80px 15px 80px;
}

.title {
  position: relative;
  font-size: 25px;
  font-weight: bold;
}

.title-location {
  font-weight: 600;
  font-size: larger;

}

.weight {
  font-weight: 100;
}


/* Custom Scrollbar */
.scrollBar::-webkit-scrollbar {
  width: 8px;
  /* Scrollbar width */
}

.scrollBar::-webkit-scrollbar-track {
  background: #f1f1f1;
  /* Track color */
  border-radius: 10px;
  /* Round edges of the track */
}

.scrollBar::-webkit-scrollbar-thumb {
  background: #6184c6;
  /* Scrollbar color */
  border-radius: 10px;
  /* Round edges of the thumb */
}

.scrollBar::-webkit-scrollbar-thumb:hover {
  background: #466AAD;
  /* Darker color on hover */
}

.scrollBar::-moz-scrollbar {
  width: 8px;
  /* Scrollbar width for Firefox */
}

.scrollBar::-moz-scrollbar-track {
  background: #f1f1f1;
  /* Track color for Firefox */
}

.scrollBar::-moz-scrollbar-thumb {
  background: #007bff;
  /* Scrollbar color for Firefox */
  border-radius: 10px;
  /* Round edges of the thumb for Firefox */
}

.scrollBar::-moz-scrollbar-thumb:hover {
  background: #0056b3;
  /* Darker color on hover for Firefox */
}
</style>