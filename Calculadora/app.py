from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    num1 = request.form.get('numero1')
    num2 = request.form.get('numero2')
    operacao = request.form.get('operacao')

    try:
        num1 = float(num1)
        num2 = float(num2)

        if operacao == 'soma':
            resultado = num1 + num2
        elif operacao == 'subtracao':
            resultado = num1 - num2
        elif operacao == 'multiplicacao':
            resultado = num1 * num2
        elif operacao == 'divisao':
            resultado = num1 / num2
        else:
            resultado = "Operação inválida!"

    except ValueError:
        resultado = "Números inválidos! Por favor, insira valores numéricos."

    return f"<h2>Resultado: {resultado}</h2><br><a href='/'>Voltar</a>"

if __name__ == '__main__':
    app.run(debug=True)