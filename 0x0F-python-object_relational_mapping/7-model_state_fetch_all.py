#!/usr/bin/python3
<<<<<<< HEAD

"""
Script that lists all State objects from the database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
    session.close()
=======
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from urllib.parse import quote_plus
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """password contain special char which use been encode to url"""
    password = 'Fikayomi31@'
    encoded_pwd = quote_plus(password)
     # engine = create_engine('mysql://root:Fikayomi31@.@localhost/hbtn_0e_6_usa')

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], encoded_pwd, sys.argv[2]), pool_pre_ping=True)
    
    Session = sessionmaker(bind=engine)

    session = Session()
    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
>>>>>>> fda1215 (task 7)
