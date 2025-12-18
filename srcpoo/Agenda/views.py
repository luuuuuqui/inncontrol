from models.cliente import Cliente
from models.servico import Servico
from models.horario import Horario
from models.profissional import Profissional
from dao_sql.clientedao import ClienteDAO
from datetime import datetime, timedelta

class View:

    def cliente_criar_admin():
        for c in View.cliente_listar():
            if c.get_email() == "admin": return
        View.cliente_inserir("admin", "admin", "fone", "1234")

    def cliente_autenticar(email, senha):
        for c in View.cliente_listar():
            if c.get_email() == email and c.get_senha() == senha:
                return {"id": c.get_id(), "nome": c.get_nome()}
        return None

    def cliente_inserir(nome, email, fone, senha):
        cliente = Cliente(0, nome, email, fone, senha)
        ClienteDAO.inserir(cliente)

    def cliente_listar():
        r = ClienteDAO.listar()
        r.sort(key = lambda obj : obj.get_nome())            
        return r     
  
    def cliente_listar_id(id):
        return ClienteDAO.listar_id(id)

    def cliente_atualizar(id, nome, email, fone, senha):
        cliente = Cliente(id, nome, email, fone, senha)
        ClienteDAO.atualizar(cliente)
    
    def cliente_excluir(id):
        cliente = Cliente(id, "", "", "", "")
        ClienteDAO.excluir(cliente)    

