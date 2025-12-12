class Quarto:
    def __init__(self, id_quarto: int, id_tipo: int, bloco: str, numero: int) -> None:
        self.set_id_quarto(id_quarto)
        self.set_id_tipo(id_tipo)
        self.set_bloco(bloco)
        self.set_numero(numero)

    # Setters:
    def set_id_quarto(self, id_quarto: int) -> None: self._id_quarto = id_quarto
    
    def set_id_tipo(self, id_tipo: int) -> None: self._id_tipo = id_tipo
    
    def set_bloco(self, bloco: str) -> None: self._bloco = bloco

    def set_numero(self, numero: int) -> None: self._numero = numero

    # Getters:
    def get_id_quarto(self) -> int: return self._id_quarto

    def get_id_tipo(self) -> int: return self._id_tipo

    def get_bloco(self) -> str: return self._bloco
    
    def get_numero(self) -> int: return self._numero

    # Métodos:
    def to_dict(self) -> dict:
        return {
            "id_quarto": self.get_id_quarto(),
            "id_tipo": self.get_id_tipo(),
            "bloco": self.get_bloco(),
            "numero": self.get_numero()
        }
    
    @staticmethod
    def from_row(row) -> 'Quarto':
        raise NotImplementedError("Método from_row ainda não implementado")

    def verificar_disponibilidade(self) -> bool:
        pass



        