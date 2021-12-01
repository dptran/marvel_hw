from app import db
from datetime import datetime as dt

class Collection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    comic_appearances = db.Column(db.Integer)
    superpowers = db.Column(db.String)
    date_created = db.Column(db.DateTime, default=dt.utcnow)
    owner = db.Column(db.Integer, db.ForeignKey('user.id'))

    def to_dict(self):
        from app.blueprints.auth.models import User

        data = {
            'body': self.body,
            'date_created': self.date_created,
            'user': User.query.get(self.user_id).to_dict()
        }
        return data
