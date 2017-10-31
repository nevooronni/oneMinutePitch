import os

class Config:
	'''
	parent configuration class
	'''
	SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://nevo:toel@localhost/pitch'

class ProductConfig(Config):
	'''
	production configuration child class
	'''
	pass

class DevConfig(Config):
	'''
	development configuration child class
	'''

	DEBUG = True

config_options = {
	'development':DevConfig,
	'production':ProductConfig
}

