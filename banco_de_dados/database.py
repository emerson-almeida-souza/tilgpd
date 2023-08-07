import sqlite3
import os

file_path = os.path.join(os.path.dirname(__file__), "BANCOLGPDISO.db")
con = sqlite3.connect(file_path)
cur = con.cursor()


def criarTabela():
    cur.execute(
        """
        CREATE TABLE questionario(
        perguntas, 
        iso_27001, 
        artigo_lgpd,
        recomendacao_adequacao
        )
        """
    )


def inserir(sql):
    cur.execute(sql)
    con.commit()
    print(f"DADO INSERIDO!")


def retorna_questionario():
    dados = []
    res = con.execute(
        "SELECT rowid, perguntas, iso_27001, artigo_lgpd, recomendacao_adequacao FROM questionario"
    )

    for dado in res:
        dados.append(dado)

    con.close()
    return dados