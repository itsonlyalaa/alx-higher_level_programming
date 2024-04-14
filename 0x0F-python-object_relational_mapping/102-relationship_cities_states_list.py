#!/usr/bin/python3
"""
A script that lists all City objects
from the database hbtn_0e_101_usa
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    
    db_ur = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_ur)
    Session = sessionmaker(bind=engine)

    session = Session()

    for city, state in session.query(City, State).filter(
            City.state_id == State.id).order_by(City.id).all():
        print("{}: {} -> {}".format(city.id, city.name, state.name))
    session.close()
