import time
import repository.db_resource as dbr

# Instância de conexão com banco de dados NoSQL Google Firestore
db = dbr.firestore_resource()       

# Obtem histórico de mensagens a partir do ID do usuário
def getById(user_id):
    collection = f"message_history_{user_id}"
    messages_ref = db.collection(collection).order_by("timestamp")
    messages = messages_ref.stream()

    return messages

# Salva mensagem para recuperação de histórico de conversa na contextualização da resposta
def store(user_id, role, message):
    collection = f"message_history_{user_id}"
    try:
        doc_ref = db.collection(collection).document()
        doc_ref.set({
            "timestamp": int(time.time()),
            "role": role,
            "parts": [message]
        })    
    except Exception as e:
        print(f"Erro ao salvar mensagem no banco de dados. Detalhes: {e}")
        return False
