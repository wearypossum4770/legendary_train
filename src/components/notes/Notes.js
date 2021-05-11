/** @format */
import { useState, useReducer } from "react";
export default function Notes({ notes }) {
  //   const handleClick = () => setNote({ ...note, visible: true });
  //   const handleChangeNote = (value, key, obj = "notes") =>
  //     setNote({ ...note, [obj]: { ...note[obj], [key]: value } });
  //   const addToNotes = () => {
  //     const notes_list = note.note_list;
  //   };
  const [isActive, setActive] = useState("false");
  const [toggleNote, setToggleNote] = useState("none");
  const handleToggle = () => setActive(!isActive);
  return (
    <div>
      {notes.map(note => (
        <span key={note.id} id={note.id} onClick={handleToggle}>
          <div className="w3-panel w3-card">
            <p>{note.title}</p>
            {isActive ? (
              <div style={{ display: toggleNote }}>
                <p>{note.content}</p>
                <button
                  className="actions"
                  shortcode=":wastebasket:"
                  content="🗑️"
                >
                  <span>delete 🗑️</span>
                </button>
                <button
                  className="actions"
                  shortcode=":down_inbox_trayarrow:"
                  content="📥"
                >
                  <span>archive 📥</span>
                </button>
              </div>
            ) : null}
          </div>
        </span>
      ))}
    </div>
  );
}
