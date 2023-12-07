export const isBase64 = (url) => {
  return /^data:image/.test(url);
};

export function getFileNameFromBase64(base64String) {
  const arr = base64String.split(",");
  const mime = arr[0].match(/:(.*?);/)[1];
  const extension = mime.split("/")[1];
  const fileName = `image_${Date.now()}.${extension}`;

  return fileName;
}

export function base64ToFile(base64String, fileName) {
  const arr = base64String.split(",");
  const mime = arr[0].match(/:(.*?);/)[1];
  const bstr = atob(arr[1]);
  let n = bstr.length;
  const u8arr = new Uint8Array(n);

  while (n--) {
    u8arr[n] = bstr.charCodeAt(n);
  }

  return new File([u8arr], fileName, { type: mime });
}
