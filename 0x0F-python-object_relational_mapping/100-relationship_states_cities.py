#!/usr/bin/python3
"""
creates the State “California” with the City“San Francisco”
from the database hbtn_0e_100_usa
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import Base, City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_s = State(name="California")
    new_c = City(name="San Francisco")
    new_s.cities.append(new_c)
    session.add(new_s, new_c)
    session.commit()
    session.close()
