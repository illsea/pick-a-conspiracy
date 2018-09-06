import os
from pick import pickacon

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    response = pickacon()
    return response