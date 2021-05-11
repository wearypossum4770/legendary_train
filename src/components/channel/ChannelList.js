/** @format */

import { useState } from "react";
export default function ChannelList() {
  let [show, setShow] = useState(false);
  const handleClose = () => setShow(false);
  //prettier-ignore
  let channels = [
    { id: 1, status: "connected", roomName: "greetings", participants: 10 },
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
            onClick={handleClose}
            className="w3-bar-item w3-button w3-large"
          >
            Close &times;
          </button>

          {channels.map(channel => (
            <a
              key={channel.id}
              href={`chat/${channel.roomName}`}
              className="w3-bar-item w3-button"
            >
              {channel.roomName}
            </a>
          ))}
        </div>
      ) : null}
    </>
  );
}
