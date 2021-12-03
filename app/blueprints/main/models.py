from app import db
from datetime import datetime as dt
# from app import login_manager
# from flask_login import UserMixin

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, default=dt.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def to_dict(self):
<<<<<<< HEAD
        
=======
    
>>>>>>> eef9db4ed2bf415e0ca66ce16e365942756f774f
        from app.blueprints.auth.models import User

        data = {
            'body': self.body,
            'date_created': self.date_created,
            'user': User.query.get(self.user_id).to_dict()
        }
        # data['user'].extend()
        return data