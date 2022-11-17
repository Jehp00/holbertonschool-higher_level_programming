#!/usr/bin/python3
"""
takes in an argument and displays all values in the states where name matches the argument.
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
                                 state_name_searched=sys.argv[4],
                                 charset='utf8')
    '''start the cursor'''
    cursor = connection.cursor()

    '''execute the query'''
    cursor.execute("SELECT * FROM states WHERE name={} ORDER BY id ASC".format(state_name_searched))
    rows = cursor.fetchall()

    '''print the rows/queries'''
    for r in rows:
        print(r)

    '''Close the cursor'''
    cursor.close()
    connection.close()
