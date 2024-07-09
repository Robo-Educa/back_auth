function display_openFullscreen() {
    var elem = document.documentElement;
    if (elem.requestFullscreen) {
        elem.requestFullscreen();
    } else if (elem.webkitRequestFullscreen) { /* Safari */
        elem.webkitRequestFullscreen();
    } else if (elem.msRequestFullscreen) { /* IE11 */
        elem.msRequestFullscreen();
    }
}

function display_closeFullscreen() {
    if (document.exitFullscreen) {
        document.exitFullscreen();
    } else if (document.webkitExitFullscreen) { /* Safari */
        document.webkitExitFullscreen();
    } else if (document.msExitFullscreen) { /* IE11 */
        document.msExitFullscreen();
    }
}

function display_goToPage(page) {
    window.location.href = page;
}

function display_quitStart() {    
    document.getElementById("divStartPublic").style.display = "none";
    document.getElementById("divImage").style.display = "none";
    document.getElementById("divMenu").style.display = "block";
}

function display_start(){
    document.getElementById("divMenu").style.display = "none";
    document.getElementById("divStartPublic").style.display = "block";
    document.getElementById("divImage").style.display = "block";                
}

