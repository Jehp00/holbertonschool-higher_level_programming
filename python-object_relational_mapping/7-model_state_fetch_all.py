#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa
"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy import sessionmaker


if __name__ = '__main__':
    '''Not imported'''

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format\
    (sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    '''start engine'''
    Base.metadata.create_all(engine)
    '''start session'''
    Session = sessionmaker(bind=engine)
    session = Session()
    '''Query'''
    query = session.query(State).order_by(State.id).all()
    '''Print query'''
    for record in query:
        print("{}: {}".format(record.id, record.name))
    '''Close'''
    session.close()