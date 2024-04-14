#!/usr/bin/python3
"""
a script that lists all cities from
the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    connection = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cr = connection.cursor()
    cr.execute(('SELECT cities.id, cities.name, states.name FROM cities '
                'LEFT JOIN states ON cities.state_id = states.id;'))
    rows = cr.fetchall()

    for row in rows:
        print(row)
        
    cr.close()
    connection.close()
