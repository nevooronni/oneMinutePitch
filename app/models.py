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

	def __repr__(self):
		return f'User {self.username}'
