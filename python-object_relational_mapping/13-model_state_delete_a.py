#!/usr/bin/python3
"""deletes all State objects with a name containing the letter
a from the database hbtn_0e_6_usa"""
from sqlalchemy import create_engine
from model_state import Base, State
import sys
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]),
        pool_pre_ping=True)

    Base.metadata.create_all(engine)

    '''associate it with our custom Session class'''
    Session = sessionmaker(bind=engine)
    session = Session()

    Query = session.query(State).filter(State.name.like('%a%'))

    for Instances in Query:
        session.delete(Instances)

    session.commit()
    session.close()
