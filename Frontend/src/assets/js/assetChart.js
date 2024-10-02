// assets/js/assetChart.js

// 도넛 차트 데이터
export const asset_data_doughnut = {
  labels: ['대출금', '상환금'],
  datasets: [
    {
      backgroundColor: ['#f6f4f9', '#fca3b9'],
      data: [40, 20],
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
      position: 'right', // 레전드가 왼쪽에 배치되도록 설정
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
  },
};

// 혼합 차트 데이터
export const mixed_data = {
  labels: ['January', 'February', 'March', 'April'],
  datasets: [
    {
      type: 'bar',
      label: 'Bar Dataset',
      data: [10, 20, 30, 30],
      borderColor: 'rgb(255, 9, 132)',
      backgroundColor: 'rgba(255, 99, 132, 0.2)',
    },
    {
      type: 'line',
      label: 'Line Dataset',
      data: [10, 20, 22, 30],
      fill: false,
      borderColor: 'rgb(54, 162, 235)',
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
