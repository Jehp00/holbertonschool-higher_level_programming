#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    #take the connection to the server
    connection = MySQLdb.connect(host="localhost",
                                port=3306,
                                user="sudo",
                                passwd=sys.argv[2],
                                database=sys.argv[3],
                                charset='utf8')
    #start the cursor
    cursor = conncection.cursor()

    #execute the query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()

    #print the rows/queries
    for r in rows:
        print(r)
        print("\n")

    #Close the cursor
    cursor.close()
    connection.close()