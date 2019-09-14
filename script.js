function myFunction() {
  var x = document.getElementById("myTopnav");
  if (x.className === "topnav") {
    x.className += " responsive";
  } else {
    x.className = "topnav";
  }
}

$(document).ready(function(){	
  
  $('.container').fadeIn(1000);
  $('.container').animate({marginTop: '-10px'}, "slow");
});