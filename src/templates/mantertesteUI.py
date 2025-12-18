import streamlit as st
import pandas as pd
from views import View
import time

class ManterTesteUI:
    @staticmethod
    def main():
        st.header("Cadastro de Testes")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterTesteUI.listar()
        with tab2: ManterTesteUI.inserir()
        with tab3: ManterTesteUI.atualizar()
        with tab4: ManterTesteUI.excluir()

    @staticmethod
    def listar():
        testes = View.teste_listar()
        if len(testes) == 0: st.write("Nenhum teste cadastrado")
        else:
            list_dic = []
            for obj in testes: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df, hide_index=True)

    @staticmethod
    def inserir():
        nome = st.text_input("Informe o nome")
        if st.button("Inserir"):
            View.teste_inserir(nome)
            st.success("Teste inserido com sucesso")
            time.sleep(2)
            st.rerun()

    @staticmethod
    def atualizar():
        testes = View.teste_listar()
        if len(testes) == 0: st.write("Nenhum teste cadastrado")
        else:
            op = st.selectbox("Atualização de Testes", testes)
            nome = st.text_input("Informe o novo nome", op.get_name())
            if st.button("Atualizar"):
                id = op.get_id()
                View.teste_atualizar(id, nome)
                st.success("Teste atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    @staticmethod
    def excluir():
        testes = View.teste_listar()
        if len(testes) == 0: st.write("Nenhum teste cadastrado")
        else:
            op = st.selectbox("Exclusão de Testes", testes)
            if st.button("Excluir"):
                id = op.get_id()
                View.teste_excluir(id)
                st.success("Teste excluído com sucesso")
                time.sleep(2)
                st.rerun()