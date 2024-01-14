#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    query = ("""SELECT cities.name 
                FROM cities
                INNER JOIN states
                ON states.id=cities.state_id
                WHERE BINARY states.name= %s
                ORDER BY cities.id ASC""")

    cur.execute(query, (sys.arg[4],))
    rows = cur.fetchall()
    tmp = list(row[0] for row in rows)
    print(*tmp, sep=", ")
    cur.close()
    db.close()
