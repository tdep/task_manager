from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate(db)

class User(db.Model):
    # __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at
        }

    def __repr__(self):
        return '<User %r>' % self.username
    
class Task(db.Model):
    # __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.String(300), nullable=False)
    due_date = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __init__(self, user_id, title, description, due_date):
        self.user_id = user_id
        self.title = title
        self.description = description
        self.due_date = due_date

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'title': self.title,
            'description': self.description,
            'due_date': self.due_date,
            'created_at': self.created_at
        }
    
    def __repr__(self):
        return '<Task %r>' % self.title
