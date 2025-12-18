import sqlite3

class Database:
    conn = None
    nome_bd="agenda.db"

    @classmethod
    def abrir(cls):
        cls.conn = sqlite3.connect(cls.nome_bd)
        cls.conn.execute("PRAGMA foreign_keys = ON")
 
    @classmethod
    def fechar(cls):
        cls.conn.close()

    @classmethod
    def execute(cls, sql, params = None):
        cursor = cls.conn.cursor()
        cursor.execute(sql, params or [])
        cls.conn.commit()

    @classmethod
    def criar_tabelas(cls):
        cls.execute("""
            CREATE TABLE IF NOT EXISTS teste (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            );
        """)

if __name__ == "__main__":
    Database.abrir()
    Database.criar_tabelas()
    Database.fechar()
