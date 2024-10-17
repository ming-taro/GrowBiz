// 밑에 그래프 개업률, 폐업률
export const data_bar2 = (data) => ({
  labels: ["개업률", "폐업률"],
  datasets: [
    {
      label: "업종 평균",
      backgroundColor: "#fca3b9",
      data: [
        data.industry_opening_rate_average.toFixed(2), // 업종 평균 개업률
        data.industry_closing_rate_average.toFixed(2), // 업종 평균 폐업률
      ],
    },
    {
      label: "추천 브랜드 평균",
      backgroundColor: "#fcd752",
      data: [
        parseFloat(
          data.recommended_brand_opening_rate_average.replace("%", "")
        ), // 추천 브랜드 개업률
        parseFloat(
          data.recommended_brand_closing_rate_average.replace("%", "")
        ), // 추천 브랜드 폐업률
      ],
    },
  ],
});

export const barOptions2 = {
  responsive: true,
  maintainAspectRatio: false,
  layout: {
    padding: {
      left: 20, // 왼쪽 여백 추가
      right: 20,
      top: 20,
      bottom: 20,
    },
  },
  scales: {
    x: {
      grid: {
        color: "rgba(255, 255, 255, 0.3)",
        lineWidth: 1,
      },
      ticks: {
        display: true,
        autoSkip: true,
        maxRotation: 0,
        minRotation: 0,
        padding: 25,
        font: {
          size: 14, // x축 글자 크기
          family: "Pretendard", // 원하는 폰트 패밀리
          weight: "bold", // 글자 두께
        },
      },
    },
    y: {
      beginAtZero: true,
      grid: {
        color: "rgba(255, 255, 255, 0.3)",
        lineWidth: 1,
      },
      ticks: {
        font: {
          size: 16, // y축 글자 크기
          family: "Pretendard", // 원하는 폰트 패밀리
          weight: "light", // 글자 두께
        },
      },
    },
  },
  plugins: {
    legend: {
      display: true,
      position: "top",
      labels: {
        font: {
          size: 16, // 범례 글자 크기
          family: "Pretendard", // 원하는 폰트 패밀리
          weight: "light", // 글자 두께
        },
      },
    },
    tooltip: {
      enabled: false, // 툴팁 비활성화
    },
  },
};
