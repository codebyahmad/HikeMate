import { Box, Container, Typography } from "@mui/material";
import React from "react";
import fav1 from "../assets/images/fav1.png";
import fav2 from "../assets/images/fav2.png";
import fav3 from "../assets/images/fav3.png";
import fav4 from "../assets/images/fav4.png";
import fav5 from "../assets/images/fav5.png";
import fav6 from "../assets/images/fav6.png";
import fav7 from "../assets/images/fav7.png";
import fav8 from "../assets/images/fav8.png";
import fav9 from "../assets/images/fav9.png";

import { travelItems } from "../data";
import SecondaryButton from "./SecondaryButton";
import TravelItem from "./TravelItem";

const Travel = () => {
	return (
		<div class="fav-regions-container">
			<div class="fav-region-container">
				<div class="fav-region-card">
					<img src={fav1} alt=""/>
					<div class="fav-region-info">
						<h1>
							Grindelwald
						</h1>
						<p>North Rhine-Westphalia</p>
					</div>
				</div>
			
	
			<div class="fav-region-container">
				<div class="fav-region-card">
					<img src={fav2} alt=""/>
					<div class="fav-region-info">
						<h1>
							Baldenesee
						</h1>
						<p>Baden-Württemberg</p>
					</div>
				</div>
			</div>
	
			<div class="fav-region-container">
				<div class="fav-region-card">
					<img src={fav3} alt=""/>
					<div class="fav-region-info">
						<h1>
							Baldeneyer
						</h1>
						<p>Baden-Württemberg</p>
					</div>
				</div>
			</div>
	
			<div class="fav-region-container">
				<div class="fav-region-card">
					<img src={fav4} alt=""/>
					<div class="fav-region-info">
						<h1>
							Bahntrassentour
						</h1>
						<p>Mecklenburg- Vorpommern</p>
					</div>
				</div>
			</div>
	
			<div class="fav-region-container">
				<div class="fav-region-card">
					<img src={fav5} alt=""/>
					<div class="fav-region-info">
						<h1>
							Ruhrschleife
						</h1>
						<p>North Rhine-Westphalia</p>
					</div>
				</div>
			</div>
	
			<div class="fav-region-container">
				<div class="fav-region-card">
					<img src={fav6} alt=""/>
					<div class="fav-region-info">
						<h1>
							Jadhaus
						</h1>
						<p>North Rhine-Westphalia</p>
					</div>
				</div>
			</div>
	
			<div class="fav-region-container">
				<div class="fav-region-card">
					<img src={fav7} alt=""/>
					<div class="fav-region-info">
						<h1>
							Mechtenberg
						</h1>
						<p>North Rhine-Westphalia</p>
					</div>
				</div>
			</div>
	
			<div class="fav-region-container">
				<div class="fav-region-card">
					<img src={fav8} alt=""/>
					<div class="fav-region-info">
						<h1>
							Ruhrausflug
						</h1>
						<p>The Free State of Bavaria</p>
					</div>
				</div>
			</div>
	
			<div class="fav-region-container">
				<div class="fav-region-card">
					<img src={fav9} alt=""/>
					<div class="fav-region-info">
						<h1>
							Essenrad
						</h1>
						<p>Brandenburg</p>
					</div>
				</div>
			</div>
		</div>
	</div>
	);
};

export default Travel;
