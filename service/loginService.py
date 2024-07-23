from flask import session
import repository.userRepository as users

def login(username, password, usertype, ip_address):
    
    if usertype == "guest":
        guest = users.store_guest(ip_address)
        if guest != "error":
            status = "success" 
            session["userId"] = guest
            session["userName"] = guest
            session["userRole"] = "Guest"
        else:
            status = "errorGuest"
    else:
        user = users.find("name", username)
        if user is None:
            status = "errorUser"
        else:
            doc_dic = user[0].to_dict()
            if doc_dic["password"] != password:
                status = "errorPwd" 
            else:
                status = "success" 
                session["userId"] = doc_dic["id"]
                session["userName"] = username
                session["userRole"] = doc_dic["role"]            
    
    response = {"status": status}
    return response    

def logout():
    try:
        session.pop('userId', None)
        session.pop('userName', None)        
        session.pop('userRole', None)  
        response = {"status": "success"}
    except:
        response = {"status": "error"}
    return response