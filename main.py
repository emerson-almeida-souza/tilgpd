from flask import Flask, render_template, request
from banco_de_dados.dicionario import monta_array_questionario

app = Flask(__name__)

array_questionario = monta_array_questionario()
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/questionario")
def questionario():
    return render_template("questionario.html", array_questionario=array_questionario)
@app.route("/respostas", methods=["GET", "POST"])
def respostas():
    quantasPerguntas = len(array_questionario)
    resposta = None
    for i in range(quantasPerguntas):
        indiceFormulario = i + 1
        if request.form[f"resposta_pergunta_{indiceFormulario}"] == "NAO":
            resposta = False
        elif request.form[f"resposta_pergunta_{indiceFormulario}"] == "SIM":
            resposta = True

        print(f"RESPOSTA PERGUNTA {indiceFormulario} - ", request.form[f"resposta_pergunta_{indiceFormulario}"])
        array_questionario[i]["resposta"] = resposta
        print(f"QUESTIONARIO -  {i}", array_questionario[i]["resposta"])

    return render_template("respostas.html", array_questionario=array_questionario)

if __name__ == '__main__':
    app.run()
