from flask import Flask, render_template, request
from flask_table import Table, Col

#import requests

app = Flask(__name__)


@app.route("/")
def root():
    return render_template('home.html')


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

    items = [Item('Name1', 'Description1'),
             Item('Name2', 'Description2'),
             Item('Name3', 'Description3')]
    # Or, equivalently, some dicts
    items = [dict(name='Name1', description='Description1'),
             dict(name='Name2', description='Description2'),
             dict(name='Name3', description='Description3')]

    # Populate the table
    table = ItemTable(items)
    print(table.__html__())
    return table.__html__()


if __name__ == "__main__":
    app.run(debug=True)
