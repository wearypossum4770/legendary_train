/** @format */

const TodoList = ({ todosList, setDisplay }) => (
  <div className="todo-container">
    <div className="select">
      <select
        onSelect={({ target: { value } }) => setDisplay(value)}
        onChange={({ target: { value } }) => setDisplay(value)}
        name="todos"
        className="filter-todo"
      >
        <option value="all">All</option>
        <option value="completed">Completed</option>
        <option value="uncompleted">Uncompleted</option>
        <option value="archived">Archived</option>
        <option value="deleted">Deleted</option>
      </select>
    </div>
    <ul type="none" className="todo-list">
      {todosList.map(todo => (
        <li className="w3-bar">
          <input
            type="checkbox"
            onclick="this.parentElement.style.display='none'"
            className="w3-bar-item w3-button w3-xlarge w3-right"
            checked={todo.completed}
          />
          <span className="w3-bar-item w3-circle" style={{ width: "85px" }}>
            {todo.id}
          </span>
          <div className="w3-bar-item">
            <span className="w3-large">{todo.content}</span>
            <br />
            {/* <span>Web Designer</span> */}
          </div>
        </li>
      ))}
    </ul>
  </div>
);
export default TodoList;
