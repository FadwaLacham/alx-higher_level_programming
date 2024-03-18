#!/usr/bin/python3
"""
This script takes in the name of a state as an argument
and lists all cities of that state from the hbtn_0e_4_usa database,
sorted in ascending order by cities.id.
"""

import MySQLdb
import sys

if __name__ == '__main__':

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))
    cities = cursor.fetchall()
    if cities:
        cities_list = ", ".join([city[0] for city in cities])
        print(cities_list)
    else:
        print("No cities found for state: {}".format(state_name))

    cursor.close()
    db.close()
