from decimal import Decimal

from dao.usuariodao import UsuarioDAO
from dao.hospededao import HospedeDAO
from dao.quartodao import QuartoDAO
from dao.tipoquartodao import TipoQuartoDAO

from models.usuario import Usuario
from models.hospede import Hospede
from models.quarto import Quarto
from models.tipoquarto import TipoQuarto

# todo: adicionar verifiação de usuarios com mesmas credenciais
# exemplo: mesmo email para usuario, mesmo numero de quarto no mesmo bloco, etc.


class View:
    # Usuário
    @staticmethod
    def usuario_inserir(nome, fone, email, senha, tipoperfil, idperfil):
        u = Usuario(0, nome, fone, email, senha, tipoperfil, idperfil)
        UsuarioDAO.inserir(u)

    @staticmethod
    def usuario_listar():
        u = UsuarioDAO.listar()
        u.sort(key=lambda obj: obj.get_id_usuario())
        return u

    @staticmethod
    def usuario_listar_id(id):
        return UsuarioDAO.listar_id(id)

    @staticmethod
    def usuario_atualizar(id, nome, fone, email, tipoperfil, idperfil):
        u = Usuario(id, nome, fone, email, "********", tipoperfil, idperfil)
        UsuarioDAO.atualizar(u)

    @staticmethod
    def usuario_atualizar_senha(id, senha):
        u = Usuario(id, "a", "a", "a", senha, "a", 0)
        UsuarioDAO.atualizar_senha(u)

    @staticmethod
    def usuario_excluir(id: int):
        u = Usuario(id, "a", "a", "a", "a", "a", 0)
        UsuarioDAO.excluir(u)

    # Hóspede
    @staticmethod
    def hospede_inserir(id_usuario, endereco):
        h = Hospede(0, id_usuario, endereco)
        HospedeDAO.inserir(h)

    @staticmethod
    def hospede_listar():
        h = HospedeDAO.listar()
        h.sort(key=lambda obj: obj.get_id_hospede())
        return h

    @staticmethod
    def hospede_listar_id(id):
        return HospedeDAO.listar_id(id)

    @staticmethod
    def hospede_atualizar(id_hospede, id_usuario, endereco):
        h = Hospede(id_hospede, id_usuario, endereco)
        HospedeDAO.atualizar(h)

    @staticmethod
    def hospede_excluir(id_hospede):
        h = Hospede(id_hospede, 0, "")
        HospedeDAO.excluir(h)

    # TipoQuarto
    @staticmethod
    def tipoquarto_inserir(nome, descricao, capacidade, valor_diaria):
        tq = TipoQuarto(0, nome, descricao, capacidade, valor_diaria)
        TipoQuartoDAO.inserir(tq)

    @staticmethod
    def tipoquarto_listar():
        tq = TipoQuartoDAO.listar()  # retorna uma lista de objetos TipoQuarto
        tq.sort(key=lambda obj: obj.get_id_tipoquarto())
        return tq

    @staticmethod
    def tipoquarto_listar_id(id):
        return TipoQuartoDAO.listar_id(id)

    @staticmethod
    def tipoquarto_atualizar(id_tipoquarto, nome, descricao, capacidade, valor_diaria):
        tq = TipoQuarto(id_tipoquarto, nome, descricao, capacidade, valor_diaria)
        TipoQuartoDAO.atualizar(tq)

    @staticmethod
    def tipoquarto_excluir(id_tipoquarto):
        tq = TipoQuarto(id_tipoquarto, "a", "a", 1, Decimal(0.01))
        TipoQuartoDAO.excluir(tq)

    # Quarto
    @staticmethod
    def quarto_inserir(id_tipo, bloco, numero):
        q = Quarto(0, id_tipo, bloco, numero)
        QuartoDAO.inserir(q)

    @staticmethod
    def quarto_listar():
        q = QuartoDAO.listar()
        q.sort(key=lambda obj: obj.get_id_quarto())
        return q

    @staticmethod
    def quarto_listar_id(id):
        return QuartoDAO.listar_id(id)

    @staticmethod
    def quarto_atualizar(id_quarto, id_tipo, bloco, numero):
        q = Quarto(id_quarto, id_tipo, bloco, numero)
        QuartoDAO.atualizar(q)

    @staticmethod
    def quarto_excluir(id_quarto):
        q = Quarto(id_quarto, 0, "a", 0)
        QuartoDAO.excluir(q)
