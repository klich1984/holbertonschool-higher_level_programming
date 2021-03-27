#!/usr/bin/python3
"""
file that contains the class definition of a State and an instance
Base = declarative_base()
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """Class State"""
    __tablename__ = 'states'
    id = Column(Integer, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)

