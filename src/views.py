from decimal import Decimal
from datetime import datetime as dt

# DAOs
from dao.usuariodao import UsuarioDAO
from dao.hospededao import HospedeDAO
from dao.quartodao import QuartoDAO
from dao.tipoquartodao import TipoQuartoDAO
from dao.reservadao import ReservaDAO
from dao.pagamentodao import PagamentoDAO
from dao.consumodao import ConsumoDAO
from dao.adicionaldao import AdicionalDAO

# Models
from models.usuario import Usuario
from models.hospede import Hospede
from models.quarto import Quarto
from models.tipoquarto import TipoQuarto
from models.reserva import Reserva
from models.pagamento import Pagamento
from models.consumo import Consumo
from models.adicional import Adicional


class View:
    # Autenticação (Login)
    @staticmethod
    def usuario_autenticar(email, senha):
        """
        Verifica as credenciais do usuário.
        Retorna um dicionário com os dados do usuário se válido, ou None se falhar.
        """
        usuarios = UsuarioDAO.listar()
        for u in usuarios:
            if u.get_email() == email and u.get_senha() == senha:
                return {
                    "id": u.get_id_usuario(),
                    "nome": u.get_nome(),
                    "email": u.get_email(),
                    "tipo": u.get_tipo_perfil() 
                }
        return None

    # Usuário
    @staticmethod
    def usuario_inserir(nome, fone, email, senha, tipoperfil, idperfil):
        # validação: email único
        usuarios = UsuarioDAO.listar()
        for u in usuarios:
            if u.get_email() == email:
                raise ValueError(f"O email '{email}' já está em uso.")

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
        # validação: email único (mas permitindo o próprio email atual)
        usuarios = UsuarioDAO.listar()
        for u in usuarios:
            if u.get_email() == email and u.get_id_usuario() != id:
                raise ValueError(f"O email '{email}' já pertence a outro usuário.")

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
        # validação: o usuário já é hóspede? (1 usuário <-> 1 hóspede)
        hospedes = HospedeDAO.listar()
        for h in hospedes:
            if h.get_id_usuario() == id_usuario:
                raise ValueError("Este usuário já possui cadastro de hóspede.")

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
        # validação: Verifica se o id_usuario pertence a outro hóspede
        hospedes = HospedeDAO.listar()
        for h in hospedes:
            if h.get_id_usuario() == id_usuario and h.get_id_hospede() != id_hospede:
                raise ValueError("Este usuário já está vinculado a outro hóspede.")

        h = Hospede(id_hospede, id_usuario, endereco)
        HospedeDAO.atualizar(h)

    @staticmethod
    def hospede_excluir(id_hospede):
        h = Hospede(id_hospede, 0, "")
        HospedeDAO.excluir(h)

    # Tipo de Quarto
    @staticmethod
    def tipoquarto_inserir(nome, descricao, capacidade, valor_diaria):
        # validação: nome do tipo deve ser único
        tipos = TipoQuartoDAO.listar()
        for t in tipos:
            if t.get_nome().lower() == nome.lower():
                raise ValueError(f"O tipo de quarto '{nome}' já existe.")

        tq = TipoQuarto(0, nome, descricao, capacidade, valor_diaria)
        TipoQuartoDAO.inserir(tq)

    @staticmethod
    def tipoquarto_listar():
        tq = TipoQuartoDAO.listar()
        tq.sort(key=lambda obj: obj.get_id_tipoquarto())
        return tq

    @staticmethod
    def tipoquarto_listar_id(id):
        return TipoQuartoDAO.listar_id(id)

    @staticmethod
    def tipoquarto_atualizar(id_tipoquarto, nome, descricao, capacidade, valor_diaria):
        # validação: nome único na atualização
        tipos = TipoQuartoDAO.listar()
        for t in tipos:
            if (
                t.get_nome().lower() == nome.lower()
                and t.get_id_tipoquarto() != id_tipoquarto
            ):
                raise ValueError(f"Já existe outro tipo de quarto com o nome '{nome}'.")

        tq = TipoQuarto(id_tipoquarto, nome, descricao, capacidade, valor_diaria)
        TipoQuartoDAO.atualizar(tq)

    @staticmethod
    def tipoquarto_excluir(id_tipoquarto):
        tq = TipoQuarto(id_tipoquarto, "a", "a", 1, Decimal(0.01))
        TipoQuartoDAO.excluir(tq)

    # Quarto
    @staticmethod
    def quarto_inserir(id_tipo, bloco, numero):
        # validação: bloco + número deve ser único
        quartos = QuartoDAO.listar()
        for q in quartos:
            if q.get_bloco() == bloco and q.get_numero() == numero:
                raise ValueError(f"O quarto {numero} já existe no bloco {bloco}.")

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
        # validação: bloco + número único na atualização
        quartos = QuartoDAO.listar()
        for q in quartos:
            mesmo_bloco_num = q.get_bloco() == bloco and q.get_numero() == numero
            if mesmo_bloco_num and q.get_id_quarto() != id_quarto:
                raise ValueError(f"Já existe o quarto {numero} no bloco {bloco}.")

        q = Quarto(id_quarto, id_tipo, bloco, numero)
        QuartoDAO.atualizar(q)

    @staticmethod
    def quarto_excluir(id_quarto):
        q = Quarto(id_quarto, 0, "a", 0)
        QuartoDAO.excluir(q)

    # Reserva
    @staticmethod
    def _validar_disponibilidade(
        id_quarto, data_in_str, data_out_str, ignorar_id_reserva=None
    ):
        """
        Método auxiliar para verificar conflito de datas (Overbooking).
        """
        # converter strings para data
        try:
            nova_in = dt.strptime(data_in_str, "%Y-%m-%d")
            nova_out = dt.strptime(data_out_str, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Formato de data inválido. Use AAAA-MM-DD.")

        if nova_in >= nova_out:
            raise ValueError(
                "A data de Check-in deve ser anterior à data de Check-out."
            )

        # verificar conflitos
        reservas = ReservaDAO.listar()
        for r in reservas:
            # pula a própria reserva se for uma atualização
            if ignorar_id_reserva and r.get_id_reserva() == ignorar_id_reserva:
                continue

            # verifica apenas reservas do mesmo quarto que não foram canceladas
            if r.get_id_quarto() == id_quarto and r.get_status() != "Cancelada":
                existente_in = dt.strptime(r.get_data_checkin(), "%Y-%m-%d")
                existente_out = dt.strptime(r.get_data_checkout(), "%Y-%m-%d")

                # lógica de sobreposição de datas:
                # (checkinA < checkoutB) e (checkoutA > checkinB)
                if nova_in < existente_out and nova_out > existente_in:
                    raise ValueError(
                        f"Quarto indisponível! Já existe reserva de {r.get_data_checkin()} a {r.get_data_checkout()}."
                    )

    @staticmethod
    def reserva_inserir(id_hospede, id_quarto, data_checkin, data_checkout, status):
        # Validação de Overbooking
        View._validar_disponibilidade(id_quarto, data_checkin, data_checkout)

        r = Reserva(0, id_hospede, id_quarto, data_checkin, data_checkout, status)
        ReservaDAO.inserir(r)

    @staticmethod
    def reserva_listar():
        r = ReservaDAO.listar()
        r.sort(key=lambda obj: obj.get_id_reserva())
        return r

    @staticmethod
    def reserva_listar_id(id):
        # correção: tava retornando QuartoDAO anteriormente
        return ReservaDAO.listar_id(id)

    @staticmethod
    def reserva_atualizar(
        id_reserva, id_hospede, id_quarto, data_checkin, data_checkout, status
    ):
        # validação de overbooking (ignorando a própria reserva atual)
        View._validar_disponibilidade(
            id_quarto, data_checkin, data_checkout, ignorar_id_reserva=id_reserva
        )

        r = Reserva(
            id_reserva, id_hospede, id_quarto, data_checkin, data_checkout, status
        )
        ReservaDAO.atualizar(r)

    @staticmethod
    def reserva_calcular_pagamento(id_reserva) -> Decimal:
        """
        Calcula o total da reserva (Diárias + Consumo).
        """
        reserva = ReservaDAO.listar_id(id_reserva)
        if not reserva:
            raise ValueError("Reserva não encontrada.")

        quarto = QuartoDAO.listar_id(reserva.get_id_quarto())
        if not quarto:
            raise ValueError("Quarto não encontrado.")

        tipo_quarto = TipoQuartoDAO.listar_id(quarto.get_id_quarto_tipo())
        if not tipo_quarto:
            raise ValueError("Tipo de quarto não encontrado.")

        valor_diaria = Decimal(tipo_quarto.get_valor_diaria())

        checkin = dt.strptime(reserva.get_data_checkin(), "%Y-%m-%d")
        checkout = dt.strptime(reserva.get_data_checkout(), "%Y-%m-%d")

        dias = Decimal(abs((checkin - checkout).days))

        if dias == 0:
            dias = 1  # cobrança mínima
        elif dias < 0:
            raise ValueError("Datas inconsistentes na reserva.")

        total_diarias = valor_diaria * dias

        # calcular consumos
        lista_consumos = ConsumoDAO.listar_por_reserva(id_reserva)
        # se o DAO retornar None ou lista vazia, garantimos lista vazia
        if not lista_consumos:
            lista_consumos = []

        total_consumo = Decimal("0.00")

        for consumo in lista_consumos:
            adicional = AdicionalDAO.listar_id(consumo.get_id_adicional())
            if not adicional:
                continue  # pula se item adicional foi excluído do sistema

            valor_item = Decimal(adicional.get_valor())
            subtotal_item = valor_item * consumo.get_quantidade()
            total_consumo += subtotal_item

        total_geral = total_diarias + total_consumo

        return total_geral

    @staticmethod
    def reserva_excluir(id_reserva):
        r = Reserva(id_reserva, 0, 0, "2026-01-01", "2026-01-02", "a")
        ReservaDAO.excluir(r)

    # Pagamento
    @staticmethod
    def pagamento_registrar(id_reserva, data_pagamento, forma_pagamento, status):
        # validação: já existe pagamento para esta reserva?
        # (assumindo 1 pagamento por reserva)
        pagamento_existente = PagamentoDAO.listar_reserva(id_reserva)
        if pagamento_existente:
            raise ValueError(
                f"A reserva {id_reserva} já possui um pagamento registrado."
            )

        valor_total = View.reserva_calcular_pagamento(id_reserva)
        p = Pagamento(
            0, id_reserva, data_pagamento, valor_total, forma_pagamento, status
        )
        PagamentoDAO.inserir(p)

    @staticmethod
    def pagamento_listar():
        p = PagamentoDAO.listar()
        p.sort(key=lambda obj: obj.get_id_pagamento())
        return p

    @staticmethod
    def pagamento_listar_id(id):
        return PagamentoDAO.listar_id(id)

    @staticmethod
    def pagamento_atualizar(
        id_pagamento, id_reserva, data_pagamento, forma_pagamento, status
    ):
        # primeiro atualiza o valor financeiro
        View.pagamento_valor_atualizar(id_pagamento, id_reserva)

        # depois atualiza dados administrativos
        p = Pagamento(
            id_pagamento, id_reserva, data_pagamento, 0, forma_pagamento, status
        )
        PagamentoDAO.atualizar(p)

    @staticmethod
    def pagamento_valor_atualizar(id_pagamento, id_reserva):
        valor_total = View.reserva_calcular_pagamento(id_reserva)
        p = Pagamento(id_pagamento, id_reserva, "2000-01-01", valor_total, "a", "a")
        PagamentoDAO.atualizar_valor(p)

    @staticmethod
    def pagamento_excluir(id_pagamento):
        p = Pagamento(id_pagamento, 0, "2026-01-01", Decimal(0.01), "a", "a")
        PagamentoDAO.excluir(p)

    # Consumo
    @staticmethod
    def consumo_inserir(id_reserva, id_adicional, quantidade, data_consumo):
        # validação: quantidade positiva
        if quantidade <= 0:
            raise ValueError("A quantidade deve ser maior que zero.")

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
        if quantidade <= 0:
            raise ValueError("A quantidade deve ser maior que zero.")

        c = Consumo(id_consumo, id_reserva, id_adicional, quantidade, data_consumo)
        ConsumoDAO.atualizar(c)

    @staticmethod
    def consumo_excluir(id_consumo):
        c = Consumo(id_consumo, 0, 0, 0, "2000-01-01 00:00:00")
        ConsumoDAO.excluir(c)

    # Adicional (Produtos/Serviços)
    @staticmethod
    def adicional_inserir(descricao, valor):
        # validação: descrição única (evitar "Coca Cola" e "Coca-Cola")
        adicionais = AdicionalDAO.listar()
        for a in adicionais:
            if a.get_descricao().lower() == descricao.lower():
                raise ValueError(f"O item '{descricao}' já está cadastrado.")

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
        # validação na atualização
        adicionais = AdicionalDAO.listar()
        for a in adicionais:
            if (
                a.get_descricao().lower() == descricao.lower()
                and a.get_id_adicional() != id_adicional
            ):
                raise ValueError(f"O item '{descricao}' já existe.")

        a = Adicional(id_adicional, descricao, valor)
        AdicionalDAO.atualizar(a)

    @staticmethod
    def adicional_excluir(id_adicional):
        a = Adicional(id_adicional, "a", 0.01)
        AdicionalDAO.excluir(a)
