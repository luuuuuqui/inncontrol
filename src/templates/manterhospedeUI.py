import streamlit as st  # pyright: ignore[reportMissingImports]
import pandas as pd  # pyright: ignore[reportMissingImports]
from views import View
import time


class ManterHospedeUI:
    @staticmethod
    def main():
        st.header("Teste de CRUD de Hóspede")
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
        if len(hospedes) == 0:
            st.write("Nenhum hóspede encontrado.")
        else:
            dic_hospedes = []
            for h in hospedes:
                hd = h.to_dict()
                usuario = View.usuario_listar_id(h.get_id_usuario())

                if usuario:
                    hd.update(
                        {
                            "id_usuario": usuario.get_id_usuario(),
                            "nome": usuario.get_nome(),
                            "fone": usuario.get_fone(),
                            "email": usuario.get_email(),
                        }
                    )
                else:
                    hd.update(
                        {
                            "id_usuario": hd.get("id_usuario"),
                            "nome": None,
                            "fone": None,
                            "email": None,
                        }
                    )
                dic_hospedes.append(hd)
            
            df = pd.DataFrame(dic_hospedes)


            df = df.rename(columns={
                "id_usuario": "ID (Usuário)",
                "nome": "Nome",
                "email": "Email",
                "fone": "Telefone",
                "endereco": "Endereço",
                "id_hospede": "ID (Hóspede)",
            })
            
            df = df.reindex(columns=[f"ID (Usuário)", "Nome", "Email", "Telefone", "Endereço", "ID (Hóspede)"])

            st.dataframe(df, hide_index=True)


    @staticmethod
    def inserir():
        hospedes = [
            u for u in View.usuario_listar() if u.get_tipo_perfil().lower() == "hóspede"
        ]
        if len(hospedes) == 0:
            st.write("Nenhum usuário hóspede encontrado.")
        else:
            id_usuario = st.selectbox(
                "Selecione o usuário:",
                hospedes,
                format_func=lambda u: f"{u.get_id_usuario()} - {u.get_nome()}",
            ).get_id_usuario()
            endereco = st.text_input("Informe o endereço:")

            if st.button("Inserir"):
                try:
                    View.hospede_inserir(id_usuario, endereco)
                except Exception as e:
                    st.error("Erro ao inserir: {}".format(e))
                else:
                    st.success("Hóspede inserido com sucesso")
                    time.sleep(2)
                    st.rerun()

    @staticmethod
    def atualizar():
        hospedes = View.hospede_listar()
        if len(hospedes) == 0:
            st.write("Nenhum hóspede encontrado.")
        else:
            op = st.selectbox(
                "Atualização de Hóspedes",
                hospedes,
                format_func=lambda h: f"{h.get_id_hospede()} - {View.usuario_listar_id(h.get_id_usuario()).get_nome() if View.usuario_listar_id(h.get_id_usuario()) else 'Usuário não encontrado'} - {h.get_endereco()}", # pyright: ignore[reportOptionalMemberAccess]
            )
            usuarios_hospede = [
                u
                for u in View.usuario_listar()
                if u.get_tipo_perfil().lower() == "hóspede"
            ]
            usuario_selecionado = st.selectbox(
                "Selecione o usuário:",
                usuarios_hospede,
                format_func=lambda u: f"{u.get_id_usuario()} - {u.get_nome()}",
                key="usuario_atualizar",
            )
            id_usuario = usuario_selecionado.get_id_usuario()
            endereco = st.text_input(
                "Informe o novo endereço:", value=op.get_endereco()
            )
            if st.button("Atualizar"):
                id = op.get_id_hospede()
                View.hospede_atualizar(id, id_usuario, endereco)
                st.success("Hospede atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    @staticmethod
    def excluir():
        hospedes = View.hospede_listar()
        if len(hospedes) == 0:
            st.write("Nenhum hóspede encontrado.")
        else:
            op = st.selectbox("Exclusão de Hóspedes", hospedes)
            if st.button("Excluir"):
                id = op.get_id_hospede()
                View.hospede_excluir(id)
                st.success("Hóspede excluído com sucesso")
                time.sleep(2)
                st.rerun()
