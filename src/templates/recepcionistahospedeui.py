import streamlit as st
import pandas as pd
from views import View
import time


class RecepcionistaHospedeUI:
    @staticmethod
    def main():
        st.header("Gerenciar Hóspedes")
        tab1, tab2, tab3 = st.tabs(
            ["Listar", "Novo Hóspede (Cadastro Completo)", "Editar"]
        )

        with tab1:
            RecepcionistaHospedeUI.listar()
        with tab2:
            RecepcionistaHospedeUI.inserir_completo()
        with tab3:
            RecepcionistaHospedeUI.editar()

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
    def inserir_completo():
        with st.form("form_novo_hospede"):
            col1, col2 = st.columns(2)
            nome = col1.text_input("Nome Completo")
            email = col2.text_input("Email")
            fone = col1.text_input("Telefone")
            senha = col2.text_input("Senha Provisória", type="password")
            endereco = st.text_input("Endereço Completo")

            submitted = st.form_submit_button("Cadastrar Hóspede")

            if submitted:
                if not (nome and email and senha and endereco):
                    st.error("Preencha todos os campos obrigatórios.")
                else:
                    try:
                        View.usuario_inserir(nome, fone, email, senha, "Hóspede", 0)

                        todos_usuarios = View.usuario_listar()
                        novo_usuario = next(
                            (u for u in todos_usuarios if u.get_email() == email), None
                        )

                        if novo_usuario:
                            View.hospede_inserir(
                                novo_usuario.get_id_usuario(), endereco
                            )
                            st.success("Hóspede e Usuário cadastrados com sucesso!")
                            time.sleep(1)
                            st.rerun()
                        else:
                            st.error("Erro ao recuperar usuário criado.")
                    except Exception as e:
                        st.error(f"Erro no processo de cadastro: {e}")

    @staticmethod
    def editar():
        hospedes = View.hospede_listar()
        if not hospedes:
            st.info("Nenhum hóspede cadastrado para editar.")
            return

        hospedes_validos = []
        for h in hospedes:
            usuario = View.usuario_listar_id(h.get_id_usuario())
            if usuario and usuario.get_tipo_perfil().lower() == "hóspede":
                hospedes_validos.append(h)

        if not hospedes_validos:
            st.info("Nenhum hóspede disponível para edição.")
            return

        op = st.selectbox(
            "Selecione o Hóspede para editar:",
            hospedes_validos,
            format_func=lambda h: RecepcionistaHospedeUI._formatar_hospede_resumo(h),
        )

        usuario = View.usuario_listar_id(op.get_id_usuario())
        if not usuario:
            st.error("Usuário associado não encontrado.")
            return

        if usuario.get_tipo_perfil().lower() != "hóspede":
            st.error(
                "Apenas usuários do tipo 'Hóspede' podem ser editados por recepcionistas."
            )
            return

        with st.form("form_editar_hospede"):
            st.subheader("Editar Dados do Hóspede")
            st.info(
                "A senha não pode ser alterada por recepcionistas. Para alterar a senha, contate o administrador."
            )

            col1, col2 = st.columns(2)
            novo_nome = col1.text_input("Nome Completo", value=usuario.get_nome())
            novo_email = col2.text_input("Email", value=usuario.get_email())
            novo_fone = col1.text_input("Telefone", value=usuario.get_fone() or "")
            novo_endereco = st.text_input("Endereço Completo", value=op.get_endereco())

            submitted = st.form_submit_button("Salvar Alterações")

            if submitted:
                if not (novo_nome and novo_email and novo_endereco):
                    st.error(
                        "Preencha todos os campos obrigatórios (Nome, Email e Endereço)."
                    )
                else:
                    try:
                        View.usuario_atualizar(
                            usuario.get_id_usuario(),
                            novo_nome,
                            novo_fone,
                            novo_email,
                            usuario.get_tipo_perfil(),
                            usuario.get_id_perfil(),
                        )

                        View.hospede_atualizar(
                            op.get_id_hospede(),
                            op.get_id_usuario(),
                            novo_endereco,
                        )

                        st.success("Hóspede atualizado com sucesso!")
                        time.sleep(1)
                        st.rerun()
                    except Exception as e:
                        st.error(f"Erro ao atualizar hóspede: {e}")

    @staticmethod
    def _formatar_hospede_resumo(h):
        usuario = View.usuario_listar_id(h.get_id_usuario())
        nome = usuario.get_nome() if usuario else "Usuário Desconhecido"
        return f"ID {h.get_id_hospede()} - {nome}"
