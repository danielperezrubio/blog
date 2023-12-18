import { useEffect, useState } from "react";
import { getPostList } from "../services/post";
import { Link } from "react-router-dom";

function PostRecentList() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    const limit = 12;
    getPostList(limit).then((res) => {
      setPosts(res.data);
    });
  }, []);

  return (
    <section className="mt-5">
      <hr />
      <p className="text-center">
        <em>Recent Posts</em>
      </p>
      <div className="container">
        <div className="row justify-content-center ml-0">
          {posts.map((post) => (
            <div
              key={post.id}
              className="text-center col-xs-12 col-md-4 pb-4"
              style={{ width: "300px" }}
            >
              <em>
                <Link to={`/post/view/${post.id}`}>{post.title}</Link>
              </em>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

export default PostRecentList;
