import { Navigate, Outlet } from "react-router-dom";

function ProtectedRoute({ children, isAllowed, isLoadingUser }) {
  if (isLoadingUser) {
    return <div>Loading...</div>;
  }

  if (!isAllowed) {
    return <Navigate to="/" />;
  }

  return children ? children : <Outlet />;
}

export default ProtectedRoute;
