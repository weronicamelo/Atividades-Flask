from urllib import request

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    nome = request.form['nome']
    return f"Olá {nome}! Formulário recebido!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
