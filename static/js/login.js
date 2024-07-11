async function login() {    

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    
    document.getElementById("btLogin").disabled = true;
    document.getElementById("btLogin").style.cursor = "progress";

    await fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username: username, password: password })
    })
    .then(response => response.json())
    .then(data => {

        document.getElementById("btLogin").disabled = false;
        document.getElementById("btLogin").style.cursor = "default";
        
        switch (data.status) {
            case 'success':
                goToPage("interaction");
                break;
            case 'errorUser':
                alert("Usuário inexistente");
                document.getElementById("username").focus();
                break;
            case 'errorPwd':
                alert("Senha incorreta");
                document.getElementById("password").focus();
                break;
            default:
                break;
        }        
    });
    
}