from dao.usuariodao import UsuarioDAO
from models.usuario import Usuario

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
    def usuario_atualizar(id, nome, fone, email, senha, tipoperfil, idperfil):
        usuario = Usuario(id, nome, fone, email, senha, tipoperfil, idperfil)
        UsuarioDAO.atualizar(usuario)

    @staticmethod
    def usuario_excluir(id: int):
        usuario = Usuario(id, "a", "a", "a", "a", "a", 0)
        UsuarioDAO.excluir(usuario)