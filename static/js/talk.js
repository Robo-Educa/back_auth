async function getBotMessage() {
    let message;
    await fetch('/getBotMessage')
        .then(response => response.json())
        .then(data => {
            message = data.message;
        })
        .catch(error => message = error );
    return message;
}