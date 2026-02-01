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
            st.info("Para editar dados sensíveis de acesso, contate o administrador.")

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
