#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_4_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    '''take the connection to the server'''
    connection = MySQLdb.connect(host="localhost",
                                 port=3306,
                                 user=sys.argv[1],
                                 passwd=sys.argv[2],
                                 db=sys.argv[3],
                                 charset='utf8')
    '''start the cursor'''
    cursor = connection.cursor()

    '''execute the query'''
    cursor.execute("SELECT cities.name FROM cities\
        JOIN states ON cities.state.id=states.id WHERE \
        states.name=%s ORDER BY cities.id ASC", (sys.argv[4], ))
    rows = cursor.fetchall()
    output = []

    '''print the rows/queries'''
    for r in rows:
        output.append(r[0])
    print(', '.join(output))

    '''Close the cursor'''
    cursor.close()
    connection.close()
