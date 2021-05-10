/** @format */

import { useState } from "react";
import "./board_style.css";
import Square from "./Square";
export default function Board({ state: { nextPiece } }) {
  const renderSquare = piece => <Square value={piece} />;
  const status = `Next Player:${nextPiece}`;
  return (
    <div>
      <button>Recall Piece</button>
      <div className="status">{status}</div>
      <div className="board-row">
        {renderSquare(0)}
        {renderSquare(1)}
        {renderSquare(2)}
      </div>
      <div className="board-row">
        {renderSquare(3)}
        {renderSquare(4)}
        {renderSquare(5)}
      </div>
      <div className="board-row">
        {renderSquare(6)}
        {renderSquare(7)}
        {renderSquare(8)}
      </div>
    </div>
  );
}
