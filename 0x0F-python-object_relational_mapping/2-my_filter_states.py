#!/usr/bin/python3
""" Displays all values in states by specified name"""


import MySQLdb
import sys


def list_states(username, password, database, state_name):
    """
    Actual Implementation

    Args:
        username: SQL name
        password: SQL password
        database: SQL database
        state_name: State object
    """

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
    query = "SELECT * FROM states WHERE name = '{}' \
            ORDER BY idASC".format(state_name)

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
    state_name = sys.argv[4]

    list_states(username, password, database, state_name)
