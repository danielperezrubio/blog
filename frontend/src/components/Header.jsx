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
    <header style={{ backgroundColor: "#1f6fc4" }}>
      <nav className="navbar navbar-expand-lg" data-bs-theme="dark">
        <div className="container-fluid me-2">
          <Link className="navbar-brand" to="/">
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
              className="d-flex bg-dark rounded align-items-center justify-content-center p-2 me-5"
              style={{ height: "38px" }}
              onSubmit={handleSubmit}
            >
              <i className="bi bi-search mx-1"></i>
              <input
                className="ms-1 me-5 bg-dark"
                type="search"
                placeholder="Search"
                aria-label="Search"
                style={{ border: "none", outline: "none", color: "#ccd1d5" }}
                onChange={(e) => {
                  setFilterWord(e.target.value);
                }}
              />
            </form>
            <ul className="navbar-nav mb-2 mb-lg-0">
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
