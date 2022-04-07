"""
Init script, sets up database
"""
import sqlite3
import os


def initialize():
    dirname = os.path.dirname(__file__)

    with open(os.path.join(dirname, 'database_structure.sql'), "r") as dbs:
        database_script = dbs.read()

    db = sqlite3.connect(os.path.join(dirname, 'velkakanta.db'))
    with db:
        cur = db.cursor()
        cur.executescript(database_script)
    db.close()