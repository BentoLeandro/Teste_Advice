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

db = pymysql.connect(
    host="localhost", 
    user="root", 
    port=3306,   
    password="teste;"    
) 

from Views import * 

if __name__ == '__main__':    
    app.run(host='127.0.0.1', port=5000, debug=True) #ssl_context=context,   host='127.0.0.1', port=5500, debug=True

    
