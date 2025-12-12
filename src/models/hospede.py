class Hospede:
    def __init__(self, id_usuario: int, endereco: str) -> None:
        self.set_id_usuario(id_usuario)
        self.set_endereco(endereco)
    
    # Setters:
    def set_id_usuario(self, id_usuario: int) -> None: self._id_usuario = id_usuario

    def set_endereco(self, endereco: str) -> None: self._endereco = endereco

    # Getters:
    def get_id_usuario(self) -> int: return self._id_usuario

    def get_endereco(self) -> str: return self._endereco

    # Métodos:
    def to_dict(self) -> dict:
        return {
            "id_usuario": self.get_id_usuario(),
            "endereco": self.get_endereco()
        }
    
    @staticmethod
    def from_row(row) -> 'Hospede':
        raise NotImplementedError("Método from_row ainda não implementado")

