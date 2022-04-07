"""
Database class with methods for interacting with the database
"""
import sqlite3
import os


DATABASE = os.path.join(os.path.dirname(__file__), 'velkakanta.db')


class Database:
    """
    Database class with methods for interacting with the database
    """
    def __enter__(self):
        self._conn = sqlite3.connect(DATABASE)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._conn.close()

    def add_user(self, username: str):
        with self._conn:
            cur = self._conn.cursor()
            cur.execute(
                "INSERT INTO users (username) VALUES(?)", (username,)
            )

    def get_users(self):
        with self._conn:
            cur = self._conn.cursor()
            dat = cur.execute("SELECT username FROM users").fetchall()
            return set([x[0] for x in dat])

