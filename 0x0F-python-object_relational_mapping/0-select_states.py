#!/usr/bin/python3
"""
A script lists all states from the
database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    connection = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cr = connection.cursor()
    cr.execute("SELECT * FROM states")
    rows = cr.fetchall()

    for row in rows:
        print(row)
    cr.close()
    connection.close()
