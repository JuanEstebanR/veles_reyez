import { useState } from "react";
import axios from "axios";
import { CountryDropdown, RegionDropdown} from "react-country-region-selector";
import InfoChart from "../chart/chart.jsx";

const Dashboard = () => {
    const data = (data, value) => {
        let dataChart = [];
        data.forEach((element) => {
            dataChart.push(element[value]);
        });
        return dataChart;
    };
    const list = ["CL", "AR", "US", "CO", "BR", "UR", "MX",
                        "AL", "AF","BE", "CA", "DE", "AT", "AU", "BR", "DK", "ES",
                          "FI", "PH", "FR", "IN","HU", "HK", "IT", "JP", "UA", "TW", "SE", "RU","PT",
                        "GB", "PE"]
    const [dataReady, setDataReady] = useState(false);
    const [country, setCountry] = useState("");
    const [region, setRegion] = useState("");
    const [limit, setLimit] = useState(1);
    const [interval, setInterval] = useState(2);
    const [table, setTable] = useState("");
    const [labels, setLabels] = useState([]);
    const [dataValues, setDataValues] = useState([]);
  const handleTableChange = (event) => {
      console.log(event.target.value)
    setTable(event.target.value); // Actualizar el estado con el valor seleccionado
    if (event.target.value === "Top 25 terms U.S." || event.target.value === "Top 25 rising terms U.S.") {
      setCountry('United States')
    }
  };
  const handleSubmit = async (event) => {
      event.preventDefault();
      setDataReady(false)
      setLabels([])
      setDataValues([])

      const base_url = (endpoint)  => `http://localhost:8000/googletopterms/${endpoint}/`;
      let endpoint;
      if(table === "top_25_terms" || table === "top_25_rising_terms"){
          endpoint = "top_25_terms"
      }else if (table === "top_25_international_terms" || table === "top_25_international_rising_terms"){
          endpoint = "top_25_international_terms"
      }

      const formData = {
            country_name: country,
            limit: limit,
            interval: interval,
            table_name: table
      };
      try {
          const response = await axios.post(base_url(endpoint), {
              method: "POST",
              headers: {
                  "Content-Type": "application/json",
              },
              body: formData,
          })
            setDataReady(true);
            setLabels(data(response.data, "term"));
            setDataValues(data(response.data, "avg_score"));
      }catch (error) {
            console.log(error);
      }
  }
  return (
      <div style={{ display: "grid", gridTemplateColumns: "1fr 2fr", gap: "30px", alignItems: "start" }}>
          <div style={{ textAlign: "left" }}>
              <form onSubmit={handleSubmit} style={{ width: "100%" }}>
                  <div>
                      <select
                          style={{ backgroundColor: "black", color: "white", height: "30px", width: "100%", marginRight: "10px" }}
                          value={table}
                          onChange={handleTableChange}
                          className="form-select"
                          aria-label="Default select example"
                      >
                          <option value="">Choose a Table</option>
                          <option value="top_25_terms">Top 25 terms U.S.</option>
                          <option value="top_25_rising_terms">Top 25 rising terms U.S.</option>
                          <option value="top_25_international_terms">International Top terms</option>
                          <option value="top_25_international_rising_terms">International Rising Terms</option>
                      </select>
                  </div>
                  <div style={{ display: "flex", alignItems: "center", marginTop: "10px" }}>
                      <CountryDropdown
                          style={{ backgroundColor: "black", color: "white", height: "30px", width: "100%" }}
                          value={country || "United States"}
                          onChange={(val) => setCountry(val)}
                          showDefaultOption={false}
                          whitelist={list}
                          disabled={table === "top_25_terms" || table === "top_25_rising_terms"}
                      />
                  </div>
                  <div style={{ marginTop: "10px" }}>
                      <label htmlFor="customRange1" className="form-label">{limit}</label>
                      <input
                          type="range"
                          value={limit || 1}
                          onChange={(val) => {setLimit(val.target.value)}}
                          className="form-range"
                          id="customRange1"
                          min="1"
                          max="25"
                          style={{ width: "100%" }}
                      />
                  </div>
                  <div style={{ marginTop: "10px" }}>
                      <label htmlFor="customInterval" className="form-label">Number of days before today</label>
                      <input
                          type="number"
                          value={interval || 2}
                          onChange={(val) => {setInterval(val.target.value)}}
                          className="form-control"
                          id="customInterval"
                          min="2"
                          max="25"
                          style={{ width: "100%" }}
                      />
                  </div>
                  <div style={{ marginTop: "20px" }}>
                      <button type="submit" className="btn btn-primary" style={{ width: "100%" }}>Submit</button>
                  </div>
              </form>
          </div>
          <div style={{ height: "420px", width:"800px", backgroundColor: "lightgray", overflow: "hidden" }}>
              {dataReady && <InfoChart title={table}
                                       labels={labels}
                                       data={dataValues} />}
          </div>
      </div>
  );
};
export default Dashboard;
