import os

class Config:
	'''
	parent configuration class
	'''
	SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://nevo:speeds01@localhost/pitch'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SECRET_KEY=os.environ.get('SECRET_KEY')

class ProdConfig(Config):
	'''
	production configuration child class
	'''
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class DevConfig(Config):
	'''
	development configuration child class
	'''
	SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://nevo:speeds01@localhost/pitch'

	DEBUG = True

config_options = {
	'development':DevConfig,
	'production':ProdConfig
}

