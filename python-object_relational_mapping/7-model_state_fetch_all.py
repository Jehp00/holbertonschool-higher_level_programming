#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa
"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy import sessionmaker


if __name__ = '__main__':
    engine = create_engine('mysql+mysqld://{}:{}@localhost/{}'.format\
    (sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).order_by(State.id).all()

    for record in query:
        print("{}: {}".format(record.id, record.name))
    
    session.close()