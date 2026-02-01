import streamlit as st
import pandas as pd
from views import View
import time
import datetime as dt
from decimal import Decimal


class RecepcionistaReservaUI:
    @staticmethod
    def main():
        st.header("Gestão de Reservas")
        tab1, tab2, tab3, tab4 = st.tabs(
            ["Painel de Reservas", "Nova Reserva", "Alterar/Check-in/out", "Cancelar"]
        )

        with tab1:
            RecepcionistaReservaUI.listar()
        with tab2:
            RecepcionistaReservaUI.inserir()
        with tab3:
            RecepcionistaReservaUI.atualizar()
        with tab4:
            RecepcionistaReservaUI.excluir()

    @staticmethod
    def listar():
        reservas = View.reserva_listar()
        if not reservas:
            st.info("Nenhuma reserva encontrada.")
            return

        dic_reservas = []
        for r in reservas:
            rd = r.to_dict()

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

            try:
                checkin = dt.datetime.strptime(rd["data_checkin"], "%Y-%m-%d")
                checkout = dt.datetime.strptime(rd["data_checkout"], "%Y-%m-%d")
                diarias = abs((checkin - checkout).days)
            except (ValueError, TypeError):
                checkin = dt.datetime.now()
                checkout = dt.datetime.now()
                diarias = 0

            valor_diaria = (
                Decimal(tipo_quarto.get_valor_diaria())
                if tipo_quarto
                else Decimal("0.00")
            )
            total_diarias = Decimal(valor_diaria * diarias).quantize(Decimal("0.01"))

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
                    "Status": rd["status"]
                }
            )

        df = pd.DataFrame(dic_reservas)
        st.dataframe(df, hide_index=True, use_container_width=True)

    @staticmethod
    def inserir():
        hospedes = View.hospede_listar()
        quartos = View.quarto_listar()

        if not hospedes or not quartos:
            st.warning("Cadastre hóspedes e quartos primeiro.")
            return

        with st.form("form_nova_reserva"):
            col1, col2 = st.columns(2)
            with col1:
                hospede_selecionado = st.selectbox(
                    "Hóspede", hospedes, format_func=lambda h: f"ID {h.get_id_hospede()}"
                )
            with col2:
                quarto_selecionado = st.selectbox(
                    "Quarto",
                    quartos,
                    format_func=lambda q: f"{q.get_numero()} - {q.get_bloco()}",
                )

            estadia = st.date_input("Período", min_value=dt.datetime.now(), value=[])

            submitted = st.form_submit_button("Confirmar Reserva")

            if submitted:
                if len(estadia) == 2:
                    try:
                        View.reserva_inserir(
                            hospede_selecionado.get_id_hospede(),
                            quarto_selecionado.get_id_quarto(),
                            estadia[0],
                            estadia[1],
                            "Pendente",
                        )
                        st.success("Reserva criada!")
                        time.sleep(1)
                        st.rerun()
                    except Exception as e:
                        st.error(f"Erro: {e}")
                else:
                    st.error("Selecione data de início e fim.")

    @staticmethod
    def atualizar():
        st.caption("Use esta aba para alterar datas ou realizar Check-in/Check-out.")
        reservas = View.reserva_listar()
        if not reservas:
            st.info("Nada para atualizar.")
            return

        reserva_op = st.selectbox(
            "Selecione a Reserva:",
            reservas,
            format_func=lambda r: f"Reserva #{r.get_id_reserva()} - Status: {r.get_status()}",
        )

        status_atual = reserva_op.get_status()

        if status_atual == "Pendente":
            with st.form("form_checkin"):
                submitted = st.form_submit_button("Realizar Check-in")
                if submitted:
                    RecepcionistaReservaUI._atualizar_status(reserva_op, "Confirmado")
        elif status_atual == "Confirmado":
            with st.form("form_checkout"):
                submitted = st.form_submit_button("Realizar Check-out")
                if submitted:
                    RecepcionistaReservaUI._atualizar_status(reserva_op, "Finalizado")

    @staticmethod
    def excluir():
        st.caption("Apenas reservas NÃO finalizadas podem ser canceladas/excluídas.")
        reservas = [r for r in View.reserva_listar() if r.get_status() != "Finalizado"]

        if not reservas:
            st.info("Nenhuma reserva passível de cancelamento.")
            return

        reserva_op = st.selectbox(
            "Cancelar Reserva:",
            reservas,
            format_func=lambda r: f"#{r.get_id_reserva()} ({r.get_status()})",
        )

        with st.form("form_cancelar_reserva"):
            submitted = st.form_submit_button("Cancelar/Excluir Reserva", type="primary")

            if submitted:
                try:
                    View.reserva_excluir(reserva_op.get_id_reserva())
                    st.success("Reserva cancelada/excluída.")
                    time.sleep(1)
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro: {e}")

    @staticmethod
    def _atualizar_status(reserva, novo_status):
        try:
            View.reserva_atualizar(
                reserva.get_id_reserva(),
                reserva.get_id_hospede(),
                reserva.get_id_quarto(),
                dt.datetime.strptime(reserva.get_data_checkin(), "%Y-%m-%d"),
                dt.datetime.strptime(reserva.get_data_checkout(), "%Y-%m-%d"),
                novo_status,
            )
            st.success(f"Status alterado para {novo_status}!")
            time.sleep(1)
            st.rerun()
        except Exception as e:
            st.error(f"Erro ao mudar status: {e}")
