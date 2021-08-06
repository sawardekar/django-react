import React, { Component } from "react";
import Home from "./components/Homepage";
import Student from "./components/Student";
import Login from "./components/Login";
import {
  BrowserRouter as Router,
  Switch,
  Route
} from "react-router-dom";

class App extends Component {

  render() {
    return (
      <main className="container">
      <Router>
        <Switch>
          <Route exact path="/student">
            <Student />
          </Route>
          <Route exact path="/">
            <Home />
          </Route>
          <Route exact path="/login" component={(props)=><Login {...props}/>}>
            
          </Route>
        </Switch>
        </Router>
      </main>
    );
  }
}

export default App;