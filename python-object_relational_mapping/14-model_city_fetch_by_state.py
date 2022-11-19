#!/usr/bin/python3
"""prints all City objects from the database hbtn_0e_14_usa"""


import model_state
import model_city
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if "__main__" == __name__:
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    model_state.Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    Session = Session()

    Query = Session.query(model_city.City, model_state.State)\
        .filter(model_city.City.state_id == model_state.State.id)\
        .order_by(model_city.City.id).all()
    for i, j in Query:
        print(f"{j.name}: ({i.id}) {i.name}")

    Session.close()
