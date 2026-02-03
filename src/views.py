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
        usuario = UsuarioDAO.listar_email(email)
        if usuario and usuario.get_senha() == senha:
            return {
                "id": usuario.get_id_usuario(),
                "nome": usuario.get_nome(),
                "email": usuario.get_email(),
                "tipo": usuario.get_tipo_perfil(),
            }
        return None

    # Usuário
    @staticmethod
    def usuario_inserir(nome, fone, email, senha, tipoperfil):
        if not nome or not email or not senha:
            raise ValueError("Nome, email e senha são obrigatórios.")

        usuarios = UsuarioDAO.listar()
        for u in usuarios:
            if u.get_email() == email:
                raise ValueError(f"O email '{email}' já está em uso.")

        u = Usuario(0, nome, fone, email, senha, tipoperfil)
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
    def usuario_atualizar(id, nome, fone, email, tipoperfil):
        if not nome or not email:
            raise ValueError("Nome e email não podem ficar vazios.")

        usuarios = UsuarioDAO.listar()
        for u in usuarios:
            if u.get_email() == email and u.get_id_usuario() != id:
                raise ValueError(f"O email '{email}' já pertence a outro usuário.")

        u = Usuario(id, nome, fone, email, "********", tipoperfil)
        UsuarioDAO.atualizar(u)

    @staticmethod
    def usuario_atualizar_senha(id, senha):
        if not senha or len(senha) < 3:
            raise ValueError("A senha deve ter pelo menos 3 caracteres.")
            
        u = Usuario(id, "*", "*", "*", senha, "*")
        UsuarioDAO.atualizar_senha(u)

    @staticmethod
    def usuario_excluir(id: int):
        u = Usuario(id, "*", "*", "*", "*", "*")
        UsuarioDAO.excluir(u)

    # Hóspede
    @staticmethod
    def hospede_inserir(id_usuario, endereco):
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
    def hospede_listar_por_usuario(id_usuario):
        return HospedeDAO.listar_por_usuario(id_usuario)

    @staticmethod
    def hospede_atualizar(id_hospede, id_usuario, endereco):
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
        # Validação adicionada
        if int(capacidade) <= 0:
            raise ValueError("A capacidade deve ser maior que zero.")
        
        if float(valor_diaria) <= 0:
            raise ValueError("O valor da diária deve ser maior que zero.")

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
        # Validação adicionada
        if int(capacidade) <= 0:
            raise ValueError("A capacidade deve ser maior que zero.")
        
        if float(valor_diaria) <= 0:
            raise ValueError("O valor da diária deve ser maior que zero.")

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
        tq = TipoQuarto(id_tipoquarto, "*", "*", 1, Decimal(0.01))
        TipoQuartoDAO.excluir(tq)

    # Quarto
    @staticmethod
    def quarto_inserir(id_tipo, bloco, numero):
        if int(numero) <= 0:
            raise ValueError("O número do quarto deve ser positivo.")

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
        if int(numero) <= 0:
            raise ValueError("O número do quarto deve ser positivo.")

        quartos = QuartoDAO.listar()
        for q in quartos:
            mesmo_bloco_num = q.get_bloco() == bloco and q.get_numero() == numero
            if mesmo_bloco_num and q.get_id_quarto() != id_quarto:
                raise ValueError(f"Já existe o quarto {numero} no bloco {bloco}.")

        q = Quarto(id_quarto, id_tipo, bloco, numero)
        QuartoDAO.atualizar(q)

    @staticmethod
    def quarto_excluir(id_quarto):
        q = Quarto(id_quarto, 0, "*", 0)
        QuartoDAO.excluir(q)

    # Reserva
    @staticmethod
    def _validar_disponibilidade(
        id_quarto, data_in_str, data_out_str, ignorar_id_reserva=None
    ):
        if isinstance(data_in_str, dt):
            data_in_str = data_in_str.strftime("%Y-%m-%d")
        if isinstance(data_out_str, dt):
            data_out_str = data_out_str.strftime("%Y-%m-%d")

        try:
            nova_in = dt.strptime(data_in_str, "%Y-%m-%d")
            nova_out = dt.strptime(data_out_str, "%Y-%m-%d")
        except (ValueError, TypeError):
            raise ValueError("Formato de data inválido. Use AAAA-MM-DD.")

        # Validação de data retroativa
        # Opcional: Descomentar se não quiser permitir reservas no passado
        if nova_in.date() < dt.now().date():
            raise ValueError("A data de check-in não pode ser no passado.")

        if nova_in >= nova_out:
            raise ValueError(
                "A data de Check-in deve ser anterior à data de Check-out."
            )

        reservas = ReservaDAO.listar()
        for r in reservas:
            if ignorar_id_reserva and r.get_id_reserva() == ignorar_id_reserva:
                continue

            if r.get_id_quarto() == id_quarto and r.get_status() != "Cancelada":
                checkin_existente = r.get_data_checkin()
                checkout_existente = r.get_data_checkout()

                if isinstance(checkin_existente, dt):
                    checkin_existente = checkin_existente.strftime("%Y-%m-%d")
                if isinstance(checkout_existente, dt):
                    checkout_existente = checkout_existente.strftime("%Y-%m-%d")

                existente_in = dt.strptime(checkin_existente, "%Y-%m-%d")
                existente_out = dt.strptime(checkout_existente, "%Y-%m-%d")

                if nova_in < existente_out and nova_out > existente_in:
                    raise ValueError(
                        f"Quarto indisponível! Já existe reserva de {r.get_data_checkin()} a {r.get_data_checkout()}."
                    )

    @staticmethod
    def reserva_inserir(id_hospede, id_quarto, data_checkin, data_checkout, status):
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
        return ReservaDAO.listar_id(id)

    @staticmethod
    def reservas_listar_hospede(id_hospede) -> list[dict]:
        hospede = View.hospede_listar_id(id_hospede)
        if not hospede:
            return []
        id_usuario_logado = hospede.get_id_usuario()

        hospede = View.hospede_listar_por_usuario(id_usuario_logado)
        if not hospede:
            return []

        reservas_hospede = ReservaDAO.listar_por_hospede(hospede.get_id_hospede())

        lista_formatada = []

        for r in reservas_hospede:
            usuario = View.usuario_listar_id(id_usuario_logado)
            nome_hospede = usuario.get_nome() if usuario else "N/A"
            quarto = QuartoDAO.listar_id(r.get_id_quarto())
            tipo_quarto = (
                TipoQuartoDAO.listar_id(quarto.get_id_quarto_tipo()) if quarto else None
            )

            pagamento = PagamentoDAO.listar_reserva(r.get_id_reserva())
            reserva_paga = False
            tipo_pagamento = "Pendente"

            if pagamento:
                tipo_pagamento = pagamento.get_forma_pagamento()
                if pagamento.get_status() in ["Confirmado", "Pago"]:
                    reserva_paga = True

            consumos = ConsumoDAO.listar_por_reserva(r.get_id_reserva())
            lista_adicionais = []
            if consumos:
                for c in consumos:
                    item = AdicionalDAO.listar_id(c.get_id_adicional())
                    if item:
                        lista_adicionais.append(
                            {
                                "nome": item.get_descricao(),
                                "preco": float(item.get_valor()),
                                "quantidade": c.get_quantidade(),
                            }
                        )

            dados_reserva = {
                "id": r.get_id_reserva(),
                "hospede": nome_hospede,
                "tipo_quarto": tipo_quarto.get_nome() if tipo_quarto else "N/A",
                "numero_quarto": str(quarto.get_numero()) if quarto else "?",
                "checkin": r.get_data_checkin(),
                "checkout": r.get_data_checkout(),
                "valor_diaria": (
                    float(tipo_quarto.get_valor_diaria()) if tipo_quarto else 0.0
                ),
                "pago": reserva_paga,
                "tipo_pagamento": tipo_pagamento,
                "adicionais": lista_adicionais,
                "total": float(View.reserva_calcular_pagamento(r.get_id_reserva())),
            }
            lista_formatada.append(dados_reserva)

        return lista_formatada

    @staticmethod
    def reserva_atualizar(
        id_reserva, id_hospede, id_quarto, data_checkin, data_checkout, status
    ):
        View._validar_disponibilidade(
            id_quarto, data_checkin, data_checkout, ignorar_id_reserva=id_reserva
        )
        r = Reserva(
            id_reserva, id_hospede, id_quarto, data_checkin, data_checkout, status
        )
        ReservaDAO.atualizar(r)

    @staticmethod
    def reserva_calcular_pagamento(id_reserva) -> Decimal:
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

        checkin_str = reserva.get_data_checkin()
        checkout_str = reserva.get_data_checkout()

        if isinstance(checkin_str, dt):
            checkin_str = checkin_str.strftime("%Y-%m-%d")
        if isinstance(checkout_str, dt):
            checkout_str = checkout_str.strftime("%Y-%m-%d")

        checkin = dt.strptime(checkin_str, "%Y-%m-%d")
        checkout = dt.strptime(checkout_str, "%Y-%m-%d")

        dias = Decimal(abs((checkin - checkout).days))

        if dias == 0:
            dias = 1
        elif dias < 0:
            raise ValueError("Datas inconsistentes na reserva.")

        total_diarias = valor_diaria * dias

        lista_consumos = ConsumoDAO.listar_por_reserva(id_reserva)
        if not lista_consumos:
            lista_consumos = []

        total_consumo = Decimal("0.00")

        for consumo in lista_consumos:
            adicional = AdicionalDAO.listar_id(consumo.get_id_adicional())
            if not adicional:
                continue

            valor_item = Decimal(adicional.get_valor())
            subtotal_item = valor_item * consumo.get_quantidade()
            total_consumo += subtotal_item

        total_geral = total_diarias + total_consumo

        return total_geral

    @staticmethod
    def reserva_excluir(id_reserva):
        r = Reserva(id_reserva, 0, 0, "2026-01-01", "2026-01-02", "*")
        ReservaDAO.excluir(r)

    # Pagamento
    @staticmethod
    def pagamento_registrar(id_reserva, data_pagamento, forma_pagamento, status):
        pagamento_existente = PagamentoDAO.listar_reserva(id_reserva)
        if pagamento_existente:
            raise ValueError(
                f"A reserva {id_reserva} já possui um pagamento registrado."
            )

        valor_total = View.reserva_calcular_pagamento(id_reserva)
        # Check adicional de segurança, embora o valor venha do cálculo
        if valor_total <= 0:
            raise ValueError("O valor total do pagamento deve ser maior que zero.")

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
        View.pagamento_valor_atualizar(id_pagamento, id_reserva)
        p = Pagamento(
            id_pagamento, id_reserva, data_pagamento, 0, forma_pagamento, status
        )
        PagamentoDAO.atualizar(p)

    @staticmethod
    def pagamento_valor_atualizar(id_pagamento, id_reserva):
        valor_total = View.reserva_calcular_pagamento(id_reserva)
        p = Pagamento(id_pagamento, id_reserva, "2000-01-01", valor_total, "*", "*")
        PagamentoDAO.atualizar_valor(p)

    @staticmethod
    def pagamento_excluir(id_pagamento):
        p = Pagamento(id_pagamento, 0, "2026-01-01", Decimal(0.01), "*", "*")
        PagamentoDAO.excluir(p)

    # Consumo
    @staticmethod
    def consumo_inserir(id_reserva, id_adicional, quantidade, data_consumo):
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

    # Adicional
    @staticmethod
    def adicional_inserir(descricao, valor):
        # Validação adicionada
        if float(valor) <= 0:
            raise ValueError("O valor do adicional deve ser maior que zero.")

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
        # Validação adicionada
        if float(valor) <= 0:
            raise ValueError("O valor do adicional deve ser maior que zero.")

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
        a = Adicional(id_adicional, "*", 0.01)
        AdicionalDAO.excluir(a)

    # OUTRAS FUNÇÕES
    @staticmethod
    def consultar_disponibilidade_quarto(id_quarto, data_checkin, data_checkout):
        """
        Consulta se um quarto específico está disponível no período.
        Retorna dict com 'disponivel' (bool) e dados do conflito se houver.
        """
        try:
            View._validar_disponibilidade(id_quarto, data_checkin, data_checkout)
            return {"disponivel": True, "conflito": None}
        except ValueError as e:
            msg = str(e)
            conflito = None
            import re

            datas = re.findall(r"\d{4}-\d{2}-\d{2}", msg)
            if len(datas) >= 2:
                conflito = {"checkin": datas[0], "checkout": datas[1]}
            return {"disponivel": False, "conflito": conflito, "mensagem": msg}

    @staticmethod
    def listar_quartos_disponiveis_por_tipo(id_tipo, data_checkin, data_checkout):
        """
        Retorna lista de objetos Quarto disponíveis do tipo especificado no período.
        """
        todos_quartos = QuartoDAO.listar()
        quartos_do_tipo = [
            q for q in todos_quartos if q.get_id_quarto_tipo() == id_tipo
        ]

        disponiveis = []
        for quarto in quartos_do_tipo:
            try:
                View._validar_disponibilidade(
                    quarto.get_id_quarto(), data_checkin, data_checkout
                )
                disponiveis.append(quarto)
            except ValueError:
                continue

        return disponiveis

    @staticmethod
    def quarto_verificar_disponibilidade(id_quarto, data_in_str, data_out_str):
        """
        Verifica se um quarto está disponível no período.
        Retorna True se disponível, False se ocupado.
        """
        if hasattr(data_in_str, "strftime"):
            data_in_str = data_in_str.strftime("%Y-%m-%d")

        if hasattr(data_out_str, "strftime"):
            data_out_str = data_out_str.strftime("%Y-%m-%d")

        try:
            nova_in = dt.strptime(data_in_str, "%Y-%m-%d")
            nova_out = dt.strptime(data_out_str, "%Y-%m-%d")
        except (ValueError, TypeError):
            return False

        if nova_in >= nova_out:
            return False

        reservas = ReservaDAO.listar()
        for r in reservas:
            if r.get_id_quarto() == id_quarto and r.get_status() != "Cancelada":
                checkin_existente = r.get_data_checkin()
                checkout_existente = r.get_data_checkout()

                if hasattr(checkin_existente, "strftime"):
                    checkin_existente = checkin_existente.strftime("%Y-%m-%d")
                if hasattr(checkout_existente, "strftime"):
                    checkout_existente = checkout_existente.strftime("%Y-%m-%d")

                checkin_dt = dt.strptime(checkin_existente, "%Y-%m-%d")
                checkout_dt = dt.strptime(checkout_existente, "%Y-%m-%d")

                if nova_in < checkout_dt and nova_out > checkin_dt:
                    return False

        return True

    @staticmethod
    def quarto_listar_disponiveis_tipo(id_tipo_quarto, data_in, data_out):
        """
        Retorna uma lista de objetos Quarto daquele tipo que estão livres no período.
        """
        todos_quartos = QuartoDAO.listar()
        quartos_do_tipo = [
            q for q in todos_quartos if q.get_id_quarto_tipo() == id_tipo_quarto
        ]

        disponiveis = []
        for quarto in quartos_do_tipo:
            if View.quarto_verificar_disponibilidade(
                quarto.get_id_quarto(), data_in, data_out
            ):
                disponiveis.append(quarto)

        return disponiveis
