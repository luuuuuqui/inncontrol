from decimal import Decimal as decimal

class Adicional:
    def __init__(self, id_adicional: int, descricao: str, valor: decimal) -> None:
        self.set_id_adicional(id_adicional)
        self.set_descricao(descricao)
        self.set_valor(valor)

    # Setters:
    def set_id_adicional(self, id_adicional: int) -> None: self._id_adicional = id_adicional

    def set_descricao(self, descricao: str) -> None: self._descricao = descricao

    def set_valor(self, valor: decimal) -> None: self._valor = valor

    # Getters:
    def get_id_adicional(self) -> int: return self._id_adicional

    def get_descricao(self) -> str: return self._descricao

    def get_valor(self) -> decimal: return self._valor

    # Métodos:
    def to_dict(self) -> dict:
        return {
            "id_adicional": self.get_id_adicional(),
            "descricao": self.get_descricao(),
            "valor": self.get_valor()
        }
    
    @staticmethod
    def from_row(row) -> 'Adicional':
        raise NotImplementedError("Método from_row ainda não implementado")
    
    def atualizar_valor(self, novo_valor: decimal) -> None:
        self.set_valor(novo_valor)
