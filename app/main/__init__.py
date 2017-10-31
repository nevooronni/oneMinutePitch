from flask import Blueprint
main = Blueprint('main',__name__)#name of the blueprint and how we find it
from . import views