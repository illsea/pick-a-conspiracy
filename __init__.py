import os


from flask import Flask
app = Flask(__name__)

@app.route('/')
def con_pick():
    return 'Hello, World!'