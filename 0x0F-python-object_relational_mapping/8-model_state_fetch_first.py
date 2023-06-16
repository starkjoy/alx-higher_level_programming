#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


''' This script prints the first state object from a database '''

def list_states(username, password, database):
    ''' Actual implementation '''

    hostname = "localhost"
    port = 3306

    engine = create_engine(f"mysql://{username}:{password}@{hostname}:{port}/{database}")
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id.asc()).first()
    if state:
        print(state)
    else:
        print("Nothing")

    session.close()

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)
