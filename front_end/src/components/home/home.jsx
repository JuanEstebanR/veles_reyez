import { Link } from "react-router-dom";
import Button from 'react-bootstrap/Button';
const Home = () => {
    return (
        <div>
            <div>
                <h1 style={{
                    fontWeight: "bold",
                    fontFamily: "Railway",
                    color: "#C292FF",
                    fontSize: "80px",
                }}>Google Top Terms</h1>
            </div>
            <div className="mb-2">
                 <Link to="/signup">
                <Button style={{width: "200px", borderColor: "#C292FF"}}  size="lg">
                    Sign Up
                </Button>{' '}
            </Link>
                <Link to="/signin">
                    <Button style={{width: "200px", borderColor: "#C292FF"}}  size="lg">
                    Sign In
                    </Button>
                </Link>
            </div>
            <div>
                <p>

                </p>
            </div>
        </div>
    )
}

export default Home