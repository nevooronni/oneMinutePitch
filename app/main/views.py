from flask import render_template,redirect,url_for,abort
from . import main
from ..models import Categories,User,PitchList#ineter python relative import system
from .. import db#external python import system
from flask_login import login_required,current_user#intercept a request and check is user is authenticated
from .forms import NewPitchForm

@main.route('/')
def index():
	'''
	main pages that returns a list of pitch category on the index page
	'''
	categories = Categories.list_categories()
	title = 'Home - welcome to Pitch Perfect'
	return render_template('index.html',title = title, categories = categories)

@main.route('/category/<int:id>')
def category(id):
	'''
	This route witll return the list of pitches for that particular category
	'''
	specific_category = Categories.query.get(id)

	if specific_category is None:
		abort(404)

	pitches = PitchList.list_pitch(id)
	form = NewPitchForm()
	title = "PITCHES"

	return render_template('categories.html',title = title,specific_category = category,pitches = pitches,pitch_form = form)

@main.route('/category/pitch/new/<int:id>', methods = ['GET','POST'])
def new_pitch(id):
		'''
		route for a displaying a new pitch form
		'''
		form = NewPitchForm()
		category = Category.query.filter_by(id=id).first()

		if category is None:
			abort(404)

		if form.validate_on_submit():
			lines = form.lines.data
			# user = current_user._get_current_object()
			new_pitch = Peptalk(lines=lines,user_id=current_user.id,category_id=category.id)
			new_pitch.save_pitch()
			return redirect(url_for('.category', id = category.id))

		title = 'NEW PITCH'
		return render_template('new_pitch.html',title = title,pitch_form = form)
#@main.route('/category/pitch/new/<int:id>',methods = ["GET","POST"])
#def new_pitch(id):
	#'''
	#route for a displaying a new pitch form
	#'''
	#specific_category = Categories.query.filter_by(id=id).first()#get specific category

	#if specific_category in None:
		#abort(404)

	#form = NewPitchForm()#

	#if form.validate_on_submit():
		#lines = form.lines.data
		#update pitch instance
		#new_pitch = NewPitchForm(lines = lines,user_id = current_user.id,category_id = category.id)
		#save pitch to db
		#new_pitch.add_pitches()
		#return redirect(url_for('.category', id = category.id))

	#title = 'NEW PITCH'
	#return render_template('new_pitch.html',title = title, pitch_form = form)