var elements = document.getElementsByClassName('difficulty');

for (var i = 0; i < elements.length; i++) {
  var textContentLap = elements[i].textContent;

  if (textContentLap === '1') {
    elements[i].classList.add('green-text');
  } 
	else if (textContentLap === '3') {
    elements[i].classList.add('blue-text');
  } 
	else if (textContentLap === '5') {
    elements[i].classList.add('red-text');
  }
}



