from app import db

class Comment(db.Model):
    """This class represents the comments table."""

    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

    def __init__(self, title):
        """initialize with title."""
        self.title = title

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Comment.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Comment: {}>".format(self.title)
