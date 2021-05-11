/** @format */
class WebSocketService {
  // /https://www.fullstackdjango.com/post/django-channels-and-react-a-match-made-in-heaven
  static instance = null;
  callbacks = new Map();
  static getInstance() {
    if (!WebSocketService.instance) {
      WebSocketService.instance = new WebSocketService();
    }
    return WebSocketService.instance;
  }
  constructor() {
    this.socketRef = null;
  }
  connect(roomName) {
    this.socketRef = new WebSocket(`ws://127.0.0.1:8000/ws/chat/${roomName}/`);
    this.socketRef.onopen = () => {
      console.log("WebSocket open");
    };
    this.socketNewMessage(
      JSON.stringify({
        command: "fetch_messages",
      }),
    );
    this.socketRef.onmessage = ({ data }) => {
      this.socketNewMessage(data);
    };
    this.socketRef.onerror = ({ message }) => {
      console.log(message);
    };
    this.socketRef.onclose = () => {
      console.log("WebSocket closed let's reopen");
      this.connect(roomName);
    };
  }
  disconnect() {
    this.socketRef.close();
  }
  socketNewMessage(data) {
    const { command, message, messages } = JSON.parse(data);
    if (this.callbacks.size === 0) {
      return;
    }
    if (command === "messages") {
      this.callbacks.get(command)(messages);
    }
    if (command === "new_message") {
      this.callbacks.get(command)(message);
    }
  }
  fetchMessages(username, chat_id) {
    this.sendMessage({
      command: "fetch_messages",
      username: username,
      chat_id: chat_id,
    });
  }
  newChatMessage({ chat_id, from, content }) {
    this.sendMessage({
      command: "new_message",
      from: from,
      message: content,
      chat_id: chat_id,
    });
  }
  addCallbacks(messagesCallback, newMessageCallback) {
    this.callbacks.set("messages", messagesCallback);
    this.callbacks.set("new_message", newMessageCallback);
  }
  sendMessage(data) {
    try {
      this.socketRef.send(JSON.stringify({ ...data }));
    } catch (err) {
      console.log(err.message);
    }
  }
  state() {
    return this.socketRef.readyState;
  }
}
const WebSocketInstance = WebSocketService.getInstance();
export default WebSocketInstance;
