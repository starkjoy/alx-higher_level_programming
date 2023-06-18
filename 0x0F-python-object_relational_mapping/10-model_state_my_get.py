#!/usr/bin/python3
"""This script prints a state object with a name from database"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_states(username, password, database, state_name):
    """
    Actual implementation

    Args:
        username: SQL name
        password: SQL password
        database: SQL database
        state_name: search string
    """

    hostname = "localhost"
    port = 3306

    engine = create_engine(f"mysql://{username}:{password}@{hostname}:\
            {port}/{database}")
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State.).filter(State.name == state_name).first()
    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    list_states(username, password, database, state_name)
