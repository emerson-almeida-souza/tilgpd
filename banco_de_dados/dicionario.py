from banco_de_dados.database import retorna_questionario

def monta_array_questionario():
    array_questionario = []
    questionario = retorna_questionario()

    for linha in questionario:
        dicionario = {}
        dicionario = {
            "id": linha[0],
            "pergunta": linha[1],
            "iso": linha[2],
            "artigo": linha[3],
            "recomendacao": linha[4],
        }
        array_questionario.append(dicionario)

    return array_questionario
