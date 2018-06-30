from flask import Flask, render_template, url_for, session, request

app = Flask(__name__)
app.secret_key = "am cool"

users = {}

@app.route('/welcome')
def welcome():
	return  render_template('welcome.html')

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
	if request.method == 'POST':
		if request.form['username']:

			return render_template('register.html')
	return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'Invalid credetials. please try again'

		else:
			session['logged_in'] = True
			return render_template('/home.html')
	return render_template('login.html', error=error)


@app.route('/posts/new')
def add_post():
	return 'Add new post'

@app.route('/comments/new')
def add_comment():
	return 'Add new comment here'	

@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	return render_template('welcome.html')

if __name__ == '__main__':
	app.run(debug=True)


