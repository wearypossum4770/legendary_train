/** @format */
// getDataUpdate
let status = ["idle", "resolved", "rejected"];

export const getUniqueID = () => {
  const s4 = () =>
    Math.floor((1 + Math.random()) * 0x10000)
      .toString(16)
      .substring(1);
  return s4() + s4() + "-" + s4();
};
// https://zetcode.com/javascript/reduce/
const getAllIds = array => array.map(obj => obj.id).sort((a, b) => a - b);
const missingValues = [];
const findMissingValues = array => array;
const getLastId = array => array.pop();
const getNextId = value => value + 1;
const checkDuplicate = (prevState, state) => {
  let previousState = new Set(prevState.map(obj => obj.id));
  let target = state.filter(obj => !previousState.has(obj.id));
  return [...prevState, ...target];
};
const localTimeStamp = array =>
  array.map(item => new Date(item.date).toLocaleString());
//prettier-ignore
let initData = [{id: 1,type: "message",sender: "systemMessage",date: "2021-04-23T21:09:23.455Z",content:"\nYou are connected to chat...\nYou may send a message when ready.",},{id: 2,type: "message",sender: "lLawliet",date: "2021-04-23T21:09:38.616Z",content: "Light..",},{id: 3,type: "message",sender: "lLawliet",date: "2021-04-23T21:09:39.211Z",content: "Light Yagami",},{id: 4,type: "message",sender: "lLawliet",date: "2021-04-23T21:10:05.621Z",content:"You're father is Cheif Soichiro Yagami of the NPA? Your respect for you father is only matched by your strong sense of justice.",},{id: 5,type: "message",sender: "lightYagami",date: "2021-04-23T21:10:14.121Z",content: "Who the hell is this guy?",},];
let messagePipes = [getAllIds, findMissingValues, getLastId, getNextId];
/**
 * @function messageNextId -
 * Is a curried function that takes,
 * an array of objects and calculates the nextHighest ID
 * @param {Array.<Object>} array
 * @returns {number}
 */
const messageNextId = array =>
  messagePipes.reduce((total, fn) => fn(total), array);

console.log(messageNextId(initData));
// API_BASE
// WS_BASE
function reducer(state, action) {
  switch (action.type) {
    default:
      return { ...state };
    case "ADD_MESSAGE":
      return { ...state };
    case "AUTH_FAIL":
      return { ...state };
    case "AUTH_LOGOUT":
      return { ...state };
    case "AUTH_START":
      return { ...state };
    case "AUTH_SUCCESS":
      return { ...state };
    case "CLOSE_ADD_CHAT_POPUP":
      return { ...state };
    case "CREATE_ROOM_ERROR":
      return { ...state };
    case "CREATE_ROOM_REQUEST":
      return { ...state };
    case "CREATE_ROOM_SUCCESS":
      return { ...state };
    case "GET_CHATS_SUCCESS":
      return { ...state };
    case "HEARTBEAT":
      return { ...state };
    case "JOIN_ROOM_ERROR":
      return { ...state };
    case "JOIN_ROOM_REQUEST":
      return { ...state };
    case "JOIN_ROOM_SUCCESS":
      return { ...state };
    case "OPEN_ADD_CHAT_POPUP":
      return { ...state };
    case "RECEIVE_MESSAGE":
      return { ...state };
    case "RENDER_MESSAGE":
      return { ...state };
    case "SEND_MESSAGE":
      return { ...state };
    case "SEND_MESSAGE_REQUEST":
      return { ...state };
    case "SET_MESSAGE":
      return { ...state };
    case "SET_MESSAGES":
      return { ...state };
    case "SET_USERNAME":
      return { ...state };
    case "UPDATE_CHAT_LOG":
      return { ...state };
  }
}
