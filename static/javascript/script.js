/* Render Top Navigation */
function myFunction() {
  var x = document.getElementById("myTopnav");
  if (x.className === "topnav") {
    x.className += " responsive";
  } else {
    x.className = "topnav";
  }
}

/* Body Content Animation*/
$(document).ready(function(){ 
  $('#toanimate').fadeIn(1000);
  $("#toanimate").animate({
    marginTop: '-15px'
  }, { duration: 500, queue: false });
});