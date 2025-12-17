class Usuario:
    def __init__(self, id_usuario: int, nome: str, fone: str, email: str, senha: str, perfil: str) -> None:
        self.set_id_usuario(id_usuario)
        self.set_nome(nome)
        self.set_fone(fone)
        self.set_email(email)
        self.set_senha(senha)

    # Setters:
    def set_id_usuario(self, id_usuario: int) -> None: 
        if id_usuario <= 0: raise ValueError("ID do usuário deve ser um inteiro positivo.")
        self._id_usuario = id_usuario

    def set_nome(self, nome: str) -> None: 
        if nome == "": raise ValueError("Nome do usuário não pode ser vazio.")
        self._nome = nome

    def set_fone(self, fone: str) -> None: 
        if fone == "": raise ValueError("Telefone do usuário não pode ser vazio.")
        self._fone = fone

    def set_email(self, email: str) -> None: 
        if email == "": raise ValueError("E-mail do usuário não pode ser vazio.")
        self._email = email

    def set_senha(self, senha: str) -> None: 
        if senha == "": raise ValueError("Senha do usuário não pode ser vazia.")
        self._senha = senha

    # Getters:
    def get_id_usuario(self, id): self.__id = id
    def get_nome(self, nome):
        if nome == "": raise ValueError("Adicione o nome do usuário!")
        self.__nome = nome
    def get_fone(self, fone):
        if fone < 1: raise ValueError("Adicione o número correto!")
        self.__fone = fone
    def get_email(self, email): 
        if email == "": raise ValueError("Adicione o e-mail!")
        self.__email = email
    def get_senha(self, senha):
        if senha == "": raise ValueError("Adicione a senha!")
        self.__senha = senha
    def get_perfil(self, perfil):
        if perfil == "": raise ValueError("Adicione o nome do usuário")
        self.__nome = nome

    # Métodos:
    def to_dict(self) -> dict:
        return {
            "id_usuario": self.get_id_usuario(),
            "nome": self.get_nome(),
            "fone": self.get_fone(),
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