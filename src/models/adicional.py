from decimal import Decimal as decimal

class Adicional:
    def __init__(self, id_adicional: int, descricao: str, valor: decimal) -> None:
        self.set_id_adicional(id_adicional)
        self.set_descricao(descricao)
        self.set_valor(valor)

    # Setters:
    @staticmethod
    def set_id_adicional(self, id_adicional: int) -> None: self._id_adicional = id_adicional

    @staticmethod
    def set_descricao(self, descricao: str) -> None: self._descricao = descricao

    @staticmethod
    def set_valor(self, valor: decimal) -> None: self._valor = valor

    # Getters:
    @staticmethod
    def get_id_adicional(self) -> int: return self._id_adicional

    @staticmethod
    def get_descricao(self) -> str: return self._descricao

    @staticmethod
    def get_valor(self) -> decimal: return self._valor

    # Métodos:
    @staticmethod
    def to_dict(self) -> dict:
        return {
            "id_adicional": self.get_id_adicional(),
            "descricao": self.get_descricao(),
            "valor": self.get_valor()
        }
    
    @staticmethod
    def from_row() -> None:
        pass
    
    @staticmethod
    def atualizar_valor(self, novo_valor: decimal):
        self.set_valor(novo_valor)
