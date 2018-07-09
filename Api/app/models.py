from app import db

class User(db.Model):
    """ This is a class for users table """

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
   

    def __init__(self, username):
        """ Initialize with username """
        self.username = username
    

        
class Comment(db.Model):

    """ This is a class for comments table """

    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), nullable=False)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())

   
    def __init__(self, title):
        """ Initialize with title """
        self.title = title
    
    @staticmethod

    def get_all():
        return Comment.query.all()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def __repr__(self):
        return "Comment: {}".format(self.title)