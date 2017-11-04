from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class NewPitchForm(FlaskForm):
	lines = TextAreaField('NEW PITCH')
	submit = SubmitField('SUBMIT')

class CommentForm(FlaskForm):
	comment = TextAreaField('NEW COMMENT')
	submit = SubmitField('SUBMIT')
	