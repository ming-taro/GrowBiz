import axios from 'axios';

// assets/js/assetChart.js

const id = '1234';

// 도넛 차트 데이터
export let asset_data_doughnut = {
  // 여기서 export 추가
  labels: [],
  datasets: [
    {
      backgroundColor: ['#f6f4f9', '#fca3b9'],
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
        weight: 'bold',
        size: 14, // 글자 크기
      },
      anchor: 'center', // 중앙에 위치
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
      label: 'Bar Dataset',
      data: [10, 20, 30, 30],
      borderColor: 'rgb(255, 9, 132)',
      backgroundColor: 'rgba(255, 99, 132, 0.2)',
    },
    {
      type: 'line', // 첫 번째 라인 데이터셋
      label: 'Line Dataset 1',
      data: [10, 20, 22, 30],
      fill: false,
      borderColor: 'rgb(54, 162, 235)',
      tension: 0.1, // 선의 곡률 조정
    },
    {
      type: 'line', // 두 번째 라인 데이터셋
      label: 'Line Dataset 2',
      data: [15, 25, 20, 28], // 두 번째 라인 데이터
      fill: false,
      borderColor: 'rgb(255, 206, 86)', // 다른 색상
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
    },
  },
};

// 데이터 가져오는 함수
export async function fetchChartData(loanRepaymentStatus) {
  const response = await axios.get(`/api/kmap/member/${id}`);
  const adstrdCdNm = response.data.addressname;
  const dongname = response.data.dongname;

  const flpop = await axios.get(`/api/chart/doughnut/${adstrdCdNm}`);

  // flpop.data.mlFlpopCo 값을 대출 상환 현황에 설정
  loanRepaymentStatus.value = flpop.data.totFlpopCo; // 이 값을 대출 상환 현황에 반영

  // 가져온 데이터에서 labels 업데이트
  asset_data_doughnut.labels = [
    '남성: ' + flpop.data.mlFlpopCo,
    '여성: ' + flpop.data.fmlFlpopCo,
  ];
  asset_data_doughnut.datasets[0].data = [
    flpop.data.mlFlpopCo, // 남성 인구 수
    flpop.data.fmlFlpopCo, // 여성 인구 수
  ]; // addressname으로 도넛 차트 레이블 업데이트

  mixed_data.labels = dongname.split(', ').map((dong) => dong.trim());
}
