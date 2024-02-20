const del = document.getElementById('delprop')
document.getElementById('delpropbtn').onclick = function () {
    const vis =del.style.visibility
    if (vis === "hidden") {
        del.style.visibility = "visible";
    } else {
        del.style.visibility = "hidden";
    }
}