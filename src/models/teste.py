import sqlite3

from .dao import DAO

class Teste:
    def __init__(self, id: int = None, name: str = ""):
        self.id = id
        self.name = name

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def set_id(self, id):
        self.id = id

    def set_name(self, name):
        self.name = name

    def to_json(self):
        return {"id": self.id, "name": self.name}

    @classmethod
    def from_json(cls, data: dict):
        return cls(id=data.get("id"), name=data.get("name", ""))

    def __str__(self):
        return self.get_name() or f"Teste({self.id})"


class TesteDAO(DAO):
    _db_file = "database/teste.db"
    _objetos = []

    @classmethod
    def abrir(cls):
        cls._objetos = []
        conn = sqlite3.connect(cls._db_file)
        conn.execute('''CREATE TABLE IF NOT EXISTS teste (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL
                        )''')
        cursor = conn.execute('SELECT id, name FROM teste')
        for row in cursor:
            t = Teste(id=row[0], name=row[1])
            cls._objetos.append(t)
        conn.close()

    @classmethod
    def salvar(cls):
        conn = sqlite3.connect(cls._db_file)
        conn.execute('DELETE FROM teste')
        for obj in cls._objetos:
            conn.execute('INSERT INTO teste (id, name) VALUES (?, ?)', (obj.id, obj.name))
        conn.commit()
        conn.close()