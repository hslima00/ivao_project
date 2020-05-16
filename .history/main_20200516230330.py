from flask import Flask, render_template, request
from flask_table import Table, Col
import csv
import array


app = Flask(__name__)


@app.route("/ivao")
def ivao():

    user_id = []
    nome = []
    curso = []
    temp = []
    items = []

    class ItemTable(Table):
        user_id = Col('ID')
        nome = Col('NOME')
        curso = Col('CURSO')
        estado = Col('ESTADO')

    class Item(object):
        def __init__(self, user_id, nome, curso):
            self.user_id = user_id
            self.curso = curso
            self.nome = nome

    with open(r'teste.csv') as csv_file:
        read_csv = csv.reader(csv_file)
        line_index = 0
        for line in read_csv:

            user_id.append(line[0])
            nome.append(line[1])
            curso.append(line[2])
            line_index += 1

    for x in range(line_index):
        items.append(Item(user_id[x], nome[x], curso[x]))

    table = ItemTable(items)

    return table.__html__()


if __name__ == "__main__":
    app.run(debug=True)
