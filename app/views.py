from flask import render_template #function loads our templates
from app import app #app instance


#views
@app.route('/') #route decorator 
def index():#define the view function 

	'''
	view root page function that returns the index page and its data 
	'''

	message = 'Hello World'
	title = 'Home - Welcome to The Best one minute pitch Review website online'
	return render_template('index.html',message = message,title = title)

@app.route('/pitch/<int:pitch_id>')	#<> that is the dynamic part renedered as string in defaults but can be parts as integers
def pitch(pitch_id):

	'''
	view pitch page function that returns the pitch category and its details
	'''
	return render_template('pitch.html',id = pitch_id)
	
