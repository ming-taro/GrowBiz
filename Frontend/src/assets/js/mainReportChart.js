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
        callback: function (value) {
          return ''; // 단위를 표시하지 않음
        },
        font: {
          size: 14, // x축 글자 크기
          family: 'Pretendard', // 원하는 폰트 패밀리
          weight: 'bold', // 글자 두께
        },
      },
    },
    y: {
      grid: {
        color: 'rgba(255, 255, 255, 0.3)',
        lineWidth: 1,
      },
      ticks: {
        font: {
          size: 16, // y축 글자 크기
          family: 'Pretendard', // 원하는 폰트 패밀리
          weight: 'light', // 글자 두께
        },
      },
    },
  },
  plugins: {
    legend: {
      display: true,
      position: 'top',
      labels: {
        font: {
          size: 14, // 범례 글자 크기
          family: 'Pretendard', // 원하는 폰트 패밀리
          weight: 'bold', // 글자 두께
        },
      },
    },
    tooltip: {
      enabled: false, // 툴팁 비활성화
    },
    datalabels: {
      display: true, // 데이터 라벨 표시
      anchor: 'center', // 텍스트를 막대의 끝에 붙임
      align: 'center', // 텍스트를 막대의 끝에 맞춤
      color: '#000',
      formatter: (value, context) => {
        const index = context.dataIndex;
        if (index === 0) {
          // 첫 번째 값 (밀도)에만 1000을 나누어서 표시
          return (value / 1000).toFixed(2);
        }
        return value; // 나머지 값들은 그대로 표시
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

export const data_bar = {
  labels: [
    '밀도 (단위 : km²)',
    '가맹비 (단위 : 만원)',
    '총 인테리어 비용 (단위 : 만원)',
  ],
  datasets: [
    {
      label: '업종 평균',
      backgroundColor: '#fca3b9',
      data: [
        1.05 * 1000, // 업종 밀도 평균 (실제 데이터에 1000을 곱한 값)
        5000, // 업종 평균 가맹비
        12000, // 업종 총 인테리어 비용
      ],
    },
    {
      label: '추천 브랜드 평균',
      backgroundColor: '#fcd752',
      data: [2.05 * 1000, 4500, 10000], // 추천 브랜드 평균 데이터
    },
  ],
};
