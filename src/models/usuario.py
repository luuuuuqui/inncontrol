class Usuario:
    def __init__(self, id_usuario: int, nome: str, fone: str, email: str, senha: str, tipo_perfil: str, id_perfil: int) -> None:
        self.set_id_usuario(id_usuario)
        self.set_nome(nome)
        self.set_fone(fone)
        self.set_email(email)
        self.set_senha(senha)
        self.set_tipo_perfil(tipo_perfil)
        self.set_id_perfil(id_perfil)

    # Setters:
    def set_id_usuario(self, id_usuario: int) -> None: 
        if id_usuario < 0: raise ValueError("ID do usuário deve ser um inteiro positivo.")
        self.__id = id_usuario

    def set_nome(self, nome: str) -> None: 
        if nome.strip() == "": raise ValueError("Nome do usuário não pode ser vazio.")
        self.__nome = nome

    def set_fone(self, fone: str) -> None:
        self.__fone = fone

    def set_email(self, email: str) -> None: 
        if email.strip() == "": raise ValueError("E-mail do usuário não pode ser vazio.")
        self.__email = email

    def set_senha(self, senha: str) -> None: 
        if senha.strip() == "": raise ValueError("Senha do usuário não pode ser vazia.")
        self.__senha = senha

    def set_tipo_perfil(self, tipo_perfil: str) -> None:
        if tipo_perfil.strip() == "": raise ValueError('O tipo do usuário não pode ser vazio.')
        self.__tipo_perfil = tipo_perfil
    
    def set_id_perfil(self, id_perfil: int) -> None:
        if id_perfil < 0: raise ValueError('O tipo do usuário não pode ser vazio.')
        self.__id_perfil = id_perfil
    
    # Getters:
    def get_id_usuario(self): return self.__id
    def get_nome(self): return self.__nome
    def get_fone(self): return self.__fone
    def get_email(self): return self.__email
    def get_senha(self): return self.__senha
    def get_tipo_perfil(self): return self.__tipo_perfil
    def get_id_perfil(self): return self.__id_perfil 

    # Métodos:
    def to_dict(self) -> dict: 
        return {
            "ID": self.get_id_usuario(),
            "Nome": self.get_nome(),
            "fone": self.get_fone(),
            "email": self.get_email(),
            "perfil_tipo": self.get_tipo_perfil(),
            "perfil_id": self.get_id_perfil()
        }

    def __str__(self) -> str:
        return f"{self.get_id_usuario()} - {self.get_nome()} ({self.get_tipo_perfil()})"

    @staticmethod
    def from_row(row) -> 'Usuario':
        raise NotImplementedError("Método from_row ainda não implementado")