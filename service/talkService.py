# Dependências
from flask import session
import os
import google.generativeai as genai
from dotenv import load_dotenv
import time
# Serviços
import repository.messageHistoryRepository as messageHistory

#region - Variáveis de ambiente
load_dotenv()  
my_api_key = os.environ.get("API_KEY")                        # Gemini - API_KEY
system_instruction = os.environ.get("SYSTEM_INSTRUCTIONS")    # Gemini - Instruções do Sistema / Informa as caracteristicas do Assistente.
ai_model = os.environ.get("GEMINI_MODEL")                     # Modelo de IA Google Gemini
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
    "threshold": "BLOCK_LOW_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_LOW_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_LOW_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_LOW_AND_ABOVE"
  }
]
genai.configure(api_key=my_api_key)
model = genai.GenerativeModel(model_name=ai_model,
        generation_config=generation_config,
        system_instruction=system_instruction,
        safety_settings=safety_settings)
#endregion - Modelo Google Generative AI

# retorna histórico com formatação default para Google Gemini API
def format_messages_for_gemini(messages):
    messages_array = []
    
    # Obtem histórico de mensagens
    for message in messages:
        message_dict = message.to_dict()    
        message_timestamp = int(message_dict["timestamp"]) 

        now = int(time.time())
        diff_seconds = now - message_timestamp
        diff_minutes = diff_seconds // 60  

        # Se diferença for maior que 1min, encerra busca no histórico. Só importa ultimo minuto de conversa
        if diff_minutes >= 1:
          break  

        formatted_message = {
            "role": message_dict["role"],
            "parts": message_dict["parts"]            
        }
        messages_array.append(formatted_message)

    return messages_array

# Interação com a Google Gemini API
def talk(userMessage):
    # Obtem ID do usuário logado
    user_id = session["userId"]

    # Obtem histórico de mensagens do usuário
    message_history = messageHistory.getById(user_id)
    message_history_gemini_format = format_messages_for_gemini(message_history)   
    
    # Salva mensagem do usuário em banco de dados
    role = "user"                                       # role=user => mensagem enviada pelo usuário
    messageHistory.store(user_id, role, userMessage)    

    # Inicia interação com Gemini AI
    try:
        convo = model.start_chat(history = message_history_gemini_format) # Inicia chat, contextualizando a IA com o histórico da conversação
        convo.send_message(userMessage)                     # envia nova mensagem para ser processada pela IA
        bot_response = convo.last.text                      # Obtem resposta da IA
    except:
        bot_response = "error"

    # Salva resposta do Bot em banco de dados
    if bot_response != "error":
        role = "model"                                      # role=model => mensagem enviada pela IA
        messageHistory.store(user_id, role, bot_response)    
    else:
        bot_response = "Desculpe, não foi possível obter resposta da Inteligência Artificial."

    response = {"status": "success", "message": bot_response}
    return response