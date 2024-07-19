# Dependências
from main import app
from flask import render_template, request, session, redirect, url_for, make_response, jsonify
# Serviços
import service.loginService as loginService
import service.talkService as talkService

# Página inicial/Index
@app.route('/')
def home():
    return render_template('index.html')

# Solicitação de permissão de uso de microfone e câmera
@app.route('/devicePrompt')
def devicePrompt():
    return render_template('devicePrompt.html')

# Informação de bloqueio de uso de microfone e câmera - como desbloquear
@app.route('/deviceDenied')
def deviceDenied():
    return render_template('deviceDenied.html')

# Informação de erros referente ao uso de microfone e câmera
@app.route('/deviceError')
def deviceError():
    return render_template('deviceError.html')

# Informação de dispositivos não encontrados - microfone e câmera
@app.route('/deviceNotFound')
def deviceNotFound():
    return render_template('deviceNotFound.html') 

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():    
    if request.method == 'POST':                        
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')                      
        response = loginService.login(username, password)
        return response        
    else:        
        return render_template('login.html')

# Logout
@app.route('/logout')
def logout():
    response = loginService.logout()
    return response          

# Página de interação entre usuário e bot
@app.route('/interaction')
def interaction():
    # Verifica se usuário está logado       
    if not session.get('userId'): return redirect(url_for('login'))    
    
    return render_template('interaction.html')   

# Troca de mensagens entre usuário e bot
@app.route('/talk', methods=['POST']) 
def talk():   
    # Verifica se usuário está logado       
    if not session.get('userId'): return make_response(jsonify({"error": "Não autorizado"}), 401)

    # obtem dados da requisição - mensagem do usuário
    data = request.get_json()
    userMessage = data.get('message')    

    # Envia mensagem para Bot e aguarda respectiva resposta
    botResponse = talkService.talk(userMessage)
    
    # retorna ao Front com resposta do Bot
    return botResponse

# Teste SpeachRecognition
@app.route('/recognition')
def recognition():
    return render_template('recognition.html')