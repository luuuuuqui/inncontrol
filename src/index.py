from templates.mantertesteUI import ManterTesteUI
from dao.database import Database
import streamlit as st

class IndexUI:
    @staticmethod
    def menu_admin():
        op = st.sidebar.selectbox("Menu", ["Teste"])
        if op == "Teste":
            ManterTesteUI.main()

    @staticmethod
    def sidebar():
        IndexUI.menu_admin()

    @staticmethod
    def main():
        # Garantir que as tabelas existam antes de usar
        Database.abrir()
        Database.criar_tabelas()
        Database.fechar()
        
        IndexUI.sidebar()

if __name__ == "__main__":
    IndexUI.menu_admin()