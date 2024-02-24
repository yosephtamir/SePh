const profilebtn = document.querySelector(".profilebtn");


document.querySelector("#proimg").addEventListener("click", function () {
    const vis =profilebtn.style.visibility
    if (vis === "visible") {
        profilebtn.style.visibility = "hidden";
    } else {
        profilebtn.style.visibility = "visible";
    }
  });
