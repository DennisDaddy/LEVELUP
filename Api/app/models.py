from app import db
from flask_bcrypt import Bcrypt

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
   

    def __init__(self, username, password):
        """ Initialize with username and password """
        self.username = username
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
    
    @staticmethod

    def get_all(user_id):
        return Comment.query.filter_by(created_by=user_id)
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    # Tells python how to printobjects of this class
    def __repr__(self):
        return "Comment: {}".format(self.title)