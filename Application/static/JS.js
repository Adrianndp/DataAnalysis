function close_function() {
  document.getElementById("mySidebar").style.display = "none";
  document.getElementById("main").style.marginLeft = "0";
  document.getElementById("open_menu").style.display = "block";
}

function open_function() {
  document.getElementById("mySidebar").style.display = "block";
  document.getElementById("main").style.marginLeft = "300px";
  document.getElementById("open_menu").style.display = "none";
}