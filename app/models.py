from . import db
from sqlalchemy.orm import backref
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager
from flask_login import UserMixin
from datetime import datetime

class Pitch(db.Model):

    __tablename__ = 'pitches'
    id = db.Column(db.Integer, primary_key = True)
    pitch = db.Column(db.String(400))
    name = db.Column(db.String(20))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    likes = db.relationship('Likes', backref = 'likes', lazy = 'dynamic')
    dislikes = db.relationship('Dislikes', backref = 'dislikes', lazy = 'dynamic')
    
    def __repr__(self):
        return '<User %r>' % self.pitch



class User(UserMixin,db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(255))
    password_hash = db.Column(db.String(128))
    name = db.Column(db.String(20))
    bio = db.Column(db.Text())
    member_since = db.Column(db.DateTime, default=datetime.utcnow)
    pitches = db.relationship('Pitch', backref='author', lazy = 'dynamic')
    likes = db.relationship('Likes', backref = 'user', lazy = 'dynamic')
    dislikes = db.relationship('Dislikes', backref = 'dislike', lazy = 'dynamic')

    

    @property
    def password(self):
        raise AttributeError('password is not a readable input')
    
    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    
    def __repr__(self):
        return '<User %r>' % self.username


class Likes(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    upvote = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_likes(cls,id):
        upvotes = Dislikes.query.filter_by(pitch_id =id).all()
        return upvotes

class Dislikes(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    downvote = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_dislikes(cls,id):
        downvotes = Dislikes.query.filter_by(pitch_id =id).all()
        return downvotes




@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
 