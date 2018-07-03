from flask import Flask, jsonify, request
from flask import Response

app= Flask(__name__)

@app.route('/')
def home():
	return "Welcome to home page"

@app.route('/level/api/v1/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		username1 = request.form['dennis']
		username2 = request.json.get('username1')

		password = request.form['dennis']
		password2 = request.json.get('password')
		
	return jsonify({'username2'})


@app.route('/level/api/v1/register', methods=['GET', 'POST'])
def register():
	return "register here"

@app.route('/level/api/v1/add_comment', methods=['GET', 'POST'])
def add_comment():
	return "add a comment"

@app.route('/level/api/v1/view_comment', methods=['GET', 'POST'])
def view_comment():
	return "view comment"

@app.route('/level/api/comments', methods=['GET', 'POST'])
def comments():
	return "all comments"

@app.route('/level/api/v1/view_details', methods=['GET', 'POST'])
def view_details():
	return "User details"


if __name__ == '__main__':
		app.run(debug=True)	