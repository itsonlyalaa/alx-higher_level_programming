#!/usr/bin/python3
"""
A script that prints the State object id
with the name passed as argument
from the database hbtn_0e_6_usa .
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
    ins = session.query(State).filter(State.name == argv[4]).first()

    if ins is None:
        print('Not found')
    else:
        print('{0}'.format(ins.id))
