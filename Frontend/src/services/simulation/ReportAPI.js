import axios from "axios";

const BASE_URL = "http://localhost:8080/api/report";

export const createReport = async (userId, simulationResponseId) => {
  try {
    const response = await axios.post(
      BASE_URL,
      {
        userId: userId,
        simulationResponseId: simulationResponseId,
      },
      {
        headers: {
          "Content-Type": "application/json; charset=UTF-8",
        },
      }
    );

    console.log("Data saved successfully:", response.data);
    return response.data;
  } catch (error) {
    console.error("Error saving data:", error);
    throw error;
  }
};

export const fetchReportById = async (id) => {
  try {
    const response = await axios.get(BASE_URL + `/${id}`, {
      headers: {
        "Content-Type": "application/json; charset=UTF-8",
      },
    });

    return response.data;
  } catch (error) {
    console.error("Error saving data:", error);
    throw error;
  }
};

export const findReportIdByResponseId = async (id) => {
  try {
    const response = await axios.get(BASE_URL + `/response-id/{${id}}`, {
      headers: {
        "Content-Type": "application/json; charset=UTF-8",
      },
    });

    return response.data;
  } catch (error) {
    console.error("Error saving data:", error);
    throw error; // 오류 발생 시 예외 던지기
  }
};

export const findAllReports = async (id) => {
  try {
    const response = await axios.get(BASE_URL + `/user/${id}`, {
      headers: {
        "Content-Type": "application/json; charset=UTF-8",
      },
    });

    return response.data;
  } catch (error) {
    console.error("Error saving data:", error);
    throw error; // 오류 발생 시 예외 던지기
  }
};
