import React, { useEffect, useState } from "react";
import logo from "./logo.svg";
import "./App.css";

function App() {
  const [trails, setTrails] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch("http://127.0.0.1:8000/api/");
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        const jsonData = await response.json();
        setTrails(jsonData);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    fetchData();
  }, []);

  return (
    <div className="App">
      <div>
        <h1>Your Fetched Data:</h1>
        <ul>
          {trails.map((item) => (
            <li key={item.id}>
              {/* Customize this part based on your data structure */}
              <strong>{item.name}</strong>: {item.avg_rating}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default App;
