#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


''' This script changes the name of a state object in the database '''

def delete_state(username, password, database):
    ''' Actual implementation '''

    hostname = "localhost"
    port = 3306

    engine = create_engine(f"mysql://{username}:{password}@{hostname}:{port}/{database}")
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name.like('%a%')).all()
    for states in state:
        session.delete(states)
    session.commit()

    session.close()

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    delete_state(username, password, database)