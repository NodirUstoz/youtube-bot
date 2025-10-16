import sqlite3
import os


class Database:
    def __init__(self, db_file=None):
        if db_file is None:
            db_dir = "/var/lib/YTD-db/"
            os.makedirs(db_dir, exist_ok=True)
            self.db_file = os.path.join(db_dir, "users.db")
        else:
            self.db_file = db_file

        self.create_table()

    def create_connection(self):
        return sqlite3.connect(self.db_file)

    def create_table(self):
        conn = self.create_connection()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER UNIQUE,
                    username TEXT
                )
            """)

        conn.commit()
        conn.close()

    def add_user(self, user_id, username):
        conn = self.create_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT OR IGNORE INTO users (user_id, username)
            VALUES (?, ?)
        """, (user_id, username))
        conn.commit()
        conn.close()

    def get_user(self, user_id):
        conn = self.create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
        user = cursor.fetchone()
        conn.close()
        return user

    def get_all_users(self):
        conn = self.create_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT user_id FROM users')
        users = cursor.fetchall()
        conn.close()
        return [user[0] for user in users]
