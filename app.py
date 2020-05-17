from flask import Flask, render_template, request
from flask_table import Table, Col
import csv
import array

csv_name = 'teste.csv'
app = Flask(__name__)


@app.route("/")
def ivao():

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
