#!/usr/bin/python3
"""This scripts lists all cities from the database"""


import MySQLdb
import sys


def list_cities(username, password, database, state_name):
    """
    Actual implementation

    Args:
        username: SQL name
        password: SQL password
        database: SQL database
        state_name: search object name
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
    query = "SELECT * FROM cities as c INNER JOIN states as s ON \
            c.state_id = s.id ORDER BY c.id"
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

    list_cities(username, password, database, state_name)
