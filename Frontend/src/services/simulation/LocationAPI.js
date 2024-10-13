import axios from "axios";

export const findLocationByAddress = async (location) => {
  const REQUEST_URL = `https://dapi.kakao.com/v2/local/search/address.json?query=${encodeURIComponent(location)}`;
  const apiKey = import.meta.env.VITE_KAKAO_API_KEY;

  try {
    const response = await axios.get(REQUEST_URL, {
      headers: {
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": `KakaoAK ${apiKey}`
      }
    });

    const data = { x: response.data.documents[0].x, y: response.data.documents[0].y };
    return data;
  }catch(error) {
    console.error("Error during API request:", error);
  }
}