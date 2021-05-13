/** @format */
import "./App.css";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import Home from "../components/home/Home";
import ChatContainer from "../components/chat/ChatContainer";
import NavBar from "../components/navigation/NavBar";
import ChatLobby from "../components/chat/ChatLobby";
import WeatherContainer from "../components/weather/WeatherContainer";
import SolitareHand from "../components/solitare/SolitareHand";
import Todo from "../components/todo/ToDo";
import Profile from "../components/profile/Profile";
import Signature from "../components/signatures/Signature";
import Blog from "../components/blog/Blog";
import Post from "../components/blog/Post";
export default function App() {
  return (
    <div data-testid="rendered-app">
      <NavBar />
      <Router>
        <Switch>
          <Route exact path="/blog" component={Blog} />
          <Route exact path="/blog/:post_id" component={Post} />
          <Route exact path="/signature" component={Signature} />
          <Route exact path="/" component={Home} />
          <Route exact path="/chat" component={ChatLobby} />
          <Route exact path="/chat/:roomName" component={ChatContainer} />
          <Route exact path="/weather" component={WeatherContainer} />
          <Route exact path="/solitare" component={SolitareHand} />
          <Route exact path="/todo" component={Todo} />
          <Route exact path="/profile/:username" component={Profile} />
        </Switch>
      </Router>
      <footer className="w3-container w3-bottom w3-theme w3-margin-top">
        <h3></h3>
      </footer>
    </div>
  );
}
