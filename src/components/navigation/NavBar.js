/** @format */

import { useState } from "react";
export default function NavBar() {
  let [show, setShow] = useState(false);
  let navMenu = [
    { link: "/", page: "Home", id: 1 },
    { link: "/chat", page: "Chat", id: 2 },
    { link: "/weather", page: "Weather", id: 3 },
    { link: "/solitare", page: "Solitare", id: 4 },
    { link: "/todo", page: "Todo List", id: 5 },
    { link: "/profile/genryusai.shigekuni.yamamoto", page: "Profile", id: 6 },
    { link: "/signature", page: "SignaturePad", id: 7 },
    { link: "/blog", page: "Blog", id: 8 },
  ];
  return (
    <>
      <div className="w3-teal">
        <button
          className="w3-button w3-teal w3-xlarge"
          onClick={() => setShow(!show)}
        >
          ☰
        </button>
        <div className="w3-container">
          <h1>My Page</h1>
        </div>
      </div>
      {show ? (
        <div className="w3-sidebar w3-bar-block" id="mySidebar">
          <button
            onClick={() => setShow(false)}
            className="w3-bar-item w3-button w3-large"
          >
            Close &times;
          </button>

          {navMenu.map(nav => (
            <a key={nav.id} href={nav.link} className="w3-bar-item w3-button">
              {nav.page}
            </a>
          ))}
        </div>
      ) : null}
    </>
  );
}
