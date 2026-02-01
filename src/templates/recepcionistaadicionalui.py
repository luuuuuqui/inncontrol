import streamlit as st
import pandas as pd
from views import View
import time


class RecepcionistaAdicionalUI:
    @staticmethod
    def main():
        st.header("Produtos e Serviços")
        tab1, tab2 = st.tabs(["Listar", "Ajustar Preço"])

        with tab1:
            adicionais = View.adicional_listar()
            if not adicionais:
                st.info("Nenhum adicional cadastrado.")
                return

            dic_adicionais = []
            for a in adicionais:
                dic_adicionais.append(
                    {
                        "ID": a.get_id_adicional(),
                        "Descrição": a.get_descricao(),
                        "Valor": f"R$ {float(a.get_valor()):.2f}".replace(".", ","),
                    }
                )

            df = pd.DataFrame(dic_adicionais)
            st.dataframe(df, hide_index=True, use_container_width=True)

        with tab2:
            adicionais = View.adicional_listar()
            if not adicionais:
                return

            with st.form("form_ajustar_preco"):
                op = st.selectbox(
                    "Selecione o Item",
                    adicionais,
                    format_func=lambda x: x.get_descricao(),
                )
                novo_valor = st.number_input(
                    "Novo Valor (R$)", value=float(op.get_valor()), min_value=0.0
                )

                submitted = st.form_submit_button("Atualizar Preço")

                if submitted:
                    try:
                        View.adicional_atualizar(
                            op.get_id_adicional(), op.get_descricao(), novo_valor
                        )
                        st.success("Preço atualizado.")
                        time.sleep(1)
                        st.rerun()
                    except Exception as e:
                        st.error(f"Erro: {e}")
