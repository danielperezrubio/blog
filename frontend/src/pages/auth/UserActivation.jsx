import { useEffect, useState } from "react";
import { Link, useSearchParams } from "react-router-dom";
import { activateUser } from "../../services/user";

function UserActivation() {
  const [params] = useSearchParams();
  const token = params.get("token");
  const [errorMessage, setErrorMessage] = useState("");
  const [activated, setActivated] = useState(false);

  useEffect(() => {
    activateUser(token)
      .then((res) => {
        setActivated(true);
      })
      .catch((err) => {
        setErrorMessage(err.response.data.detail);
      });
  }, []);

  return (
    <>
      {activated && (
        <div className="container mt-4">
          <div
            className="text-center mx-auto p-4 rounded"
            style={{
              maxWidth: "400px",
              backgroundColor: "rgb(33, 41, 43)",
              borderColor: "#212d2d",
            }}
          >
            <span className="text-success">
              User account has been activated!
            </span>
            <br />
            <Link className="btn btn-outline-primary btn-sm mt-2" to="/">
              Go Home
            </Link>
          </div>
        </div>
      )}
      {errorMessage && (
        <div className="container mt-4">
          <div
            className="text-center mx-auto text-danger"
            style={{ maxWidth: "400px" }}
          >
            Invalid token!
          </div>
        </div>
      )}
    </>
  );
}

export default UserActivation;
