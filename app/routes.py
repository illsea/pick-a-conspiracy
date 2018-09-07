from app import app
from app import pick
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    response = pick.pickacon()
    return render_template('index.html', title="Create-A-Conspiracy", response = response)