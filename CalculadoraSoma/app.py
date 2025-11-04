from flask import Flask, render_template, request, flash

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    num1 = request.form.get('numero1')
    num2 = request.form.get('numero2')

    try:
        resultado = int(num1) + int(num2)
    except (ValueError, TypeError):(resultado) = "Números inválidos! Por favor, insira números válidos."

    return f"<h2>Resultado: {resultado}</h2>"

if __name__ == '__main__':
    app.run(debug=True)