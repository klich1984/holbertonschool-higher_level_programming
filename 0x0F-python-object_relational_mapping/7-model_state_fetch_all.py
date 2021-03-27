#!/usr/bin/python3
"""
script that lists all State objects from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # create an engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    # generate database schema
    Base.metadata.create_all(engine)
    # create a configured "Session" class
    session = sessionmaker(bind=engine)
    for state in session().query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session().close()
