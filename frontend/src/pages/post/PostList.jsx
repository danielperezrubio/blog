import { useEffect, useState } from "react";
import { Link, useNavigate, useSearchParams } from "react-router-dom";
import { getFilteredPost, getPostList } from "../../services/post";

function PostList() {
  const [params] = useSearchParams();
  const filter_word = params.get("filter_word");
  const page = params.get("page");
  const [posts, setPosts] = useState([]);
  const navigate = useNavigate();
  const limit = 12;

  useEffect(() => {
    const offset = (parseInt(page) - 1) * limit;
    if (filter_word) {
      getFilteredPost(filter_word, offset, limit)
        .then((res) => {
          setPosts(res.data);
        })
        .catch((err) => {});
    } else {
      getPostList(limit, offset)
        .then((res) => {
          setPosts(res.data);
        })
        .catch((err) => {});
    }
  }, [filter_word, page]);

  function handleNext(event) {
    const next_page = page ? parseInt(page) + 1 : 2;
    navigate(`/post/list?filter_word=${filter_word}&page=${next_page}`);
  }

  function handlePrev(event) {
    const prev_page = parseInt(page) - 1;
    navigate(`/post/list?filter_word=${filter_word}&page=${prev_page}`);
  }

  return (
    <div className="container text-center mt-3">
      <h3>Posts{filter_word ? ` with "${filter_word}"` : ""}</h3>

      <ul>
        {posts.map((post) => (
          <li key={post.id} className="mb-1">
            <em>
              <Link to={`/post/view/${post.id}`}>{post.title}</Link>
            </em>
          </li>
        ))}
        <button
          className={
            parseInt(page) > 1
              ? "btn btn-outline-primary btn-sm mt-4 me-2"
              : "btn btn-outline-primary btn-sm mt-4 me-2 disabled"
          }
          onClick={handlePrev}
        >
          Previous
        </button>
        <button
          className={
            posts.length === limit
              ? "btn btn-outline-primary btn-sm mt-4"
              : "btn btn-outline-primary btn-sm mt-4 disabled"
          }
          onClick={handleNext}
        >
          Next
        </button>
      </ul>
    </div>
  );
}

export default PostList;
