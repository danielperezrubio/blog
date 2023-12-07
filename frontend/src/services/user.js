import { userApi } from "../api/userApi";

export function activateUser(token) {
  return userApi().patch(`/activate?token=${token}`);
}

export function getUser(token) {
  return userApi(token).get("/me");
}

export function updateUserPassword(token, password) {
  const data = { token, password };
  return userApi().patch(`/password`, data);
}

export function resetUserPassword(email) {
  return userApi().get(`/password?email=${email}`);
}
