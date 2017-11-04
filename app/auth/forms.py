from flask_wtf import FlaskForm#class from the extension
from wtforms import StringField,SubmitField,ValidationError,PasswordField,BooleanField#input fields
from wtforms.validators import Required,Email,EqualTo#equal to compares two passwords
from ..models import User

class RegistrationForm(FlaskForm):
	email = StringField('Your Email Address',validators=[Required(),Email()])
	username = StringField('Enter Your Username',validators=[Required()])
	password = PasswordField('Password',validators=[Required(),EqualTo('password_confirm',message = 'passwords must match')])
	password_confirm = PasswordField('Confirm Password',validators=[Required()])
	submit = SubmitField('REGISTER')

	#CUSTOM VALIDATORS
	def validate_email(self,data_field):
		if User.query.filter_by(email =data_field.data).first():
			raise ValidationError('that email address is already in use!')

	def validate_username(self,data_field):
		if User.query.filter_by(username =data_field.data).first():
			raise ValidationError('that username is already taken!')		

class LoginForm(FlaskForm):
	email = StringField('Your Email Address',validators=[Required(),Email()])
	Password = PasswordField('password',validators=[Required()])
	remeber = BooleanField('Remember me')	
	submit = SubmitField('LOG IN')


