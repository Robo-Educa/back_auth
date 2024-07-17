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

function interactionMessage(message) {
    interactionMsg = message;
    document.getElementById("divInteractionMsg").innerHTML = interactionMsg;
}

function interactionImage(status) {
    switch (status) {
        case 'thinking':
            document.getElementById("divInteractionImage").style.display = "none";
            document.getElementById("divSpinner").style.display = "block";
            break;
        case 'talking':
            document.getElementById("divSpinner").style.display = "none";
            document.getElementById("interactionImage").src = "/static/images/wavesOn.gif";
            document.getElementById("divInteractionImage").style.display = "block";            
            break;            

        default:
            break;
    }
}

function displayMic() {
    document.getElementById("divMic").style.display = "block";
}