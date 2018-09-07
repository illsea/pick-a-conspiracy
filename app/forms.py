from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class WhoForm(FlaskForm):
    who = StringField('Who', validators=[DataRequired()])
    submit = SubmitField('Submit')

class WhatForm(FlaskForm):
    what = StringField('What', validators=[DataRequired()])
    submit = SubmitField('Submit')

class HowForm(FlaskForm):
    how = StringField('How', validators=[DataRequired()])
    submit = SubmitField('Submit')

