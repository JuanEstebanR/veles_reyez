import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Home from './components/home/home.jsx'
import Signin from "./components/signin/signin.jsx";
import Signup from "./components/signup/signup.jsx";
import Dashboard from "./components/dashboard/dashboard.jsx";
import './App.css'

function App() {

  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/signin" element={<Signin />} />
            <Route path="/signup" element={<Signup />} />
            <Route path="/dashboard" element={<Dashboard />} />
        </Routes>
      </BrowserRouter>
    </>
  )
}

export default App
