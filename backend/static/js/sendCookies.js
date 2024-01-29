function getCookie(name) {
	const value = `; ${document.cookie}`;
	const parts = value.split(`; ${name}=`);
	if (parts.length === 2) return parts.pop().split(';').shift();

	console.log(`Cookie ${name}`);
}

function constructLink() {
	const region = getCookie('region');
	const features = getCookie('features');
	const length_min = getCookie('length_min');
	const length_max = getCookie('length_max');
	const difficulty = getCookie('difficulty');
	const duration_min = getCookie('duration_min');
	const duration_max = getCookie('duration_max');
	
	const link = `http://127.0.0.1:8000/filtered-trials/
	?region=${region}&features=${features}&duration_min=${duration_min}&duration_max=${duration_max}
	&difficulty=${difficulty}&length_min=${length_min}&length_max=${length_max}`;

	console.log(link);
	window.location.href = link;
}

document.getElementById('finishBtn').addEventListener('click', constructLink);
