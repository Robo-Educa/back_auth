async function talk(userMessage) {
    let botMessage;

    await fetch('/talk', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: userMessage })
    })
    .then(response => response.json())
    .then(data => {               
        switch (data.status) {
            case 'success':                
                botMessage = data.message;
                break;
            case 'error':                
                botMessage = "Erro na requisição";               
                break;
            default:
                botMessage = "Resposta inesperada";
                break;
        }        
    });

    return botMessage;
}