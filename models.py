from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class User(db.Model):
    __tablename__ = 'users'
    address = db.Column(db.String, primary_key=True, nullable=False)
    active = db.Column(db.Boolean, default=True)
    name = db.Column(db.String, nullable=True, default=None)
    profile_picture = db.Column(db.String, nullable=True, default=None)
    collections = db.relationship('Collection', backref='user', lazy=True)

    def __repr__(self):
        return '<User {}>'.format(self.address)

class Collection(db.Model):
    __tablename__ = 'collections'
    address = db.Column(db.String, primary_key=True, nullable=False)
    owner = db.Column(db.String, db.ForeignKey('users.address'), nullable=True, default=None)
    name = db.Column(db.String, nullable=True, default=None)
    description = db.Column(db.String, nullable=True, default=None)
    image = db.Column(db.String, nullable=True, default=None)
    royalty = db.Column(db.Integer, nullable=False, default=0)

    # social links
    twitter = db.Column(db.String, nullable=True, default=None)
    instagram = db.Column(db.String, nullable=True, default=None)
    discord = db.Column(db.String, nullable=True, default=None)
    telegram = db.Column(db.String, nullable=True, default=None)
    website = db.Column(db.String, nullable=True, default=None)
    email = db.Column(db.String, nullable=True, default=None)
    platform_created = db.Column(db.Boolean, default=False)

    # category from CATEGORIES list
    category = db.Column(db.String, nullable=True, default=None)

    def __repr__(self):
        return '<Collection {}>'.format(self.address)



