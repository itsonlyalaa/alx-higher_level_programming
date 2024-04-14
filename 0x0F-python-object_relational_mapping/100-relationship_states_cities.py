#!/usr/bin/python3
"""
A script that prints all City objects
from the database 'hbtn_0e_14_usa'.
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    db_ur = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_ur)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()
    cali_state = State(name='California')
    Sfr_city = City(name='San Francisco')
    cali_state.cities.append(Sfr_city)

    session.add(cali_state)
    session.commit()
    session.close()
