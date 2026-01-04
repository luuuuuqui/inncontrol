from dao.usuariodao import UsuarioDAO
from models.usuario import Usuario
from models.hospede import Hospede
from dao.hospededao import HospedeDAO

class View:
    # Itens 
    @staticmethod
    def usuario_inserir(nome, fone, email, senha, tipoperfil, idperfil):
        usuario = Usuario(0, nome, fone, email, senha, tipoperfil, idperfil)
        UsuarioDAO.inserir(usuario)

    @staticmethod
    def usuario_listar():
        r = UsuarioDAO.listar()
        # r.sort(key = lambda obj : obj.get_nome())
        return r

    @staticmethod
    def usuario_listar_id(id):
        return UsuarioDAO.listar_id(id)

    @staticmethod
    def usuario_atualizar(id, nome, fone, email, tipoperfil, idperfil):
        usuario = Usuario(id, nome, fone, email, "********", tipoperfil, idperfil)
        UsuarioDAO.atualizar(usuario)
    
    @staticmethod
    def usuario_atualizar_senha(id, senha):
        usuario = Usuario(id, "", "", "", senha, "", 0)
        UsuarioDAO.atualizar_senha(usuario)

    @staticmethod
    def usuario_excluir(id: int):
        usuario = Usuario(id, "a", "a", "a", "a", "a", 0)
        UsuarioDAO.excluir(usuario)
    
    # Hospede
    @staticmethod
    def hospede_inserir(id_usuario, endereco):
        hospede = Hospede(0, id_usuario, endereco)
        HospedeDAO.inserir(hospede)

    @staticmethod
    def hospede_listar():
        return HospedeDAO.listar()

    @staticmethod
    def hospede_listar_id(id):
        return HospedeDAO.listar_id(id)

    @staticmethod
    def hospede_atualizar(id_hospede, id_usuario, endereco):
        hospede = Hospede(id_hospede, id_usuario, endereco)
        HospedeDAO.atualizar(hospede)

    @staticmethod
    def hospede_excluir(id_hospede):
        hospede = Hospede(id_hospede, 0, "")
        HospedeDAO.excluir(hospede)