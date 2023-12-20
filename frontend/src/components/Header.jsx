import { NavLink, Link, useNavigate } from "react-router-dom";
import { useContext, useState } from "react";
import { UserContext } from "../context/user";
import "./Header.css";

function Header() {
  const { user } = useContext(UserContext);
  const [filter_word, setFilterWord] = useState("");
  const navigate = useNavigate();

  function handleSubmit(event) {
    event.preventDefault();
    navigate(`/post/list?filter_word=${filter_word}`);
  }

  return (
    <header style={{ backgroundColor: "rgba(47, 152, 255, 0.5)" }}>
      <nav className="navbar navbar-expand-lg" data-bs-theme="dark">
        <div className="container-fluid">
          <Link className="navbar-brand ps-lg-4" to="/">
            Blog
          </Link>
          <button
            className="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span className="navbar-toggler-icon"></span>
          </button>
          <div
            className="collapse navbar-collapse justify-content-end"
            id="navbarSupportedContent"
          >
            <form
              className="d-flex rounded align-items-center p-2 mx-auto"
              style={{
                height: "38px",
                backgroundColor: "#233f59",
              }}
              onSubmit={handleSubmit}
            >
              <i className="bi bi-search mx-1"></i>
              <input
                className="ms-1 me-5"
                type="search"
                placeholder="Search"
                aria-label="Search"
                style={{
                  border: "none",
                  outline: "none",
                  color: "white",
                  backgroundColor: "inherit",
                }}
                onChange={(e) => {
                  setFilterWord(e.target.value);
                }}
              />
            </form>
            <ul className="navbar-nav mb-lg-0 pe-lg-4">
              <li className="nav-item">
                <NavLink
                  activeclassname="active"
                  className="nav-link"
                  aria-current="page"
                  to="/"
                >
                  Home
                </NavLink>
              </li>
              <li className="nav-item">
                <NavLink
                  activeclassname="active"
                  className="nav-link"
                  to="/post/list"
                >
                  Posts
                </NavLink>
              </li>
              {user.isAdmin && (
                <li className="nav-item">
                  <NavLink
                    activeclassname="active"
                    className="nav-link"
                    to="/post/add"
                  >
                    Editor
                  </NavLink>
                </li>
              )}
              {!user.id ? (
                <li className="nav-item">
                  <NavLink
                    activeclassname="active"
                    className="nav-link"
                    aria-current="page"
                    to="/login"
                  >
                    Sign In
                  </NavLink>
                </li>
              ) : (
                <li className="nav-item">
                  <NavLink
                    activeclassname="active"
                    className="nav-link"
                    aria-current="page"
                    to="/logout"
                  >
                    Logout
                  </NavLink>
                </li>
              )}
            </ul>
          </div>
        </div>
      </nav>
    </header>
  );
}

export default Header;
