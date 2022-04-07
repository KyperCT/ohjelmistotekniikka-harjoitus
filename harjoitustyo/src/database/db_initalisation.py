"""
Init script, sets up database
"""
import sqlite3


def initialize():
    with open("database_structure.sql", "r") as dbs:
        database_script = dbs.read()

    db = sqlite3.connect("velkakanta.db")
    with db:
        cur = db.cursor()
        cur.executescript(database_script)
    db.close()