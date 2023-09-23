#!/usr/bin/python3
"""Script that takes on the name of a state as an argument
and lists all the cities
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    db = MySQLdb.connect(host="localhost", user=username, password=password,
                         database=database, port=3306)

    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities\
                 RIGHT JOIN states ON cities.state_id = states.id\
                 WHERE states.name LIKE BINARY %(name)s\
                 ORDER BY cities.id ASC", {'name': state})

    query_rows = cur.fetchall()
    print_city = []
    for row in query_rows:
        for city in row:
            print_city.append(city)
    print(", ".join(print_city))

    cur.close()
    db.close()
