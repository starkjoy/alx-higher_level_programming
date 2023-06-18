#!/usr/bin/python3
"""This script updates a state object in database"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def delete_state(username, password, database):
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
            {port}/{database}")
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
