import streamlit as st # pyright: ignore[reportMissingImports]
import pandas as pd
from views import View
import time


class ManterUsuarioUI:
    @staticmethod
    def main():
        st.header("Gerenciar Usuários")
        tab1, tab2, tab3, tab4, tab5 = st.tabs(
            ["Listar", "Inserir", "Atualizar", "Alterar Senha", "Excluir"]
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
        if not usuarios:
            st.info("Nenhum usuário encontrado.")
            return

        data = []
        for u in usuarios:
            data.append(
                {
                    "ID": u.get_id_usuario(),
                    "Nome": u.get_nome(),
                    "Email": u.get_email(),
                    "Telefone": u.get_fone(),
                    "Tipo Perfil": u.get_tipo_perfil(),
                }
            )

        df = pd.DataFrame(data)
        st.dataframe(df, hide_index=True, use_container_width=True)

    @staticmethod
    def inserir():
        nome = st.text_input("Nome:", placeholder="João da Silva")
        email = st.text_input("Email:", placeholder="joao@email.com")
        fone = st.text_input("Telefone:", placeholder="(11) 99999-9999")
        senha = st.text_input("Senha:", type="password")

        tipos_perfil = ["Administrador", "Recepcionista", "Hóspede"]
        # Added unique key
        tipo_perfil = st.selectbox(
            "Tipo de Perfil:", tipos_perfil, key="sb_inserir_perfil"
        )

        # O campo ID perfil parece ser legado ou para chaves externas manuais, mantendo conforme original
        id_perfil = st.number_input(
            "ID Externo do Perfil (Opcional):", min_value=0, step=1, value=0
        )

        if st.button("Inserir"):
            if not (nome and email and senha):
                st.error("Nome, Email e Senha são obrigatórios.")
            else:
                try:
                    View.usuario_inserir(
                        nome, fone, email, senha, tipo_perfil, id_perfil
                    )
                    st.success("Usuário inserido!")
                    time.sleep(1)
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro: {e}")

    @staticmethod
    def atualizar():
        usuarios = View.usuario_listar()
        if not usuarios:
            st.info("Nenhum usuário para editar.")
            return

        op = st.selectbox(
            "Selecione o Usuário:",
            usuarios,
            format_func=lambda u: f"{u.get_id_usuario()} - {u.get_nome()}",
        )

        novo_nome = st.text_input("Nome:", value=op.get_nome())
        novo_email = st.text_input("Email:", value=op.get_email())
        novo_fone = st.text_input("Telefone:", value=op.get_fone())

        tipos_perfil = ["Administrador", "Recepcionista", "Hóspede"]
        idx_perfil = (
            tipos_perfil.index(op.get_tipo_perfil())
            if op.get_tipo_perfil() in tipos_perfil
            else 0
        )

        # Added unique key
        novo_tipo = st.selectbox(
            "Tipo de Perfil:", tipos_perfil, index=idx_perfil, key="sb_atualizar_perfil"
        )
        novo_id_perfil = st.number_input(
            "ID Externo:", min_value=0, step=1, value=op.get_id_perfil()
        )

        if st.button("Salvar Alterações"):
            try:
                View.usuario_atualizar(
                    op.get_id_usuario(),
                    novo_nome,
                    novo_fone,
                    novo_email,
                    novo_tipo,
                    novo_id_perfil,
                )
                st.success("Usuário atualizado!")
                time.sleep(1)
                st.rerun()
            except Exception as e:
                st.error(f"Erro: {e}")

    @staticmethod
    def atualizar_senha():
        usuarios = View.usuario_listar()
        if not usuarios:
            st.info("Nenhum usuário encontrado.")
            return

        op = st.selectbox(
            "Selecione o Usuário:",
            usuarios,
            format_func=lambda u: f"{u.get_id_usuario()} - {u.get_nome()}",
            key="sb_senha_user",
        )

        nova_senha = st.text_input("Nova Senha:", type="password")

        if st.button("Alterar Senha"):
            if not nova_senha:
                st.error("Digite a nova senha.")
            else:
                try:
                    View.usuario_atualizar_senha(op.get_id_usuario(), nova_senha)
                    st.success("Senha atualizada!")
                    time.sleep(1)
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro: {e}")

    @staticmethod
    def excluir():
        usuarios = View.usuario_listar()
        if not usuarios:
            st.info("Nenhum usuário para excluir.")
            return

        op = st.selectbox(
            "Selecione para excluir:",
            usuarios,
            format_func=lambda u: f"{u.get_id_usuario()} - {u.get_nome()}",
        )

        if st.button("Excluir"):
            try:
                View.usuario_excluir(op.get_id_usuario())
                st.success("Usuário excluído!")
                time.sleep(1)
                st.rerun()
            except Exception as e:
                st.error(f"Erro: {e}")
