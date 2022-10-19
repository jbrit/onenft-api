from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class User(db.Model):
    __tablename__ = 'users'
    address = db.Column(db.String, primary_key=True, nullable=False)
    active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return '<User {}>'.format(self.address)
