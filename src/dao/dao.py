import sqlite3
import os

class DAO:
    conn = None
    basedirectory = os.path.dirname(os.path.abspath(__file__))
    pathdb = os.path.join(basedirectory, "inncontrol.db")

    @classmethod
    def abrir(cls):
        cls.conn = sqlite3.connect(cls.pathdb, check_same_thread=False)
        cls.conn.execute("PRAGMA foreign_keys = ON")
        # print("USANDO BANCO:", cls.pathdb)
 
    @classmethod
    def fechar(cls):
        cls.conn.close()

    @classmethod
    def execute(cls, sql, params = None):
        cursor = cls.conn.cursor()
        cursor.execute(sql, params or [])
        cls.conn.commit()
        return cursor
