import sqlite3
import os


class DAO:
    try:
        basedirectory = os.path.dirname(os.path.abspath(__file__))
        pathdb = os.path.join(basedirectory, "inncontrol.db")
        conn = sqlite3.connect(pathdb, check_same_thread=False)
        conn.execute("PRAGMA foreign_keys = ON")
    except Exception as e:
        print(f"Error opening database: {e}")
        raise RuntimeError(f"Error opening database: {e}")

    @classmethod
    def abrir(cls):
        cls.conn = sqlite3.connect(cls.pathdb, check_same_thread=False)
        cls.conn.execute("PRAGMA foreign_keys = ON")

    @classmethod
    def fechar(cls):
        if cls.conn is not None:
            cls.conn.close()

    @classmethod
    def execute(cls, sql, params=None):
        if cls.conn is None:
            raise RuntimeError("Database connection not opened. Call abrir() first.")
        cursor = cls.conn.cursor()
        cursor.execute(sql, params or [])
        cls.conn.commit()
        return cursor
