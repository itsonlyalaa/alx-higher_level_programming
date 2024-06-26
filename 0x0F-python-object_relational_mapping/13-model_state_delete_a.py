#!/usr/bin/python3
"""
A script that deletes all State objects
with a name containing the letter 'a'
from the database 'hbtn_0e_6_usa'.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
  
    db_ur = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_ur)
    Session = sessionmaker(bind=engine)

    session = Session()

    for ins in session.query(State).filter(State.name.contains('a')):
        session.delete(ins)

    session.commit()
    session.close()
