import json
import os

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
    _arquivo = "teste.json"
    _objetos = []

    @classmethod
    def abrir(cls):
        cls._objetos = []
        if not os.path.exists(cls._arquivo):
            return
        try:
            with open(cls._arquivo, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            data = []

        for item in data:
            t = Teste.from_json(item)
            cls._objetos.append(t)

    @classmethod
    def salvar(cls):
        data = [obj.to_json() for obj in cls._objetos]
        with open(cls._arquivo, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)