class Quarto:
    def __init__(self, id_quarto: int, id_tipo: int, bloco: str, numero: int) -> None:
        self.set_id_quarto(id_quarto)
        self.set_id_tipo(id_tipo)
        self.set_bloco(bloco)
        self.set_numero(numero)

    # Setters:
    @staticmethod
    def set_id_quarto(self, id_quarto: int) -> None: self._id_quarto = id_quarto
    
    @staticmethod
    def set_id_tipo(self, id_tipo: int) -> None: self._id_tipo = id_tipo
    
    @staticmethod
    def set_bloco(self, bloco: str) -> None: self._bloco = bloco

    @staticmethod
    def set_numero(self, numero: int) -> None: self._numero = numero

    # Getters:
    @staticmethod
    def get_id_quarto(self) -> int: return self._id_quarto

    @staticmethod
    def get_id_tipo(self) -> int: return self._id_tipo

    @staticmethod
    def get_bloco(self) -> str: return self._bloco
    
    @staticmethod
    def get_numero(self) -> int: return self._numero

    # Métodos:
    @staticmethod
    def to_dict(self) -> dict:
        return {
            "id_quarto": self.get_id_quarto(),
            "id_tipo": self.get_id_tipo(),
            "bloco": self.get_bloco(),
            "numero": self.get_numero()
        }
    
    @staticmethod
    def from_row() -> None:
        pass

    @staticmethod
    def verificar_disponibilidade() -> None:
        pass



        