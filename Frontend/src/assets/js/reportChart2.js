
// 밑에 그래프 개업률, 폐업률
export const data_bar2 = {
  labels: ['Category A', 'Category B'],
  datasets: [
    {
      label: 'Data Set 1',
      backgroundColor: '#42a5f5',
      data: [30, 50], // Category A와 B에 대한 값
    },
    {
      label: 'Data Set 2',
      backgroundColor: '#ff7043',
      data: [20, 40], // Category A와 B에 대한 값
    },
  ],
};

export const barOptions2 = {
  responsive: true,
  maintainAspectRatio: false,
  scales: {
    x: {
      grid: {
        color: 'rgba(255, 255, 255, 0.3)',
        lineWidth: 1,
      },
      ticks: {
        display: true,
        autoSkip: true,
        maxRotation: 0,
        minRotation: 0,
        padding: 10,
      },
    },
    y: {
      beginAtZero: true,
      grid: {
        color: 'rgba(255, 255, 255, 0.3)',
        lineWidth: 1,
      },
    },
  },
  plugins: {
    legend: {
      display: true,
      position: 'top',
    },
  },
};
