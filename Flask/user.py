from flask import Flask, render_template, url_for, session, request, redirect

app = Flask(__name__)
app.secret_key = "am cool"


users = []
user_info = {}
@app.route('/welcome')
def welcome():
	return  render_template('welcome.html')

@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])

# Register user function
def register():
	
	if request.method == 'POST':
		user_info['user_id'] = len(users)+1
		user_info['username'] = request.form.get('username')
		user_info['email'] = request.form.get('email')
		user_info['password'] = request.form.get('password')
		users.append(user_info)
		# print users in terminal 
		print(users)
		return render_template('register.html')
	return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])

# Login user function
def login():
	error = None
	if request.method == 'POST':
		for user in users:
		    if user_info['username'] == request.form['username']:
		        return redirect(url_for('welcome'))
		    else:
		        return redirect(url_for('register'))
	return render_template('login.html', error=error)

@app.route('/posts/new')
# user add post function 
def add_post():
	return 'Add new post'

@app.route('/comments/new')

# user add comment function 
def add_comment():
	return 'Add new comment here'	

@app.route('/logout')

# user logout function 
def logout():
	session.pop('logged_in', None)
	return render_template('home.html')

if __name__ == '__main__':
	app.run(debug=True)


