from app import app
from models import db, User, Task
from datetime import datetime
from faker import Faker
from random import randint

fake = Faker()

def run_seeds():
    print('Seeding database ... 🌱')
    # Add your seed data here
    with app.app_context():
        db.drop_all()
        db.create_all()
        
        allUsers = []
        allTasks = []

        for _ in range(30):
            user = User(fake.user_name(), fake.ascii_email(), fake.ripe_id())
            task = Task(randint(0,31), fake.text(max_nb_chars=20), fake.text(max_nb_chars=160), fake.future_date())
            allUsers.append(user)
            allTasks.append(task)

            db.session.add_all([user])
            db.session.add_all([task])
            db.session.commit()


        print('Done! 🌳')

run_seeds()