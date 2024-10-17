const axios = require('axios');
const cheerio = require('cheerio');

// 네이버 API 인증 정보 (발급받은 클라이언트 ID와 시크릿을 입력하세요)
const CLIENT_ID = import.meta.env.VITE_NAVER_API_KEY;
const CLIENT_SECRET = import.meta.env.VITE_NAVER_SECRET;

// 뉴스 검색을 위한 함수
async function getNews(query) {
  try {
    const response = await axios.get(
      'https://openapi.naver.com/v1/search/news.json',
      {
        headers: {
          'X-Naver-Client-Id': CLIENT_ID,
          'X-Naver-Client-Secret': CLIENT_SECRET,
        },
        params: {
          query: query, // 검색할 키워드
          display: 10, // 검색 결과 출력 개수
          start: 1, // 검색 시작 위치
          sort: 'date', // 날짜순 정렬 (sim: 정확도순, date: 날짜순)
        },
      }
    );

    const newsItems = response.data.items;
    console.log('뉴스 검색 결과:');

    // 각 뉴스의 상세 페이지를 크롤링하여 썸네일, 본문, 날짜를 가져옵니다.
    for (let item of newsItems) {
      console.log(`뉴스 제목: ${item.title}`);
      console.log(`네이버 뉴스 링크: ${item.link}`);
      await getNewsDetails(item.link);
    }
  } catch (error) {
    console.error('뉴스 검색 중 오류 발생:', error);
  }
}

// 뉴스 상세 페이지에서 썸네일, 본문, 날짜를 가져오는 함수
async function getNewsDetails(newsUrl) {
  try {
    const response = await axios.get(newsUrl);
    const html = response.data;
    const $ = cheerio.load(html);

    // 뉴스 페이지에서 썸네일 이미지 추출
    const thumbnail = $('meta[property="og:image"]').attr('content');

    // 뉴스 본문 추출 (HTML 구조에 따라 달라질 수 있음)
    let newsContent = '';
    $('p').each((i, elem) => {
      newsContent += $(elem).text().trim();
    });

    // 본문에서 첫 50글자만 추출
    const shortContent = newsContent.slice(0, 100);

    // 뉴스 날짜 추출
    const dateTime = $('span.media_end_head_info_datestamp_time').attr(
      'data-date-time'
    );
    const newsDate = dateTime ? dateTime.split(' ')[0] : '날짜 정보 없음';

    console.log(`썸네일 이미지: ${thumbnail}`);
    console.log(`뉴스 본문 (100글자): ${shortContent}`);
    console.log(`뉴스 날짜: ${newsDate}`);
  } catch (error) {
    console.error('뉴스 상세 페이지 크롤링 중 오류 발생:', error);
  }
}

// 검색할 키워드 설정
const searchQuery = '주식'; // 예시로 "주식" 키워드를 사용
getNews(searchQuery);
