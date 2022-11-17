#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa that starting with N
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
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cursor.fetchall()

    '''print the rows/queries'''
    for r in rows:
        print(r)

    '''Close the cursor'''
    cursor.close()
    connection.close()
