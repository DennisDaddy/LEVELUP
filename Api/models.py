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
    comments = relationship("Comment")

    def __ref__(self)
    return '<User: {}>'.format(self.name)

class Comment(db.Model):

    __tablename__ = "comments"

    id = db.Column(db.integer, primary_key=True)
    title = db.Column(db.String(60), nullable=False)
    content = db.Column(db.String(200), nullable=False)
    posts = relationship("Comment")
    

    def __ref__(self)
    return '<Comment: {}>'.format(self.title)