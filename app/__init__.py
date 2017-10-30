from flask import Flask #import the flask class 
from .config import DevConfig #import our devconfig subclass

#initializing application
app = Flask(__name__)  #use flask class to create an app instance

#setting up configuration 
app.config.from_object(DevConfig)

from app import views #import our views from app folder