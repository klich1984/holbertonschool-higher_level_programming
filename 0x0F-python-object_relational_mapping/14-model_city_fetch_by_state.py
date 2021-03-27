#!/usr/bin/python3
"""
script that prints all City objects from the database hbtn_0e_14_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City

if __name__ == '__main__':
    # create an engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    all_cities = session.query(State.name, City.id, City.name).join(City).all()
    for i in all_cities:
        print("{}: ({}) {}".format(i[0], i[1], i[2]))

    session.close()
