from flask import current_app
from . import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(128), nullable=False)
    confirmed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return "User('{}')".format(self.email)
