from sqlalchemy import (create_engine)
from models import Dog
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///:memory:')

def create_table(Base):
    sql = '''
        CREATE TABLE IF NOT EXISTS dogs(
          id INTEGER PRIMARY KEY,
          name TEXT,
          breed TEXT,
        );
        '''
    return engine

def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    dogs = [dog for dog in session.query(Dog)]
    return dogs

def find_by_name(session, name):
    return session.query.filter_by(name == name)

def find_by_id(session, id):
    return session.query.filter_by(id == id)

def find_by_name_and_breed(session, name, breed):
      return session.query(Dog).filter_by(name = name, breed = breed)

# def update_breed(session, dog, breed):
#     session.query(Dog).update({dog.breed = breed})