import { authApi } from "../api/authApi";

export function generate_token(username, password) {
  const formData = new FormData();
  formData.append("username", username);
  formData.append("password", password);
  return authApi.post("", formData);
}
