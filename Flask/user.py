from flask import Flask

app = Flask(__name__)

@app.route('/')

def home():
	return 'Welcom to Flask levelUp Application'

@app.route('/register')

def register():
	return 'Register here'

@app.route('/login')
def login():
	return 'Login here'

@app.route('/posts/new')
def add_post():
	return 'Add new post'

@app.route('/comments/new')
def add_comment():
	return 'Add new comment here'		

if __name__ == '__main__':
	app.run(debug=True)