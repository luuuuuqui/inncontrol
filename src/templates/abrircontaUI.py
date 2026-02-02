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
            # Endereço é um dado obrigatório da entidade Hóspede (F15)
            endereco = st.text_input("Endereço Completo")

            submitted = st.form_submit_button("Criar Conta")

            if submitted:
                # Validação básica de campos obrigatórios (NF10)
                if not (nome and email and senha and endereco):
                    st.error("Todos os campos são obrigatórios.")
                else:
                    try:
                        # 1. Criação do Usuário Genérico
                        # Tipo fixo "Hóspede" conforme regra de negócio
                        # ID Perfil 0 (padrão quando não especificado)
                        View.usuario_inserir(nome, fone, email, senha, "Hóspede", 0)

                        # 2. Recuperação do ID (Padrão existente no projeto)
                        # Busca o usuário recém-criado pelo e-mail para obter o ID gerado pelo banco
                        todos_usuarios = View.usuario_listar()
                        novo_usuario = next(
                            (u for u in todos_usuarios if u.get_email() == email), None
                        )

                        if novo_usuario:
                            # 3. Criação do Vínculo de Hóspede
                            View.hospede_inserir(
                                novo_usuario.get_id_usuario(), endereco
                            )

                            st.success(
                                "Conta criada com sucesso! Faça login para continuar."
                            )
                            time.sleep(2)
                            st.rerun()  # Recarrega a página para voltar ao Login
                        else:
                            st.error("Erro interno: Usuário criado não foi encontrado.")

                    except ValueError as ve:
                        st.error(f"Erro de validação: {ve}")
                    except Exception as e:
                        st.error(f"Erro ao criar conta: {e}")
