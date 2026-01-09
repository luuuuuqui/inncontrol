import streamlit as st  # pyright: ignore[reportMissingImports]

from templates.manterusuarioUI import ManterUsuarioUI as UsuarioUI
from templates.manterhospedeUI import ManterHospedeUI as HospedeUI
from templates.manterquartoUI import ManterQuartoUI as QuartoUI
from templates.mantertipoquartoUI import ManterTipoQuartoUI as TipoQuartoUI
from templates.manteradicionalUI import ManterAdicionalUI as AdicionalUI

from dao.database import Database


class IndexUI:
    @staticmethod
    def menu_admin():
        op = st.sidebar.selectbox(
            "Menu", ["Usuário", "Hóspede", "Quarto", "Tipo de Quarto", "Adicional"]
        )
        match op:
            case "Usuário":
                UsuarioUI.main()
            case "Hóspede":
                HospedeUI.main()
            case "Quarto":
                QuartoUI.main()
            case "Tipo de Quarto":
                TipoQuartoUI.main()
            case "Adicional":
                AdicionalUI.main()
            case _:
                st.error("Opção inválida.")

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
