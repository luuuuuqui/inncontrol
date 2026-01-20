import streamlit as st # pyright: ignore[reportMissingImports]
import time
from views import View

class LoginUI:
    @staticmethod
    def main():
        st.header("Entrar no Sistema")

        with st.container():
            with st.form(key="login_form"):
                email = st.text_input("E-mail")
                senha = st.text_input("Senha", type="password")
                submit_button = st.form_submit_button(label="Entrar")

            if submit_button:
                if not email or not senha:
                    st.warning("Preencha o e-mail e a senha.")
                else:
                    LoginUI.autenticar_usuario(email, senha)

    @staticmethod
    def autenticar_usuario(email, senha):
        usuario_encontrado = View.usuario_autenticar(email, senha)

        if usuario_encontrado:
            # armazena dados do usuário na sessão
            st.session_state["usuario_id"] = usuario_encontrado["id"]
            st.session_state["usuario_nome"] = usuario_encontrado["nome"]
            st.session_state["usuario_tipo"] = usuario_encontrado["tipo"]
            st.session_state["usuario_primeiro_nome"] = usuario_encontrado["nome"].split()[0]
            st.session_state["usuario_sobrenome"] = usuario_encontrado["nome"].split()[-1]

            primeiro_nome = st.session_state["usuario_primeiro_nome"]
            tipo_formatado = usuario_encontrado["tipo"].lower()
            st.success(
                f"Login como {tipo_formatado} realizado com sucesso. Bem-vindo(a), {primeiro_nome}!"
            )

            time.sleep(1)
            st.rerun()
        else:
            st.error("E-mail ou senha inválidos.")
