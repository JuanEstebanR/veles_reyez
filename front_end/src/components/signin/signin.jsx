import axios from "axios";
import { useState } from "react";
import { Link } from "react-router-dom";
function Signin() {
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
        "http://localhost:8000/googletopterms/login/",
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
      <div style={{marginTop: "60px"}}>
        <h1
          style={{
            fontSize: 80,
            fontWeight: "bold",
            color: "#C292FF",
            marginTop: "20px",
              fontFamily: "Railway",
          }}
        >
          GOOGLE TOP TERMS
        </h1>
      </div>
      <div>
        <div>
          <h1 style={{ color: "white", fontSize: "40px", fontWeight: "bold", fontFamily: "Railway", }}>
            Welcome Again
          </h1>
        </div>
        <form onSubmit={sendForm}>
          <div style={{ marginBottom: "10px", marginTop: "10px" }}>
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
                color: "#C292FF",
                backgroundColor: "#F2F2F2",
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
                marginTop: "20px",
                color: "#C292FF",
                background: "black",
                border: "none",
              }}
            >
              Sign In
            </button>
          </div>
        </form>
        <div style={{ marginTop: "10px" }}>
          <p style={{ color: "white", fontFamily: "Railway", }}>
            Dont have an account?{" "}
            <Link to="/signup" style={{ color: "#C292FF" }}>
              Create One
            </Link>
          </p>
        </div>
        <div>
          <p style={{ marginTop: "10px", color: "red", fontWeight: "bold" }}>
            {errorMessage}
          </p>
        </div>
      </div>
    </div>
  );
}

export default Signin;
