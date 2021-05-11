/** @format */

import { useEffect, useReducer } from "react";
import TripleToggle from "./TripleToggle";
// import useFetchData from '../../adapters/useFetchData'
import WeatherWidget from "./WeatherWidget";
import { reducer, initialState } from "./weather_helpers";

let temp = "fake data";
let feels_like = "fake data";
let temp_min = "fake data";
let temp_max = "fake data";
const WeatherContainer = () => {
  const [state, dispatch] = useReducer(reducer, initialState);
  function geoFindMe() {
    let target = {};
    function success(position) {
      let { latitude, longitude } = position.coords;
      dispatch({
        type: "SET_LOCATION",
        payload: { latitude: latitude, longitude: longitude },
      });
      return;
      // message.classList.add('success');
      // message.textContent = `Your location: (${latitude},${longitude})`;
    }
    const error = () => (target["err"] = "Unable to retrieve your location");

    // message.classList.add('error');
    // message.textContent = `Failed to get your location!`;
    if (!navigator.geolocation) {
      console.log(`Your browser doesn't support Geolocation`);
      return;
    }
    navigator.geolocation.getCurrentPosition(success, error);
    console.log(target);
    return target;
  }
  const getLocation = () => {
    let { latitude, longitude } = geoFindMe();
    console.log(latitude);

    dispatch({ type: "SET_WEATHER" });
  };
  console.log(state);
  const { weatherObtained } = state;
  // let WEATHER_API_KEY = "0d379932ab8f74b262973b9886276755"
  // let {response,error} = useFetchData({ url : `https://api.openweathermap.org/data/2.5/weather?lat=${latitude}&lon=${longitude}&appid=${WEATHER_API_KEY}`})
  // let { temp, feels_like, temp_min, temp_max, id } = state.weather;
  useEffect(() => {});
  return !weatherObtained ? (
    <div>
      <button onClick={getLocation}>Get Location</button>obtaining location....
    </div>
  ) : (
    <div>
      <h1>Weather Widget</h1>
      <TripleToggle
        props={{
          temp: temp,
          feels_like: feels_like,
          temp_min: temp_min,
          temp_max: temp_max,
        }}
      />
      <WeatherWidget />
    </div>
  );
};
export default WeatherContainer;
// let accesibleDictionary = new Map();
console.log("🍺 🛋️");
// console.log(id);
// function convertTemperature() {}

// const {
//   main: { temp, feels_like, temp_min, temp_max, pressure, humidity },
//   sys: { sunrise, sunset },
//   timezone,
//   visibility,
//   weather: [{ description, icon, id }],
//   wind: { deg, speed },
//   clouds: { all: cloudinessPercentage },
// }
/**dispatch({
          type: "SET_WEATHER",
          payload: {
            temp: temp,
            visibility: visibility,
            feels_like: feels_like,
            temp_min: temp_min,
            temp_max: temp_max,
            pressure: pressure,
            humidity: humidity,
            sunrise: sunrise,
            sunset: sunset,
            timezone: timezone,
            description: description,
            icon: icon,
            deg: deg,
            id: id,
            speed: speed,
            cloudinessPercentage: cloudinessPercentage,
          },
        }); 
                // "Unable to retrieve your location"
        // "Geolocation is not supported by your browser"
        dispatch({ type: "SET_ERRORS", errors: { ...error } });
        
        
        */
