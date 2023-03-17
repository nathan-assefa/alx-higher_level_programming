#!/usr/bin/python3

# This script prints all the cities related to a specific state

from sys import argv
import MySQLdb

db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
cr = db.cursor()

cr.execute(
    "SELECT cities.name FROM cities \
    LEFT JOIN states ON states.id = cities.state_id WHERE states.name LIKE BINARY '{}'".format(argv[4])
)
for i in cr.fetchall():
    [print(city, end=", ") for city in i]
print()
