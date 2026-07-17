import sqlite3

class Database:

    def __init__(self, file):
        self.conn = sqlite3.connect(file)
        self.cursor = self.conn.cursor()

        self.create_tables()

    def create_tables(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS settings(
            key TEXT PRIMARY KEY,
            value TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS replied(
            user_id INTEGER PRIMARY KEY,
            last_reply INTEGER
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS whitelist(
            user_id INTEGER PRIMARY KEY
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS blacklist(
            user_id INTEGER PRIMARY KEY
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            username TEXT,
            fullname TEXT,
            block TEXT,
            time INTEGER
        )
        """)

        self.conn.commit()

    def get_setting(self, key):

        self.cursor.execute(
            "SELECT value FROM settings WHERE key=?",
            (key,)
        )

        row = self.cursor.fetchone()

        if row:
            return row[0]

        return None

    def set_setting(self, key, value):

        self.cursor.execute(
            """
            INSERT OR REPLACE INTO settings
            VALUES(?,?)
            """,
            (key, value)
        )

        self.conn.commit()
