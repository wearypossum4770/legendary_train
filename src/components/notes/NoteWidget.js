/** @format */

import localforage from "localforage";
export default function NoteWidget({ note, setNote }) {
  const handleSubmit = e => {
    e.preventDefault();
    // let formData = new FormData([form]);
    console.log(e);
  };
  const handleChange = ({ target: { name, value } }) =>
    setNote({ ...note, [name]: value });
  const handleReset = () => {
    note = null;
    setNote({ title: "", content: "" });
  };
  return (
    <form id="add-note">
      <label htmlFor="title">
        <input
          onChange={handleChange}
          autoFocus
          id="add-note"
          className="note-widget"
          placeholder="Title"
          name="title"
        />
      </label>
      <label htmlFor="content">
        <textarea
          onChange={handleChange}
          id="content"
          className="note-widget"
          placeholder="Note Content"
          name="content"
        ></textarea>
      </label>
      <button type="submit" onSubmit={handleSubmit}>
        Add Note
      </button>
      <button type="reset" onClick={handleReset} onReset={handleReset}>
        Clear
      </button>
    </form>
  );
}
