from flask import Flask, render_template, request
from flask_table import Table, Col
import csv
import array

# import requests

app = Flask(__name__)


@app.route("/ivao")
def ivao():

    # Get some objects

    f = open("teste.csv", "r")
    user_id = []
    nome = []
    curso = []
    '''OPENING and reading CSV'''
    with open(r'teste.csv') as csv_file:
        read_csv = csv.reader(csv_file)
        for line in read_csv:
            user_id.append(line[0])
            nome.append(line[1])
            curso.append(line[2])

    print(curso)

    class ItemTable(Table):
        name = Col('Name')
        description = Col('Description')

    class Item(object):
        def __init__(self, user_id, nome, curso):
            self.user_id = user_id
            self.curso = curso
            self.nome = nome

    items = [Item(user_id, nome, curso)]

    # Populate the table
    table = ItemTable(items)
    print(table.__html__())
    return table.__html__()


if __name__ == "__main__":
    app.run(debug=True)
