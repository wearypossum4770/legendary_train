/** @format */
// https://www.w3schools.com/HOWTO/howto_js_slideshow.asp
import * as systemAvatar from "./computer.png";
import * as lightYagami from "./lightYagami.jpg";
import * as lLawliet from "./lLawliet.jpg";
/**
 * @function ChatList
 * @param {Object} arguments
 * @param {Array.<Object>}messageList
 * @param {boolean} arguments.setSendMessage
 * @default
 * arguments.setSendMessage false
 * arguments.setSendMessage null
 * @returns
 */
export default function ChatList({ messageList }) {
  let themeSwitcher = from =>
    new Map([
      ["systemMessage", "darker"],
      ["lLawliet", "darkest"],
      ["lightYagami", ""],
    ]).get(from);
  let imageMapper = source =>
    new Map([
      ["lightYagami", lightYagami.default],
      ["lLawliet", lLawliet.default],
      ["admin1", systemAvatar.default],
      ["admin2", systemAvatar.default],
      ["systemMessage", systemAvatar.default],
    ]).get(source);
  return (
    <>
      {messageList.map((msg, index) => (
        <div
          key={Number.isNaN(msg.id) ? index : msg.id}
          className={`container ${themeSwitcher(msg.author)}`}
        >
          <div>{msg.author}</div>
          <img
            src={imageMapper(msg.author)}
            alt="Avatar"
            style={{ width: "100%" }}
          />
          <p>{msg.content}</p>
          <span className="time-right">
            {new Date(msg.timestamp).toLocaleTimeString("en-US")}
          </span>
        </div>
      ))}
    </>
  );
}
