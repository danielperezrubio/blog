import axios from "axios";
import { baseUrl } from "./urls";

export function userApi(token) {
  return axios.create({
    baseURL: `${baseUrl}/user`,
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
}
