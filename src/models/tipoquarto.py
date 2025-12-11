from decimal import Decimal as decimal

class TipoQuarto:
    def __init__(self, id_tipo: int, nome: str, descricao: str, capacidade: int, valor_diaria: decimal) -> None:
        self.set_id_tipo(id_tipo)
        self.set_nome(nome)
        self.set_descricao(descricao)
        self.set_capacidade(capacidade)
        self.set_valor_diaria(valor_diaria)

    # Setters:
    @staticmethod
    def set_id_tipo(self, id_tipo: int) -> None: self._id_tipo = id_tipo

    @staticmethod
    def set_nome(self, nome: str) -> None: self._nome = nome

    @staticmethod
    def set_descricao(self, descricao: str) -> None: self._descricao = descricao

    @staticmethod
    def set_capacidade(self, capacidade: int) -> None: self._capacidade = capacidade

    @staticmethod
    def set_valor_diaria(self, valor_diaria: decimal) -> None: self._valor_diaria = valor_diaria

    # Getters:
    @staticmethod
    def get_id_tipo(self) -> int: return self._id_tipo

    @staticmethod
    def get_nome(self) -> str: return self._nome

    @staticmethod
    def get_descricao(self) -> str: return self._descricao
    
    @staticmethod
    def get_capacidade(self) -> int: return self._capacidade
    
    @staticmethod
    def get_valor_diaria(self) -> decimal: return self._valor_diaria

    # Métodos:
    @staticmethod
    def to_dict(self) -> dict:
        return {
            "id_tipo": self.get_id_tipo(),
            "nome": self.get_nome(),
            "descricao": self.get_descricao(),
            "capacidade": self.get_capacidade(),
            "valor_diaria": self.get_valor_diaria()
        }
    
    @staticmethod
    def from_row() -> None:
        pass


    