#!/usr/bin/python3

# This script prints all the cities in the database

from sys import argv
import MySQLdb

db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
cr = db.cursor()

cr.execute(
    "SELECT cities.id, cities.name, states.name FROM cities \
    LEFT JOIN states ON states.id = cities.state_id"
)
[print(city) for city in cr.fetchall()]
