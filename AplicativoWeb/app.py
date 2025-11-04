from flask import Flask, render_template, request
import random

app = Flask(__name__)

lorem_phases = {
    "latim": [
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
        "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.",
        "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    ],
    "portugues": [
        "O sol nasce para todos, mas o calor é para quem acorda cedo.",
        "A vida é feita de escolhas e cada escolha define o nosso destino.",
        "Nem sempre o caminho mais fácil é o melhor.",
        "A paciência é a chave para grandes conquistas.",
        "A felicidade está nas pequenas coisas do dia a dia."
    ],
    "ingles": [
        "The quick brown fox jumps over the lazy dog.",
        "Success is not final, failure is not fatal: it is the courage to continue that counts.",
        "Every moment is a fresh beginning.",
        "Dream big and dare to fail.",
        "Happiness depends upon ourselves."
    ]
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        error = None
        try:
            num_paragrafos = int(request.form['num_paragrafos'])
            num_palavras = int(request.form['num_palavras'])
            idioma = request.form['idioma']

            if num_paragrafos <= 0 or num_palavras <= 0:
                error = "Digite números positivos."
                raise ValueError
            if idioma not in lorem_phases:
                error = "Idioma inválido."
                raise ValueError

        except ValueError:
            return render_template('index.html', error=error)

        paragrafos = []
        for i in range(num_paragrafos):
            paragrafo = gerar_paragrafo_quantidade_palavras(num_palavras, idioma)
            paragrafos.append(paragrafo)

        return render_template('resultado.html', paragrafos=paragrafos, idioma=idioma)

    return render_template('index.html')

def gerar_paragrafo_quantidade_palavras(num_palavras, idioma):
    paragrafo = ""
    palavras_atuais = 0

    while palavras_atuais < num_palavras:
        frase = random.choice(lorem_phases[idioma])
        palavras_da_frase = frase.split()
        palavras_faltando = num_palavras - palavras_atuais

        contador = 0
        for palavra in palavras_da_frase:
            if contador >= palavras_faltando:
                break
            paragrafo += palavra + " "
            contador += 1
            palavras_atuais += 1

    return paragrafo.strip()

if __name__ == '__main__':
    app.run(debug=True)
