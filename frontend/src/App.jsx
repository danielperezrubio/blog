import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.min.js";
import "bootstrap-icons/font/bootstrap-icons.css";
import "react-toastify/dist/ReactToastify.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Header from "./components/Header";
import Editor from "./pages/post/Editor";
import PostView from "./pages/post/PostView";
import UserActivation from "./pages/auth/UserActivation";
import SingIn from "./pages/auth/SignIn";
import ProtectedRoute from "./components/ProtectedRoute";
import Logout from "./pages/auth/Logout";
import { useContext } from "react";
import { UserContext } from "./context/user";
import Home from "./pages/Home";
import PostList from "./pages/post/PostList";
import ChangePassword from "./pages/auth/ChangePassword";
import PasswordRecovery from "./pages/auth/PasswordRecovery";
import PostEdit from "./pages/post/PostEdit";
import { ToastContainer } from "react-toastify";
import { icons } from "./quill-icons";
import Footer from "./components/Footer";

function App() {
  const { user, isLoadingUser } = useContext(UserContext);

  return (
    <BrowserRouter>
      <Header />
      <ToastContainer
        position="top-right"
        autoClose={5000}
        hideProgressBar={false}
        newestOnTop={false}
        closeOnClick
        rtl={false}
        pauseOnFocusLoss
        draggable
        pauseOnHover
        theme="dark"
      />

      <Routes>
        <Route index element={<Home />} />
        <Route path="/post/*">
          <Route
            element={
              <ProtectedRoute
                isAllowed={user.isAdmin}
                isLoadingUser={isLoadingUser}
              />
            }
          >
            <Route path="add" element={<Editor />} />
            <Route path="edit/:id" element={<PostEdit />} />
          </Route>
          <Route path="view/:id" element={<PostView />} />
          <Route path="list" element={<PostList />} />
        </Route>

        <Route path="/user/*">
          <Route path="change_password" element={<ChangePassword />} />
          <Route path="activate" element={<UserActivation />} />
        </Route>

        <Route path="/login" element={<SingIn />} />
        <Route path="/logout" element={<Logout />} />
        <Route path="/password_recovery" element={<PasswordRecovery />} />
      </Routes>
      <Footer />
    </BrowserRouter>
  );
}

export default App;
