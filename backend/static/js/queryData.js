function storeDurationValues(){
    var duration_min = document.getElementById('duration_min').value;
    var duration_max = document.getElementById('duration_max').value;

    document.cookie = "duration_min=" + duration_min + "; expires=Fri, 01 Jan 9999 00:00:00 GMT";
    document.cookie = "duration_max=" + duration_max + "; expires=Fri, 01 Jan 9999 00:00:00 GMT";
}


function storeLengthValues(){
	var length_min = document.getElementById('length_min').value;
	var length_max = document.getElementById('length_max').value;

	document.cookie = "length_min=" + length_min + "; expires=Fri, 01 Jan 9999 00:00:00 GMT";
	document.cookie = "length_max=" + length_max + "; expires=Fri, 01 Jan 9999 00:00:00 GMT";
}

function storeNumberOfTrails(){
	var num_of_trials = document.getElementById('num_of_trials').value;

	document.cookie = "num_of_trials=" + num_of_trials + "; expires=Fri, 01 Jan 9999 00:00:00 GMT";
}
