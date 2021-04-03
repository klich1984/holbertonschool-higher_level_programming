#!/usr/bin/python3
"""
file that contains the class definition of a City and an instance
"""

from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship
from relationship_state import Base, State


class City(Base):
    """ class City of reprentation a city"""
    __tablename__ = 'cities'
    id = Column(Integer,
                autoincrement=True,
                nullable=False,
                unique=True,
                primary_key=True)
    name = Column(String(128),
                  nullable=False)
    state_id = Column(Integer,
                      ForeignKey('states.id'),
                      nullable=False,
                      )
