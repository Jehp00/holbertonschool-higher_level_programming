#!/usr/bin/python3
"""prints all City objects from the database hbtn_0e_14_usa"""
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

    Query = session.query(
        model_city.City, model_state.State).filter(
        model_city.City.state_id == model_state.State.id).order_by(
        model_city.City.id).all()

    for i, j in Query:
        print(f"{j.name}: ({i.id}) {i.name}")
    session.close()
