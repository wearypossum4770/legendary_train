/** @format */

import React from "react";
import { render } from "react-dom";
import "./index.css";
import App from "./app/App";
import reportWebVitals from "./core/reportWebVitals";
import * as serviceWorkerRegistration from "./core/serviceWorkerRegistration";
import dotenv from "dotenv/config";
render(
  <React.StrictMode>
    <App environment={dotenv} />
  </React.StrictMode>,
  document.getElementById("root"),
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://cra.link/PWA
serviceWorkerRegistration.unregister();
