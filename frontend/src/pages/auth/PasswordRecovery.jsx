import { useState } from "react";
import { resetUserPassword } from "../../services/user";
import { toast } from "react-toastify";

function PasswordRecovery() {
  const [email, setEmail] = useState("");
  const [successMessage, setSuccessMessage] = useState("");

  function validateEmail(email) {
    const regularExpression = /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i;
    return regularExpression.test(email);
  }

  function handleSubmit(event) {
    event.preventDefault();
    if (validateEmail(email)) {
      resetUserPassword(email)
        .then((res) => {
          document.getElementById("passwordRecoveryForm").hidden = true;
          setSuccessMessage(
            "We have sent you an email, please check it to change your password."
          );
        })
        .catch((err) => {
          toast.error("The provided email is not associated with any account.");
        });
    } else {
      toast.error("Please enter a valid email address.");
    }
  }

  return (
    <div className="container">
      {successMessage && (
        <div
          className="alert alert-success text-center mx-auto mt-2"
          style={{
            width: "600px",
            backgroundColor: "#262d2c",
            color: "#5bb93f",
            borderColor: "#32372f",
          }}
          role="alert"
        >
          <i className="bi bi-check-circle me-1"></i>
          {successMessage}
        </div>
      )}
      <form
        style={{ width: "300px" }}
        className="mx-auto mt-3"
        id="passwordRecoveryForm"
      >
        <h3 className="text-center">Password Recovery</h3>
        <input
          type="email"
          className="form-control mb-2"
          placeholder="Email"
          onChange={(e) => {
            setEmail(e.target.value);
          }}
        />
        <button className="btn btn-primary w-100" onClick={handleSubmit}>
          Reset Password
        </button>
      </form>
    </div>
  );
}

export default PasswordRecovery;
