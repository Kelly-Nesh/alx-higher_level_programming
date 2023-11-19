#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb as mysql
import sys

if __name__ == "__main__":
    if '\'' in sys.argv[4]:
        sys.argv[4] = sys.argv[4].split('\'')[0]
    db = mysql.connect(host='localhost', user=sys.argv[1],
                       password=sys.argv[2], port=3306, db=sys.argv[3])

    cur = db.cursor()
    cur.execute("""SELECT cities.name FROM cities where cities.state_id=(
            SELECT id from states where name='{}')
            ORDER BY(cities.id) ASC""".format(sys.argv[4]))
    cities = cur.fetchall()
    if not cities:
        print()
    else:
        for idx, city in enumerate(cities):
            if idx != len(cities) - 1:
                print(city[0], end=', ')
            else:
                print(city[0])
