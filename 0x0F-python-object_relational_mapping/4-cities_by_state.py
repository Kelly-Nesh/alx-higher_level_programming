#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb as mysql
import sys

if __name__ == "__main__":
    db = mysql.connect(host='localhost', user=sys.argv[1],
                       password=sys.argv[2], port=3306, db=sys.argv[3])

    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM cities
            JOIN states on cities.state_id=states.id
            ORDER BY(cities.id) ASC""")
    states = cur.fetchall()
    for state in states:
        print(state)
