import streamlit as st
import pandas as pd
from views import View
import time
import datetime as dt
from decimal import Decimal


class ManterReservaUI:
    @staticmethod
    def main():
        st.header("Gestão de Reservas")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])

        with tab1:
            ManterReservaUI.listar()
        with tab2:
            ManterReservaUI.inserir()
        with tab3:
            ManterReservaUI.atualizar()
        with tab4:
            ManterReservaUI.excluir()

    @staticmethod
    def listar():
        reservas = View.reserva_listar()
        if not reservas:
            st.info("Nenhuma reserva encontrada.")
            return

        dic_reservas = []
        for r in reservas:
            rd = r.to_dict()

            # --- Recuperação de Objetos Relacionados ---
            hospede = View.hospede_listar_id(r.get_id_hospede())
            usuario_hospede = (
                View.usuario_listar_id(hospede.get_id_usuario()) if hospede else None
            )

            quarto = View.quarto_listar_id(r.get_id_quarto())
            tipo_quarto = (
                View.tipoquarto_listar_id(quarto.get_id_quarto_tipo())
                if quarto
                else None
            )

            # --- Tratamento de Datas e Cálculos ---
            try:
                checkin = dt.datetime.strptime(rd["data_checkin"], "%Y-%m-%d")
                checkout = dt.datetime.strptime(rd["data_checkout"], "%Y-%m-%d")
                diarias = abs((checkin - checkout).days)
            except (ValueError, TypeError):
                # Fallback caso as datas venham corrompidas
                checkin = dt.datetime.now()
                checkout = dt.datetime.now()
                diarias = 0

            # Formatação de Valores
            valor_diaria = (
                Decimal(tipo_quarto.get_valor_diaria())
                if tipo_quarto
                else Decimal("0.00")
            )
            total_diarias = Decimal(valor_diaria * diarias).quantize(Decimal("0.01"))

            # --- Construção do Dicionário para o DataFrame ---
            dic_reservas.append(
                {
                    "ID": rd["id_reserva"],
                    "Hóspede": usuario_hospede.get_nome()
                    if usuario_hospede
                    else "Não encontrado",
                    "Quarto": f"Nº {quarto.get_numero()}" if quarto else "N/A",
                    "Bloco": quarto.get_bloco() if quarto else "N/A",
                    "Tipo": tipo_quarto.get_nome() if tipo_quarto else "N/A",
                    "Check-In": checkin.strftime("%d/%m/%Y"),
                    "Check-Out": checkout.strftime("%d/%m/%Y"),
                    "Diárias": f"{diarias} diária{'s' if diarias != 1 else ''}",
                    "Total": f"R$ {total_diarias:.2f}".replace(".", ","),
                    "Status": ManterReservaUI._formatar_status_icone(rd["status"]),
                }
            )

        df = pd.DataFrame(dic_reservas)
        st.dataframe(df, hide_index=True, use_container_width=True)

    @staticmethod
    def inserir():
        hospedes = View.hospede_listar()
        quartos = View.quarto_listar()

        if not hospedes or not quartos:
            st.error(
                "É necessário ter hóspedes e quartos cadastrados para criar uma reserva."
            )
            return

        # Seleção de Hóspede
        hospede_selecionado = st.selectbox(
            "Selecione o Hóspede:",
            hospedes,
            format_func=lambda h: ManterReservaUI._formatar_hospede(h),
        )

        # Seleção de Quarto
        quarto_selecionado = st.selectbox(
            "Selecione o Quarto:",
            quartos,
            format_func=lambda q: ManterReservaUI._formatar_quarto(q),
        )

        # Seleção de Data
        estadia = st.date_input(
            "Período de Estadia:",
            value=[],  
            min_value=dt.datetime.now(),
            format="DD/MM/YYYY",
            help="Selecione a data inicial e final no calendário.",
        )

        if len(estadia) == 2:
            checkin, checkout = estadia
        else:
            checkin, checkout = None, None

        status = st.selectbox("Status Inicial:", ("Pendente", "Confirmado"))

        # Botão de Ação
        bloquear = not (
            hospede_selecionado and quarto_selecionado and checkin and checkout
        )

        if st.button("Inserir Reserva", disabled=bloquear):
            try:
                View.reserva_inserir(
                    hospede_selecionado.get_id_hospede(),
                    quarto_selecionado.get_id_quarto(),
                    checkin,
                    checkout,
                    status,
                )
                st.success("Reserva inserida com sucesso!")
                time.sleep(1)
                st.rerun()
            except Exception as e:
                st.error(f"Erro ao inserir: {e}")

    @staticmethod
    def atualizar():
        reservas = View.reserva_listar()

        if not reservas:
            st.info("Nenhuma reserva encontrada.")
            return

        # Selectbox principal para escolher qual reserva editar
        reserva_op = st.selectbox(
            "Selecione a reserva para editar:",
            reservas,
            format_func=lambda r: ManterReservaUI._formatar_resumo_reserva(r),
        )

        # Dados para preenchimento dos campos
        hospedes = View.hospede_listar()
        quartos = View.quarto_listar()

        # Determinar índices atuais para pré-selecionar nos componentes
        idx_hospede = ManterReservaUI._obter_indice(
            hospedes, reserva_op.get_id_hospede(), lambda h: h.get_id_hospede()
        )

        idx_quarto = ManterReservaUI._obter_indice(
            quartos, reserva_op.get_id_quarto(), lambda q: q.get_id_quarto()
        )

        lista_status = ["Pendente", "Confirmado", "Cancelado", "Finalizado"]
        idx_status = (
            lista_status.index(reserva_op.get_status())
            if reserva_op.get_status() in lista_status
            else 0
        )

        # Tratamento das datas atuais da reserva
        try:
            data_in_atual = dt.datetime.strptime(
                reserva_op.get_data_checkin(), "%Y-%m-%d"
            ).date()
            data_out_atual = dt.datetime.strptime(
                reserva_op.get_data_checkout(), "%Y-%m-%d"
            ).date()
        except:
            data_in_atual = dt.date.today()
            data_out_atual = dt.date.today()

        # --- Formulário de Edição ---

        novo_hospede = st.selectbox(
            "Hóspede:",
            hospedes,
            index=idx_hospede,
            format_func=lambda h: ManterReservaUI._formatar_hospede(h),
        )

        novo_quarto = st.selectbox(
            "Quarto:",
            quartos,
            index=idx_quarto,
            format_func=lambda q: ManterReservaUI._formatar_quarto(q),
        )

        nova_estadia = st.date_input(
            "Período (Check-in / Check-out):",
            value=(data_in_atual, data_out_atual),
            format="DD/MM/YYYY",
        )

        # Garante que temos as duas datas
        if isinstance(nova_estadia, tuple) and len(nova_estadia) == 2:
            n_checkin, n_checkout = nova_estadia
        else:
            # Fallback se o usuário limpar o campo
            n_checkin, n_checkout = data_in_atual, data_out_atual

        novo_status = st.selectbox("Status:", lista_status, index=idx_status)

        if st.button("Salvar Alterações"):
            try:
                # Nota: Assumindo que a View espera (id, id_hospede, id_quarto, checkin, checkout, status)
                # Se a View esperar 'dias' em vez de datas, a lógica deve ser ajustada aqui.
                View.reserva_atualizar(
                    reserva_op.get_id_reserva(),
                    novo_hospede.get_id_hospede(),
                    novo_quarto.get_id_quarto(),
                    n_checkin,
                    n_checkout,
                    novo_status,
                )
                st.success("Reserva atualizada com sucesso!")
                time.sleep(1)
                st.rerun()
            except Exception as e:
                st.error(f"Erro ao atualizar: {e}")

    @staticmethod
    def excluir():
        reservas = View.reserva_listar()

        if not reservas:
            st.info("Nenhuma reserva encontrada.")
            return

        reserva_op = st.selectbox(
            "Selecione a reserva para excluir:",
            reservas,
            format_func=lambda r: ManterReservaUI._formatar_resumo_reserva(r),
        )

        if st.button("Excluir Reserva", type="primary"):
            try:
                View.reserva_excluir(reserva_op.get_id_reserva())
                st.success("Reserva excluída com sucesso!")
                time.sleep(1)
                st.rerun()
            except Exception as e:
                st.error(f"Erro ao excluir: {e}")

    # métodos auxiliares de formatação
    # só pra deixar legível e fácil de entender o que, do que/de quem e pra o que/quem você está trocando

    @staticmethod
    def _formatar_status_icone(status):
        match status:
            case "Pendente":
                return "❔ Pendente"
            case "Confirmado":
                return "✔️ Confirmado"
            case "Cancelado":
                return "❌ Cancelado"
            case "Finalizado":
                return "☑️ Finalizado"
            case _:
                return status

    @staticmethod
    def _formatar_hospede(h):
        usuario = View.usuario_listar_id(h.get_id_usuario())
        return f"{h.get_id_hospede()} - {usuario.get_nome() if usuario else 'Usuário Desconhecido'}"

    @staticmethod
    def _formatar_quarto(q):
        tipo = View.tipoquarto_listar_id(q.get_id_quarto_tipo())
        nome_tipo = tipo.get_nome() if tipo else "Tipo desc."
        return f"{q.get_bloco()} - Nº {q.get_numero()} - {nome_tipo}"

    @staticmethod
    def _formatar_resumo_reserva(r):
        """Cria string legível para selectbox de Reservas"""
        h = View.hospede_listar_id(r.get_id_hospede())
        u = View.usuario_listar_id(h.get_id_usuario()) if h else None
        nome = u.get_nome() if u else "Desconhecido"

        q = View.quarto_listar_id(r.get_id_quarto())
        num_quarto = q.get_numero() if q else "?"
        bloco_quarto = q.get_bloco() if q else "Bloco ?"

        try:
            checkin = dt.datetime.strptime(r.get_data_checkin(), "%Y-%m-%d")
            checkout = dt.datetime.strptime(r.get_data_checkout(), "%Y-%m-%d")

            checkin_format = checkin.strftime("%d/%m/%Y")

            diarias = abs((checkin - checkout).days)
        except:
            checkin_format = r.get_data_checkin()

            diarias = "?"

        return f"ID {r.get_id_reserva()} - {nome} - {bloco_quarto} Nº{num_quarto} - {checkin_format} - {diarias} diária{'s' if diarias != 1 else ''} - {r.get_status()}"

    @staticmethod
    def _obter_indice(lista, id_alvo, get_id_func):
        """Retorna o índice de um objeto na lista baseando-se no ID"""
        for i, item in enumerate(lista):
            if get_id_func(item) == id_alvo:
                return i
        return 0
