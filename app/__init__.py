from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()#bs instance
db = SQLAlchemy()#created a db instance 

def create_app(config_name):
	app = Flask(__name__)

	#configurations
	app.config.from_object(config_options[config_name])

	#initializing flask extensions
	bootstrap.init_app(app)
	db.init_app(app)#passed app instance 

	#register our blueprint
	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)

	return app