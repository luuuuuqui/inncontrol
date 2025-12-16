import streamlit as st
import pandas as pd
from controller.controller import Controller
import time

class ManterTesteUI:
    @staticmethod
    def main():
        st.header("Cadastro de Itens")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterTesteUI.listar()
        with tab2: ManterTesteUI.inserir()
        with tab3: ManterTesteUI.atualizar()
        with tab4: ManterTesteUI.excluir()

    @staticmethod
    def listar():
        itens = Controller.teste_listar()
        if len(itens) == 0: st.write("Nenhum teste cadastrado")
        else:
            list_dic = []
            for obj in itens: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic, columns=["id", "name"])
            df = df.sort_values(by="id")
            st.dataframe(df, hide_index=True)

    @staticmethod
    def inserir():
        nome = st.text_input("nome:")
        if st.button("Inserir"):
            Controller.teste_inserir(nome)
            st.success("Teste inserido com sucesso")
            time.sleep(1)
            st.rerun()

    @staticmethod
    def atualizar():
        itens = Controller.teste_listar()
        if len(itens) == 0: st.write("Nenhum teste cadastrado")
        else:
            op = st.selectbox("Atualização de Itens", itens, format_func=lambda x: f'{x.get_id()} - {x.get_name()}')
            if op is not None:
                nome = st.text_input("Informe o novo nome:", op.get_name())
                if st.button("Atualizar"):
                    id = op.id
                    Controller.teste_atualizar(id, nome)
                    st.success("Teste atualizado com sucesso")
                    time.sleep(1)
                    st.rerun()

    @staticmethod
    def excluir():
        itens = Controller.teste_listar()
        if len(itens) == 0: st.write("Nenhum teste cadastrado")
        else:
            op = st.selectbox("Exclusão de Itens", itens, format_func=lambda x: f'{x.get_id()} - {x.get_name()}')
            if op is not None and st.button("Excluir"):
                id = op.id
                Controller.teste_excluir(id)
                st.success("Teste excluído com sucesso")
                time.sleep(1)
                st.rerun()
