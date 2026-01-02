import streamlit as st  # pyright: ignore[reportMissingImports]
import pandas as pd  # pyright: ignore[reportMissingImports]
from views import View
import time

class ManterHospedeUI:
    @staticmethod
    def main():
        st.header("Teste de CRUD de Hóspede")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterHospedeUI.listar()
        with tab2: ManterHospedeUI.inserir()
        with tab3: ManterHospedeUI.atualizar()
        with tab4: ManterHospedeUI.excluir()

    @staticmethod
    def listar():
        hospedes = View.hospede_listar()
        if len(hospedes) == 0: st.write("Nenhum hóspede encontrado.")
        else:
            list_dic = []
            df = pd.DataFrame([h.to_dict() for h in hospedes])
            st.dataframe(df, hide_index=True)


    @staticmethod
    def inserir():
        id_usuario = st.number_input("Informe o id do usuário:", step=1, min_value=0)
        endereco = st.text_input("Informe o endereço:")
        
        if st.button("Inserir"):
            try:
                View.hospede_inserir(id_usuario, endereco)
            except Exception as e:
                st.error("Erro ao inserir: {}".format(e))
            else:
                st.success("Hóspede inserido com sucesso")
                time.sleep(2)
                st.rerun()

    @staticmethod
    def atualizar():
        hospedes = View.hospede_listar()
        if len(hospedes) == 0: st.write("Nenhum hóspede encontrado.")
        else:
            op = st.selectbox("Atualização de Hóspedes", hospedes)
            id_usuario = st.number_input("Informe o novo id do usuário:", step=1, min_value=0, value=op.get_id_usuario())
            endereco = st.text_input("Informe o novo endereço:", value=op.get_endereco())
            if st.button("Atualizar"):
                id = op.get_id_hospede()
                View.hospede_atualizar(id, id_usuario, endereco)
                st.success("Hospede atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    @staticmethod
    def excluir():
        hospedes = View.hospede_listar()
        if len(hospedes) == 0: st.write("Nenhum hóspede encontrado.")
        else:
            op = st.selectbox("Exclusão de Hóspedes", hospedes)
            if st.button("Excluir"):
                id = op.get_id_hospede()
                View.hospede_excluir(id)
                st.success("Hóspede excluído com sucesso")
                time.sleep(2)
                st.rerun()