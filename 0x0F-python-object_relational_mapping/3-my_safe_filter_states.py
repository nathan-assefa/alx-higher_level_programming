#!/usr/bin/python3
# This script prints a satate that is matched to an argument
# + passed in the command line interface

import MySQLdb
from sys import argv

db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
cr = db.cursor()

cr.execute("""SELECT * FROM states WHERE states.name LIKE BINARY '{}'""".format(argv[4]))
[print(state) for state in cr.fetchall()]
