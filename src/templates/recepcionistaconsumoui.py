import streamlit as st
from views import View
import time
from datetime import datetime


class RecepcionistaConsumoUI:
    @staticmethod
    def main():
        st.header("Lançamento de Consumo")
        tab1, tab2 = st.tabs(["Histórico", "Novo Lançamento"])

        with tab1:
            from .manterconsumoUI import ManterConsumoUI

            ManterConsumoUI.listar()

        with tab2:
            RecepcionistaConsumoUI.inserir()

    @staticmethod
    def inserir():
        reservas_ativas = [
            r
            for r in View.reserva_listar()
            if r.get_status() in ["Confirmado", "Pendente"]
        ]

        if not reservas_ativas:
            st.warning("Não há reservas ativas para lançar consumo.")
            return

        with st.form("form_novo_consumo"):
            reserva = st.selectbox(
                "Reserva",
                reservas_ativas,
                format_func=lambda r: f"Reserva #{r.get_id_reserva()} (Check-in: {r.get_data_checkin()})",
            )
            adicionais = View.adicional_listar()

            item = st.selectbox(
                "Item/Serviço",
                adicionais,
                format_func=lambda a: f"{a.get_descricao()} - R$ {a.get_valor()}",
            )
            qtd = st.number_input("Quantidade", min_value=1, value=1)

            submitted = st.form_submit_button("Lançar na Conta")

            if submitted:
                try:
                    View.consumo_inserir(
                        reserva.get_id_reserva(),
                        item.get_id_adicional(),
                        qtd,
                        datetime.now(),
                    )
                    st.success("Lançamento realizado!")
                    time.sleep(1)
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro: {e}")
