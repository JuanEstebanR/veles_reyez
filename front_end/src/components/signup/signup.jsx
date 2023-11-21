import axios from "axios";
import { useState } from "react";
import { Link } from "react-router-dom";

function Signup() {
  const [data, setData] = useState({ username: "", password: "" });
  const [errorMessage, setErrorMessage] = useState("");
  const handleUsernameChange = (event) => {
    setData({ ...data, username: event.target.value });
  };

  const handlePasswordChange = (event) => {
    setData({ ...data, password: event.target.value });
  };
  const sendForm = async (e) => {
    e.preventDefault();
    try {
        setData({ username: "", password: "" })
      const response = await axios.post(
        "http://localhost:8000/googletopterms/register/",
        { username: data.username, password: data.password },
      );
    } catch (err) {
      console.log(err);
    }
  };
  return (
    <div
      style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "20px" }}
    >
      <div>
        <h1
          style={{
            fontSize: 80,
            fontWeight: "bold",
            color: "#C292FF",
            flex: "auto",
              fontFamily: "Railway",
          }}
        >
          GOOGLE TOP TERMS
        </h1>
      </div>
      <div style={{ marginTop: "60px"}}>
        <form onSubmit={sendForm}>
          <div style={{ marginBottom: "10px", marginTop: "20px" }}>
            <input
              type="text"
              placeholder="Enter Username"
              style={{
                  height: "30px",
                  width: "60%",
                  backgroundColor: "#F2F2F2",
                  color: "black",
              }}
              value={data.username}
              onChange={handleUsernameChange}
              required={true}
            />
          </div>
          <div style={{ marginBottom: "10px" }}>
            <input
              type="password"
              placeholder="Password"
              style={{
                  height: "30px",
                  width: "60%",
                  backgroundColor: "#F2F2F2",
                  color: "black",
              }}
              value={data.password}
              onChange={handlePasswordChange}
              required={true}
            />
          </div>
          <div>
            <button
              type="submit"
              style={{
                width: "40%",
                padding: "10px",
                marginTop: "10px",
                color: "#C292FF",
                background: "black",
                border: "none",
              }}
            >
              Sign Up
            </button>
          </div>
        </form>
        <div style={{ marginTop: "10px" }}>
          <p style={{ color: "white", fontFamily: "Railway" }}>
            Do you have an account?{" "}
            <Link to="/signin" style={{ color: "#C292FF" }}>
              Sign In
            </Link>
          </p>
        </div>
        <p style={{ marginTop: "10px", color: "red", fontWeight: "bold" }}>
          {errorMessage}
        </p>
      </div>
    </div>
  );
}

export default Signup;
