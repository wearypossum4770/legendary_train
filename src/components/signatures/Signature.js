/** @format */

import { useEffect, useRef, useReducer } from "react";
import { initialState, reducer } from "./helpers";
import Point from "./Point";
//https://github.com/szimek/signature_pad/tree/master/src
//https://codepen.io/kunukn/pen/kkbNvx
const clear = (ctx, canvas) => {
  ctx.fillStyle = this.backgroundColor;
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.fillRect(0, 0, canvas.width, canvas.height);
};

export default function Signature(props) {
  const canvasRef = useRef(null);

  const [state, dispatch] = useReducer(reducer, initialState);
  const strokeBegin = e => {
    let pointGroup = { color: state.penColor, points: [] };
    state.onBegin();
  };
  const strokeEnd = e => null;
  const strokeMoveUpdate = e => console.log(e);
  const handleMouseDown = e => {
    if (e.nativeEvent.which === 1) {
      dispatch({ type: "MOUSE_DOWN" });
      strokeBegin();
    }
  };
  const handleMouseUp = e => {
    if (e.nativeEvent.which === 1 && state.mouseButtonDown) {
      dispatch({ type: "MOUSE_UP" });
      strokeEnd();
    }
  };
  const handleMouseMove = e => {
    if (state.mouseButtonDown) {
      strokeMoveUpdate(e);
    }
  };
  const handleTouchStart = e => console.log(e);
  const handleTouchMove = e => console.log(e);
  const handleTouchEnd = e => console.log(e);

  useEffect(() => {
    const canvas = canvasRef.current;
    const context = canvas.getContext("2d");
    //Our first draw
    Object.assign(context, state);
    context.fillStyle = state.penColor;
  }, []);

  return (
    <div>
      <canvas
        ref={canvasRef}
        height="200"
        width="400"
        onMouseDown={handleMouseDown}
        onMouseUp={handleMouseUp}
        onMouseMove={handleMouseMove}
        onTouchEnd={handleTouchEnd}
        onTouchMove={handleTouchMove}
        onTouchStart={handleTouchStart}
        {...props}
      />
    </div>
  );
}
