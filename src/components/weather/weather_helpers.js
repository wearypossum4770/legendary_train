/** @format */
function reducer(state, action) {
  switch (action.type) {
    default:
      return { ...state };
    case "SET_LOCATION":
      return {
        ...state,
        latitude: action.payload.latitude,
        longitude: action.payload.longitude,
        locationObtained: true,
      };
    case "USE_CELSIUS":
      return { ...state };
    // case "USE_"
    case "GET_WEATHER":
      return { ...state };
    case "SET_WEATHER":
      return { ...state, weather: action.payload, weatherObtained: true };
    case "SET_ERRORS":
      return { ...state, errors: [...state.errors, [action.errors]] };
  }
}
const initialState = {
  weather: {},
  errors: [],
  locationObtained: false,
  weatherObtained: false,
};

export default function Locator() {
  let target = {};
  function success(position) {
    const { latitude, longitude } = position.coords;
    target["latitude"] = latitude;
    target["longitude"] = longitude;
    // message.classList.add('success');
    // message.textContent = `Your location: (${latitude},${longitude})`;
  }
  function error() {
    // message.classList.add('error');
    // message.textContent = `Failed to get your location!`;
  }
  if (!navigator.geolocation) {
    console.log(`Your browser doesn't support Geolocation`);
    return;
  }
  navigator.geolocation.getCurrentPosition(success, error);
  console.log(target);
  return target;
}
function locationSearch() {}
export { reducer, initialState };
