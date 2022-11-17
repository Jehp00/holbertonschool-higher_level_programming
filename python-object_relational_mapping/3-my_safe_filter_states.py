#!/usr/bin/python3
"""
takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!
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
    cursor.execute("SELECT * FROM states WHERE name=%s"(sys.argv[4], ))
    rows = cursor.fetchall()

    '''print the rows/queries'''
    for r in rows:
        print(r)

    '''Close the cursor'''
    cursor.close()
    connection.close()
