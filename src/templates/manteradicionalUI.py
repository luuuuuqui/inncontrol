import streamlit as st # pyright: ignore[reportMissingImports]
import pandas as pd
from views import View
import time


class ManterAdicionalUI:
    @staticmethod
    def main():
        st.header("Gerenciar Adicionais (Produtos/Serviços)")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1:
            ManterAdicionalUI.listar()
        with tab2:
            ManterAdicionalUI.inserir()
        with tab3:
            ManterAdicionalUI.atualizar()
        with tab4:
            ManterAdicionalUI.excluir()

    @staticmethod
    def listar():
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

    @staticmethod
    def inserir():
        descricao = st.text_input("Descrição:", placeholder="Ex: Refrigerante Lata")
        valor = st.number_input("Valor (R$):", min_value=0.0, step=0.01, format="%.2f")

        if st.button("Inserir"):
            if not descricao:
                st.error("Informe a descrição.")
            else:
                try:
                    View.adicional_inserir(descricao, valor)
                    st.success("Adicional inserido!")
                    time.sleep(1)
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro: {e}")

    @staticmethod
    def atualizar():
        adicionais = View.adicional_listar()
        if not adicionais:
            st.info("Nenhum adicional para atualizar.")
            return

        op = st.selectbox(
            "Selecione o Adicional:",
            adicionais,
            format_func=lambda a: f"{a.get_id_adicional()} - {a.get_descricao()}",
        )

        nova_desc = st.text_input("Descrição:", value=op.get_descricao())
        novo_valor = st.number_input(
            "Valor (R$):",
            min_value=0.0,
            step=0.01,
            format="%.2f",
            value=float(op.get_valor()),
        )

        if st.button("Salvar Alterações"):
            try:
                View.adicional_atualizar(op.get_id_adicional(), nova_desc, novo_valor)
                st.success("Atualizado com sucesso!")
                time.sleep(1)
                st.rerun()
            except Exception as e:
                st.error(f"Erro: {e}")

    @staticmethod
    def excluir():
        adicionais = View.adicional_listar()
        if not adicionais:
            st.info("Nenhum adicional para excluir.")
            return

        op = st.selectbox(
            "Selecione para excluir:",
            adicionais,
            format_func=lambda a: f"{a.get_id_adicional()} - {a.get_descricao()}",
        )

        if st.button("Excluir"):
            try:
                View.adicional_excluir(op.get_id_adicional())
                st.success("Excluído com sucesso!")
                time.sleep(1)
                st.rerun()
            except Exception as e:
                st.error(f"Erro: {e}")