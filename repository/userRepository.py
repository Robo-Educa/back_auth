import repository.db_resource as dbr

# Main
collection = "users"                # Nome da coleção de documentos.
db = dbr.firestore_resource()       # Instância de conexão com banco NoSQL

def get_all():
    docs_ref = db.collection(collection).order_by("name")
    docs = docs_ref.stream()    
    return docs

def find(field: str, value: str):
    response = None
    doc = db.collection(collection).where(field_path=field, op_string="==", value=value).get()
    if doc:
        response = doc        
    return response

def delete(field: str, value: str):
    try:        
        doc = find(field,value)
        if doc:
            doc[0].reference.delete()
        response = "success"
    except Exception as e:
        response = e
    return response

def update(field: str, value: str, new_doc: dict):
    try:        
        doc = find(field, value)
        if doc:
            doc[0].reference.update(new_doc)
            response = "success"
    except Exception as e:
        response = e
    return response