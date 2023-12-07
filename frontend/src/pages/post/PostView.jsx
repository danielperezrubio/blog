import { useContext, useEffect, useState } from "react";
import { deletePost, getLatestPost, getPost } from "../../services/post";
import DOMPurify from "dompurify";
import ReactQuill from "react-quill";
import "react-quill/dist/quill.bubble.css";
import { Link, useNavigate, useParams } from "react-router-dom";
import PostRecentList from "../../components/PostRecentList";
import { quillModules } from "../../constants";
import { UserContext } from "../../context/user";
import { toast } from "react-toastify";

function PostView() {
  const { id } = useParams();
  const [post, setPost] = useState({
    id: null,
    title: null,
    content: null,
    tags: [],
    owner_id: null,
    published_at: null,
    updated_at: null,
  });
  const { user, token } = useContext(UserContext);
  const navigate = useNavigate();

  function sanitizeHTML(content) {
    return DOMPurify.sanitize(content);
  }

  useEffect(() => {
    if (id === "latest") {
      getLatestPost()
        .then((res) => {
          const data = res.data[0];
          data.content = sanitizeHTML(data.content);
          setPost(data);
        })
        .catch((err) => {});
    } else {
      getPost(id)
        .then((res) => {
          const data = res.data;
          data.content = sanitizeHTML(data.content);
          setPost(data);
        })
        .catch((err) => {});
    }
  }, [id]);

  function handleDelete() {
    deletePost(token, post.id)
      .then((res) => {
        toast.success("The post has been deleted!");
        navigate("/");
      })
      .catch((err) => {
        toast.error("An error has ocurred!");
      });
  }

  const formatDate = (dateString) => {
    const options = { year: "numeric", month: "long", day: "numeric" };
    return new Date(dateString).toLocaleDateString("en", options);
  };

  return (
    <div className="container mt-3 mb-4">
      <h1 style={{ color: "rgb(194, 213, 230)", paddingLeft: "12px" }}>
        {post.title}
      </h1>
      <div
        style={{ fontSize: "0.9em", marginBottom: "10px", paddingLeft: "12px" }}
      >
        <span className="text-muted">
          {post.updated_at !== null && (
            <>Updated {formatDate(post.updated_at)}</>
          )}
          {post.updated_at === null && post.published_at !== null ? (
            <>Published {formatDate(post.published_at)}</>
          ) : null}
        </span>
      </div>

      <ReactQuill
        modules={{ ...quillModules }}
        value={post.content}
        theme="bubble"
        readOnly
      />

      {post.tags.map((tag) => (
        <span key={tag} className="ms-5 text-muted">
          <Link
            to={`/post/list?filter_word=${tag}`}
            style={{ textDecoration: "none" }}
          >
            {tag}
          </Link>
        </span>
      ))}
      <br />
      {user.isAdmin & (post.id !== null) ? (
        <>
          <Link to={`/post/edit/${id}`} className="btn btn-primary ms-3 mt-3">
            <i className="bi bi-pencil-square"></i>
            <span className="ms-1">Edit</span>
          </Link>
          <button
            className="btn btn-danger ms-3 mt-3"
            type="button"
            data-bs-toggle="modal"
            data-bs-target="#deletePostModal"
          >
            <i className="bi bi-trash-fill"></i>
            <span className="ms-1">Delete</span>
          </button>
        </>
      ) : null}

      <div className="modal" tabIndex="-1" id="deletePostModal">
        <div className="modal-dialog">
          <div className="modal-content">
            <div className="modal-header">
              <h5 className="modal-title">Delete Post</h5>
              <button
                type="button"
                className="btn-close"
                data-bs-dismiss="modal"
                aria-label="Close"
              ></button>
            </div>
            <div className="modal-body">
              <p>Are you sure you want to remove this post?</p>
            </div>
            <div className="modal-footer">
              <button
                type="button"
                className="btn btn-danger"
                onClick={handleDelete}
                data-bs-dismiss="modal"
              >
                Yes
              </button>
              <button
                type="button"
                className="btn btn-secondary"
                data-bs-dismiss="modal"
              >
                No
              </button>
            </div>
          </div>
        </div>
      </div>

      <PostRecentList />
    </div>
  );
}

export default PostView;
