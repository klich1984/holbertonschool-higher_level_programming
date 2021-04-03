#!/usr/bin/python3
"""
creates the State “California” with the City “San Francisco” from the database hbtn_0e_100_usa
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship


if __name__ == "__main__":
    # create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
# generate database schema
Base.metadata.create_all(engine)
# create a configured "Session" class
Session = sessionmaker(bind=engine)
session = Session()
# addong data Cyty = Father, State = Child
# add State
state_new = State(name="California")
session.add(state_new)
session.commit()
# Add City
city_new = City(name="San Francisco", state=state_new)
session.add(city_new)
session.commit()

# city_new.state_id.append_foreign_key(fk)

# session.add(state_new)


# session.add(city_new)
# # city_new.state = state_new
# session.commit()
# session.close()
