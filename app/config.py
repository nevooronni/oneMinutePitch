class Config:
	'''
	General configuration parent class
	'''
	pass

class ProdConfig(Config):
	'''
	production configuration child class
	
	Args:
		config: The parent configuration class with Genreal configuration settings
	'''
	pass

class DevConfig(Config):
	'''
	Development configuration child class

	Args:
		config: The parent configuration class with Generatal configuration settings
	'''

	DEBUG = True