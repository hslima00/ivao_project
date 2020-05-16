from flask import Flask, render_template, request
from flask_table import Table, Col
import csv
import array

#import requests

#app = Flask(__name__)


@app.route("/ivao")
def ivao():
    class ItemTable(Table):
        name = Col('Name')
        description = Col('Description')

    # Get some objects

    class Item(object):
        def __init__(self, name, description):
            self.name = name
            self.description = description

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


"""  items = [Item('Name1', 'Description1'),
             Item('Name2', 'Description2'),
             Item('Name3', 'Description3')]

    # Populate the table
    table = ItemTable(items)
    print(table.__html__())
    return table.__html__() """


""" if __name__ == "__main__":
    app.run(debug=True)
 """
