import os

SECRET_KEY = 'test435679'
SEND_FILE_MAX_AGE_DEFAULT = 0
UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) +'/uploads' #__file__ é o nome do arquivo app.py
