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
    
    username = request.json()["username"]
    email  = request.json()["email"]
    password = request.json()["password"]
    password_confirmation = request.json()["password_confirmation"]
    
    user_info.update({email:{"username": username, "password": password, "password_confirmation": password_confirmation}})
    if email in user_info:
        return jsonify({"message": "successful registered"})
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
@app.route('/level/api/v1/account/<string:name>', methods=['GET'])
def user_details(name):
    """ This is a function fetchs user info """
    uzer = [user for user in users if user['name'] == name]
    return jsonify({'language' : uzer[0]})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
    