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

function debugMsg(message) {    
    console.log(message);
}

function showImage(status) {
    showElement("divInteractionImage")
    switch (status) {        
        case 'speaking':
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

function hideAllExceptClose() {
    const allElements = document.body.children; // Get all direct children of <body>

    for (let i = 0; i < allElements.length; i++) {
      const element = allElements[i];
      if (element.id !== "divClose") { // Check if it's NOT the divClose element
        element.style.display = "none"; // Hide the element
      }
    }
}

function showMessage(message) {
    var messageDiv = document.getElementById("divMessage");
    messageDiv.textContent = message;
    messageDiv.style.display = "block";
}
