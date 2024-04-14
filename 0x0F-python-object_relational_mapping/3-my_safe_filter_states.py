#!/usr/bin/python3
"""
A script that takes in an argument and
displays all values in the states
where 'name' matches the argument
from the database 'hbtn_0e_0_usa' but the script is safe from MySQL injections.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    connection = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cr = connection.cursor()
    cr.execute("SELECT * FROM states WHERE name LIKE BINARY %s "
                "ORDER BY id ASC", (sys.argv[4], ))
    rows = cr.fetchall()

    for row in rows:
        print(row)
    
    cr.close()
    connection.close()
