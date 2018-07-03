from flask import Flask, jsonify, request
from flask import Response

app= Flask(__name__)

@app.route('/')
def home():
	return "Welcome to home page"

@app.route('/level/api/v1/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		data = request.get_json()
		user_name = data['user_name']
		password = data['password']
		return jsonify({'user_name' : user_name, 'password' : password})

@app.route('/level/api/v1/register', methods=['GET', 'POST'])
def register():
	if request.method == 'POST':
		data = request.get_json()
		first_name = data['first_name']
		last_name = data['last_name']
		user_name = data['user_name']
		email = data['email']
		password = data['password']

		return jsonify({'first_name' : first_name, 'last_name' : last_name, 'user_name' : user_name, 'email' : email,
			'password' :password})


@app.route('/level/api/v1/add_comment', methods=['GET', 'POST'])
def add_comment():
	comment = request.json['title']
	return comment

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