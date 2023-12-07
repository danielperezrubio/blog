import { useState } from "react";
import { useSearchParams } from "react-router-dom";
import { updateUserPassword } from "../../services/user";
import { toast } from "react-toastify";
import { useNavigate } from "react-router-dom";

function ResetPassword() {
  const [params] = useSearchParams();
  const [password, setPassword] = useState("");
  const token = params.get("token");
  const navigate = useNavigate();

  function handleSubmit(event) {
    event.preventDefault();
    updateUserPassword(token, password)
      .then((res) => {
        toast.success("Password has been changed!");
        navigate("/login");
      })
      .catch((err) => {
        toast.error("Token is invalid or expired!");
      });
  }

  return (
    <div className="container">
      <form style={{ width: "280px" }} className="mx-auto mt-3">
        <h4 className="text-center">Change Password</h4>
        <input
          type="password"
          className="form-control mb-2"
          placeholder="New Password"
          onChange={(e) => setPassword(e.target.value)}
        />
        <button onClick={handleSubmit} className="btn btn-primary w-100">
          Change
        </button>
      </form>
    </div>
  );
}

export default ResetPassword;
