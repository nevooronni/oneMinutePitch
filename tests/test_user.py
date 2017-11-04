import unittest
from app.models import User

class UserTest(unittest.TestCase):
	'''
	test for user model
	'''
	def setUp(self):
		self.new_user = User(password = 'banana')

	def test_password_setter(self):
		self.assertTrue(self.new_user.pass_secure is not None)#checks password is being hashed  and the pass_secure contanis a value

	def test_no_access_password(self):
		with self.assertRaises(AttributeError):#checks to see if our app raises an attribute error when we try to access the password
			self.new_user.password

	def test_password_verification(self):
		self.assertTrue(self.new_user.verify_password('banana'))
