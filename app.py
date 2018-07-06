""" Import python modules"""
from flask import Flask, jsonify, request, abort
import jwt
import datetime
from functools import wraps


app = Flask(__name__)

app.config['SECRET_KEY'] = 'supe-user'


posts = [{'id' : 1, 'title' : u'this is one', 'content' : u'this is the content'},
         {'id' : 2, 'title' : u'this is two', 'content' : u'this is the second content'}]

user_info = {}

# Root/Home endpoint
@app.route('/', methods=['GET'])
def home():
    """ This function retuns the home page  """
    return jsonify({'message' : 'Welcome to home page'})
#Authentication
def token_required(f):
    """ Authentication  function"""
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'message' : 'Token is missing'}), 403
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'message' : 'Token is invalid'}), 403

        return f(*args, **kwargs)
    return decorated

# Register user endpoint
@app.route('/level/api/v1/register', methods=['POST'])
def register():
    """ This is a function for refistering users  """
    username = request.get_json()["username"]
    email = request.get_json()["email"]
    password = request.get_json()["password"]
    password_confirmation = request.get_json()["password_confirmation"]

    if not username or len(username.strip()) == 0:
        return jsonify({"message": "Username cannot be blank"}), 401
    elif not email:
        return jsonify({"message": "Email cannot be blank"}), 401

    elif not password:
        return jsonify({"message": "Password cannot be blank"}), 401
    user_info.update({username:{"email": email, "password": password,
                                "password_confirmation": password_confirmation}})
    if username in user_info:
        return jsonify({'message': "You are successfuly Registered"})
    return jsonify({'message': "You are successfuly Registered"})
 # Login user endpoint
@app.route('/level/api/v1/login', methods=['POST'])
def login():
    """ This is a function for loggin a user """
    if auth and auth.password == 'password':
        token = jwt.encode({'user' : auth.username, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
        return jsonify('token': token)
    username = request.get_json()["username"]
    password = request.get_json()["password"]
    if username in user_info:
        if password == user_info[username]["password"]:
            return jsonify({"message": "You are successfuly  logged in"})
    return jsonify({'message': "You are successfuly Registered"})
# Add comment endpoint
@app.route('/level/api/v1/add_comment', methods=['POST'])
def add_comment():
    """ This is a function for adding comments"""
    if not request.json or not 'title' in request.json:
        abort(400)
    post = {
        'id' : posts[-1]['id'] + 1,
        'title': request.json['title'],
        'content': request.json['content'],
    }
    posts.append(post)
    return jsonify({'post' : post})

# List comments
@app.route('/level/api/v1/comments', methods=['GET'])
def comments():
    """ This is a function listing registering users"""
    return jsonify({'posts' : posts})

# Delete comment
@app.route('/level/api/v1/comments/<int:post_id>', methods=['DELETE'])
def delete_comment(post_id):
    """ This is a function for deleting a comment """
    post = [post for post in posts if post['id'] == post_id]
    if len(post) == 0:
        return jsonify({'message' : "No comment"})
    posts.remove(post[0])
    return jsonify({'result': True})

 # User details endpoint
@app.route('/level/api/v1/account', methods=['GET'])
def user_details():
    """ This is a function fetchs user info """
    return jsonify(user_info)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
