#!/usr/bin/python3
""" Lists state object from database"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_states(username, password, database):
    """
    Actual implementation

    Args:
        username: SQL name
        password: SQL password
        database: SQL database
    """

    hostname = "localhost"
    port = 3306

    engine = create_engine(f"mysql://{username}:{password}@{hostname}:\
            {port}/{database}", pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))

    session.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)
