from decimal import Decimal
from datetime import date, timedelta

from dao.usuariodao import UsuarioDAO
from dao.hospededao import HospedeDAO
from dao.quartodao import QuartoDAO
from dao.tipoquartodao import TipoQuartoDAO
from dao.reservadao import ReservaDAO
from dao.consumodao import ConsumoDAO
from dao.adicionaldao import AdicionalDAO

from models.usuario import Usuario
from models.hospede import Hospede
from models.quarto import Quarto
from models.tipoquarto import TipoQuarto
from models.reserva import Reserva
from models.consumo import Consumo
from models.adicional import Adicional

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

    # Reserva
    @staticmethod
    def reserva_inserir(id_hospede, id_quarto, data_reserva, qtd_dias, status):
        r = Reserva(0, id_hospede, id_quarto, data_reserva, qtd_dias, status)
        ReservaDAO.inserir(r)

    @staticmethod
    def reserva_listar():
        r = ReservaDAO.listar()
        r.sort(key=lambda obj: obj.get_id_reserva())
        return r

    @staticmethod
    def reserva_listar_id(id):
        return QuartoDAO.listar_id(id)

    @staticmethod
    def reserva_atualizar(
        id_reserva, id_hospede, id_quarto, data_reserva, qtd_dias, status
    ):
        r = Reserva(id_reserva, id_hospede, id_quarto, data_reserva, qtd_dias, status)
        ReservaDAO.atualizar(r)

    @staticmethod
    def reserva_calcular_total(id_reserva) -> Decimal:
        """
        Cálculo do total da reserva baseado no ID da reserva.

        :param id_reserva: ID da reserva a calcular o valor.
        """
        reserva = ReservaDAO.listar_id(id_reserva)
        if not reserva:
            raise ValueError("Reserva não encontrada.")

        quarto = QuartoDAO.listar_id(reserva.get_id_quarto())
        tipo_quarto = TipoQuartoDAO.listar_id(
            quarto.get_id_quarto_tipo()
        )  # pyright: ignore[reportOptionalMemberAccess]
        valor_diaria = Decimal(
            tipo_quarto.get_valor_diaria()
        )  # pyright: ignore[reportOptionalMemberAccess]

        dias = reserva.get_qtd_dias()

        if dias == 0:
            dias = 1  # Cobrança mínima de 1 diária
        elif dias < 0:
            raise ValueError("A reserva tem um número negativo de dias.")

        total_diarias = valor_diaria * dias

        # 4. Calcular Consumos
        lista_consumos = ConsumoDAO.listar_por_reserva(id_reserva)
        total_consumo = Decimal("0.00")

        for consumo in lista_consumos:
            adicional = AdicionalDAO.listar_id(consumo.get_id_adicional())
            valor_item = Decimal(
                adicional.get_valor()
            )  # pyright: ignore[reportOptionalMemberAccess]
            subtotal_item = valor_item * consumo.get_quantidade()

            total_consumo += subtotal_item

        total_geral = total_diarias + total_consumo

        return total_geral

    @staticmethod
    def reserva_excluir(id_reserva):
        r = Reserva(id_reserva, 0, 0, "2000-01-01", 0, "a")
        ReservaDAO.excluir(r)

    # Pagamento
    # calma calabreso. eu ainda vou adicionar, bonitão. não se preocupe :)

    # Consumo
    @staticmethod
    def consumo_inserir(id_reserva, id_adicional, quantidade, data_consumo):
        c = Consumo(0, id_reserva, id_adicional, quantidade, data_consumo)
        ConsumoDAO.inserir(c)

    @staticmethod
    def consumo_listar():
        c = ConsumoDAO.listar()
        c.sort(key=lambda obj: obj.get_id_consumo())
        return c

    @staticmethod
    def consumo_listar_id(id):
        return ConsumoDAO.listar_id(id)

    @staticmethod
    def consumo_atualizar(
        id_consumo, id_reserva, id_adicional, quantidade, data_consumo
    ):
        c = Consumo(id_consumo, id_reserva, id_adicional, quantidade, data_consumo)
        ConsumoDAO.atualizar(c)

    @staticmethod
    def consumo_excluir(id_consumo):
        c = Consumo(id_consumo, 0, 0, 0, "2000-01-01 00:00:00")
        ConsumoDAO.excluir(c)

    # Adicional
    @staticmethod
    def adicional_inserir(descricao, valor):
        a = Adicional(0, descricao, valor)
        AdicionalDAO.inserir(a)

    @staticmethod
    def adicional_listar():
        a = AdicionalDAO.listar()
        a.sort(key=lambda obj: obj.get_id_adicional())
        return a

    @staticmethod
    def adicional_listar_id(id):
        return AdicionalDAO.listar_id(id)

    @staticmethod
    def adicional_atualizar(id_adicional, descricao, valor):
        a = Adicional(id_adicional, descricao, valor)
        AdicionalDAO.atualizar(a)

    @staticmethod
    def adicional_excluir(id_adicional):
        a = Adicional(id_adicional, "a", 0.01)
        AdicionalDAO.excluir(a)
