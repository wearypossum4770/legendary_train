/** @format */
import { useState } from "react";
import { useHistory } from "react-router-dom";
export default function ChatLobby() {
  const [roomName, setRoomName] = useState("");
  let history = useHistory();
  const handleEnterRoom = () => history.push(`/chat/${roomName.roomName}`);
  const handleEnterKey = ({ keyCode }) =>
    keyCode === 13 ? handleEnterRoom() : null;
  const handleChange = ({ target: { value, name } }) =>
    setRoomName({ ...roomName, [name]: value });
  return (
    <div className="w3-container">
      Enter room name to continue....
      <label htmlFor="roomName">
        <input
          autoFocus
          onKeyUp={e => handleEnterKey(e)}
          name="roomName"
          onChange={handleChange}
        />
      </label>
      <label htmlFor={`enter ${roomName.roomName} chatroom`}>
        <input type="button" onClick={handleEnterRoom} value="Enter Room!" />
      </label>
    </div>
  );
}
