import streamlit as st
import pandas as pd
from views import View
import time


class ManterQuartoUI:
    @staticmethod
    def main():
        st.header("Gerenciar Quartos")
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
        if not quartos:
            st.info("Nenhum quarto cadastrado.")
            return

        dic_quartos = []
        for q in quartos:
            tipo = View.tipoquarto_listar_id(q.get_id_quarto_tipo())
            nome_tipo = tipo.get_nome() if tipo else "Tipo Excluído"

            dic_quartos.append(
                {
                    "ID": q.get_id_quarto(),
                    "Tipo": nome_tipo,
                    "Bloco": q.get_bloco(),
                    "Número": q.get_numero(),
                }
            )

        df = pd.DataFrame(dic_quartos)
        st.dataframe(df, hide_index=True, use_container_width=True)

    @staticmethod
    def inserir():
        tipos = View.tipoquarto_listar()
        if not tipos:
            st.warning("Cadastre Tipos de Quarto antes de inserir quartos.")
            return

        tipo_selecionado = st.selectbox(
            "Tipo de Quarto:", tipos, format_func=lambda t: t.get_nome()
        )

        bloco = st.text_input("Bloco:", placeholder="Ex: A")
        numero = st.number_input("Número do Quarto:", step=1, min_value=1)

        if st.button("Inserir"):
            if not bloco:
                st.error("Informe o bloco.")
            else:
                try:
                    View.quarto_inserir(
                        tipo_selecionado.get_id_tipoquarto(), bloco, numero
                    )
                    st.success("Quarto inserido!")
                    time.sleep(1)
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro: {e}")

    @staticmethod
    def atualizar():
        quartos = View.quarto_listar()
        if not quartos:
            st.info("Nenhum quarto para atualizar.")
            return

        op = st.selectbox(
            "Selecione o Quarto:",
            quartos,
            format_func=lambda q: ManterQuartoUI._formatar_quarto_resumo(q),
        )

        # Prepara seleção do tipo
        tipos = View.tipoquarto_listar()
        idx_tipo = ManterQuartoUI._obter_indice(
            tipos, op.get_id_quarto_tipo(), lambda t: t.get_id_tipoquarto()
        )

        novo_tipo = st.selectbox(
            "Tipo de Quarto:", tipos, index=idx_tipo, format_func=lambda t: t.get_nome()
        )

        novo_bloco = st.text_input("Bloco:", value=op.get_bloco())
        novo_numero = st.number_input(
            "Número:", step=1, min_value=1, value=op.get_numero()
        )

        if st.button("Salvar Alterações"):
            try:
                View.quarto_atualizar(
                    op.get_id_quarto(),
                    novo_tipo.get_id_tipoquarto(),
                    novo_bloco,
                    novo_numero,
                )
                st.success("Quarto atualizado!")
                time.sleep(1)
                st.rerun()
            except Exception as e:
                st.error(f"Erro: {e}")

    @staticmethod
    def excluir():
        quartos = View.quarto_listar()
        if not quartos:
            st.info("Nenhum quarto para excluir.")
            return

        op = st.selectbox(
            "Selecione o Quarto para excluir:",
            quartos,
            format_func=lambda q: ManterQuartoUI._formatar_quarto_resumo(q),
        )

        if st.button("Excluir"):
            try:
                View.quarto_excluir(op.get_id_quarto())
                st.success("Quarto excluído!")
                time.sleep(1)
                st.rerun()
            except Exception as e:
                st.error(f"Erro: {e}")

    # --- Helpers ---
    @staticmethod
    def _formatar_quarto_resumo(q):
        tipo = View.tipoquarto_listar_id(q.get_id_quarto_tipo())
        nome_tipo = tipo.get_nome() if tipo else "?"
        return f"ID {q.get_id_quarto()} - {q.get_bloco()} Nº {q.get_numero()} ({nome_tipo})"

    @staticmethod
    def _obter_indice(lista, id_alvo, get_id_func):
        for i, item in enumerate(lista):
            if get_id_func(item) == id_alvo:
                return i
        return 0
