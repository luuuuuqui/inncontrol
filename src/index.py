from templates.manterusuarioUI import ManterUsuarioUI as UsuarioUI
from templates.manterhospedeUI import ManterHospedeUI as HospedeUI
from dao.database import Database
import streamlit as st

class IndexUI:
    @staticmethod
    def menu_admin():
        op = st.sidebar.selectbox("Menu", ["Usuário", "Hóspede"])
        match op:
            case "Usuário": UsuarioUI.main()
            case "Hóspede": HospedeUI.main()
            case _: st.error("Opção inválida.")

    @staticmethod
    def sidebar():
        IndexUI.menu_admin()

    @staticmethod
    def main():
        # garantir que as tabelas existam
        Database.abrir()
        Database.criar_tabelas()
        Database.fechar()
        
        IndexUI.sidebar()

if __name__ == "__main__":
    IndexUI.main()