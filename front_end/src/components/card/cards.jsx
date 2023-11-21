import { Link } from "react-router-dom";
import "./card.css";
const HomeCards = ({title, body}) => {
    return (
        <div className="card-container">
            <div className="card-tittle">
                <h3>
                    {title}
                </h3>
            </div>
            <div className="card-body">
                <p>
                    {body}
                </p>
            </div>
        </div>
    );
}

export default HomeCards;