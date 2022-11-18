#!/usr/bin/python3
"""
contains the class definition of a City
"""

import sys
from model_state import Base, State
from sqlalchemy import Column, Integer, String, Foreignkey

class City(model_state.Base):
    '''
    City class inherited from Base
    Args:
        Base class inherited'''
    __tablename__ = "cities"
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, Foreignkey=('states.id'))
