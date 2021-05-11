/** @format */

import { useState } from "react";
/**
 * @function ChatMessage
 * @param {Object} arguments
 * @param {{
 * type:string,
 * sender:string,
 * content:string,
 * date: new Date
 * }} arguments
 * @param {boolean} arguments.socketRef
 * @param {string} arguments.roomName
 * @default
 * arguments.setSendMessage false
 * arguments.setSendMessage null
 * @returns
 */
let username = "lLawliet";
export default function ChatMessage({ socketRef, roomName }) {
  const [isResponding, setIsResponding] = useState(false);
  const [message, setMessage] = useState();
  const handleChange = ({ target: { name, value } }) =>
    setMessage({ ...message, [name]: value });
  const handleSendMessage = async () => {
    if (socketRef.readyState === 3) {
      console.log("Reconnecting to the chat server...");
      socketRef.connect(roomName);
    }
    if (socketRef.readyState === 1) {
      socketRef.send(
        JSON.stringify({
          command: "new_message",
          message: message.message,
          from: username,
          date: Date.now(),
        }),
      );
      console.log("\n\nsending...\n\n");
      setIsResponding(false);
      document.getElementById("message box").value = "";
    }
  };
  const handleSubmit = async e => [e.preventDefault(), handleSendMessage()];
  return (
    <div className="container">
      <div>{isResponding ? `${username} is typing` : null}</div>
      <form className="w3-container" onSubmit={handleSubmit}>
        <label>
          Message:
          <input
            id="message box"
            onBlur={() => setIsResponding(false)}
            onFocus={() => setIsResponding(true)}
            className="w3-input"
            name="message"
            onChange={handleChange}
          />
        </label>
        <button
          className="w3-btn w3-grey"
          onClick={handleSendMessage}
          type="button"
        >
          Send Message
        </button>
      </form>
    </div>
  );
}
