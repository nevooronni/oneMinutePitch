from flask_wtf import FlaskForm 
from wtforms import StringField,TextAreaField,SubmitField

class NewPitchForm(FlaskForm):
	pitch = TextAreaField('NEW PITCH')
	submit = SubmitField('SUBMIT')
	