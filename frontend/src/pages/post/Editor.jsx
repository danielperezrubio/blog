import ReactQuill from "react-quill";
import "react-quill/dist/quill.snow.css";
import { useContext, useRef, useState } from "react";
import { useNavigate } from "react-router-dom";
import { load } from "cheerio";

import { createPost } from "../../services/post";
import { uploadImage } from "../../services/image";
import { UserContext } from "../../context/user";
import { quillModules } from "../../constants";
import { toast } from "react-toastify";
import { isBase64, getFileNameFromBase64, base64ToFile } from "./helpers";

const Editor = () => {
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");
  const [tags, setTags] = useState([]);
  const [inputValue, setInputValue] = useState("");
  const { token } = useContext(UserContext);
  const navigate = useNavigate();

  const quillRef = useRef(null);

  const handleImageUpload = (imageUrls) => {
    for (let image of imageUrls) {
      if (isBase64(image)) {
        const fileName = getFileNameFromBase64(image);
        const file = base64ToFile(image, fileName);
        uploadImage(token, file)
          .then((res) => {
            let imageUrl = `${import.meta.env.VITE_IMAGES_URL}/${
              res.data.image_name
            }`;
            const editorContent = quillRef.current.getEditor().root.innerHTML;
            const updatedContent = editorContent.replace(image, imageUrl);
            quillRef.current.getEditor().root.innerHTML = updatedContent;
          })
          .catch((err) => {});
      }
    }
  };

  const handleChange = (content) => {
    setContent(content);
    const $ = load(content);
    const imageTags = $("img");

    const imageUrls = imageTags
      .map((index, element) => {
        return $(element).attr("src");
      })
      .get();
    handleImageUpload(imageUrls);
  };

  const handleInputChange = (event) => {
    setInputValue(event.target.value);
  };

  const handleKeyDown = (event) => {
    if (event.key === "Enter" && inputValue.trim() !== "") {
      const trimmedValue = inputValue.trim().toLowerCase();
      if (!tags.map((tag) => tag.toLowerCase()).includes(trimmedValue)) {
        setTags([...tags, trimmedValue]);
      }
      setInputValue("");
    }
  };

  const handleTagRemove = (tag) => {
    setTags(tags.filter((t) => t !== tag));
  };

  function handleSubmit(event) {
    event.preventDefault();
    if (!title) {
      toast.error("Title field is required!");
      return;
    }
    if (!content | (content === "<p><br></p>")) {
      toast.error("Content field is required!");
      return;
    }
    if (tags.length === 0) {
      toast.error("Tags are required!");
      return;
    }
    createPost(token, title, content, tags)
      .then((res) => {
        navigate(`/post/view/${res.data.id}`);
      })
      .catch((err) => {});
  }

  return (
    <div className="container mb-4">
      <div className="mt-3">
        <input
          type="text"
          className="form-control"
          value={inputValue}
          onChange={handleInputChange}
          onKeyDown={handleKeyDown}
          placeholder="Enter a tag and press Enter"
        />
        <ul>
          {tags.map((tag) => (
            <li key={tag} className="mt-2">
              {tag}
              <button
                className="btn btn-danger ms-2 btn-sm"
                onClick={() => handleTagRemove(tag)}
              >
                Remove
              </button>
            </li>
          ))}
        </ul>
      </div>

      <form className="mt-4">
        <div className="mb-2">
          <input
            type="text"
            className="form-control"
            style={{ fontSize: "2em" }}
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            placeholder="Title"
          />
        </div>
        <ReactQuill
          ref={quillRef}
          modules={{ ...quillModules }}
          theme="snow"
          onChange={handleChange}
        />
        <button className="btn btn-success mt-1" onClick={handleSubmit}>
          Create
        </button>
      </form>
    </div>
  );
};

export default Editor;
