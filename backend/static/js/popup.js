document.getElementById("open-popup").addEventListener("click", function(){
	document.body.classList.add("active-popup");

	var questionnaireDivs = document.querySelectorAll(".questionnaire");
	questionnaireDivs.forEach(function(div) {
		div.classList.remove("visible");
	});
	document.getElementById("question1").classList.add("visible");
});


document.querySelector(".pop-up .btn-close").addEventListener("click", function(){
	document.body.classList.remove("active-popup");
});