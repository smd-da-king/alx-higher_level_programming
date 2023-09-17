#!/usr/bin/python3
"""List values with a specific name."""
import MySQLdb
from sys import argv


if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cur = db.cursor()
    query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id"

    cur.execute(query, (argv[4],))
    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
