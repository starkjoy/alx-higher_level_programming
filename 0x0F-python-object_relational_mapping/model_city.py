#!/usr/bin/python3
import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from model_state import Base

''' This script creates a class that contains the definition of a city '''


class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

engine = sqlalchemy.create_engine('mysql://username:password@localhost:3306/database')
Base.metadata.create_all(engine)
