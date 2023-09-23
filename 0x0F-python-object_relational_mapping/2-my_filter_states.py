#!/usr/bin/python3
"""Script that takes in an argument and display all value in
the states table
"""

import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    db = MySQLdb.connect(host="localhost", user=username,
                         password=password, database=database, port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'\
                ORDER BY states.id ASC".format(state))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    db.close()
