from app import db
from datetime import datetime as dt

<<<<<<< HEAD

=======
>>>>>>> eef9db4ed2bf415e0ca66ce16e365942756f774f
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
<<<<<<< HEAD
            'name': self.name,
            'description': self.description,
            'date_created': self.date_created,
            'owner': User.query.get(self.owner).to_dict()
=======
            'body': self.body,
            'date_created': self.date_created,
            'user': User.query.get(self.user_id).to_dict()
>>>>>>> eef9db4ed2bf415e0ca66ce16e365942756f774f
        }
        return data
