#!/usr/bin/python3
"""City class definition"""


import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from model_state import Base


class City(Base):
    """Actual class implementation"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

engine = sqlalchemy.create_engine('mysql://username:password@\
        localhost:3306/database')
