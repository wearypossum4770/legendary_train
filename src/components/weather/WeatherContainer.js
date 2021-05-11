/** @format */

import { useEffect, useReducer } from "react";
import { reducer, initialState } from "./weather_helpers";
import WeatherWidget from "./WeatherWidget";
export default function WeatherContainer() {
  const [state, dispatch] = useReducer(reducer, initialState);
  function geoFindMe() {
    if (state.locationObtained) {
      return;
    }
    const success = position => {
      const { latitude, longitude } = position.coords;
      dispatch({
        type: "SET_LOCATION",
        payload: { latitude: latitude, longitude: longitude },
      });
    };
    const error = () => alert("couldn't get your location");
    if (!navigator.geolocation) {
      alert(`Your browser doesn't support this feature`);
      return;
    }
    navigator.geolocation.getCurrentPosition(success, error);
  }
  useEffect(() => {});
  const { locationObtained } = state;
  console.log(state);
  return (
    <div>
      {locationObtained ? (
        <WeatherWidget />
      ) : (
        <button
          onClick={geoFindMe}
          style={{ textAlign: "center", fontSize: "25px" }}
          className="btn"
        >
          <span>🌎</span> Locate Me
        </button>
      )}
    </div>
  );
}
