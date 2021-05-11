/** @format */
/**
 * @todo
 * - use websocket context
 * - chatcontainer passes roomname to websoket context
 */
import { useEffect } from "react";
import { useParams } from "react-router-dom";
import ChatRoom from "./ChatRoom";
import WebSocketInstance from "../../adapters/WebSocketService";
import "./message.css";
export default function ChatContainer() {
  ChatContainer.displayName = "chat_container";
  let { roomName } = useParams();
  useEffect(() => {
    WebSocketInstance.connect(roomName.roomName);
  }, [roomName]);
  return (
    <div>
      <ChatRoom
        socket={WebSocketInstance}
        currentUser="lightYagami"
        roomName={roomName}
      />
    </div>
  );
}
