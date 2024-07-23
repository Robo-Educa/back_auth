async function login(usertype) {    

    let username = document.getElementById('username').value;
    let password = document.getElementById('password').value;    

    displayStartLogin();
    
    await fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username: username, password: password, usertype: usertype })
    })
    .then(response => response.json())
    .then(data => {

        displayStopLogin();
        
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
            case 'errorGuest':
                alert("Não foi possível criar usuário temporário. Tente novamente!");                
                break;                
            default:
                break;
        }        
    });
    
}

async function logout() {   
    
    synth.cancel();     // Interrompe eventual reprodução de audio em andamento

    // Inicia processo de LogOut no backEnd
    await fetch('/logout')
        .then(response => response.json())
        .then(data => {
            response = data.status;            
        })
        .catch(error => response = error );
    if (response = "success") {
        goToPage("login");
    } 
    else{
        alert("Não foi possível efetuar LogOut");
    }
    
}