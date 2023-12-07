import axios from "axios";
import { baseUrl } from "./urls";

export function postApi(token) {
  return axios.create({
    baseURL: `${baseUrl}/post`,
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
}
