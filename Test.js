function myMove() {
    var elem = document.getElementById("animate")

    var pos = 0;
    var id = setInterval(frame, 5);
    function frame() {
        if (pos == 350) {
            elem.style.top = 0;
            pos = 0;
            frame()
        } else {
            pos++;
            elem.style.top = pos + "px";
        }
    }
}