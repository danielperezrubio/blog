import { imageApi } from "../api/imageApi";

export function uploadImage(token, image) {
  const formData = new FormData();
  formData.append("file", image);
  return imageApi(token).post("", formData);
}
