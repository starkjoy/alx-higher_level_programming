#!/usr/bin/python3
"""This script adds the state object 'Louisiana' to database"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def add_state(username, password, database):
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

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    print(new_state.id)

    session.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    add_state(username, password, database)
