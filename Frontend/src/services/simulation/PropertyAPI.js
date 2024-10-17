import axios from "axios";

const BASE_URL = "http://localhost:8080/api/property";

export const fetchPropertyById = async (plno) => {
  try {
    const response = await axios.get(
      BASE_URL + `/${plno}`,
      {
        headers: {
          "Content-Type": "application/json; charset=UTF-8",
        },
      }
    );

    return response.data;
  } catch (error) {
    console.error(error);
    throw error;
  }
};