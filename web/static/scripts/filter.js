const profilebtn = document.querySelector(".profilebtn");
document.querySelector("#proimg").addEventListener("click", function () {
    const vis =profilebtn.style.visibility
    if (vis === "hidden") {
        profilebtn.style.visibility = "visible";
    } else {
        profilebtn.style.visibility = "hidden";
    }
  });
