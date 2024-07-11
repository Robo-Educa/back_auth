from main import app
from flask import render_template, request
from geminiBot import *
import repository.users as users

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

@app.route('/interaction')
def interaction():
    return render_template('interaction.html')

@app.route('/login', methods=['GET', 'POST'])
def login():    
    if request.method == 'POST':                        
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        
        user = users.find("name", username)
        if user is None:
            status = "errorUser"
        else:
            doc_dic = user[0].to_dict()
            if doc_dic["password"] != password:
                status = "errorPwd" 
            else:
                status = "success" 
                #userRole = doc_dic["role"]            
        
        response = {"status": status}
        return response        
        
    return render_template('login.html')

@app.route('/getBotMessage')
def getBotMessage():    
    response = botMessage()    
    return response
