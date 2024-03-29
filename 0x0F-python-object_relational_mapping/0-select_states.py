#!/usr/bin/python3
"""This script takes 3 argument and lists all the states
+ the data base"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3]
    )
    cr = db.cursor()

    cr.execute("SELECT states.id, states.name FROM states")
    [print(state) for state in cr.fetchall()]
