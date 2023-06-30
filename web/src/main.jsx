import React from "react";
import ReactDOM from "react-dom/client";
import {BrowserRouter} from "react-router-dom"
import Login from "src/pages/LoginPage/Login.jsx";
import Course from "src/pages/CoursePage/Course.jsx";
import Term from "src/pages/TermPage/Term.jsx";
import Chat from "src/pages/ChatPage/Chat.jsx";
import App from "./App.jsx"
import "./index.css";

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </React.StrictMode>
);
