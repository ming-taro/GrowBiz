// 위에 그래프 업종 밀도 평균, 업종 평균 가맹비, 업종 인테리어 총 비용
import ChartDataLabels from 'chartjs-plugin-datalabels';

  
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
          callback: function(value) {
            return ''; // 아래 단위 제거
          },
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
          display: true,
          position: 'top',
        },
        datalabels: {
          display: true,
          anchor: 'end',
          align: 'end',
          color: '#000',
          formatter: (value) => {
            // 음수 값을 양수로 표시
            return Math.abs(value); // 데이터 값을 양수로 표시
          },
        },
    },
    elements: {
        bar: {
          // 막대의 두께를 설정
          barThickness: 50, // 막대의 두께 (픽셀 단위)
        },
      },
  };
  
    