#!/usr/bin/python3
"""query all states that contains "a" in State model"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                    sys.argv[2],
                                                    sys.argv[3]),
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State)
    states = query.filter(State.name.like('%a%')).order_by(State.id).all()

    for state in states:
        print('{}: {}'.format(state.id, state.name))

    session.close()
