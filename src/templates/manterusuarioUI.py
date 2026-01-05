import streamlit as st  # pyright: ignore[reportMissingImports]
import pandas as pd  # pyright: ignore[reportMissingImports]
from views import View
import time


class ManterUsuarioUI:
    @staticmethod
    def main():
        st.header("Teste de CRUD de Usuário")
        tab1, tab2, tab3, tab4, tab5 = st.tabs(
            ["Listar", "Inserir", "Atualizar", "Atualizar Senha", "Excluir"]
        )
        with tab1:
            ManterUsuarioUI.listar()
        with tab2:
            ManterUsuarioUI.inserir()
        with tab3:
            ManterUsuarioUI.atualizar()
        with tab4:
            ManterUsuarioUI.atualizar_senha()
        with tab5:
            ManterUsuarioUI.excluir()

    @staticmethod
    def listar():
        usuarios = View.usuario_listar()
        if len(usuarios) == 0:
            st.write("Nenhum usuário encontrado.")
        else:
            df = pd.DataFrame([u.to_dict() for u in usuarios])
            df = df.rename(
                columns={
                    "id_usuario": "ID",
                    "nome": "Nome",
                    "email": "Email",
                    "fone": "Telefone",
                    "perfil_tipo": "Tipo de Perfil",
                    "perfil_id": "ID (Perfil)",
                }
            )
            df = df.reindex(
                columns=[
                    "ID",
                    "Nome",
                    "Email",
                    "Telefone",
                    "Tipo de Perfil",
                    "ID (Perfil)",
                ]
            )
            st.dataframe(df, hide_index=True)

    @staticmethod
    def inserir():
        nome = st.text_input("Informe o nome:", placeholder="João da Silva")
        fone = st.text_input("Informe o telefone:", placeholder="(11) 99999-0000")
        email = st.text_input("Informe o email:", placeholder="joaosilva@exemple.com")
        senha = st.text_input(
            "Informe a senha:", type="password", placeholder="********"
        )
        tipoperfil = st.selectbox(
            "Informe o tipo do perfil:",
            ("Administrador", "Recepcionista", "Hóspede"),
        )
        idperfil = st.number_input(
            f"Informe o id do {tipoperfil.lower()}:", step=1, min_value=0
        )

        bloquear = not (nome and email and senha)

        if st.button("Inserir", disabled=bloquear):
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
        if len(usuarios) == 0:
            st.write("Nenhum usuario encontrado.")
        else:
            op = st.selectbox(
                "Escolha o usuário a atualizar",
                usuarios,
                format_func=lambda x: x.__str__(),
                key="selectboxatualizar",
            )

            if "ultimo_id_selecionado" not in st.session_state:
                st.session_state.ultimo_id_selecionado = None

            # Se o ID mudou, atualizamos as chaves do session_state com os dados do banco
            if st.session_state.ultimo_id_selecionado != op.get_id_usuario():
                st.session_state.ultimo_id_selecionado = op.get_id_usuario()
                st.session_state.atualizarnome = op.get_nome()
                st.session_state.atualizarfone = op.get_fone()
                st.session_state.atualizaremail = op.get_email()
                st.session_state.atualizartipoperfil = op.get_tipo_perfil()
                st.session_state.atualizaridperfil = op.get_id_perfil()

            nome = st.text_input("Informe o novo nome", key="atualizarnome")
            fone = st.text_input(
                "Informe o novo telefone:",
                key="atualizarfone",
                placeholder="Usuário sem telefone.",
            )
            email = st.text_input("Informe o novo email:", key="atualizaremail")

            tipoperfil = st.selectbox(
                "Informe o tipo do perfil:",
                ("Administrador", "Recepcionista", "Hóspede"),
                key="atualizartipoperfil",
            )

            idperfil = st.number_input(
                f"Informe o id do {tipoperfil.lower()}:",
                step=1,
                min_value=0,
                key="atualizaridperfil",
            )

            if st.button("Atualizar usuário"):
                id = op.get_id_usuario()
                View.usuario_atualizar(id, nome, fone, email, tipoperfil, idperfil)
                st.success("Usuario atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    @staticmethod
    def atualizar_senha():
        usuarios = View.usuario_listar()
        if len(usuarios) == 0:
            st.write("Nenhum usuario encontrado.")
        else:
            op = st.selectbox(
                "Escolha o usuário a atualizar",
                usuarios,
                format_func=lambda x: x.__str__(),
                key="sb_atualizar_senha",
            )

            # Inicializa a variável de controle se não existir
            if "ultimo_usuario" not in st.session_state:
                st.session_state.ultimo_usuario = op.get_id_usuario()

            # Compara o usuário atual com o último armazenado
            if st.session_state.ultimo_usuario != op.get_id_usuario():
                st.session_state.atualizarsenha = ""  # Limpa o campo de senha
                st.session_state.ultimo_usuario = (
                    op.get_id_usuario()
                )  # Atualiza o controle

            senha = st.text_input(
                "Informe a nova senha:", type="password", key="atualizarsenha"
            )

            if st.button("Atualizar senha", key="btn_atualizar_senha"):
                id = op.get_id_usuario()
                View.usuario_atualizar_senha(id, senha)
                st.success("Senha atualizada com sucesso!")
                time.sleep(2)
                st.rerun()

    @staticmethod
    def excluir():
        usuarios = View.usuario_listar()
        if len(usuarios) == 0:
            st.write("Nenhum usuario encontrado.")
        else:
            op = st.selectbox("Exclusão de Usuarios", usuarios)
            if st.button("Excluir"):
                id = op.get_id_usuario()
                View.usuario_excluir(id)
                st.success("Usuario excluído com sucesso")
                time.sleep(2)
                st.rerun()
