  function toggleRotation() {
    var toggleCheckbox = document.getElementById("toggleCheckbox");
    var gira = document.getElementById("gira");
    var gira2 = document.getElementById("gira2");
    var gira3 = document.getElementById("gira3");
    var color = document.getElementById("colito");
    
    if (toggleCheckbox.checked) {
      gira.classList.add("rotating");
      gira2.classList.add("rotating");
      gira3.classList.add("rotating");
      color.classList.add("rainbow");
    } else {
      gira.classList.remove("rotating");
      gira2.classList.remove("rotating");
      gira3.classList.remove("rotating");
      color.classList.remove("rainbow");
    }
  }