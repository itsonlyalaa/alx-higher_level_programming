#!/usr/bin/python3
"""
A script that takes in the name of a state as an argument
and lists all cities of that state,
using the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    connection = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cr = connection.cursor()
    cr.execute("SELECT cities.name FROM cities LEFT JOIN states "
                "ON cities.state_id = states.id WHERE states.name = %s "
                "ORDER BY cities.id ASC", (sys.argv[4], ))
    rows = cr.fetchall()
    cities = [row[0] for row in rows]
    print(', '.join(cities))

    for row in rows:
        print(row)
        
    cr.close()
    connection.close()
