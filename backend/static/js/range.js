function updateDurationValue(value) {
	// Update the range input value based on the entered number
	document.getElementById('customRange3').value = value;
}

// Optional: You can also update the number input based on the range input
document.getElementById('customRange3').addEventListener('input', function() {
	document.getElementById('numberInput').value = this.value;
});
