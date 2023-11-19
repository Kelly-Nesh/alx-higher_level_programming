#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa"""

from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = select(State.name, City.id, City.name).select_from(City).join(State, City.state_id==State.id)
    states = session.execute(query)
    for instance in states:
        print("{}: ({}) {}".format(instance[0], instance[1], instance[2]))
