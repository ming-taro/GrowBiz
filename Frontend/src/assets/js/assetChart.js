import axios from 'axios';

import { useAuthStore } from '@/stores/auth';
// assets/js/assetChart.js

var id = '1234';

const authStore = useAuthStore();

const mno = authStore.state.mno;

// 도넛 차트 데이터
export let asset_data_doughnut = {
  // 여기서 export 추가
  labels: [],
  datasets: [
    {
      backgroundColor: [
        '#4A90E2',
        '#F5A623',
        '#F8E71C',
        '#7ED321',
        '#9B9B9B',
        '#BD10E0',
        '#9013FE',
      ],
      data: [], // 예시 데이터; 필요에 따라 수정 가능
    },
  ],
};

// 도넛 차트 옵션
export const asset_doughnutoptions = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: {
      display: true,
      position: 'right',
      labels: {
        boxWidth: 8,
        padding: 10,
        usePointStyle: true,
        pointStyle: 'circle',
        font: {
          size: 14,
        },
      },
    },
    tooltip: {
      callbacks: {
        label: function (tooltipItem) {
          const dataset = tooltipItem.dataset;
          const currentValue = dataset.data[tooltipItem.dataIndex];
          const total = dataset.data.reduce((acc, val) => acc + val, 0);
          const percentage = ((currentValue / total) * 100).toFixed(2);
          return `${tooltipItem.label}: ${currentValue} (${percentage}%)`;
        },
      },
    },
    datalabels: {
      formatter: (value, ctx) => {
        const dataset = ctx.chart.data.datasets[0];
        const total = dataset.data.reduce((acc, val) => acc + val, 0);
        const percentage = ((value / total) * 100).toFixed(2);
        return `${percentage}%`; // 데이터와 퍼센트 함께 표시
      },
      color: '#000', // 글자 색상
      font: {
        weight: '',
        size: 12, // 글자 크기
      },
      anchor: '', // 중앙에 위치
      align: 'center', // 중앙 정렬
    },
  },
};

// 혼합 차트 데이터
export let mixed_data = {
  labels: ['Label 1', 'Label 2', 'Label 3', 'Label 4'], // 라벨 설정
  datasets: [
    {
      type: 'bar',
      label: '금일 판매량',
      data: [],
      borderColor: 'rgb(255, 9, 132)',
      backgroundColor: 'rgba(255, 99, 132, 0.2)',
    },
    {
      type: 'bar', // 첫 번째 라인 데이터셋
      label: '일주일 전 판매량',
      data: [],
      fill: false,
      borderColor: 'rgb(54, 162, 235)',
      tension: 0.1, // 선의 곡률 조정
    },
  ],
};

// 혼합 차트 옵션
export const mixed_options = {
  responsive: true,
  scales: {
    y: {
      beginAtZero: true,
      grid: {
        display: false, // y축 가로선(그리드 라인)을 숨김
      },
    },
  },
  plugins: {
    datalabels: {
      display: false, // 막대 위의 숫자를 숨김
    },
    tooltip: {
      enabled: true, // 마우스 오버 시 툴팁은 여전히 표시
    },
  },
};

// 데이터 가져오는 함수
export async function fetchChartData(loanRepaymentStatus) {
  if (mno != '') {
    id = mno;
  }

  let response = await axios.get(`/api/kmap/member/${id}`);

  if (response.data.length == 0) {
    id = '1234';
    response = await axios.get(`/api/kmap/member/${id}`);
  }

  const svcIndutyCdNm = response.data.svcIndutyCdNm;

  const doughnut = await axios.get(`/api/chart/doughnut/${svcIndutyCdNm}`);

  const sortedData = doughnut.data.sort((a, b) => b.amount - a.amount);

  asset_data_doughnut.labels = sortedData.map(
    (item) => `${item.categoryName}: ${item.amount.toLocaleString()}원`
  );
  asset_data_doughnut.datasets[0].data = sortedData.map((item) => item.amount);

  loanRepaymentStatus.value = sortedData
    .reduce((acc, item) => acc + item.amount, 0)
    .toLocaleString();

  const mixchart = await axios.get(`/api/chart/mixchart/${svcIndutyCdNm}`);

  const firstData = [];
  const secondData = [];

  const categorizedData = mixchart.data.reduce((acc, item) => {
    if (!acc[item.category]) {
      acc[item.category] = [];
    }

    if (acc[item.category].length === 0) {
      acc[item.category].push(item);
      firstData.push(item); // 첫 번째 데이터를 firstData에 추가
    } else if (acc[item.category].length === 1) {
      acc[item.category].push(item);
      secondData.push(item); // 두 번째 데이터를 secondData에 추가
    }
    return acc;
  }, {});

  mixed_data.labels = firstData.map((item) => item.categoryName);

  mixed_data.datasets[0].data = secondData.map((item) => item.amount);
  mixed_data.datasets[1].data = firstData.map((item) => item.amount);
}
