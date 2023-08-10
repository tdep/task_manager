import os
from flask import Flask, send_file, request, jsonify
from flask_migrate import Migrate
from flask_cors import CORS
from config import Config
from models import db, User, Task

app = Flask(__name__, static_folder='public')
CORS(app, origins=['*'])
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)

@app.get('/')
def home():
    return send_file('welcome.html')

@app.route('/users')
def index():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@app.route('/users/<int:id>')
def show_user(id):
    users = User.query.all()
    if len(users):
        users_data = []
        for user in users:
            if user.id == id:
                users_data.append(user.toJSON())
        return jsonify(users_data)
    else:
        return {}, 404
    
@app.get('/tasks')
def all_tasks():
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks])

@app.post('/login')
def login():
    data = request.form
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        return({'error': 'No account found'}), 404
    else:
        given_password = data['password']
        if user.password == given_password:
            return jsonify({'user': user.to_dict()}), 200
        else:
            return jsonify({'error': 'Invalid password'}), 422


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=os.environ.get('PORT', 3000))