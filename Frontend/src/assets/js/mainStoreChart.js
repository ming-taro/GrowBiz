import axios from 'axios';

const id = '1234';

// 혼합 차트 데이터
export let store_data_bar = {
  labels: [], // 라벨 설정
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
export const store_barOptions = {
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
  try {
    const response = await axios.get(`/api/kmap/member/${id}`);
    const svcIndutyCdNm = response.data.svcIndutyCdNm;

    const doughnut = await axios.get(`/api/chart/doughnut/${svcIndutyCdNm}`);

    const sortedData = doughnut.data.sort((a, b) => b.amount - a.amount);

    // 데이터 설정
    store_data_bar.labels = sortedData.map((item) => item.categoryName);

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

    // 데이터 반영
    store_data_bar.datasets[0].data = secondData.map((item) => item.amount);

    store_data_bar.datasets[1].data = firstData.map((item) => item.amount);
  } catch (error) {
    console.error('차트 데이터를 가져오는 중 오류 발생:', error);
  }
}
