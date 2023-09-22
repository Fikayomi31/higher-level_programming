#!/usr/bin/python3
"""Script to list all states with a name starting
with N (upper N) from the database
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", user=username,
                         password=password, database=database, port=3306)
    cur = db.cursor()
    cur.execute("SELECT name FROM states WHERE name LIKE BINARY 'N%'\
                 ORDER BY states.id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
