from templates.admin.manterclienteUI import ManterClienteUI
from templates.visitante.abrircontaUI import AbrirContaUI
from templates.visitante.loginUI import LoginUI
from views import View

import streamlit as st

class IndexUI:
    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Abrir Conta"])
        if op == "Entrar no Sistema": LoginUI.main()
        if op == "Abrir Conta": AbrirContaUI.main()

    def menu_admin():            
        op = st.sidebar.selectbox("Menu", ["Cadastro de Clientes", "Cadastro de Serviços", "Cadastro de Horários", "Cadastro de Profissionais"])
        if op == "Cadastro de Clientes": ManterClienteUI.main()
        if op == "Cadastro de Serviços": st.write("Em construção")
        if op == "Cadastro de Horários": st.write("Em construção")
        if op == "Cadastro de Profissionais": st.write("Em construção")

    def menu_cliente():
        op = st.sidebar.selectbox("Menu", ["Meus Serviços", "Agendar Serviço", "Meus Dados"])
        if op == "Meus Serviços": st.write("Em construção")
        if op == "Agendar Serviço": st.write("Em construção")
        if op == "Meus Dados": st.write("Em construção")

    def menu_profissional():
        op = st.sidebar.selectbox("Menu", ["Minha Agenda", "Abrir Agenda", "Confirmar Serviço", "Meus Dados"])
        if op == "Minha Agenda": st.write("Em construção")
        if op == "Abrir Agenda": st.write("Em construção")
        if op == "Confirmar Serviço": st.write("Em construção")
        if op == "Meus Dados": st.write("Em construção")

    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["usuario_tipo"]
            del st.session_state["usuario_id"]
            del st.session_state["usuario_nome"]
            st.rerun()
    
    def sidebar():
        if "usuario_id" not in st.session_state:
            # usuário não está logado
            IndexUI.menu_visitante()   
        else:
            # usuário está logado, verifica se é o admin
            admin = st.session_state["usuario_nome"] == "admin"
            # verifica se é cliente ou profissional
            cliente = st.session_state["usuario_tipo"] == "cliente"
            prof = st.session_state["usuario_tipo"] == "prof"
            # mensagem de bem-vindo
            st.sidebar.write("Bem-vindo(a), " + st.session_state["usuario_nome"])
            # menu do usuário
            if admin: IndexUI.menu_admin()
            else:
                if cliente: IndexUI.menu_cliente()
                if prof: IndexUI.menu_profissional()
            # controle de sair do sistema
            IndexUI.sair_do_sistema() 

    def main():
        # verifica a existe o usuário admin
        View.cliente_criar_admin()
        # monta o sidebar
        IndexUI.sidebar()

IndexUI.main()

