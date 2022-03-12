from . import db




class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(50), unique = True, nullable = False)
    email = db.Column(db.String(), unique = True, nullable = False)


# def __repr__(self): 