from models.usuario import Usuario
from dao.usuariodao import UsuarioDAO
import streamlit as st  # pyright: ignore[reportMissingImports]
import pandas as pd  # pyright: ignore[reportMissingImports]
from views import View
import time

class ManterUsuarioUI:
    @staticmethod
    def main():
        st.header("Teste de CRUD de Usuário")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterUsuarioUI.listar()
        with tab2: ManterUsuarioUI.inserir()
        with tab3: ManterUsuarioUI.atualizar()
        with tab4: ManterUsuarioUI.excluir()

    @staticmethod
    def listar():
        usuarios = View.usuario_listar()
        if len(usuarios) == 0: st.write("Nenhum usuário encontrado.")
        else:
            list_dic = []
            df = pd.DataFrame([u.to_dict() for u in usuarios])
            st.dataframe(df, hide_index=True)


    @staticmethod
    def inserir():
        nome = st.text_input("Informe o nome:")
        fone = st.text_input("Informe o telefone:")
        email = st.text_input("Informe o email:")
        senha = st.text_input("Informe a senha:", type="password")
        tipoperfil = st.selectbox(
            "Informe o tipo do perfil:",
            ("Administrador", "Recepcionista", "Hóspede"),
        )
        idperfil = st.number_input(f"Informe o id do {tipoperfil.lower()}:", step=1, min_value=0)
        
        if st.button("Inserir"):
            try:
                View.usuario_inserir(nome, fone, email, senha, tipoperfil, idperfil)
            except Exception as e:
                st.error("Erro ao inserir: {}".format(e))
            else:
                st.success("Usuario inserido com sucesso")
                time.sleep(2)
                st.rerun()

    @staticmethod
    def atualizar():
        usuarios = View.usuario_listar()
        if len(usuarios) == 0: st.write("Nenhum usuario encontrado.")
        else:
            op = st.selectbox("Atualização de Usuarios", usuarios)

            nome = st.text_input("Informe o novo nome", op.get_nome())
            fone = st.text_input("Informe o telefone:", op.get_fone())
            email = st.text_input("Informe o email:", op.get_email())
            senha = st.text_input("Informe a senha:", type="password", value=op.get_senha())
            tipoperfil = st.selectbox(
                "Informe o tipo do perfil:",
                ("Administrador", "Recepcionista", "Hóspede"), key='atualizartipoperfil')
            idperfil = st.number_input(f"Informe o id do {tipoperfil.lower()}:", step=1, min_value=0, value=op.get_id_perfil())
            if st.button("Atualizar"):
                id = op.get_id_usuario()
                View.usuario_atualizar(id, nome, fone, email, senha, tipoperfil, idperfil)
                st.success("Usuario atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    @staticmethod
    def excluir():
        usuarios = View.usuario_listar()
        if len(usuarios) == 0: st.write("Nenhum usuario encontrado.")
        else:
            op = st.selectbox("Exclusão de Usuarios", usuarios)
            if st.button("Excluir"):
                id = op.get_id_usuario()
                View.usuario_excluir(id)
                st.success("Usuario excluído com sucesso")
                time.sleep(2)
                st.rerun()