// 위에 그래프 업종 밀도 평균, 업종 평균 가맹비, 업종 인테리어 총 비용
export const data_bar = {
    labels: ['Category 1', 'Category 2', 'Category 3'],
    datasets: [
      {
        label: '업종 평균',
        backgroundColor: '#42a5f5',
        data: [-20, -30, -40], // 음수 값으로 설정하여 왼쪽으로 그려지도록 설정
      },
      {
        label: '추천 브랜드 평균',
        backgroundColor: '#ff7043',
        data: [20, 30, 40], // 양수 값으로 설정하여 오른쪽으로 그려지도록 설정
      },
    ],
  };
  
  export const barOptions = {
    responsive: true,
    maintainAspectRatio: false,
    indexAxis: 'y', // 가로 막대 그래프 설정
    scales: {
      x: {
        grid: {
          color: 'rgba(255, 255, 255, 0.3)',
          lineWidth: 1,
        },
        ticks: {
          beginAtZero: true, // x축이 0에서 시작되도록 설정
        },
      },
      y: {
        grid: {
          color: 'rgba(255, 255, 255, 0.3)',
          lineWidth: 1,
        },
      },
    },
    plugins: {
      legend: {
        display: true, // 레전드 표시
        position: 'top', // 레전드 위치 설정 (top, bottom, left, right)
      },
    },
  };
  
    