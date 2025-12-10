class Usuario:
    def __init__(self, id_usuario: int, nome: str, telefone: str, email: str, senha: str, perfil: str) -> None:
        self.set_id_usuario(id_usuario)
        self.set_nome(nome)
        self.set_telefone(telefone)
        self.set_email(email)
        self.set_senha(senha)
        self.set_perfil(perfil)

    # Setters:
    @staticmethod
    def set_id_usuario(self, id_usuario: int) -> None: self._id_usuario = id_usuario

    @staticmethod
    def set_nome(self, nome: str) -> None: self._nome = nome

    @staticmethod
    def set_telefone(self, telefone: str) -> None: self._telefone = telefone

    @staticmethod
    def set_email(self, email: str) -> None: self._email = email

    @staticmethod
    def set_senha(self, senha: str) -> None: self._senha = senha

    @staticmethod
    def set_perfil(self, perfil: str) -> None: self._perfil = perfil

    # Getters:
    @staticmethod
    def get_id_usuario(self) -> int: return self._id_usuario
    @staticmethod

    def get_nome(self) -> str: return self._nome

    @staticmethod
    def get_telefone(self) -> str: return self._telefone

    @staticmethod
    def get_email(self) -> str: return self._email

    @staticmethod
    def get_senha(self) -> str: return self._senha

    @staticmethod
    def get_perfil(self) -> str: return self._perfil

    # Métodos:
    @staticmethod
    def to_dict(self) -> dict:
        return {
            "id_usuario": self.get_id_usuario(),
            "nome": self.get_nome(),
            "telefone": self.get_telefone(),
            "email": self.get_email(),
            "senha": self.get_senha(),
            "perfil": self.get_perfil()
        }
    
    @staticmethod
    def from_row() -> None:
        pass

    @staticmethod
    def validar_senha(senha: str) -> None:
        pass

    @staticmethod
    def alterar_senha(nova_senha: str) -> None:
        pass