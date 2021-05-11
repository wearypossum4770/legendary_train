/** @format */

import Board from "./Board";
import { useState, useRef, useReducer } from "react";
const Game = () => {
  const canvasRef = useRef(null);
  const [scene, setScene] = useState({ width: "480", height: "270" });

  return (
    <div>
      <canvas ref={canvasRef} style={scene}></canvas>
    </div>
  );
};
export default Game;
