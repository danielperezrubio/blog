import axios from "axios";
import { baseUrl } from "./urls";

export function imageApi(token) {
  return axios.create({
    baseURL: `${baseUrl}/image`,
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
}
