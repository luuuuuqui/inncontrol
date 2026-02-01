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
                    "Status": rd["status"],
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

                def formatar_hospede(h):
                    usuario = View.usuario_listar_id(h.get_id_usuario())
                    if usuario:
                        nome = usuario.get_nome()
                    else:
                        nome = "Não encontrado"
                    return f"#{h.get_id_hospede()} - {nome}"

                hospede_selecionado = st.selectbox(
                    "Hóspede",
                    hospedes,
                    format_func=formatar_hospede,
                )
            with col2:

                def formatar_quarto(q):
                    tipo = View.tipoquarto_listar_id(q.get_id_quarto_tipo())
                    if tipo:
                        nome_tipo = tipo.get_nome()
                    else:
                        nome_tipo = "N/A"
                    return f"{q.get_bloco()} - {q.get_numero()} - {nome_tipo}"

                quarto_selecionado = st.selectbox(
                    "Quarto",
                    quartos,
                    format_func=formatar_quarto,
                )

            estadia = st.date_input(
                "Período", min_value=dt.datetime.now(), format="DD/MM/YYYY", value=[]
            )

            status = st.selectbox("Status Inicial:", ("Pendente", "Confirmado"))

            submitted = st.form_submit_button("Confirmar Reserva")

            if submitted:
                if len(estadia) == 2:
                    try:
                        # Converter datetime.date para string no formato esperado
                        data_checkin_str = estadia[0].strftime("%Y-%m-%d")
                        data_checkout_str = estadia[1].strftime("%Y-%m-%d")

                        View.reserva_inserir(
                            hospede_selecionado.get_id_hospede(),
                            quarto_selecionado.get_id_quarto(),
                            data_checkin_str,
                            data_checkout_str,
                            status,
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

        # Converter as datas atuais da reserva para datetime.date para usar no date_input
        try:
            checkin_atual = dt.datetime.strptime(
                reserva_op.get_data_checkin(), "%Y-%m-%d"
            ).date()
            checkout_atual = dt.datetime.strptime(
                reserva_op.get_data_checkout(), "%Y-%m-%d"
            ).date()
        except (ValueError, TypeError):
            checkin_atual = dt.datetime.now().date()
            checkout_atual = dt.datetime.now().date()

        # Formulário para alterar datas
        with st.form("form_alterar_datas"):
            st.subheader("Alterar Datas")
            # Ajustar min_value para permitir datas passadas se a reserva já tiver
            min_date = min(dt.datetime.now().date(), checkin_atual)
            estadia = st.date_input(
                "Período",
                value=[checkin_atual, checkout_atual],
                min_value=min_date,
                format="DD/MM/YYYY",
            )
            salvar_alteracoes = st.form_submit_button(
                "Salvar Alterações de Data", use_container_width=True
            )

            if salvar_alteracoes:
                try:
                    # Preparar datas
                    if len(estadia) == 2:
                        data_checkin_str = estadia[0].strftime("%Y-%m-%d")
                        data_checkout_str = estadia[1].strftime("%Y-%m-%d")
                    else:
                        # Se não selecionou duas datas, usar as atuais
                        data_checkin_str = reserva_op.get_data_checkin()
                        data_checkout_str = reserva_op.get_data_checkout()

                    # Atualizar reserva mantendo o status atual
                    View.reserva_atualizar(
                        reserva_op.get_id_reserva(),
                        reserva_op.get_id_hospede(),
                        reserva_op.get_id_quarto(),
                        data_checkin_str,
                        data_checkout_str,
                        status_atual,
                    )

                    st.success("Datas atualizadas com sucesso!")
                    time.sleep(1)
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro: {e}")

        st.divider()

        # Ações de Check-in e Check-out (fora do formulário de datas)
        st.subheader("Ações")
        col1, col2 = st.columns(2)

        with col1:
            if status_atual == "Pendente":
                if st.button("Realizar Check-in", use_container_width=True):
                    try:
                        # Garantir que as datas sejam strings
                        data_checkin = reserva_op.get_data_checkin()
                        data_checkout = reserva_op.get_data_checkout()

                        if isinstance(data_checkin, dt.datetime):
                            data_checkin = data_checkin.strftime("%Y-%m-%d")
                        if isinstance(data_checkout, dt.datetime):
                            data_checkout = data_checkout.strftime("%Y-%m-%d")

                        View.reserva_atualizar(
                            reserva_op.get_id_reserva(),
                            reserva_op.get_id_hospede(),
                            reserva_op.get_id_quarto(),
                            data_checkin,
                            data_checkout,
                            "Confirmado",
                        )
                        st.success("Check-in realizado com sucesso!")
                        time.sleep(1)
                        st.rerun()
                    except Exception as e:
                        st.error(f"Erro: {e}")
            else:
                if status_atual == "Confirmado":
                    st.info("Check-in já realizado")
                else:
                    st.info("Reserva finalizada")

        with col2:
            if status_atual == "Confirmado":
                if st.button("Realizar Check-out", use_container_width=True):
                    try:
                        # Garantir que as datas sejam strings
                        data_checkin = reserva_op.get_data_checkin()
                        data_checkout = reserva_op.get_data_checkout()

                        if isinstance(data_checkin, dt.datetime):
                            data_checkin = data_checkin.strftime("%Y-%m-%d")
                        if isinstance(data_checkout, dt.datetime):
                            data_checkout = data_checkout.strftime("%Y-%m-%d")

                        View.reserva_atualizar(
                            reserva_op.get_id_reserva(),
                            reserva_op.get_id_hospede(),
                            reserva_op.get_id_quarto(),
                            data_checkin,
                            data_checkout,
                            "Finalizado",
                        )
                        st.success("Check-out realizado com sucesso!")
                        time.sleep(1)
                        st.rerun()
                    except Exception as e:
                        st.error(f"Erro: {e}")
            else:
                if status_atual == "Pendente":
                    st.info("Faça o check-in primeiro")
                else:
                    st.info("Check-out já realizado")

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
            submitted = st.form_submit_button(
                "Cancelar/Excluir Reserva", type="primary"
            )

            if submitted:
                try:
                    View.reserva_excluir(reserva_op.get_id_reserva())
                    st.success("Reserva cancelada/excluída.")
                    time.sleep(1)
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro: {e}")
