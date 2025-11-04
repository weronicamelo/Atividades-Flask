from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form['nome']
        cor = request.form['cor']
        return redirect(url_for('saudacao', nome=nome, cor=cor))
    return render_template('index.html')

@app.route('/saudacao/<nome>/<cor>')
def saudacao(nome, cor):
    return render_template('saudacao.html', nome=nome, cor=cor)

if __name__ == '__main__':
    app.run(debug=True)
