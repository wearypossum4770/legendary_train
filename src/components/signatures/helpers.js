/** @format */

export const initialState = {
  get dotSize() {
    return (this.minWidth + this.maxWidth) / 2;
  },
  velocityFilterWeight: 0.7,
  minWidth: 0.5,
  maxWidth: 2.5,
  throttle: 16,
  minDistance: 5,
  backgroundColor: "rgba(0,0,0,0)",
  penColor: "black",
  points: [],
  data: [],
  isEmpty: true,
  mouseDown: false,
  get fillStyle() {
    return this.penColor;
  },
  get lastWidth() {
    return (this.minWidth + this.maxWidth) / 2;
  },
  touchStart: false,
  onBegin: () => null,
  onEnd: () => null,
  mouseButtonDown: false,
  onTouchStart: ({ target }) => console.log(target.value),
  onTouchMove: () => null,
  onTouchEnd: () => null,
  onTouchCancel: () => null,
};

export function reducer(state, action) {
  switch (action.type) {
    default:
      return { ...state };
    case "STROKE_BEGIN":
      return { ...state };
    case "MOUSE_DOWN":
      return { ...state, mouseButtonDown: true };
    case "MOUSE_UP":
    case "RESET":
      return {
        ...state,
        lastPoints: [],
        lastVelocity: 0,
        fillStyle: state.penColor,
        lastWidth: (state.minWidth + state.maxWidth) / 2,
      };

      return { ...state, mouseButtonDown: false };
  }
}
