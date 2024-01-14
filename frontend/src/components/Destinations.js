import React from "react";

import { Box, Container, Typography } from "@mui/material";

import location from "../assets/images/location.svg";
import star from "../assets/images/star.svg";
import trail1 from "../assets/images/trail1.png";
import trail2 from "../assets/images/trail2.png";
import trail3 from "../assets/images/trail3.png";
import { destinations } from "../data";
import DestinationItem from "./DestinationItem";

const Destionations = () => {
	return (
		<div class="container-trail">
			<div class="rec-h1"><h1>
			Recommended Routes:
		</h1>
		</div>
		<div class="card-container">
			
			<div class="card">
				<img src={trail1} alt="" class="preview-img"/>
				<div class="card-content">
					<div class="rate-star">
						<p> <span class="difficulty">Difficult</span></p>
						<div class="star-span">
							<img src={star} alt=""/>
							<img src={star} alt=""/>
							<img src={star} alt=""/>
							<img src={star} alt=""/>
							<img src={star} alt=""/>
						</div>
					</div>	
					<h3>First - Bachalpsee</h3>
					<div class="location-card">
						<img src={location} alt="" class="location-img"/>
						<p>Grindelwald, Bern, Switzerland</p>
					</div>

					<div class="add-info">
						<p>Length:</p>
						<div class="length-info">6.0 Km</div>
					</div>
					<div class="description-info">This hike leads over a wide, well-kept path along blooming alpine meadows to the Bachalpsee. 
						At the beginning of the hike there is a short but steep climb to the Gummihütte that has to be mastered.
					</div>
					<a href="/trail.html" class="btn-read">Explore now</a>
				</div>
			</div>

			<div class="card">
				<img src={trail2}  alt="" class="preview-img"/>
				<div class="card-content">
					<div class="rate-star">
						<p><span class="difficulty">Medium</span></p>
						<div class="star-span">
							<img src={star} alt=""/>
							<img src={star} alt=""/>
							<img src={star} alt=""/>
							<img src={star} alt=""/>
							<img src={star} alt=""/>
						</div>
					</div>	
					<h3>Lake Oeschinen Loop</h3>
					<div class="location-card">
						<img src={location} alt="" class="location-img"/>
						<p>Grindelwald, Bern, Switzerland</p>
					</div>

					<div class="add-info">
						<p>Length:</p>
						<div class="length-info">6.0 Km</div>
					</div>
					<div class="description-info">This hike leads over a wide, well-kept path along blooming alpine meadows to the Bachalpsee. 
						At the beginning of the hike there is a short but steep climb to the Gummihütte that has to be mastered.
					</div>
					<a href="/trail.html" class="btn-read">Explore now</a>
				</div>
			</div>

			<div class="card">
				<img src={trail3}  alt="" class="preview-img"/>
				<div class="card-content">
					<div class="rate-star">
						<p><span class="difficulty">Easy</span></p>
						<div class="star-span">
							<img src={star} alt=""/>
							<img src={star} alt=""/>
							<img src={star} alt=""/>
							<img src={star} alt=""/>
							<img src={star} alt=""/>
						</div>
					</div>	
					<h3>Northface Trail</h3>
					<div class="location-card">
						<img src={location} alt="" class="location-img"/>
						<p>Grindelwald, Bern, Switzerland</p>
					</div>

					<div class="add-info">
						<p>Length:</p>
						<div class="length-info">6.0 Km</div>
					</div>
					<div class="description-info">This hike leads over a wide, well-kept path along blooming alpine meadows to the Bachalpsee. 
						At the beginning of the hike there is a short but steep climb to the Gummihütte that has to be mastered.
					</div>
					<a href="/trail.html" class="btn-read">Explore now</a>
				</div>
			</div>
		</div>
		</div>	
	);
};

export default Destionations;
