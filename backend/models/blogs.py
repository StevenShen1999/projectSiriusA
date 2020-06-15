from app import db

class Blogs(db.Model):
    __tablename__ = 'blogs'

    id = db.Column(db.Text, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    createdon = db.Column(db.DateTime(timezone=True), nullable=False)

    def jsonifySelf(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'createdOn': self.createdon
        }