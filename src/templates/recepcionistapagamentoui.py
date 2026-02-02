import streamlit as st
import pandas as pd
from views import View
import time
import datetime as dt
from decimal import Decimal


class RecepcionistaPagamentoUI:
    @staticmethod
    def main():
        st.header("Gestão de Pagamentos")
        tab1, tab2, tab3 = st.tabs(
            ["Histórico", "Registrar Pagamento", "Atualizar/Corrigir"]
        )

        with tab1:
            RecepcionistaPagamentoUI.listar()
        with tab2:
            RecepcionistaPagamentoUI.inserir()
        with tab3:
            RecepcionistaPagamentoUI.atualizar()

    @staticmethod
    def listar():
        pagamentos = View.pagamento_listar()
        if not pagamentos:
            st.info("Nenhum pagamento registrado.")
            return

        dic_pagamentos = []
        for p in pagamentos:
            reserva = View.reserva_listar_id(p.get_id_reserva())
            nome_hospede = "Desconhecido"

            if reserva:
                hospede = View.hospede_listar_id(reserva.get_id_hospede())
                if hospede:
                    usuario = View.usuario_listar_id(hospede.get_id_usuario())
                    if usuario:
                        nome_hospede = usuario.get_nome()

            valor_obj = Decimal(p.get_valor_total())
            valor_formatado = f"R$ {valor_obj:.2f}".replace(".", ",")

            try:
                data_pag = dt.datetime.strptime(
                    p.get_data_pagamento(), "%Y-%m-%d"
                ).strftime("%d/%m/%Y")
            except Exception:
                data_pag = p.get_data_pagamento()

            dic_pagamentos.append(
                {
                    "ID Pagto": f"#{p.get_id_pagamento()}",
                    "Reserva": f"#{p.get_id_reserva()}",
                    "Hóspede": nome_hospede,
                    "Data": data_pag,
                    "Valor": valor_formatado,
                    "Forma": p.get_forma_pagamento(),
                    "Status": p.get_status(),
                }
            )

        df = pd.DataFrame(dic_pagamentos)
        st.dataframe(df, hide_index=True, use_container_width=True)

    @staticmethod
    def inserir():
        reservas = View.reserva_listar()

        if not reservas:
            st.error("Não há reservas cadastradas para efetuar pagamentos.")
            return

        reserva_selecionada = st.selectbox(
            "Selecione a Reserva para pagar:",
            reservas,
            format_func=lambda r: RecepcionistaPagamentoUI._formatar_resumo_reserva(r),
            key="ins_reserva_pagamento",
        )

        if reserva_selecionada:
            try:
                valor_previsto = View.reserva_calcular_pagamento(
                    reserva_selecionada.get_id_reserva()
                )
                st.info(
                    f"Valor total calculado para esta reserva: **R$ {valor_previsto:.2f}**"
                )
            except Exception as e:
                st.warning(f"Não foi possível calcular o valor prévio: {e}")

        with st.form("form_registrar_pagamento"):
            col1, col2 = st.columns(2)
            with col1:
                data_pagamento = st.date_input(
                    "Data do Pagamento:",
                    value=dt.datetime.now(),
                    format="DD/MM/YYYY",
                    key="ins_data_pagamento",
                )

            with col2:
                forma_pagamento = st.selectbox(
                    "Forma de Pagamento:",
                    [
                        "Pix",
                        "Cartão de Crédito",
                        "Cartão de Débito",
                        "Dinheiro",
                        "Transferência",
                    ],
                    key="ins_forma_pagamento",
                )

            status = st.selectbox(
                "Status do Pagamento:",
                ("Confirmado", "Pendente", "Estornado"),
                key="ins_status_pagamento",
            )

            submitted = st.form_submit_button(
                "Registrar Pagamento", key="btn_ins_pagamento"
            )

            if submitted:
                if reserva_selecionada is None:
                    st.error("Selecione uma reserva para registrar o pagamento.")
                    return

                try:
                    View.pagamento_registrar(
                        reserva_selecionada.get_id_reserva(),
                        data_pagamento,
                        forma_pagamento,
                        status,
                    )
                    st.success("Pagamento registrado com sucesso!")
                    time.sleep(1)
                    st.rerun()
                except ValueError as ve:
                    st.error(f"Erro de Validação: {ve}")
                except Exception as e:
                    st.error(f"Erro ao inserir: {e}")

    @staticmethod
    def atualizar():
        st.caption("Permite corrigir a forma de pagamento, data ou status.")
        pagamentos = View.pagamento_listar()
        if not pagamentos:
            st.info("Nada para atualizar.")
            return

        pagamento_op = st.selectbox(
            "Selecione o Pagamento:",
            pagamentos,
            format_func=lambda p: f"ID {p.get_id_pagamento()} - Reserva {p.get_id_reserva()} - R$ {p.get_valor_total()}",
            key="rec_upd_pag",
        )

        if pagamento_op is None:
            return

        lista_formas = [
            "Pix",
            "Cartão de Crédito",
            "Cartão de Débito",
            "Dinheiro",
            "Transferência",
        ]
        idx_forma = (
            lista_formas.index(pagamento_op.get_forma_pagamento())
            if pagamento_op.get_forma_pagamento() in lista_formas
            else 0
        )

        lista_status = ["Confirmado", "Pendente", "Estornado"]
        idx_status = (
            lista_status.index(pagamento_op.get_status())
            if pagamento_op.get_status() in lista_status
            else 0
        )

        try:
            data_atual = dt.datetime.strptime(
                pagamento_op.get_data_pagamento(), "%Y-%m-%d"
            ).date()
        except Exception:
            data_atual = dt.date.today()

        with st.form("form_upd_pagamento"):
            col1, col2 = st.columns(2)
            nova_data = col1.date_input("Data", value=data_atual)
            nova_forma = col2.selectbox(
                "Forma de Pagamento", lista_formas, index=idx_forma
            )
            novo_status = st.selectbox("Status", lista_status, index=idx_status)

            if st.form_submit_button("Salvar Alterações"):
                try:
                    View.pagamento_atualizar(
                        pagamento_op.get_id_pagamento(),
                        pagamento_op.get_id_reserva(),
                        nova_data,
                        nova_forma,
                        novo_status,
                    )
                    st.success("Pagamento atualizado!")
                    time.sleep(1)
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro: {e}")

    @staticmethod
    def _formatar_resumo_reserva(r):
        h = View.hospede_listar_id(r.get_id_hospede())
        nome = "Desconhecido"
        if h:
            u = View.usuario_listar_id(h.get_id_usuario())
            if u:
                nome = u.get_nome()

        return f"Reserva {r.get_id_reserva()} - {nome} ({r.get_data_checkin()} a {r.get_data_checkout()})"
