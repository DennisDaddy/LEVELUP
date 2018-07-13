from app import db
from flask_bcrypt import Bcrypt
import jwt
from datetime import datetime, timedelta

class User(db.Model):
    """ This is a class for user table"""
    __tablename__ = 'users'

    # Column for users

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

    comments = db.relationship(
        'Comment', order_by='Comment.id', cascade="all, delete-orphan"
    )

    def __init__(self, email, password):
        """initialize user with email and password """
        self.email = email
        self.password = Bcrypt().generate_password_hash(password).decode()
    
    def password_is_valid(self, password):
        """ validates password """
        return Bcrypt().check_password_hash(self.password, password)
    
    def save(self):
        """ Save user to the database"""
        db.session.add(self)
        db.session.commit()

    def generate_token(self, user_id):
        """Generate access token """
        try:
            # try setting up payload with expiration time
            payload = {
                'exp': datetime.utcnow() + timedelta(minutes=5),
                'iat': datetime.utcnow(),
                'sub': user_id
            }

            # create the string token using payload and the secret kay
            jwt_string = jwt.encode(
                payload,
                current_app.config.get('SECRET'),
                algorithm='HS256'
            )

            return jwt_string

        except Exception as e:
            # return an error in string format is an exception ocurs
            return str(e)
        

        @staticmethod

        def decode_token(token):
            """ Decodes access token from authorized header"""
            try:
                # try decoding the token 
                payload = jwt.decode(token, current_app.config.get('SECRET'))
                return payload['sub']
            except jwt.ExpiredSignatureError:
                # the token is expired return an error string
                return "Expired token please login to get a new token"
            except jwt.InvalidTokenError:
                # the token is invalid, return an error string
                return "Invalid token, please register or login" 






class Comment(db.Model):
    """This class represents the comments table."""

    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())
    created_by = db.Column(db.Integer, db.ForeignKey(User.id))

    def __init__(self, title, created_by):
        """initialize with title."""
        self.title = title
        self.created_by = created_by

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all(user_id):
        return Comment.query.filter_by(created_by=user_id)

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Comment: {}>".format(self.title)
