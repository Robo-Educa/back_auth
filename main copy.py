from flask import Flask, render_template, request, redirect, url_for
import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()  

#region - Variáveis de ambiente
my_api_key = os.environ.get("API_KEY")                        # Gemini - API_KEY
system_instruction = os.environ.get("SYSTEM_INSTRUCTIONS")    # Gemini - Instruções do Sistema / Informa as caracteristicas do Assistente.
#endregion

#region - Modelo Google Generative AI
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_NONE"
  },
]
genai.configure(api_key=my_api_key)
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash",
        generation_config=generation_config,
        system_instruction=system_instruction,
        safety_settings=safety_settings)
#endregion - Modelo Google Generative AI

app = Flask(__name__)

#region - ROTAS
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/devicePrompt', methods=['GET'])
def devicePrompt():
    return render_template('devicePrompt.html')

@app.route('/deviceDenied', methods=['GET'])
def deviceDenied():
    return render_template('deviceDenied.html')

@app.route('/deviceError', methods=['GET'])
def deviceError():
    return render_template('deviceError.html')

@app.route('/deviceNotFound', methods=['GET'])
def deviceNotFound():
    return render_template('deviceNotFound.html')

@app.route('/talk')
def talk():
    body_message = "Oi"
    message_history = []
    
    convo = model.start_chat(history = message_history) # Inicia chat, contextualizando a IA com o histórico da conversação
    convo.send_message(body_message)                    # envia nova mensagem para ser processada pela IA
    botResponse = convo.last.text                       # Obtem resposta da IA
    response = {"message": botResponse}
    
    return response

#endregion 

if __name__ == '__main__':
    app.run(debug=True)
