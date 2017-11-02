from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

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

	#from .auth import auth as auth_blueprint
	#app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

	#initialize flask_login
	#login_manager = LoginManager()
	#login_manager.session_protection = 'strong'#provides security levels strong will moniter changes to a user request header and log the user out.
	#login_manager.login_view = 'auth.login'#prefix the login endpoint with the blueprint name because it is located inside a blueprint

	return app