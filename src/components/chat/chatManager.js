/** @format */

class ChatManager {
  static TYPE_ADMIN = "admin";
  static TYPE_REGULAR = "regular";
  static #MAX_INSTANCES = 2;
  static #instances = 0;
  constructor() {
    this.rooms = [];
    if (ChatManager.#instances > ChatManager.#MAX_INSTANCES) {
      throw new Error("Too many instances of chat");
    }
  }
  connect(roomName) {
    this.rooms.push(roomName);
    ChatManager.#instances++;
  }
  subscribe() {}
  unsubscribe() {}
}
let manager = new ChatManager();
console.log(manager);
// export default function chatManager() {}
