# -*- coding: utf-8 -*-

import configparser
import csv
import os
import threading

from flask import Flask, render_template
from webeye import get_online_friends, LoginInvalidError

'''GLOBAL VARS'''
csv_name = 'friends.csv'
run_time = 100.0
'''-----------------'''

app = Flask(__name__)

'''READING CONFIG.INI'''
config = configparser.ConfigParser()
try:
    assert config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))
except AssertionError:
    raise FileNotFoundError('config.ini NOT found! Please create one as specified in the README!')
'''-----------------'''

# Se o login do webeye estiver inválido, este bloco tenta durante 5 segundos até dar timeout
# todo: implementar async para não bloquear a execução
# Corre o webeye de x em x tempo, tempo definido pela global var run_time
# ------------------------------------------------------------------------------------------------------------------
online_friends = []

def run_webeye():	
		threading.Timer(run_time, run_webeye).start() 
		try:
				online_friends = get_online_friends(config['ACCOUNT']['user'], config['ACCOUNT']['password'])
				login_status = 'WebEye login successful'
		except LoginInvalidError:
				login_status = 'WebEye login invalid'

		'''ABRIR CSV FILE'''
		user_list = []
		try:
				with open(csv_name) as csv_file:
						read_csv = csv.reader(csv_file)
						for line in read_csv:
								user = {"user_id": line[0],
												"nome": line[1],
												"curso": line[2],
												# simple hack to check if IDs on friends.csv appear on the online_friends list
												"estado": 1 if line[0] in ' '.join([user for person in online_friends for user in person]) else 0}  # 0=0ff 1=On}
								user_list.append(user)
		except FileNotFoundError:
				raise FileNotFoundError('friends.csv NOT found! Please create one as specified in the README!')
		'''-----------------'''
		print(user_list)
		return user_list, login_status

users, webeye_login_status = run_webeye()
print(users)

@app.route("/")
def ivao():		
		return render_template('home.html', users=users, webeye_login_status=webeye_login_status)


if __name__ == "__main__":
    app.run(debug=True)
