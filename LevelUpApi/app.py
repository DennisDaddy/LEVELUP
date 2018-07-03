from flask import Flask, jsonify, request
from flask import Response

app= Flask(__name__)
#users = []
#user_info ={}

comments = [{'title': 'This is one'}, {'title': 'This is one'}]
users = [{'name': 'John two one'}, {'name': 'kevin omosh four'}]


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

@app.route('/level/api/v1/view_comment', methods=['GET', 'POST'])
def view_comment():
	return "view comment"

@app.route('/level/api/comments', methods=['GET'])
def comments():
	return jsonify({'comments' : comments})
	

if __name__ == '__main__':
		app.run(debug=True)	