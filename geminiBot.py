import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()  

my_api_key = os.environ.get("API_KEY")                        # Gemini - API_KEY
system_instruction = os.environ.get("SYSTEM_INSTRUCTIONS")    # Gemini - Instruções do Sistema / Informa as caracteristicas do Assistente.
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

def botMessage():
    body_message = "Oi"
    message_history = []
    
    convo = model.start_chat(history = message_history) # Inicia chat, contextualizando a IA com o histórico da conversação
    convo.send_message(body_message)                    # envia nova mensagem para ser processada pela IA
    botResponse = convo.last.text                       # Obtem resposta da IA
    response = {"message": botResponse}
    
    return response