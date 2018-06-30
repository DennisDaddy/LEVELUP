from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def home():
	return 'Welcom to Flask levelUp Application'

@app.route('/register')

def register():
	return render_template('register.html')

@app.route('/login', methods=['GET'], ['POST'])
def login():
	return render_template('login.html')

@app.route('/posts/new')
def add_post():
	return 'Add new post'

@app.route('/comments/new')
def add_comment():
	return 'Add new comment here'		

if __name__ == '__main__':
	app.run(debug=True)