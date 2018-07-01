from flask import Flask, render_template, url_for, session, request, redirect

app = Flask(__name__)
app.secret_key = "am cool"


users = []
user_info = {}

comments = []
comment_info = {}

posts = []
post_info = {}

@app.route('/welcome')
def welcome():
	return  render_template('welcome.html')

@app.route('/home')
def home():
	return render_template('home.html')

# Register user
@app.route('/register', methods=['GET', 'POST'])
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

# Login User
@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		for user in users:
		    if user_info['username'] == request.form['username']:
		        return redirect(url_for('welcome'))
		    else:
		        return redirect(url_for('register'))
	return render_template('login.html', error=error)

# Create post
@app.route('/posts/new', methods=['GET', 'POST'])
def add_post():
	if request.method == 'POST':
		post_info['post_id'] = len(posts)+1
		post_info['title'] = request.form.get('title')
		post_info['content'] = request.form.get('content')
		
		posts.append(post_info)
		# print posts in terminal 
		print(posts)
		return render_template('new_post.html')
	return render_template('new_post.html')

# Create comment
@app.route('/comments/new', methods=['GET','POST'])
def add_comment():
	if request.method == 'POST':
		comment_info['comment_id'] = len(comments)+1
		comment_info['title'] = request.form.get('title')
		comment_info['content'] = request.form.get('content')
		
		comments.append(comment_info)
		# print comments in terminal 
		print(comments)
		return render_template('new_comment.html')
	return render_template('new_comment.html')

# Logout user
@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	return render_template('home.html')

if __name__ == '__main__':
	app.run(debug=True)


