import time
import streamlit as st  # pyright: ignore[reportMissingImports]

from dao.database import Database

# admin
from templates.manterusuarioUI import ManterUsuarioUI as UsuarioUI
from templates.manterhospedeUI import ManterHospedeUI as HospedeUI
from templates.manterquartoUI import ManterQuartoUI as QuartoUI
from templates.mantertipoquartoUI import ManterTipoQuartoUI as TipoQuartoUI
from templates.manterreservaUI import ManterReservaUI as ReservaUI
from templates.manterpagamentoUI import ManterPagamentoUI as PagamentoUI
from templates.manterconsumoUI import ManterConsumoUI as ConsumoUI
from templates.manteradicionalUI import ManterAdicionalUI as AdicionalUI
from templates.manterrelatoriosui import RelatoriosUI


# recepcionista
# (nenhum por enquanto)

# hóspede
from templates.perfilhospedeui import PerfilHospedeUI

# visitante
from templates.loginUI import LoginUI


class IndexUI:
    @staticmethod
    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Abrir Conta"])
        match op:
            case "Entrar no Sistema":
                LoginUI.main()
            case "Abrir Conta":
                st.info(
                    "Hey, essa funcionalidade ainda não está disponível! Fique à vontade para entrar em contato com a recepção para abrir uma conta."
                )

    @staticmethod
    def menu_admin():
        op = st.sidebar.selectbox(
            "Menu",
            [
                "Usuário",
                "Hóspede",
                "Quarto",
                "Tipo de Quarto",
                "Reserva",
                "Pagamento",
                "Consumo",
                "Adicional",
                "Relatórios",
            ],
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
            case "Reserva":
                ReservaUI.main()
            case "Pagamento":
                PagamentoUI.main()
            case "Consumo":
                ConsumoUI.main()
            case "Adicional":
                AdicionalUI.main()
            case "Relatórios":
                RelatoriosUI.main()
            case _:
                st.error("Opção inválida.")

    @staticmethod
    def sair_do_sistema():
        if st.sidebar.button("Sair do Sistema"):
            try:
                st.session_state.clear()
            except Exception as e:
                st.error(f"Erro ao sair: {e}")
            finally:
                st.success("Você saiu do sistema com sucesso.")
                time.sleep(1)
                st.rerun()

    @staticmethod
    def sidebar():
        if not st.session_state.get("usuario_id"):
            IndexUI.menu_visitante()
        else:
            st.sidebar.write(
                f"Bem-vindo(a), {st.session_state['usuario_nome'].split()[0]}!"
            )
            IndexUI.sair_do_sistema()
            match st.session_state.get("usuario_tipo", "").lower():
                case "administrador":
                    IndexUI.menu_admin()
                case "recepcionista":
                    st.info(
                        "Ops! O menu de recepcionista ainda não está implementado. Em breve estaremos trazendo essa funcionalidade!"
                    )
                case "hóspede" | "hospede":
                    PerfilHospedeUI.main()
                case _:
                    st.error(
                        f'Ei! Seu tipo de usuário, "{st.session_state["usuario_tipo"]}", não foi reconhecido por nosso sistema. Entre em contato com nosso suporte.'
                    )

    @staticmethod
    def main():
        # garantir que as tabelas existam
        Database.abrir()
        Database.criar_tabelas()
        Database.fechar()

        IndexUI.sidebar()


if __name__ == "__main__":
    IndexUI.main()
