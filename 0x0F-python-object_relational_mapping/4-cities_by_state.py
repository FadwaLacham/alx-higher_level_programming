#!/usr/bin/python3
"""
This script lists all cities from the hbtn_0e_4_usa database,
sorted in ascending order by cities.id.
"""

import MySQLdb
import sys

if __name__ == '__main__':

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """
    cursor.execute(query)
    cities = cursor.fetchall()
    for city in cities:
        print(city)

    cursor.close()
    db.close()
