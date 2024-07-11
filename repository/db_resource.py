import os
import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv
load_dotenv()  

# Inicializa o FireStore - Banco NoSQL
def firestore_resource():  
    path_credential = os.environ.get("PATH_CREDENTIAL_FIRESTORE")    
    cred = credentials.Certificate(path_credential)                 
    firebase_admin.initialize_app(cred)
    return firestore.client()