function menu() {
  if (document.getElementById("mySidebar").style.display === "none") {
    document.getElementById("mySidebar").style.display = "block";
    document.getElementById("main").style.marginLeft = "300px";
  }
  else {
    document.getElementById("mySidebar").style.display = "none";
    document.getElementById("main").style.marginLeft = "0";
  }
}