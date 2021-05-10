/** @format */
import { Component } from "react";
import "./message.css";
import Title from "./Title";
import ChatList from "./ChatList";
import WebSocketInstance from "../../adapters/WebSocketService";
import ChatMessage from "./ChatMessage";
// import TostNotification from "./TostNotification";
// let instanceOne = "cknvqmzm10000bum9f0h0fhk4";
// let instanceTwo = "cknvqn1jn0001bum92igm73u1";
// let instanceThree = "cknvqn2fs0002bum99wh6fd14";
// const roomId = 9796712;
export default class ChatRoom extends Component {
  constructor(props) {
    super(props);
    this.state = {
      messageList: [],
    };
    this.waitForSocketConnection(() => {
      WebSocketInstance.addCallbacks(
        this.setMessages.bind(this),
        this.addMessage.bind(this),
      );
      WebSocketInstance.fetchMessages(this.props.currentUser);
    });
  }
  addMessage(message) {
    this.setState({ messageList: [...this.state.messageList, message] });
  }
  setMessages(messages) {
    this.setState({ messageList: messages.reverse() });
  }
  waitForSocketConnection(callback) {
    const component = this;
    setTimeout(function () {
      if (WebSocketInstance.state() === 1) {
        console.log("Connection is made");
        callback();
        return;
      } else {
        console.log("wait for connection...");
        component.waitForSocketConnection(callback);
      }
    }, 100);
  }
  render() {
    const {
      roomName,
      socket: { socketRef },
    } = this.props;
    const { messageList } = this.state;
    return (
      <div>
        <Title roomName={roomName} />
        <ChatList messageList={messageList} />
        <ChatMessage roomName={roomName} socketRef={socketRef} />
      </div>
    );
  }
}
