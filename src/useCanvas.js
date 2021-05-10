/** @format */

import { useEffect, useRef } from "react";
export default function useCanvas() {
  const canvasRef = useRef(null);
  useEffect(() => {
    const context = canvasRef.current.getContext("2d");
  }, [canvasRef]);
  return <canvas ref={canvasRef} />;
}
