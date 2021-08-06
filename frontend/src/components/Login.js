import React, { useState } from "react";
import {
    Button,
    Form,
    Label,
    FormGroup,
    Input
  } from "reactstrap";
import "./Login.css";

export default function Login(props) {
  console.log(props);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  function validateForm() {
    return email.length > 0 && password.length > 0;
  }

  function handleSubmit(event) {
    event.preventDefault();
  }
  function onLogin() {
    props.history.push("/");
  }
  return (
    <div className="Login">
      <Form onSubmit={handleSubmit}>
        <FormGroup size="lg" controlId="email">
          <Label>Email</Label>
          <Input
            autoFocus
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </FormGroup>
        <FormGroup size="lg" controlId="password">
          <Label>Password</Label>
          <Input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </FormGroup>
        <Button block size="lg" type="submit" disabled={!validateForm()}  onClick={() => onLogin()}>
          Login
        </Button>
      </Form>
    </div>
  );
}