############## Seyhan Van Khan & Alizeh Khan
############## Dubai Little League
############## June 2020 - July 2020
############## dubailittleleague.com

################################ IMPORT MODULES ################################


from flask import Flask, render_template, session, request, Markup
from data import *

svg = {key: Markup(value) for key, value in svg.items()}


################################### INIT APP ###################################


app = Flask(__name__)
app.secret_key = "stubblyainslieprocrastination"


################################### HOME PAGE ##################################


@app.route('/')
def index():
	return render_template('index.html',
												 svg=svg,
						             session_username=session['username'] if 'username' in session else None)


################################ DIVISION & FEES ###############################


@app.route('/divisions-fees')
def divisions_fees():
	return render_template('divisions-fees.html',
												 divisionTableHeaders=divisionTableHeaders,
												 divisionTable=divisionTable,
												 challengerDescription=challengerDescription,
												 svg=svg)


################################### VOLUNTEER ##################################


@app.route('/volunteer')
def volunteer():
	return render_template('volunteer.html',
												 svg=svg)


################################### SCHEDULE ###################################


@app.route('/schedule')
def schedule():
	return render_template('schedule.html',
												 svg=svg)


##################################### LOGIN ####################################


@app.route('/login')
def login():
	return render_template('login.html',
												 svg=svg)


#################################### SIGNUP ####################################


@app.route('/signup')
def signup():
	return render_template('signup.html',
												 svg=svg)


################################ MOBILE REDIRECT ###############################


@app.route('/error')
def error_page():
	return """
		<script type="text/javascript" src="static/js/compRedirect.js"></script>
		<h1>
			Please view this site on desktop or laptop
		</h1>
	"""


################################# OTHER ROUTES #################################


@app.errorhandler(404)
def not_found(e):
	print()
	print(e)
	print()
	return render_template('error404.html',
												 request_path=request.path)


#################################### APP RUN ###################################


if __name__ == "__main__":
    app.run(debug=True)
