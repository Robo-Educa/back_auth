from main import app
from flask import render_template, request, session, redirect, url_for
import service.loginService as loginService

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/devicePrompt')
def devicePrompt():
    return render_template('devicePrompt.html')

@app.route('/deviceDenied')
def deviceDenied():
    return render_template('deviceDenied.html')

@app.route('/deviceError')
def deviceError():
    return render_template('deviceError.html')

@app.route('/deviceNotFound')
def deviceNotFound():
    return render_template('deviceNotFound.html') 

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

@app.route('/logout')
def logout():
    response = loginService.logout()
    return response          

@app.route('/interaction')
def interaction():
    if not session.get('userName'):
        return redirect(url_for('login'))    
            
    return render_template('interaction.html')   
    
    
