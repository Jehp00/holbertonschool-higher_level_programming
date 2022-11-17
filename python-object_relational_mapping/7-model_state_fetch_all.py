
#!/usr/bin/python3
"""cript that lists all State objects
   from the database hbtn_0e_6_usa"""
from sqlalchemy import (create_engine)
from model_state import State, Base
from sys import argv
from sqlalchemy.orm import sessionmaker


def model_state():
    """initializate function model_state for db"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1],
        argv[2],
        argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    '''associate it with our custom Session class'''
    Session = sessionmaker(bind=engine)

    session = Session()

    query = session.query(State).order_by(State.id).all()

    for record in query:
        print("{}: {}".format(record.id, record.name))

    session.close()


if __name__ == '__main__':
    model_state()