from . import db

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

class User(db.Model):
	'''
	class that identifiers a user
	'''
	__tablename__ = 'users'
	id = db.Column(db.Integer,primary_key = True)
	username = db.Column(db.String(255))
	role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))#foreign key column definig the one to many relationship
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
