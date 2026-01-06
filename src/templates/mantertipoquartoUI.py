import streamlit as st  # pyright: ignore[reportMissingImports]
import pandas as pd  # pyright: ignore[reportMissingImports]
from views import View
import time

from models.tipoquarto import TipoQuarto


class ManterTipoQuartoUI:
    @staticmethod
    def main():
        st.header("Teste de CRUD de Tipo Quarto")
        tab1, tab2, tab3, tab4 = st.tabs(
            ["Listar", "Inserir", "Atualizar", "Excluir"]
        )
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
        tiposquarto = View.tipoquarto_listar()
        if len(tiposquarto) == 0:
            st.write("Nenhum tipoquarto encontrado.")
        else:
            df = pd.DataFrame([u.to_dict() for u in tiposquarto])
            # id: int,
            # nome: str,
            # descricao: str,
            # capacidade: int,
            # valor_diaria: decimal,
            df = df.rename(
                columns={
                    "id": "ID",
                    "nome": "Nome",
                    "descricao": "Descrição",
                    "capacidade": "Capacidade",
                    "valor_diaria": "Valor da Diária"
                }
            )
            df = df.reindex(
                columns=[
                    "ID",
                    "Nome",
                    "Descrição",
                    "Capacidade",
                    "Valor da Diária"
                ]
            )

            st.dataframe(
                df,
                hide_index=True,
                column_config={
                    "Valor da Diária": st.column_config.NumberColumn(
                        "Valor da Diária", format="R$ %.2f"
                    )
                },
            )

    @staticmethod
    def inserir():
        nome = st.text_input("Informe o nome:", placeholder="Quarto Luxo")
        descricao = st.text_input("Informe a descrição:", placeholder="Quarto espaçoso com vista para o mar.")
        capacidade = st.number_input("Informe a capacidade:", min_value=1, step=1)
        valor_diaria = st.number_input("Informe o valor da diária:", min_value=0.0, step=0.01)

        bloquear = not (nome and descricao and capacidade and valor_diaria)

        if st.button("Inserir", disabled=bloquear):
            try:
                View.tipoquarto_inserir(nome, descricao, capacidade, valor_diaria)
            except Exception as e:
                st.error("Erro ao inserir: {}".format(e))
            else:
                st.success("TipoQuarto inserido com sucesso")
                time.sleep(2)
                st.rerun()

    @staticmethod
    def atualizar():
        tipoquartos = View.tipoquarto_listar()
        if len(tipoquartos) == 0:
            st.write("Nenhum tipoquarto encontrado.")
        else:
            op = st.selectbox(
                "Escolha o tipo de quarto a atualizar",
                tipoquartos,
                format_func=lambda x: x.__str__(),
                key="selectboxatualizar",
            )

            if "ultimo_id_selecionado" not in st.session_state:
                st.session_state.ultimo_id_selecionado = None

            # Se o ID mudou, atualizamos as chaves do session_state com os dados do banco
            if st.session_state.ultimo_id_selecionado != op.get_id_tipoquarto():
                st.session_state.ultimo_id_selecionado = op.get_id_tipoquarto()
                st.session_state.atualizarnome = op.get_nome()
                st.session_state.atualizardescricao = op.get_descricao()
                st.session_state.atualizarcapacidade = op.get_capacidade()
                st.session_state.atualizarvalordiaria = op.get_valor_diaria()       

            nome = st.text_input("Informe o novo nome", key="atualizarnome")
            descricao = st.text_input("Informe a nova descrição", key="atualizardescricao")
            capacidade = st.number_input("Informe a nova capacidade:", min_value=1, step=1, key="atualizarcapacidade")
            valor_diaria = st.number_input("Informe o novo valor da diária:", min_value=0.0, step=0.01, key="atualizarvalordiaria")

            if st.button("Atualizar tipo de quarto"):
                id = op.get_id_tipoquarto()
                View.tipoquarto_atualizar(id, nome, descricao, capacidade, valor_diaria)
                st.success("TipoQuarto atualizado com sucesso")
                time.sleep(2)
                st.rerun()


    @staticmethod
    def excluir():
        tipoquartos = View.tipoquarto_listar()
        if len(tipoquartos) == 0:
            st.write("Nenhum tipo de quarto encontrado.")
        else:
            op = st.selectbox("Exclusão de tipo de quartos", tipoquartos, format_func=lambda x: x.__str__())
            if st.button("Excluir"):
                id = op.get_id_tipoquarto()
                View.tipoquarto_excluir(id)
                st.success("TipoQuarto excluído com sucesso")
                time.sleep(2)
                st.rerun()
