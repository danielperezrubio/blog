import { useContext, useState } from "react";
import { generate_token } from "../../services/auth";
import { Link, useNavigate } from "react-router-dom";
import { UserContext } from "../../context/user";
import { toast } from "react-toastify";

function SingIn() {
  const [userData, setUserData] = useState({ username: "", password: "" });

  const { updateToken } = useContext(UserContext);

  const navigate = useNavigate();

  function handleSubmit(event) {
    event.preventDefault();
    generate_token(userData.username, userData.password)
      .then((res) => {
        updateToken(res.data.access_token);
        toast.success("Logged in successfully!");
        navigate("/");
      })
      .catch((err) => {
        toast.error("Invalid username or password!");
      });
  }

  return (
    <div className="container">
      <form style={{ maxWidth: "350px" }} className="mx-auto mt-3">
        <h3 className="text-center">Sign in</h3>
        <div className="input-group mb-1">
          <span className="input-group-text" id="basic-addon1">
            <i className="bi bi-person-fill"></i>
          </span>
          <input
            type="text"
            className="form-control"
            placeholder="Username"
            aria-label="Username"
            aria-describedby="basic-addon1"
            onChange={(e) =>
              setUserData({ ...userData, username: e.target.value })
            }
          />
        </div>
        <div className="input-group mb-1">
          <span className="input-group-text" id="basic-addon2">
            <i className="bi bi-key-fill"></i>
          </span>
          <input
            type="password"
            className="form-control"
            placeholder="Password"
            aria-label="Password"
            aria-describedby="basic-addon2"
            onChange={(e) =>
              setUserData({ ...userData, password: e.target.value })
            }
          />
        </div>
        <Link
          to={"/password_recovery"}
          className="d-inline-block mb-2"
          style={{ textDecoration: "none" }}
        >
          Forgot password?
        </Link>
        <button className="btn btn-primary w-100" onClick={handleSubmit}>
          Send
        </button>
      </form>
    </div>
  );
}

export default SingIn;
