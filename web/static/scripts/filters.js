const profilebtn = document.querySelector(".profilebtn");
const logo = document.querySelector(".logoimg")
const home = document.querySelector("#homebtn")
document.querySelector("#proimg").addEventListener("click", function () {
    const vis =profilebtn.style.visibility
    if (vis === "visible") {
        profilebtn.style.visibility = "hidden";
    } else {
        profilebtn.style.visibility = "visible";
    }
  });
logo.addEventListener("click", function() {
    home.click();
});