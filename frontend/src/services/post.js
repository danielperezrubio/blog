import { postApi } from "../api/postApi";

export function createPost(token, title, content, tags) {
  const data = {
    title,
    content,
    tags,
  };
  return postApi(token).post("", data);
}

export function getPost(id) {
  return postApi().get(`/${id}`);
}

export function getLatestPost() {
  return postApi().get(`?limit=1`);
}

export function getPostList(limit, offset = null) {
  const offset_param = offset ? `&offset=${offset}` : "";
  return postApi().get(`?send_content=false&limit=${limit}` + offset_param);
}

export function getFilteredPost(filter_word, offset, limit) {
  const offset_param = offset ? `&offset=${offset}` : "";
  return postApi().get(
    `?filter_word=${filter_word}&send_content=false&limit=${limit}` +
      offset_param
  );
}

export function updatePost(token, id, title, content, tags) {
  const data = { title, content, tags };
  return postApi(token).put(`/${id}`, data);
}

export function deletePost(token, id) {
  return postApi(token).delete(`/${id}`);
}
