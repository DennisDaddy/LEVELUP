""" Import python modules"""
from flask import Flask, jsonify, request

app = Flask(__name__)
#users = []
#user_info ={}

comms = [{'title' : 'this is one', 'content' : 'this is the content'},
         {'title' : 'this is two', 'content' : 'this is the second content'}]
users = [{'name': 'John'}, {'name': 'kevin'}]

# Root/Home endpoint
@app.route('/', methods=['GET'])
def home():
    """ This function retuns the home page  """
    return jsonify({'message' : 'Welcome to home page'})

 # Login user endpoint
@app.route('/level/api/v1/login', methods=['POST'])
def login():
    """ This is a function for loggin a user """
    if request.method == 'POST':
        data = request.get_json()
        user_name = data['user_name']
        password = data['password']
    return jsonify({'user_name' : user_name, 'password' : password})

# Register user endpoint
@app.route('/level/api/v1/register', methods=['POST'])
def register():
    """ This is a function for refistering users  """
    if request.method == 'POST':
        data = request.get_json()
        first_name = data['first_name']
        last_name = data['last_name']
        user_name = data['user_name']
        email = data['email']
        password = data['password']
    return jsonify({'first_name' : first_name, 'last_name' : last_name,
        	           'user_name' : user_name, 'email' : email, 'password' :password})

# Add comment endpoint
@app.route('/level/api/v1/add_comment', methods=['POST'])
def add_comment():
    """ This is a function for adding comments"""
    if request.method == 'POST':
        data = request.get_json()
        title = data['title']
        content = data['content']
    return jsonify({'title' : title, 'content' : content})

# List comments
@app.route('/level/api/v1/comments', methods=['GET'])
def comments():
    """ This is a function listing registering users"""
    return jsonify({'comms' : comms})

 # User details endpoint
@app.route('/level/api/v1/account/<string:name>', methods=['GET'])
def user_details(name):
    """ This is a function fetchs user info """
    uzer = [user for user in users if user['name'] == name]
    return jsonify({'language' : uzer[0]})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
    