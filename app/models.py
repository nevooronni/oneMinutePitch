from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime
from flask_login import UserMixin#configures our user model to work with the flask-login extension
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))#queries db and gets a user with the id.

class Categories(db.Model):
	'''
	class that for different pitch category
	'''
	__tablename__ = 'categories'

	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(255))
	overview = db.Column(db.String(300))

	def add_category(self):
		'''
		this function will add a category to our db
		'''
		db.session.add(self)
		db.session.commit()

	@classmethod
	def list_categories(cls):
		'''
		function that will query the database and to get our list of pitch categories
		'''
		categories = Categories.query.all()
		return categories

class User(UserMixin,db.Model):
	'''
	class that identifiers a user
	'''
	__tablename__ = 'users'
	id = db.Column(db.Integer,primary_key = True)
	username = db.Column(db.String(255))
	email = db.Column(db.String(255),unique = True,index = True)
	role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))#foreign key column definig the one to many relationship
	pass_secure = db.Column(db.String(255))

	@property
	def password(self):#blocks access to the password property not users to have access to that property
		raise AttributeError('You cannot read the password')

	@password.setter
	def password(self,password):
		self.pass_secure = generate_password_hash(password)

	def verify_password(self,password):
		return check_password_hash(self.pass_secure,password)	

	def __repr__(self):
		return f'User {self.username}'

class Role(db.Model):
	'''
	class that assigns a role e.g admin or user to a person using the application
	'''
	__tablename__ = 'roles'
	id = db.Column(db.Integer,primary_key = True)
	name = db.Column(db.String(255))
	users = db.relationship('User',backref = 'role',lazy="dynamic")#virtual column that connects with our foreign key backref to access User class and get their tole lazy is how sqlalchemy loads our projects

	def __repr__(self):
		return f'User {self.name}'

class PitchList(db.Model):
	'''
	class that list of the pitches for a specific category
	'''
	pitch_list = []

	__tablename__ = 'pitches'

	id = db.Column(db.Integer,primary_key = True)
	user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
	category_id = db.Column(db.Integer,db.ForeignKey('categories.id'))
	lines = db.Column(db.Integer,primary_key = True)
	date = db.Column(db.DateTime,default=datetime.now)

	def add_pitches(self):
		'''
		add pitches to db
		'''
		db.session.add(self)
		db.session.commit()

	@classmethod
	def list_pitch(cls,id):
		pitches = PitchList.query.order_by(PitchList.date.desc()).filter_by(category_id=id)
		return pitches

	@classmethod
	def list_all_pitches(cls):
		all_pitches = PitchList.query.all()
		return all_pitches

