import React from "react";

import { Box, Container, Typography } from "@mui/material";

import vector1 from "../assets/images/Vector1.svg";
import rec1 from "../assets/images/rec1.png";
import rec2 from "../assets/images/rec2.png";
import rec3 from "../assets/images/rec3.png";
import rec4 from "../assets/images/rec4.png";
import rec5 from "../assets/images/rec5.png";
import rec6 from "../assets/images/rec6.png";
import bgImage from "../assets/main/bg-image.webp";
import Navbar from "./Navbar";
import SearchNav from "./SearchNav";

const Hero = () => {
	return (
			<div class="container">
			<Navbar />
			<div class="content">
			<img src={vector1} alt=""></img>
			<h1>Find Your Trail<br/>and Let It Lead You <br/> to Adventure!</h1>

			<form action="" class="search-bar">
				<input type="text" placeholder="Select region" name="q"/>
				<button type="submit">Recommend</button>
			</form>
			
			<div class="recommend-part">
				<img src={rec1} alt=""/>
				<img src={rec2} alt=""/>
				<img src={rec3} alt=""/>
				<img src={rec4} alt=""/>
				<img src={rec5} alt=""/>
				<img src={rec6} alt=""/>
				<p>350+ people already rated trails</p>
			</div>
		</div>	
			</div>
	);
};

export default Hero;
