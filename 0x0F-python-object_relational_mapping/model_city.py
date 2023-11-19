#!/usr/bin/python3
"""
contains the class definition of a State
    inherits from Base Tips
    links to the MySQL table citys
"""
from sqlalchemy import (Column, Integer, String, Sequence, create_engine,
                        ForeignKey)
import sys

from model_state import Base


class City(Base):
    """Represents a city for a MySQL database.

    __tablename__ (str): The name of the MySQL table to store Cities.
    id (Integer): The city's id.
    name (String): The city's name.
    """
    __tablename__ = "cities"
    id = Column(Integer, Sequence('cities_id_seq'), primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
