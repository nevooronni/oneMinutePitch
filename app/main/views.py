from flask import render_template
from . import main
from ..models import Categories#ineter python relative import system
from .. import db#external python import system

@main.route('/')
def index():
	'''
	main pages that returns a list of pitch category on the index page
	'''
	categories = Categories.list_categories()
	title = 'Home - welcome to Pitch Perfect'
	return render_template('index.html',title = title, categories = categories)