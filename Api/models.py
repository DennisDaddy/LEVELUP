from app import db

class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __init__(self)

    def __ref__(self)
    return '<{}>'.format(self.name)