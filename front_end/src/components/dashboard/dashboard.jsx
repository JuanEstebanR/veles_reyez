import { useState } from "react";
import axios from "axios";
import { CountryDropdown, RegionDropdown} from "react-country-region-selector";

const Dashboard = () => {
    const base_url = (table_name)  => `http://localhost:8000/googletopterms/${table_name}/`;
      const list = ["CL", "AR", "US", "CO", "BR", "UR", "MX",
                            "AL", "AF","BE", "CA", "DE", "AT", "AU", "BR", "DK", "ES",
                              "FI", "PH", "FR", "IN","HU", "HK", "IT", "JP", "UA", "TW", "SE", "RU","PT",
                            "GB", "PE"]
      const [country, setCountry] = useState("");
      const [region, setRegion] = useState("");
      const [limit, setLimit] = useState(0);
      const [interval, setInterval] = useState(2);
      const [table, setTable] = useState("");
  const handleTableChange = (event) => {
      console.log(event.target.value)
    setTable(event.target.value); // Actualizar el estado con el valor seleccionado
    if (event.target.value === "Top 25 terms U.S." || event.target.value === "Top 25 rising terms U.S.") {
      setCountry('United States')
    }
  };
  const handleSubmit = async (event) => {
      event.preventDefault();
      console.log(country, region, limit, interval, table)
      const formData = {
            country_name: country,
            dma_name: region,
            limit: limit,
            interval: interval,
            table_name: table
      };
            await axios.post(base_url(table), {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(formData),
            }).then((response) => {
                console.log(response);
            }).catch((error) => {
                console.log(error);
            });
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
                          <option value="top_terms_international_country">Internationale Top One</option>
                      </select>
                  </div>
                  <div style={{ display: "flex", alignItems: "center", marginTop: "10px" }}>
                      <CountryDropdown
                          style={{ backgroundColor: "black", color: "white", height: "30px", width: "50%", marginRight: "10px" }}
                          value={country}
                          onChange={(val) => setCountry(val)}
                          showDefaultOption={false}
                          whitelist={list}
                          disabled={table === "top_25_terms" || table === "top_25_rising_terms"}
                      />
                      <RegionDropdown
                          style={{ backgroundColor: "black", color: "white", height: "30px", width: "50%" }}
                          country={country}
                          value={region}
                          onChange={(val) => setRegion(val)}
                      />
                  </div>
                  <div style={{ marginTop: "10px" }}>
                      <label htmlFor="customRange1" className="form-label">{limit}</label>
                      <input
                          type="range"
                          value={limit || 0}
                          onChange={(val) => {setLimit(val.target.value)}}
                          className="form-range"
                          id="customRange1"
                          min="0"
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
          <div style={{ height: "600px", width:"800px", backgroundColor: "lightgray", overflow: "hidden" }}>
              {/* Área de gráficos o contenido grande */}
          </div>
      </div>
  );
};
export default Dashboard;
