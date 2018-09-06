import os
from app import pick
from flask import render_template


@app.route('/')
def pick_con():
    response = pick.pickacon()
    return render_template('index.html', title="Create-A-Conspiracy", response = response)