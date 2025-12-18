class Cliente:
    def __init__(self, id, nome, email, fone, senha):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
        self.set_senha(senha)

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_fone(self): return self.__fone
    def get_senha(self): return self.__senha

    def set_id(self, id): self.__id = id
    def set_nome(self, nome): self.__nome = nome
    def set_email(self, email): self.__email = email
    def set_fone(self, fone): self.__fone = fone
    def set_senha(self, senha): self.__senha = senha

    def to_json(self):
        dic = {"id":self.__id, "nome":self.__nome, "email":self.__email, "fone":self.__fone, "senha":self.__senha}
        return dic
    
    @staticmethod
    def from_json(dic):
        return Cliente(dic["id"], dic["nome"], dic["email"], dic["fone"], dic["senha"])

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}"
