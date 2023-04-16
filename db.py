'''
db
database file, containing all the logic to interface with the sql database
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import *
import bcrypt

# "database/main.db" specifies the database file
# change it if you wish
# turn echo = True to display sql output
engine = create_engine("sqlite:///database/main.db", echo=False)

# initializes the database
Base.metadata.create_all(engine)

# inserts a user to the database
def insert_user(username: str, password: str):
    # Hashes given password with salt before posting to database
    password = password.encode('utf-8')
    password = bcrypt.hashpw(password, bcrypt.gensalt())
    with Session(engine) as session:
        user = User(username=username, password=password)
        session.add(user)
        session.commit()

# gets a user from the database
def get_user(username: str):
    with Session(engine) as session:
        return session.get(User, username)
