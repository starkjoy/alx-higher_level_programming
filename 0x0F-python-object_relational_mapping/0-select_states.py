#!/usr/bin/python3
""" Lists state objects' from a database """


import MySQLdb
import sys


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
    query = "SELECT * FROM `states` ORDER BY id ASC"
    cursor.execute(query)
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
