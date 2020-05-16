from flask import Flask, render_template, request
from flask_table import Table, Col
import csv
import array

# import requests

app = Flask(__name__)


@app.route("/ivao")
def ivao():

    # criar arrays
    user_id = []
    nome = []
    curso = []
    temp = []
    items = []

    '''-----objects-------'''
    class ItemTable(Table):
        user_id = Col('ID')
        nome = Col('NOME')
        curso = Col('CURSO')

    class Item(object):
        def __init__(self, user_id, nome, curso):
            self.user_id = user_id
            self.curso = curso
            self.nome = nome
    '''-------------------'''

    """ abir o csv """
    with open(r'teste.csv') as csv_file:
        read_csv = csv.reader(csv_file)
        line_index = 0
        for line in read_csv:
            # adicionar as merdas q tão em cada linha ao respetivo array
            user_id.append(line[0])
            nome.append(line[1])
            curso.append(line[2])
            line_index += 1
    print(line_index)
    ''' mete os arrays todos nos items'''
    for x in range(line_index):
        items.append(Item(user_id[x], nome[x], curso[x]))

    # meter as merdas todas numa variavel
    table = ItemTable(items)
    # print(table.__html__())
    # mandar as merdas em HTML
    return table.__html__()


if __name__ == "__main__":
    app.run(debug=True)
