from main import app
from flask import render_template
from geminiBot import *

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

@app.route('/getBotMessage')
def getBotMessage():    
    response = botMessage()    
    return response
