import configparser
import csv
import os

from flask import Flask, render_template
from webeye import get_online_friends, LoginInvalidError

csv_name = 'teste.csv'
app = Flask(__name__)

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))


@app.route("/")
def ivao():

    online_friends = []
    try:
        online_friends = get_online_friends(config['ACCOUNT']['user'], config['ACCOUNT']['password'])
    except LoginInvalidError:
        return '<h1>WebEye login invalid<h1>'

    item_list = []

    with open(csv_name) as csv_file:
        read_csv = csv.reader(csv_file)
        for line in read_csv:

            item = {"user_id": line[0],
                    "nome": line[1],
                    "curso": line[2],
                    "estado": line[3]}  # 0=0ff 1=On}
            item_list.append(item)

    return render_template('home.html', item_list=item_list)


if __name__ == "__main__":
    app.run(debug=True)
