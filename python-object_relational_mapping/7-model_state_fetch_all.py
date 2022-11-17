#!/usr/bin/python3
"""
lists all State objects from the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


def model_state():
    """initializate function model_state for db"""
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        argv[1],
        argv[2],
        argv[3]),
        pool_pre_ping=True)
    '''start engine'''
    Base.metadata.create_all(engine)
    '''start session'''
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    '''Query'''
    query = session.query(State).order_by(State.id).all()
    '''Print query'''
    for record in query:
        print("{}: {}".format(record.id, record.name))
    '''Close'''
    session.close()

if __name__ = "__main__":
    model_state()
