/** @format */

import { render, screen } from "@testing-library/react";
import App from "./App";

describe("App", () => {
  test("renders learn react link", () => {
    render(<App />);
    const appElement = screen.getByTestId(/rendered-app/i);
    expect(appElement).toBeInTheDocument();
  });
});
