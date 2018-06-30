from flask import Flask, render_template, url_for, session, request

app = Flask(__name__)

users = {}

@app.route('/')
def home():
	return 'Welcom to Flask levelUp Application'

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
		if valid_login(request.form['username'],
			request.form['password']):
		    return render_template('login.html')
	return render_template('login.html', error=error)

@app.route('/posts/new')
def add_post():
	return 'Add new post'

@app.route('/comments/new')
def add_comment():
	return 'Add new comment here'	

@app.route('/logout')
def logout():
	pass

if __name__ == '__main__':
	app.run(debug=True)