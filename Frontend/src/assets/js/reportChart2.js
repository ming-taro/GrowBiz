
// 밑에 그래프 개업률, 폐업률
export const data_bar2 = (data) => ({
  labels: ['개업률', '폐업률'],
  datasets: [
    {
      label: '업종 평균',
      backgroundColor: '#42a5f5',
      data: [
        data.industry_opening_rate_average, // 업종 평균 개업률
        data.industry_closing_rate_average, // 업종 평균 폐업률 recommended_brand_opening_rate_average

      ],
    },
    {
      label: '추천 브랜드',
      backgroundColor: '#ff7043',
      data: [
        data.recommended_brand_opening_rate_average, // 추천 브랜드 개업률
        data.recommended_brand_closing_rate_average, // 추천 브랜드 폐업률
      ],
    },
  ],
});

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