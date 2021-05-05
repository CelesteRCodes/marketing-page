import os

from random import choice, randint

import CRUD
import model
import server

os.system('dropdb marketing-page')
os.system('createdb marketing-page')
# creates and deletes databases

model.connect_to_db(server.app)
# runs like python3 model.py

model.db.create_all()
# creates db tables



for n in range(5):
    email = f'user{n}@test.com'  
    
    name = f'user{n}'
    
    user = CRUD.create_user(name=name, email=email)