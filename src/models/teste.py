class Teste:
    def __init__(self, id: int, name: str) -> None:
        self.set_id(id)
        self.set_name(name)

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name

    def to_json(self):
        return {"id": self.__id, "name": self.__name}

    @classmethod
    def from_json(cls, data: dict):
        return cls(id=data.get("id") or 0, name=data.get("name", ""))

    def __str__(self):
        return f"{self.__id} - {self.__name}"