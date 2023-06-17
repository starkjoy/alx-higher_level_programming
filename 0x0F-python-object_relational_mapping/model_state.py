#!/usr/bin/python3
"""Creates a state class"""


import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class State(Base):
    """Actual Class"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


engine = sqlalchemy.create_engine('mysql://username:password@\
        localhost:3306/database')

Base.metadata.create_all(engine)
