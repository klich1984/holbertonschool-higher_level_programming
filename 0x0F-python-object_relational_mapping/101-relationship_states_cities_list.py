#!/usr/bin/python3
"""
script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
"""

from sys import argv
from sqlalchemy import create_engine
from relationship_state import State
from relationship_city import Base, City
from sqlalchemy.orm import relationship, sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State).order_by(State.id).all()
    for i in query:
        print(f'{i.id}: {i.name}')
        for j in i.cities:
            print(f'    {j.id}: {j.name}')
    session.close()
