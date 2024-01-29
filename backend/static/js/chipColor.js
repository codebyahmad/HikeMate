function changeColor(button) {
  button.classList.toggle("active-feature");
}

function changeColorDifficulty(button) {
  button.classList.toggle("active-difficulty");
}

function setCookies(id, className, cookieName){
  const chipContainer = document.getElementById(id);
  const buttons = chipContainer.getElementsByTagName("button");

  for(var i = 0; i < buttons.length; i++){
    if(buttons[i].classList.contains(className)){
      const feature = buttons[i].id;
      var currentCookie = getCookie(cookieName);
      if(currentCookie === null) {
        currentCookie = "";     
        const newCookie = feature;
        setCookie(cookieName, newCookie, 1000)
      } else {
        const newCookie = currentCookie + "," + feature;
        setCookie(cookieName, newCookie, 1000)
      }
    }
  }
}

function getCookie(name) {
  var nameEQ = name + "=";
  var ca = document.cookie.split(';');
  for(var i=0;i < ca.length;i++) {
      var c = ca[i];
      while (c.charAt(0)==' ') c = c.substring(1,c.length);
      if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
  }
  return null;
}

function setCookie(name,value,days) {
  var expires = "";
  if (days) {
      var date = new Date();
      date.setTime(date.getTime() + (days*24*60*60*1000));
      expires = "; expires=" + date.toUTCString();
  }
  document.cookie = name + "=" + (value || "")  + expires + "; path=/";
}

