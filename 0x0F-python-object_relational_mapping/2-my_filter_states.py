#!/usr/bin/python3
import MySQLdb
import sys


''' This script displays all values in states by specified name '''

def list_states(username, password, database, state_name):
    ''' Actual implementation '''

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
    query = "SELECT * FROM states WHERE  name = '{}' ORDER BY id ASC".format(state_name)
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
