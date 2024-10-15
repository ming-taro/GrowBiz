import axios from 'axios';

import { useAuthStore } from '@/stores/auth';

const authStore = useAuthStore();

const mno = authStore.state.mno;

var id = '1234';

// 혼합 차트 데이터
export let mixed_data = {
  labels: [], // 라벨 설정
  datasets: [
    {
      type: 'bar',
      label: '나의 매출',
      data: [],
      borderColor: 'rgb(255, 9, 132)',
      backgroundColor: 'rgba(255, 99, 132, 0.2)',
    },
    {
      type: 'bar', // 첫 번째 라인 데이터셋
      label: '지역별 평균 매출',
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

export let mixed_data2 = {
  labels: [], // 라벨 설정
  datasets: [
    {
      type: 'bar',
      label: '나의 매출',
      data: [],
      borderColor: 'rgb(255, 9, 132)',
      backgroundColor: 'rgba(255, 99, 132, 0.2)',
    },
    {
      type: 'bar', // 첫 번째 라인 데이터셋
      label: '지역별 평균 매출',
      data: [],
      fill: false,
      borderColor: 'rgb(54, 162, 235)',
      tension: 0.1, // 선의 곡률 조정
    },
  ],
};

// 혼합 차트 옵션
export const mixed_options2 = {
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
    id = 1234;
    response = await axios.get(`/api/kmap/member/${id}`);
  }

  const dongname = response.data.dongname;
  const svcIndutyCdNm = response.data.svcIndutyCdNm;

  const mcfirst = await axios.get(`/api/chart/mcfirst/${svcIndutyCdNm}`, {
    params: { dongname },
  });
  const mcsecend = await axios.get(`/api/chart/mcsecend/${svcIndutyCdNm}`);

  const mcfirstdata = mcfirst.data;

  const mcsecenddata = mcsecend.data.reduce(
    (sum, item) => sum + item.amount,
    0
  );

  mixed_data2.labels = mcfirstdata.map((item) => item.adstrdCdNm);
  // 먼저 mcfirstdata의 길이를 기반으로 datasets[0].data를 설정
  mixed_data2.datasets[0].data = Array(mcfirstdata.length).fill(mcsecenddata);

  // 그 후 datasets[1].data에 mcfirstdata의 값을 설정
  mixed_data2.datasets[1].data = mcfirstdata.map(
    (item) => item.mdwkSelngAmt / 150
  );

  // const mixchart = await axios.get(`/api/chart/mixchart`);

  // const firstData = [];
  // const secondData = [];

  // const categorizedData = mixchart.data.reduce((acc, item) => {
  //   if (!acc[item.category]) {
  //     acc[item.category] = [];
  //   }

  //   if (acc[item.category].length === 0) {
  //     acc[item.category].push(item);
  //     firstData.push(item); // 첫 번째 데이터를 firstData에 추가
  //   } else if (acc[item.category].length === 1) {
  //     acc[item.category].push(item);
  //     secondData.push(item); // 두 번째 데이터를 secondData에 추가
  //   }
  //   return acc;
  // }, {});

  const sum = await axios.get(`/api/chart/sum/${svcIndutyCdNm}`);

  mixed_data.labels = mcfirstdata.map((item) => item.adstrdCdNm);

  mixed_data.datasets[0].data = Array(mcfirstdata.length).fill(sum.data.amount);
  mixed_data.datasets[1].data = mcfirstdata.map(
    (item) => item.thsmonSelngAmt / 100
  );
}
