class Hospede:
    def __init__(self, id_usuario: int, endereco: str) -> None:
        self.set_id_usuario(id_usuario)
        self.set_endereco(endereco)
    
    # Setters:
    @staticmethod
    def set_id_usuario(self, id_usuario: int) -> None: self._id_usuario = id_usuario

    @staticmethod
    def set_endereco(self, endereco: str) -> None: self._endereco = endereco

    # Getters:
    @staticmethod
    def get_id_usuario(self) -> int: return self._id_usuario

    @staticmethod
    def get_endereco(self) -> str: return self._endereco

    # Métodos:
    @staticmethod
    def to_dict(self) -> dict:
        return {
            "id_usuario": self.get_id_usuario(),
            "endereco": self.get_endereco()
        }
    
    @staticmethod
    def from_row() -> None:
        pass

