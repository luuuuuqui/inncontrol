class Hospede:
    def __init__(self, id_hospede: int, id_usuario: int, endereco: str) -> None:
        self.set_id_hospede(id_hospede)
        self.set_id_usuario(id_usuario)
        self.set_endereco(endereco)

    # Setters:
    def set_id_hospede(self, id_hospede: int) -> None:
        if id_hospede < 0:
            raise ValueError("ID do hóspede deve ser um inteiro positivo.")
        self._id_hospede = id_hospede

    def set_id_usuario(self, id_usuario: int) -> None:
        if id_usuario <= 0:
            raise ValueError("ID do usuário deve ser um inteiro positivo.")
        self._id_usuario = id_usuario

    def set_endereco(self, endereco: str) -> None:
        if endereco == "":
            raise ValueError("Endereço do hóspede não pode ser vazio.")
        self._endereco = endereco

    # Getters:
    def get_id_hospede(self) -> int:
        return self._id_hospede

    def get_id_usuario(self) -> int:
        return self._id_usuario

    def get_endereco(self) -> str:
        return self._endereco

    # Métodos:
    def to_dict(self) -> dict:
        return {
            "id_hospede": self.get_id_hospede(),
            "id_usuario": self.get_id_usuario(),
            "endereco": self.get_endereco(),
        }

    def __str__(self) -> str:
        return f"{self.get_id_hospede()} - {self.get_id_usuario()}"