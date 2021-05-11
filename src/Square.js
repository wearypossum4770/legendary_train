/** @format */

import { useState } from "react";
let player = 1;
const Square = () => {
  const renderSelection = player => (player === 1 ? "X" : "O");
  const placePiece = () => null;
  const playPiece = () => null;
  const recallPiece = () => null;
  const [next, setNext] = useState(true);
  const [piece, setPiece] = useState();
  return (
    <button
      onClick={() => setPiece(renderSelection(player))}
      className="square"
    >
      {piece}
    </button>
  );
};

export default Square;
