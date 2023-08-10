from app import app
from models import db, User, Task
from datetime import datetime

def run_seeds():
    print('Seeding database ... 🌱')
    # Add your seed data here
    with app.app_context():
        db.drop_all()
        db.create_all()
        
        user1 = User('Joreerb', 'jorb@jorb.com', '0000')

        db.session.add_all([user1])
        db.session.commit()

        task1 = Task(1, 'Demo task', 'Seeding the database', datetime.strptime(('01/01/31 17:00:00'), '%m/%d/%y %H:%M:%S'))

        db.session.add_all([task1])
        db.session.commit()


        print('Done! 🌳')

run_seeds()