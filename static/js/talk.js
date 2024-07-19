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

function speak(message) {
    message = removerEmojis(message);
    const synth = window.speechSynthesis;
    const utterThis = new SpeechSynthesisUtterance(message);

    utterThis.onstart = function () {        
        showElement("divSpinnerWaves");             // Exibe Spinner - ondas sonoras
    };
    utterThis.onend = function () {
        hideElement('divSpinnerWaves');             // Oculta Spinner - ondas sonoras
        showElement("divSpinnerHeart");         // Spinner indicando Coração batendo
    };

    utterThis.pitch = 2;
    utterThis.rate = 2;
    synth.speak(utterThis);
}

function removerEmojis(texto) {
    return texto
      .replace(/\p{Emoji}/gu, '') // Remove emojis
      .replace(/\s+/g, ' ') // Remove espaços em branco extras
      .trim(); // Remove espaços em branco no início e no fim
  }
  