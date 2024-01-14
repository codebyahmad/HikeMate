import React from "react";

import { Typography } from "@mui/material";
import { Box, Container } from "@mui/system";

import trendy1 from "../assets/images/trendy1.png";
import trendy2 from "../assets/images/trendy2.png";
import trendy3 from "../assets/images/trendy3.png";
import trendy4 from "../assets/images/trendy4.png";
import { hotelsRestaurants } from "../data";
import HotelRestaurantItem from "./HotelRestaurantItem";
import SecondaryButton from "./SecondaryButton";

const HotelsAndRestaurants = () => {
	return (
		<div class="trendy-card-class">

		<div class="rec-h1"><h1>
			Trendy Trails:
		</h1>
		</div>

		<div class="trendy-card-container">
			<div class="trendy-card">
				<img src={trendy1} alt=""/>
				<div class="trendy-card-info">
					<h1>
						Grindelwald - <br/> Glacier Canyon
					</h1>
					<div class="add-info">
						<h2>Length:</h2>
						<h2 class="length-info">6.0Km</h2>
					</div>
					<a href="">Explore More</a>
				</div>
			</div>

			<div class="trendy-card">
				<img src={trendy2} alt=""/>
				<div class="trendy-card-info">
					<h1>
						Harder Kulm <br/> Loop Trail
					</h1>
					<div class="add-info">
						<h2>Length:</h2>
						<h2 class="length-info">6.0Km</h2>
					</div>
					<a href="">Explore More</a>
				</div>
			</div>		
			
			<div class="trendy-card">
				<img src={trendy3} alt=""/>
				<div class="trendy-card-info">
					<h1>
						Northface Trail <br/> Mürren 
					</h1>
					<div class="add-info">
						<h2>Length:</h2>
						<h2 class="length-info">6.0Km</h2>
					</div>
					<a href="">Explore More</a>
				</div>
			</div>	

			<div class="trendy-card">
				<img src={trendy4} alt=""/>
				<div class="trendy-card-info">
					<h1>
						Schynige Platte <br/> Panorama Trail
					</h1>
					<div class="add-info">
						<h2>Length:</h2>
						<h2 class="length-info">6.0Km</h2>
					</div>
					<a href="">Explore More</a>
				</div>
			</div>	
		</div>

		<button class="all-trails">All Trails</button>
	</div>
	);
};

export default HotelsAndRestaurants;
