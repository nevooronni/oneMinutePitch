import os

class Config:
	'''
	parent configuration class
	'''
	SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://nevo:speeds01@localhost/pitch'


class ProdConfig(Config):
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
	'production':ProdConfig
}

