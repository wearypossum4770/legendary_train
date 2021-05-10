/** @format */
let toatTitle = "Oops!!";
const toastMessage = (
  <span>
    <p>The chat app stop unexpectedly</p>
    <p>Troubleshoot Steps:</p>
    <ul>
      <li>If this is your first time seeing this message</li>
      <ol>
        <li>
          Save all unsaved work (Documents-Microsoft Word, spreadsheets-
          Microsoft Excel, etc).
        </li>
        <li>Close your browswer (the program).</li>
        <li>Restart your computer.</li>
        <li>Try to come back to this page again.</li>
      </ol>
      <li>If this is not your first time seeing this message.</li>
      <ol>
        Don't panic, I have already notified customer service of the issue.
      </ol>
    </ul>
  </span>
);
export default function TostNotification() {
  return (
    <div className="w3-container">
      <div className="w3-panel w3-pale-red w3-leftbar w3-border-red">
        <h1>{toatTitle}</h1>
        {toastMessage()}
      </div>
    </div>
  );
}
