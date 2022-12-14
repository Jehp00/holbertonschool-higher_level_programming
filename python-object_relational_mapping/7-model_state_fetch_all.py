#!/usr/bin/python3
"""cript that lists all State objects
   from the database hbtn_0e_6_usa"""
from sqlalchemy import create_engine
from model_state import Base, State
import sys
from sqlalchemy.orm import sessionmaker


def model_state():
    """initializate function model_state for db"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    '''associate it with our custom Session class'''
    Session = sessionmaker(bind=engine)

    session = Session()

    Query = session.query(State).order_by(State.id).all()

    # query python instances in database
    for instance in Query:
        print("{}: {}".format(instance.id, instance.name))

    session.close()


if __name__ == '__main__':
    model_state()
