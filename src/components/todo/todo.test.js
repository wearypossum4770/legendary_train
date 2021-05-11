/** @format */
import { addNewTodo, getById, displayTodo } from "./ToDo";
import { testCases } from "./todoinit";
let updatedTodo = addNewTodo(testCases, {
  title: "New Note",
  content: "Test creation of new todo item.",
  isDeleted: false,
  isArchived: false,
  completed: false,
  isLocal: true,
});
let all = displayTodo(testCases, "all");
let allUpdatedTodo = displayTodo(updatedTodo, "all");
let deleted = displayTodo(testCases, "deleted");
let archived = displayTodo(testCases, "archived");
let completed = displayTodo(testCases, "completed");
let uncompleted = displayTodo(testCases, "uncompleted");
let getTodo = getById(testCases, 4);
let lastTodo = updatedTodo.slice(-1).pop();
describe("Todo functionality", () => {
  test("creation of new todo item", () => {
    expect(lastTodo.isLocal).toBe(true);
    expect(lastTodo.completed).toBe(false);
    expect(lastTodo.title).toBe("New Note");
    expect(lastTodo.id).toBe(9);
    expect(lastTodo.content).toBe("Test creation of new todo item.");
  });
  test("Display all todo items", () => {
    expect(all.length).toBe(8);
  });
  test("Get todo By Id", () => {
    expect(getTodo.id).toStrictEqual(4);
  });
  test("completed only", () => {
    expect(completed[0].content).toMatch(/Learn React/i);
  });
  test("completed and deleted", () => {
    expect(deleted[0].content).toMatch(/Learn Redux/i);
  });
  test("completed and archived", () => {
    expect(archived[0].content).toMatch(/Build something fun!/i);
  });
  test("completed, archived and deleted", () => {
    expect(deleted[1].content).toMatch(/Do the dishes/i);
  });
  test("uncompleted only", () => {
    expect(uncompleted[0].content).toMatch(/take out the trash/i);
  });
  test("uncompleted and deleted", () => {
    expect(deleted[2].content).toMatch(/Check Facebook/i);
  });
  test("uncompleted and archived", () => {
    expect(archived[1].content).toMatch(/Finish doing laundry/i);
  });
  test("uncompleted, archived and deleted", () => {
    expect(deleted[3].content).toMatch(/Watch the news/i);
  });
  test("all after todo", () => {
    expect(allUpdatedTodo.length).toBe(9);
  });
});
