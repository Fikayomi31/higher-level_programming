#!/usr/bin/python3
"""Start link class to table in database 
"""
import sys
from model_state import Base, State
from urllib.parse import quote_plus
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    """password contain special char which use been encode to url"""
    password = 'Fikayomi31@'
    encoded_pwd = quote_plus(password)
     # engine = create_engine('mysql://root:Fikayomi31@.@localhost/hbtn_0e_6_usa')

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], encoded_pwd, sys.argv[2]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
