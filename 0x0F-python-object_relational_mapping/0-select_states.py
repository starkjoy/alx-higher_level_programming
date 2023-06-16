#!/usr/bin/python3
""" Lists state objects from a database """


import sys
import MySQLdb


def list_states(username, password, database):
    """ Actual implementation """

    hostname = "localhost"
    port = 3306

    connection = MySQLdb.connect(
            host=hostname,
            port=port,
            user=username,
            passwd=password,
            db=database
            )

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    connection.close()

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)
