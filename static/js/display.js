function openFullscreen() {
    var elem = document.documentElement;
    if (elem.requestFullscreen) {
        elem.requestFullscreen();
    } else if (elem.webkitRequestFullscreen) { /* Safari */
        elem.webkitRequestFullscreen();
    } else if (elem.msRequestFullscreen) { /* IE11 */
        elem.msRequestFullscreen();
    }
}

function closeFullscreen() {
    if (document.exitFullscreen) {
        document.exitFullscreen();
    } else if (document.webkitExitFullscreen) { /* Safari */
        document.webkitExitFullscreen();
    } else if (document.msExitFullscreen) { /* IE11 */
        document.msExitFullscreen();
    }
}

function goToPage(page) {
    window.location.href = page;
}

function showMessage(message) {
    document.getElementById("messages").value = message
}

function showImage(status) {
    switch (status) {        
        case 'talking':
            document.getElementById("interactionImage").src = "/static/images/wavesOn.gif";
            break;            
        default:
            break;
    }
}

function hideElement(element) {
    document.getElementById(element).style.display = "none";
}

function showElement(element) {
    document.getElementById(element).style.display = "block";
}
