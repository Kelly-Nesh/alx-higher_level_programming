#!/usr/bin/python3
"""
contains the class definition of a State
    inherits from Base Tips
    links to the MySQL table states
"""
from sqlalchemy import Column, Integer, String, Sequence, create_engine
from sqlalchemy.ext.declarative import declarative_base
import sys

Base = declarative_base()
if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        'root', 'root', 'hbtn_0e_6_usa', pool_pre_ping=True))
    Base.metadata.create_all(engine)

    class State(Base):
        __tablename__ = "states"
        id = Column(Integer, Sequence('states_id_seq'), primary_key=True)
        name = Column(String(128), nullable=False)
