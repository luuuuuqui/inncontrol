import streamlit as st # pyright: ignore[reportMissingImports]
import pandas as pd
from views import View
import time


class ManterHospedeUI:
    @staticmethod
    def main():
        st.header("Gerenciar Hóspedes")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1:
            ManterHospedeUI.listar()
        with tab2:
            ManterHospedeUI.inserir()
        with tab3:
            ManterHospedeUI.atualizar()
        with tab4:
            ManterHospedeUI.excluir()

    @staticmethod
    def listar():
        hospedes = View.hospede_listar()
        if not hospedes:
            st.info("Nenhum hóspede cadastrado.")
            return

        dic_hospedes = []
        for h in hospedes:
            usuario = View.usuario_listar_id(h.get_id_usuario())
            nome_usuario = usuario.get_nome() if usuario else "Usuário Removido"
            email_usuario = usuario.get_email() if usuario else "-"
            fone_usuario = usuario.get_fone() if usuario else "-"

            dic_hospedes.append(
                {
                    "ID Hóspede": h.get_id_hospede(),
                    "Nome": nome_usuario,
                    "Email": email_usuario,
                    "Telefone": fone_usuario,
                    "Endereço": h.get_endereco(),
                }
            )

        df = pd.DataFrame(dic_hospedes)
        st.dataframe(df, hide_index=True, use_container_width=True)

    @staticmethod
    def inserir():
        # Filtra apenas usuários com perfil de hóspede
        usuarios_hospede = [
            u for u in View.usuario_listar() if u.get_tipo_perfil().lower() == "hóspede"
        ]

        if not usuarios_hospede:
            st.warning("Não há usuários com perfil 'Hóspede' disponíveis.")
            return

        usuario_selecionado = st.selectbox(
            "Selecione o Usuário:",
            usuarios_hospede,
            format_func=lambda u: f"{u.get_id_usuario()} - {u.get_nome()}",
        )

        endereco = st.text_input("Endereço:")

        if st.button("Inserir"):
            if not endereco:
                st.error("Informe o endereço.")
            else:
                try:
                    View.hospede_inserir(usuario_selecionado.get_id_usuario(), endereco)
                    st.success("Hóspede cadastrado com sucesso!")
                    time.sleep(1)
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro: {e}")

    @staticmethod
    def atualizar():
        hospedes = View.hospede_listar()
        if not hospedes:
            st.info("Nenhum hóspede para atualizar.")
            return

        op = st.selectbox(
            "Selecione o Hóspede:",
            hospedes,
            format_func=lambda h: ManterHospedeUI._formatar_hospede_resumo(h),
        )

        # Lógica para pre-selecionar o usuário vinculado
        todos_usuarios = View.usuario_listar()
        idx_usuario = ManterHospedeUI._obter_indice(
            todos_usuarios, op.get_id_usuario(), lambda u: u.get_id_usuario()
        )

        novo_usuario = st.selectbox(
            "Vincular Usuário:",
            todos_usuarios,
            index=idx_usuario,
            format_func=lambda u: f"{u.get_id_usuario()} - {u.get_nome()}",
        )

        novo_endereco = st.text_input("Endereço:", value=op.get_endereco())

        if st.button("Salvar Alterações"):
            try:
                View.hospede_atualizar(
                    op.get_id_hospede(), novo_usuario.get_id_usuario(), novo_endereco
                )
                st.success("Hóspede atualizado!")
                time.sleep(1)
                st.rerun()
            except Exception as e:
                st.error(f"Erro: {e}")

    @staticmethod
    def excluir():
        hospedes = View.hospede_listar()
        if not hospedes:
            st.info("Nenhum hóspede para excluir.")
            return

        op = st.selectbox(
            "Selecione o Hóspede para excluir:",
            hospedes,
            format_func=lambda h: ManterHospedeUI._formatar_hospede_resumo(h),
        )

        if st.button("Excluir"):
            try:
                View.hospede_excluir(op.get_id_hospede())
                st.success("Hóspede excluído!")
                time.sleep(1)
                st.rerun()
            except Exception as e:
                st.error(f"Erro: {e}")

    # --- Helpers ---
    @staticmethod
    def _formatar_hospede_resumo(h):
        u = View.usuario_listar_id(h.get_id_usuario())
        nome = u.get_nome() if u else "Usuário Desconhecido"
        return f"ID {h.get_id_hospede()} - {nome}"

    @staticmethod
    def _obter_indice(lista, id_alvo, get_id_func):
        for i, item in enumerate(lista):
            if get_id_func(item) == id_alvo:
                return i
        return 0
