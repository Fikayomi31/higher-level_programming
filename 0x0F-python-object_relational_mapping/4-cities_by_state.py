#!/usr/bin/python3
"""Script that list al cities from the database
"""

import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", user=username, password=password,
                         database=database, port=3306)

    cur = db.cursor()
    cur.execute("SELECT cities.id, state.name FROM cities\
                NATURAL JOIN state\
                WHERE cities.states_id = states.id\
                ORDER BY cities,id ASC")
    query_rows = cur.fetchll()
    for row in query_rows:
        print(row)

    cur.close()
    dn.close()
