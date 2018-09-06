import os
from pick import pickacon
from flask import render_template

from flask import Flask
app = Flask(__name__)

@app.route('/')
def pick_con():
    response = pickacon()
    return render_template('index.html', title="Create-A-Conspiracy", response = response)