from app import db
from flask_bcrypt import Bcrypt
import jwt
from datetime import datetime, timedelta

class User(db.Model):
    """ This is a class for users table """

    __tablename__ = "users"
    # Columns for the users
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    comments = db.relationship(
        'Comment', order_by='Comment.id', cascade="all, delete-orphan"
    )
   

    def __init__(self,first_name, last_name, email, address, password):
        """ Initialize with email and password """
        self.first_name = data.get('first_name')
        self.last_name = data.get('last_name')
        self.email = data.get('email')
        self.username = data.get('username')
        self.address = data.get('address')
        self.password = Bcrypt().generate_password_hash(password).decode()
    
    def password_is_valid(self, password):
        """ Checks the password and validates it """
        return Bcrypt().check_password_hash(self.password, password)

    def save(self):
        """Save the user to the database """
        db.session.add(self)
        db.session.commit()

   


        
class Comment(db.Model):

    """ This is a class for comments table """

    __tablename__ = "comments"

    # Columns for the comments
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    created_by = db.Column(db.Integer, db.ForeignKey(User.id))

   
    def __init__(self, title, created_by):
        """ Initialize with title """
        self.title = title
        self.created_by = created_by
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def generate_token(self, user_id):
        """ Method for generating access token """
        try:
            payload ={
                'exp': datetime.utcnow() + timedelta(minutes=5),
                'iat': datetime.utcnow(),
                'sub': user_id
            }

            jwt_string = jwt.encode(
                payload,
                current_app.config.get(SECRET),
                algorithm='HS256'
            )
            return jwt_string
        except Exception as e:
            return str(e)

    @staticmethod
    def decode_token(token):
        """ Method for decoding access token """
        try:
            payload = jwt.decode(token, current_app.config.get('SECRET'))
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return "Expired token, please login to get new token"
        except jwt.InvalidTokenError:
            return "Invalid token please register or login"



    def get_all(user_id):
        return Comment.query.filter_by(created_by=user_id)
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    # Tells python how to printobjects of this class
    def __repr__(self):
        return "Comment: {}".format(self.title)