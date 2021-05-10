/** @format */
import { useState } from "react";
import array from "./todoinit";
import TodoList from "./TodoList";
//

const Form = ({ setTodosList, todosList, todo, setTodo }) => {
  const handleChange = ({ target: { name, value } }) =>
    setTodo({ ...todo, [name]: value });
  const toggleCheckbox = ({ target: { name, value } }) =>
    setTodo({ ...todo, [name]: value === "off" ? false : true });
  return (
    <form className="w3-container" onSubmit={e => e.preventDefault()}>
      <label htmlFor="todo title">
        Todo Title:{" "}
        <input className="w3-input" name="title" onChange={handleChange} />
      </label>
      <label htmlFor="todo content">
        Todo Content:{" "}
        <input className="w3-input" name="content" onChange={handleChange} />
      </label>
      <label htmlFor="mark as completed">
        Completed?
        <input
          className="w3-input"
          type="checkbox"
          name="completed"
          onChange={toggleCheckbox}
          onInput={toggleCheckbox}
        />
      </label>
      <label htmlFor="mark as Archived">
        Archived?
        <input
          className="w3-input"
          type="checkbox"
          name="archived"
          onChange={toggleCheckbox}
          onInput={toggleCheckbox}
        />
      </label>
      <label htmlFor="mark as Deleted">
        Deleted?
        <input
          className="w3-input"
          type="checkbox"
          name="deleted"
          onChange={toggleCheckbox}
          onInput={toggleCheckbox}
        />
      </label>
      <button
        className="w3-btn"
        onClick={() => setTodosList([...todosList, { isLocal: true, ...todo }])}
      >
        Add Note... <i className="fas fa-plus-square"></i>
      </button>
    </form>
  );
};
export const displayTodo = (arr, predicate) => {
  switch (predicate) {
    default:
      return arr;
    case "deleted":
      return arr.filter(todo => todo.isDeleted === true);
    case "archived":
      return arr.filter(
        todo => todo.isArchived === true && todo.isDeleted !== true,
      );
    case "all":
      return arr;
    case "completed":
      return arr.filter(
        todo =>
          todo.completed === true &&
          todo.isDeleted === false &&
          todo.isArchived === false,
      );
    case "uncompleted":
      return arr.filter(
        todo =>
          todo.completed === false &&
          todo.isDeleted === false &&
          todo.isArchived === false,
      );
  }
};
export const getAllIds = arr => arr.map(todo => todo.id);
export const getLastId = arr => getAllIds(arr).slice(-1).pop();
export const getNextId = arr => getLastId(arr) + 1;
export const getById = (arr, _id) => arr.filter(todo => todo.id === _id).pop();
export const addNewTodo = (arr, data) => [
  ...arr,
  { id: getNextId(arr), ...data },
];
export default function Todo() {
  const [display, setDisplay] = useState("all");
  const [todo, setTodo] = useState();
  const [todosList, setTodosList] = useState(array);
  return (
    <div>
      <div>
        <Form
          setTodosList={setTodosList}
          todo={todo}
          todosList={todosList}
          setTodo={setTodo}
        />
      </div>
      <div>
        <TodoList
          setDisplay={setDisplay}
          todosList={displayTodo(todosList, display)}
        />
      </div>
    </div>
  );
}
