import { Link } from "react-router-dom";
import Button from 'react-bootstrap/Button';
import HomeCards from "../card/cards.jsx";
import './home.css'
const Home = () => {
    return (
        <div>
            <div>
                <h1 style={{ color: "white", fontSize: "120px", fontWeight: "bolder", fontFamily: "Railway", marginBottom: "20px" }}>
                    Google Top Terms
                </h1>
                <div>
                    <p style={{fontSize: "40px", fontFamily: "Railway"}}>Choose a <Link to="/dashboard" style={{color:"#C292FF"}}> dataset </Link> </p>
                </div>
            </div>
            <div style={{display: 'flex', justifyContent: 'space-between' }}>
                <div>
                    <HomeCards title='TOP 25 TERMS' body='Query the rising terms in the United States market.
                      You can view its popularity and current ranking'/>
                </div>
                <div>
                    <HomeCards title='TOP RISING TERMS' body='Query the most searched terms in the United States market.
                      You can view its popularity and current ranking '/>
                </div>
                <div>
                    <HomeCards title='TOP INTL. TERMS' body='Query the most searched terms in the United States market.
                    You can view its popularity and current ranking  '/>
                </div>
                <div>
                    <HomeCards title='TOP INTL. RISING TERMS' body='Query the most searched terms in the United States market.
                    You can view its popularity and current ranking  '/>
                </div>
            </div>
            <div style={{marginTop: "40px"}}>
                <Link className="link" to="/dashboard">
                    Go to Dashboard
                </Link>
            </div>
        </div>

    )
}

export default Home