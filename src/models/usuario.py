class Usuario:
    def __init__(self, id_usuario: int, nome: str, telefone: str, email: str, senha: str, perfil: str) -> None:
        self.set_id_usuario(id_usuario)
        self.set_nome(nome)
        self.set_telefone(telefone)
        self.set_email(email)
        self.set_senha(senha)
        self.set_perfil(perfil)

    # Setters:
    def set_id_usuario(self, id_usuario: int) -> None: self._id_usuario = id_usuario

    def set_nome(self, nome: str) -> None: self._nome = nome

    def set_telefone(self, telefone: str) -> None: self._telefone = telefone

    def set_email(self, email: str) -> None: self._email = email

    def set_senha(self, senha: str) -> None: self._senha = senha

    def set_perfil(self, perfil: str) -> None: self._perfil = perfil

    # Getters:
    def get_id_usuario(self) -> int: return self._id_usuario

    def get_nome(self) -> str: return self._nome

    def get_telefone(self) -> str: return self._telefone

    def get_email(self) -> str: return self._email

    def get_senha(self) -> str: return self._senha

    def get_perfil(self) -> str: return self._perfil

    # Métodos:
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
    def from_row(row) -> 'Usuario':
        raise NotImplementedError("Método from_row ainda não implementado")

    def validar_senha(self, senha: str) -> None:
        pass

    def alterar_senha(self, nova_senha: str) -> None:
        pass