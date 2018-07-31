//insert javascript here
function toUWU() {
  var englishInput = document.getElementbyId('word').value;
  var uwuOUT = "";
    for(var i = 0; i < englishInput.length; i++) {
      if ((englishInput.charAt(i) == 'r') || (englishInput.charAt(i) == 'l')){
        uwuOUT += "w";
      }
      else if(englishInput.charAt(i) == 'n') {
        uwuOUT += "ny";
      }
      else if(englishInput.charAt(i) == '!') {
        uwuOUT += "~ uwu";
      }
      else{
        uwuOUT += englishInput.charAt(i);
      }
    }
    document.getElementbyId("demo").innerHTML = uwuOUT;
    console.log(uwuOUT);
}
