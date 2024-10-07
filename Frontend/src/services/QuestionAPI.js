import axios from "axios";

const BASE_URL = "http://localhost:8080/api/simulation";

export const getQuestions = async() => {
  return axios.get(BASE_URL + '/question')
    .then(response => response.data)
    .catch(error => {
      console.error(error);
      throw error;
    });
};