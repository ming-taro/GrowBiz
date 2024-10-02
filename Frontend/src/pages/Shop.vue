<template>
  <div>
    <h1>로컬 서버에서 가져온 데이터</h1>
    <div v-if="data">{{ data }}</div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      data: null,
    };
  },
  mounted() {
    this.fetchData();
  },
  methods: {
    async fetchData() {
      try {
        const response = await axios.get('/api/board');
        this.data = response.data;
      } catch (error) {
        console.error('Error fetching data from local server:', error);
      }
    },
  },
};
</script>
