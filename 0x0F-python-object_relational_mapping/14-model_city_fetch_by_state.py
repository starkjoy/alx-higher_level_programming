#!/usr/bin/python3
"""This scripts lists all city objects from database"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City


def list_cities(username, password, database):
    """
    Actual implementation

    Args:
        username: SQL username
        password: SQL password
        database: SQL database
    """

    hostname = "localhost"
    port = 3306

    engine = create_engine(f"mysql://{username}:{password}@{hostname}:\
            {port}/{database}")
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City, State).filter(City.state_id == State.id).\
        order_by(City.id)
    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.commit()
    session.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_cities(username, password, database)
