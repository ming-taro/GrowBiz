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

export const createSimulationAnswer = async (userID, answer) => {
  try {
    const response = await axios.post(
      BASE_URL + "/answer",
      {
        user_id: userID,
        answer: answer,
      },
      {
        headers: {
          "Content-Type": "application/json; charset=UTF-8",
        },
      }
    );

    console.log("Data saved successfully:", response.data);
    return response.data; // 저장된 데이터 반환
  } catch (error) {
    console.error("Error saving data:", error);
    throw error; // 오류 발생 시 예외 던지기
  }
};

export const fetchResponseById = async (id) => {
  try {
    const response = await axios.get(BASE_URL + `/answer/${id}`, {
      headers: {
        "Content-Type": "application/json; charset=UTF-8",
      },
    });

    return response.data.answer;
  } catch (error) {
    console.error("Error saving data:", error);
    throw error;
  }
};

export const executeFranchiseAnalyze = async (id) => {
  try {
    const response = await axios.post(
      BASE_URL + `/start`,
      {
        id: id,
      },
      {
        headers: {
          "Content-Type": "application/json; charset=UTF-8",
        },
      }
    );

    return response.data;
  } catch (error) {
    console.error("Error saving data:", error);
    throw error;
  }
};

export const findLocation = async (id) => {
  const data = await fetchResponseById(id);
  return data[0].district + " " + data[0].neighborhoods;
};
