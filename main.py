from flask import Flask
import os
from dotenv import load_dotenv
load_dotenv()  

app = Flask(__name__)

from routes import *

app.secret_key = os.environ.get("SECRET_KEY") 

if __name__ == '__main__':
    app.run(debug=True)