from distutils.log import debug
from multiprocessing import context
from flask import Flask, render_template, request
#import mysql.connector
import pymysql, pymysql.cursors
import os
import time
from datetime import timedelta
import ssl
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
app.config.from_pyfile('config.py')
app.permanent_session_lifetime = timedelta(hours=5)                                         

#==============================================================================
#================================== ATENÇÃO ===================================
#==============================================================================
# 1 - Importar o banco << carford.sql >> no MySQL adicionando o nome.: carford.
# 2 - Adicionar o password correto.
# 3 - Os comandos.: SELECT, INSERT, UPDATE E DELETE estão usando o nome do 
# banco de dados para localizar as tabelas, exemplo, carford.tbcarro 
#==============================================================================
db = pymysql.connect(
    host="localhost", 
    user="root", 
    port=3306,   
    password="teste;"    
) 

from Views import * 

if __name__ == '__main__':    
    app.run(host='127.0.0.1', port=5000, debug=True) #host='127.0.0.1', port=5500, debug=True

    
