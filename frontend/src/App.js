import React, { useEffect, useState } from "react";
import Destinations from "./components/Destinations";
import HotelsAndRestaurants from "./components/HotelsAndRestaurants";
import Hero from "./components/Hero";
import Travel from "./components/Travel";
import AboutUs from "./components/AboutUs";
import Footer from "./components/Footer";
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
				const trailData = await response.json();
				setTrails(trailData);
			} catch (error) {
				console.error("Error fetching data:", error);
			}
		};

		fetchData();
	}, []);

	return (
		// <div className="App">
		//   <div>
		//     <h1>Your Fetched Data:</h1>
		//     <ul>
		//       {trails.map((item) => (
		//         <li key={item.id}>
		//           {/* Customize this part based on your data structure */}
		//           <strong>{item.name}</strong>: {item.avg_rating}
		//         </li>
		//       ))}
		//     </ul>
		//   </div>
		// </div>
		<>
			<Hero />
			<Destinations />
			<HotelsAndRestaurants />
			<Travel />
			<AboutUs />
			<Footer />
		</>
	);
}

export default App;
