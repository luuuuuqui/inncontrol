import streamlit as st # pyright: ignore[reportMissingImports]
import pandas as pd
from views import View
import time


class ManterTipoQuartoUI:
    @staticmethod
    def main():
        st.header("Gerenciar Tipos de Quarto")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1:
            ManterTipoQuartoUI.listar()
        with tab2:
            ManterTipoQuartoUI.inserir()
        with tab3:
            ManterTipoQuartoUI.atualizar()
        with tab4:
            ManterTipoQuartoUI.excluir()

    @staticmethod
    def listar():
        tipos = View.tipoquarto_listar()
        if not tipos:
            st.info("Nenhum tipo de quarto cadastrado.")
            return

        dic_tipos = []
        for t in tipos:
            dic_tipos.append(
                {
                    "ID": t.get_id_tipoquarto(),
                    "Nome": t.get_nome(),
                    "Descrição": t.get_descricao(),
                    "Capacidade": f"{t.get_capacidade()} pessoa(s)",
                    "Valor Diária": f"R$ {float(t.get_valor_diaria()):.2f}".replace(
                        ".", ","
                    ),
                }
            )

        df = pd.DataFrame(dic_tipos)
        st.dataframe(df, hide_index=True, use_container_width=True)

    @staticmethod
    def inserir():
        nome = st.text_input("Nome:", placeholder="Ex: Quarto Luxo")
        descricao = st.text_input("Descrição:", placeholder="Ex: Vista para o mar")
        capacidade = st.number_input("Capacidade:", min_value=1, step=1)
        valor_diaria = st.number_input(
            "Valor da Diária (R$):", min_value=0.0, step=0.01, format="%.2f"
        )

        if st.button("Inserir"):
            if not (nome and descricao and capacidade and valor_diaria):
                st.error("Preencha todos os campos.")
            else:
                try:
                    View.tipoquarto_inserir(nome, descricao, capacidade, valor_diaria)
                    st.success("Tipo de quarto inserido com sucesso!")
                    time.sleep(1)
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro ao inserir: {e}")

    @staticmethod
    def atualizar():
        tipos = View.tipoquarto_listar()
        if not tipos:
            st.info("Nenhum tipo encontrado para atualizar.")
            return

        op = st.selectbox(
            "Selecione o tipo para editar:",
            tipos,
            format_func=lambda x: f"{x.get_id_tipoquarto()} - {x.get_nome()}",
        )

        nome = st.text_input("Novo Nome:", value=op.get_nome())
        descricao = st.text_input("Nova Descrição:", value=op.get_descricao())
        capacidade = st.number_input(
            "Nova Capacidade:", min_value=1, step=1, value=op.get_capacidade()
        )

        valor_diaria = st.number_input(
            "Novo Valor (R$):",
            min_value=0.0,
            step=0.01,
            format="%.2f",
            value=float(op.get_valor_diaria()),
        )

        if st.button("Salvar Alterações"):
            try:
                View.tipoquarto_atualizar(
                    op.get_id_tipoquarto(), nome, descricao, capacidade, valor_diaria
                )
                st.success("Atualizado com sucesso!")
                time.sleep(1)
                st.rerun()
            except Exception as e:
                st.error(f"Erro ao atualizar: {e}")

    @staticmethod
    def excluir():
        tipos = View.tipoquarto_listar()
        if not tipos:
            st.info("Nenhum tipo encontrado para excluir.")
            return

        op = st.selectbox(
            "Selecione o tipo para excluir:",
            tipos,
            format_func=lambda x: f"{x.get_id_tipoquarto()} - {x.get_nome()}",
        )

        if st.button("Excluir"):
            try:
                View.tipoquarto_excluir(op.get_id_tipoquarto())
                st.success("Excluído com sucesso!")
                time.sleep(1)
                st.rerun()
            except Exception as e:
                st.error(f"Erro ao excluir: {e}")
