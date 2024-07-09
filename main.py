from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)
