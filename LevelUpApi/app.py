from flask import Flask, jsonify, request
from flask import Response

app= Flask(__name__)
#users = []
#user_info ={}

comms = [{'title' : 'this is one', 'content' : 'this is the content'},{'title' : 'this is two', 'content' : 'this is the second content'}]
users = [{'name': 'John'}, {'name': 'kevin'}]


@app.route('/', methods=['GET'])
def home():
	return "Welcome to home page"
	return jsonify({'message' : 'Welcome to home page'})

@app.route('/level/api/v1/login', methods=['POST'])
def login():
	if request.method == 'POST':
		data = request.get_json()
		user_name = data['user_name']
		password = data['password']
		return jsonify({'user_name' : user_name, 'password' : password})

@app.route('/level/api/v1/register', methods=['POST'])
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


@app.route('/level/api/v1/add_comment', methods=['POST'])
def add_comment():
	if request.method == 'POST':
		data = request.get_json()
		title = data['title']
		content = data['content']
		return jsonify({'title' : title, 'content' : content})
	else:	
	    return jsonify({'title' : 'comment not created'})	


@app.route('/level/api/v1/user/<string:name>', methods=['GET'])
def user_details(name):
	uzer = [user for user in users if user['name']== name]
	return jsonify({'language' : uzer[0]})


if __name__ == '__main__':
		app.run(debug=True, port=5000)	