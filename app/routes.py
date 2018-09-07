from app import app
from app import pick
from faker import Faker
from time import strftime
from time import strptime
from flask import render_template, flash, redirect, url_for
from app.forms import WhoForm
from app.forms import WhatForm
from app.forms import HowForm
from app.who import who as who_list
from app.how import how as how_list
from app.what import what as what_list




@app.route('/')
@app.route('/index')
def index():
    fake = Faker()
    response1 = pick.pickacon()
    response2 = pick.pickacon()
    response3 = pick.pickacon()
    response4 = pick.pickacon()
    response5 = pick.pickacon()
    randomtext = fake.text() + " " + fake.text() + " " + fake.text() + " " + fake.text()+ " " + fake.text() + " " + fake.text() + " " + fake.text()+ " " + fake.text() + " " + fake.text() + " " + fake.text()
    randomtext1 = fake.text() + " " + fake.text() + " " + fake.text() + " " + fake.text()+ " " + fake.text() + " " + fake.text() + " " + fake.text()+ " " + fake.text() + " " + fake.text() + " " + fake.text()
    randomtext2 = fake.text() + " " + fake.text() + " " + fake.text() + " " + fake.text()+ " " + fake.text() + " " + fake.text() + " " + fake.text()+ " " + fake.text() + " " + fake.text() + " " + fake.text()
    randomtext3 = fake.text() + " " + fake.text() + " " + fake.text() + " " + fake.text()+ " " + fake.text() + " " + fake.text() + " " + fake.text()+ " " + fake.text() + " " + fake.text() + " " + fake.text()
    randomtext4 = fake.text() + " " + fake.text() + " " + fake.text() + " " + fake.text()+ " " + fake.text() + " " + fake.text() + " " + fake.text()+ " " + fake.text() + " " + fake.text() + " " + fake.text()
    name = fake.name()
    name1 = fake.name()
    name2 = fake.name()
    name3 = fake.name()
    name4 = fake.name()
    date = fake.date()
    city = fake.city()
    state = fake.state()

    return render_template('newbase.html', title="Create-A-Conspiracy", response1 = response1, response2 = response2,
     response3 = response3, response4 = response4, response5 = response5, randomtext = randomtext,
     randomtext1 = randomtext1, randomtext2 = randomtext2, randomtext3 = randomtext3, randomtext4 = randomtext4, name=name,
     name1 = name1, name2= name2, name3=name3, name4=name4, date = date, city = city, state = state)

@app.route('/who', methods=['GET', 'POST'])
def who():
    form = WhoForm()
    if form.validate_on_submit():
        flash('Adding {}'.format(form.who.data))
        who_list.append(form.who.data)
        return redirect('/who')
    return render_template('who.html', title='Whodoneit?', form=form, who_list=who_list)

@app.route('/what', methods=['GET', 'POST'])
def what():
    form = WhatForm()
    if form.validate_on_submit():
        flash('Adding {}'.format(form.what.data))
        what_list.append(form.what.data)
        return redirect('/what')
    return render_template('what.html', title='Whatdidtheydo?', form=form, what_list = what_list)

@app.route('/how', methods=['GET', 'POST'])
def how():
    form = HowForm()
    if form.validate_on_submit():
        flash('Adding {}'.format(form.how.data))
        how_list.append(form.how.data)
        return redirect('/how')
    return render_template('how.html', title='Howdidtheydoit?', form=form, how_list = how_list)
