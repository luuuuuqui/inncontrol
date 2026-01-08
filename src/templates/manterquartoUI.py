import streamlit as st  # pyright: ignore[reportMissingImports]
import pandas as pd  # pyright: ignore[reportMissingImports]
from views import View
import time


class ManterQuartoUI:
    @staticmethod
    def main():
        st.header("Teste de CRUD de Quarto")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1:
            ManterQuartoUI.listar()
        with tab2:
            ManterQuartoUI.inserir()
        with tab3:
            ManterQuartoUI.atualizar()
        with tab4:
            ManterQuartoUI.excluir()

    @staticmethod
    def listar():
        quartos = View.quarto_listar()
        if len(quartos) == 0:
            st.write("Nenhum quarto encontrado.")
        else:
            dic_quartos = []
            for q in quartos:
                qd = q.to_dict()
                tipo = View.tipoquarto_listar_id(q.get_id_quarto_tipo())

                if tipo:
                    qd["tipo_descricao"] = tipo.get_nome()
                else:
                    qd["tipo_descricao"] = "Tipo não encontrado"

                dic_quartos.append(qd)

            df = pd.DataFrame(dic_quartos)

            df = df.rename(
                columns={
                    "id_quarto": "ID",
                    "tipo_descricao": "Tipo do Quarto",
                    "bloco": "Bloco",
                    "numero": "Número",
                }
            )
            df = df.reindex(columns=["ID", "Tipo do Quarto", "Bloco", "Número"])
            st.dataframe(df, hide_index=True)

    @staticmethod
    def inserir():
        quartos = View.tipoquarto_listar()
        if len(quartos) == 0:
            st.write("Nenhum usuário quarto encontrado.")
        else:
            """
            quarto:
            id: int,
            id_tipo: int,
            bloco: str,
            numero: int
            """

            tipo = st.selectbox(
                "Selecione o tipo do quarto:", View.tipoquarto_listar()
            ).get_id_tipoquarto()

            bloco = st.text_input("Informe o bloco:", placeholder="Bloco A")

            numero = st.number_input("Informe o número do quarto:", step=1, min_value=1)

            if st.button("Inserir"):
                try:
                    View.quarto_inserir(tipo, bloco, numero)
                except Exception as e:
                    st.error("Erro ao inserir: {}".format(e))
                else:
                    st.success("Quarto inserido com sucesso")
                    time.sleep(2)
                    st.rerun()

    @staticmethod
    def atualizar():
        quartos = View.quarto_listar()
        if len(quartos) == 0:
            st.write("Nenhum quarto encontrado.")
        else:
            op = st.selectbox(
                "Selecione o quarto para atualizar:",
                quartos,
                format_func=lambda h: f"{h.get_id_quarto()} - {View.tipoquarto_listar_id(h.get_id_quarto_tipo()).get_nome()} - {h.get_bloco()} - {h.get_numero()}",
            )

            tipo = st.selectbox(
                "Selecione o novo tipo do quarto:",
                View.tipoquarto_listar(),
                index=[
                    i
                    for i, t in enumerate(View.tipoquarto_listar())
                    if t.get_id_tipoquarto() == op.get_id_quarto_tipo()
                ][0],
            ).get_id_tipoquarto()

            bloco = st.text_input("Informe o bloco:", value=op.get_bloco())

            numero = st.number_input(
                "Informe o número do quarto:",
                step=1,
                min_value=1,
                value=op.get_numero(),
            )

            if st.button("Atualizar"):
                id = op.get_id_quarto()
                View.quarto_atualizar(id, tipo, bloco, numero)
                st.success("Quarto atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    @staticmethod
    def excluir():
        quartos = View.quarto_listar()
        if len(quartos) == 0:
            st.write("Nenhum quarto encontrado.")
        else:
            # Corrigido o selectbox que estava comentado e quebrado
            op = st.selectbox(
                "Selecione o quarto para excluir:",
                quartos,
                format_func=lambda h: f"{h.get_id_quarto()} - {View.tipoquarto_listar_id(h.get_id_quarto_tipo()).get_nome()} - {h.get_bloco()} - {h.get_numero()}",
            )
            if st.button("Excluir"):
                id = op.get_id_quarto()
                View.quarto_excluir(id)
                st.success("Quarto excluído com sucesso")
                time.sleep(2)
                st.rerun()
