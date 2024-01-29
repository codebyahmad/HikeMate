import React from "react";

import { Box, Container, Link, Typography } from "@mui/material";
import linkedin from "../assets/images/linkedin.svg";
import logo from "../assets/images/logo_2.svg";
import messenger from "../assets/images/messenger.svg";
import twitter from "../assets/images/twitter.svg";
import twoo from "../assets/images/twoo.svg";


const Footer = () => {
	return (
		<footer>

	<div class="footer-content">
		<div class="footer-socials">
		<img src={logo} alt=""/>
		<p>Where the Trail Leads, <br/> Adventure Follows</p>

			<div class="socials-icons">
				<a href=""><img src={linkedin} alt=""/></a>
				<a href=""><img src={messenger} alt=""/></a>
				<a href=""><img src={twitter} alt=""/></a>
				<a href=""><img src={twoo} alt=""/></a>
			</div>
		</div>

		<div class="extra-footer-info">
			<a href="#"><h1>Sitemap</h1></a>
			<a href="#"><p>Home</p></a>
			<a href="#"><p>Recommendation</p></a>
			<a href="#"><p>Trends</p></a>
			<a href="#"><p>Regions</p></a>
		</div>

		<div class="extra-footer-info">
			<a href="#"><h1>Regions</h1></a>
			<a href="#"><p>Bern</p></a>
			<a href="#"><p>Graubünden</p></a>
			<a href="#"><p>Zürich</p></a>
			<a href="#"><p class="all-regions">All Regions</p></a>
		</div>

		<div class="search-footer-info">
			<h1>Join Our Newsletter</h1>

			<form action="" class="search-bar-footer">
				<input type="text" placeholder="Your email address" name="q"/>
				<button type="submit">Subscribe</button>
			</form>

			<p>* Will send you weekly updates for your better <br/>tour packages.</p>
	</div>
</div>
<div class="horizontal-line"></div>

<p class="copy-right">Copyright @ HikeMate 2023. All Rights Reserved.</p>
</footer>
	);
};

export default Footer;
