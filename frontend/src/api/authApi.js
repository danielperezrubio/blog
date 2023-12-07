import axios from "axios";
import { baseUrl } from "./urls";

export const authApi = axios.create({
  baseURL: `${baseUrl}/token`,
});
