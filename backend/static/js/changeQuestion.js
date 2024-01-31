let currentDivIndex = 0;
const divs = document.querySelectorAll('.questionnaire');
const divNext = document.getElementById('buttons-container');
const divFinish = document.getElementById('buttons-container-finish');

function showNext() {
  if (currentDivIndex < divs.length - 1) {
    divs[currentDivIndex].style.display = 'none';
    currentDivIndex++;
    divs[currentDivIndex].style.display = 'block';

    if (divs[currentDivIndex].id === 'question5') {
      divNext.style.display = 'none';
      divFinish.style.display = 'flex';
    } else {
      divNext.style.display = 'flex';
      divFinish.style.display = 'none';
    }
  }
}

function showPrevious() {
  if (currentDivIndex > 0) {
      divs[currentDivIndex].style.display = 'none';
      currentDivIndex--;
      divs[currentDivIndex].style.display = 'block';

      
      if (divs[currentDivIndex].id === 'question4') {
        divNext.style.display = 'flex';
        divFinish.style.display = 'none';
      }
  }
}

function changeAddBtn(){
  var addBtn = document.getElementById('save-btn');

  addBtn.style.backgroundColor = 'green';
}
