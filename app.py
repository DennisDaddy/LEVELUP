""" Import python modules"""
from flask import Flask, jsonify, request, abort

app = Flask(__name__)
#users = []


comms = [{'id' : 1, 'title' : u'this is one', 'content' : u'this is the content'},
         {'id' : 2, 'title' : u'this is two', 'content' : u'this is the second content'}]
users = [{'id' : 1, 'username': 'John', 'email': 'email@username', 'password': 'password',
 'password_confirmation': 'password_confirmation'}, {'id' : 1, 'username': 'John', 'email': 'email@username',
  'password': 'password', 'password_confirmation': 'password_confirmation'}]
user_info ={}

# Root/Home endpoint
@app.route('/', methods=['GET'])
def home():
    """ This function retuns the home page  """
    return jsonify({'message' : 'Welcome to home page'})

# Register user endpoint
@app.route('/level/api/v1/register', methods=['POST'])
def register():
    """ This is a function for refistering users  """
    if not request.json or not 'username' in request.json:
        abort(400)
    user = {
    'id': users[-1]['id'] + 1,
    'username' : request.json['username'],
    'email' : request.json['email'],
    'password' : request.json['password'],
    'password_confirmation' : request.json['password_confirmation']

    }

    users.append(user)
    if not 'email' in request.json and type(request.json['email']()) != unicode:
    	abort (400)
    return jsonify({'user': user})

 # Login user endpoint
@app.route('/level/api/v1/login', methods=['POST'])
def login():
    """ This is a function for loggin a user """
    loger = [user for user in users if user['email'] == email]
    return jsonify({'email' : "You are logged in"})
# Add comment endpoint
@app.route('/level/api/v1/add_comment', methods=['POST'])
def add_comment():
    """ This is a function for adding comments"""
    if not request.json or not 'title' in request.json:
    	abort(400)
    comm = {
            'id' : comms[-1]['id'] + 1,
            'title': request.json['title'],
            'content': request.json['content'],
    }
    comms.append(comm)
    return jsonify({'comm' : comm})

# List comments
@app.route('/level/api/v1/comments', methods=['GET'])
def comments():
    """ This is a function listing registering users"""
    return jsonify({'comms' : comms})

# Delete comment
@app.route('/level/api/v1/comments/<int:comm_id>', methods=['DELETE'])
def delete_comment(comm_id):
    comm = [comm for comm in comms if comm['id'] == comm_id]
    if len(comm) == 0:
         return jsonify({'message' : "No comment"})
    comms.remove(comm[0])
    return jsonify({'result': True})

 # User details endpoint
@app.route('/level/api/v1/account/<int:user_id>', methods=['GET'])
def user_details(user_id):
    """ This is a function fetchs user info """
    uzer = [user for user in users if user['id'] == user_id]
    return jsonify({'user' : uzer[0]})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
    