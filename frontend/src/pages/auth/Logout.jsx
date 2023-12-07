import { useContext, useEffect } from "react";
import { UserContext } from "../../context/user";
import { toast } from "react-toastify";
import { Navigate } from "react-router-dom";

function Logout() {
  const { deleteToken } = useContext(UserContext);

  useEffect(() => {
    deleteToken();
    toast.success("User has been logged out!");
  }, []);

  return <Navigate to={"/"} />;
}

export default Logout;
