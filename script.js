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

  $("#toanimate, #river-button").click(function(){
    $("#toanimate").hide();
    $("#page1").show();
    $("#page3").hide();
  });

  $("#page1, #river-button").click(function(){
    $("#page1").hide();
    $("#page2").show();
    $("#page3").hide();
  });

  $("#page2, #river-button").click(function(){
    $("#page2").hide();
    $("#page3").show();
  });

  $("#page3, #river-button").click(function(){
    $("#page3").hide();
    $("#page4").show();
  });

  $("#page4, #river-button").click(function(){
    $("#page4").hide();
    $("#page5").show();
  });

});

