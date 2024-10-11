import axios from "axios";

const BASE_URL = "http://localhost:8080/api/simulation";

export const getQuestions = async () => {
  return axios
    .get(BASE_URL + "/question")
    .then((response) => response.data)
    .catch((error) => {
      console.error(error);
      throw error;
    });
};

export const saveSimulationAnswer = async (answer) => {
  axios
    .post(
      BASE_URL + "/answer",
      {
        data: answer,
      },
      {
        headers: {
          "Content-Type": "application/json; charset=UTF-8",
        },
      }
    )
    .then((response) => {
      console.log("Data saved successfully:", response.data);
      return response.data; // 저장된 데이터 반환
    })
    .catch((error) => {
      console.error("Error saving data:", error);
      throw error; // 오류 발생 시 예외 던지기
    });
};
