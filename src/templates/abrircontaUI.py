import streamlit as st
import time
from views import View


class AbrirContaUI:
    @staticmethod
    def main():
        """
        Exibe o formulário de auto-cadastro para hóspedes.
        Cria sequencialmente o Usuário e a entidade Hóspede associada.
        """
        st.header("Crie sua conta")
        st.markdown("Preencha os dados abaixo para ter acesso às suas reservas.")

        with st.form("form_abrir_conta"):
            nome = st.text_input("Nome Completo")
            email = st.text_input("E-mail")
            fone = st.text_input("Telefone")
            senha = st.text_input("Senha", type="password")
            endereco = st.text_input("Endereço Completo")

            submitted = st.form_submit_button("Criar Conta")

            if submitted:
                if not (nome and email and senha and endereco):
                    st.error("Todos os campos são obrigatórios.")
                else:
                    try:
                        View.usuario_inserir(nome, fone, email, senha, "Hóspede")

                        todos_usuarios = View.usuario_listar()
                        novo_usuario = next(
                            (u for u in todos_usuarios if u.get_email() == email), None
                        )

                        if novo_usuario:
                            View.hospede_inserir(
                                novo_usuario.get_id_usuario(), endereco
                            )

                            st.success(
                                "Conta criada com sucesso! Faça login para continuar."
                            )
                            time.sleep(2)
                            st.rerun()
                        else:
                            st.error("Erro interno: Usuário criado não foi encontrado.")

                    except ValueError as ve:
                        st.error(f"Erro de validação: {ve}")
                    except Exception as e:
                        st.error(f"Erro ao criar conta: {e}")
