#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb as mysql
import sys

if __name__ == "__main__":
    db = mysql.connect(host='localhost', user=sys.argv[1],
                       password=sys.argv[2], port=3306, db=sys.argv[3])

    cur = db.cursor()
    cur.execute("""SELECT id, name FROM states WHERE name
                LIKE BINARY '{}' ORDER BY(id) ASC""".format(sys.argv[4]))
    states = cur.fetchall()
    for state in states:
        print(state)
