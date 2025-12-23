import sqlite3
import os

class Database:
    conn = None
    basedirectory = os.path.dirname(os.path.abspath(__file__))
    pathdb = os.path.join(basedirectory, "inncontrol.db")

    @classmethod
    def abrir(cls):
        cls.conn = sqlite3.connect(cls.pathdb, check_same_thread=False)
        cls.conn.execute("PRAGMA foreign_keys = ON")
 
    @classmethod
    def fechar(cls):
        cls.conn.close()

    @classmethod
    def execute(cls, sql, params = None):
        cursor = cls.conn.cursor()
        cursor.execute(sql, params or [])
        cls.conn.commit()
        return cursor

    @classmethod
    def criar_tabelas(cls):
        # criar a tabela usuário
        cls.execute("""
        CREATE TABLE IF NOT EXISTS usuario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            fone TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL,
            perfil_tipo TEXT NOT NULL,
            perfil_id INTEGER NOT NULL
        );
        """)

""" if __name__ == "__main__":
    Database.abrir()
    Database.criar_tabelas()
    Database.fechar()
 """