/* Render Top Navigation */
function myFunction() {
  var x = document.getElementById("myTopnav");
  if (x.className === "topnav") {
    x.className += " responsive";
  } else {
    x.className = "topnav";
  }
}

$(document).ready(function(){ 
  /* Body Content Animation*/
  $('#toanimate').fadeIn(1000);
  $("#toanimate").animate({
    marginTop: '-15px'
  }, { duration: 500, queue: false });

  /* River's Assistant Form*/
  $("#river").click(function(){
    $("p").slideDown();
  });
});

