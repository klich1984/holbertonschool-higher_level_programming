#!/usr/bin/python3
"""
script that prints the State object with the name passed
as argument from the database hbtn_0e_6_usa
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
    state = session().query(State).filter(State.name.like(argv[4])).all()
    if len(state) == 0:
        print("Not found")
    else:
        for st in state:
            print(st.id)
    session().close()
