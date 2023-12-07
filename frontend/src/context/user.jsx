import { createContext, useEffect, useState } from "react";
import { getUser } from "../services/user";
import { getToken, removeToken, saveToken } from "../services/token";

export const UserContext = createContext();

export function UserProvider({ children }) {
  const [user, setUser] = useState({
    username: null,
    id: null,
    isActive: null,
    isAdmin: null,
  });
  const [token, setToken] = useState("");
  const [isLoadingUser, setIsLoadingUser] = useState(true);

  function updateToken(new_token) {
    setToken(new_token);
    saveToken(new_token);
  }

  function deleteToken() {
    setToken("");
    removeToken();
  }

  function updateUser() {
    if (token) {
      getUser(token)
        .then((res) => {
          setUser({
            ...user,
            username: res.data.username,
            id: res.data.id,
            isActive: res.data.is_active,
            isAdmin: res.data.is_admin,
          });
          setIsLoadingUser(false);
        })
        .catch((err) => {});
    } else {
      setUser({
        username: null,
        id: null,
        isActive: null,
        isAdmin: null,
      });
      if (token === null) {
        setIsLoadingUser(false);
      }
    }
  }

  useEffect(() => {
    setToken(getToken());
  }, []);

  useEffect(() => {
    updateUser();
  }, [token]);

  return (
    <UserContext.Provider
      value={{
        user,
        token,
        setUser,
        updateToken,
        setToken,
        deleteToken,
        isLoadingUser,
      }}
    >
      {children}
    </UserContext.Provider>
  );
}
