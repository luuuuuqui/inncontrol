import streamlit as st  # pyright: ignore[reportMissingImports]
import pandas as pd  # pyright: ignore[reportMissingImports]
from views import View
import time


class ManterAdicionalUI:
    @staticmethod
    def main():
        st.header("Teste de CRUD de Adicional")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1:
            ManterAdicionalU,,,I.listar()
        with tab2:
            ManterAdicionalUI.inserir()
        with tab3:
            ManterAdicionalUI.atualizar()
        with tab4:
            ManterAdicionalUI.excluir()

    @staticmethod
    def listar():
        adicionais = View.adicional_listar()
        if len(adicionais) == 0:
            st.write("Nenhum adicional encontrado.")
        else:
            # Cria uma lista de dicionários personalizada para formatar o valor
            dic_adicionais = []
            for a in adicionais:
                ad = a.to_dict()
                # Formata o valor float (ex: 6.99) para string moeda (ex: R$ 6,99)
                ad["valor"] = f"R$ {a.get_valor()}".replace(".", ",")
                dic_adicionais.append(ad)

            df = pd.DataFrame(dic_adicionais)

            df = df.rename(
                columns={
                    "id_adicional": "ID",
                    "descricao": "Descrição",
                    "valor": "Valor",
                }
            )

            st.dataframe(df, hide_index=True)

    @staticmethod
    def inserir():
        descricao = st.text_input(
            "Informe a descrição:", placeholder="Água Mineral Crystal Sem Gás"
        )

        valor = st.number_input(
            "Informe o valor:", value=None, placeholder="2.99", step=0.01, min_value=0.0
        )

        st.code(f"{type(valor)}\n{valor}", language="python")

        bloquear = not (descricao and valor)

        if st.button("Inserir", disabled=bloquear):
            try:
                View.adicional_inserir(descricao, valor)
            except Exception as e:
                st.error("Erro ao inserir: {}".format(e))
            else:
                st.success("Adicional inserido com sucesso")
                time.sleep(2)
                st.rerun()

    @staticmethod
    def atualizar():
        adicionais = View.adicional_listar()
        if len(adicionais) == 0:
            st.write("Nenhum adicional encontrado.")
        else:
            op = st.selectbox(
                "Escolha o adicional a atualizar",
                adicionais,
                format_func=lambda x: x.__str__(),
                key="selectboxatualizar",
            )

            if "ultimo_id_selecionado" not in st.session_state:
                st.session_state.ultimo_id_selecionado = None

            # Se o ID mudou, atualizamos as chaves do session_state com os dados do banco
            if st.session_state.ultimo_id_selecionado != op.get_id_adicional():
                st.session_state.ultimo_id_selecionado = op.get_id_adicional()
                st.session_state.atualizardescricao = op.get_descricao()
                st.session_state.atualizarvalor = float(op.get_valor())

            descricao = st.text_input(
                "Informe a nova descrição:", key="atualizardescricao"
            )

            valor = st.number_input("Informe o novo valor:", key="atualizarvalor")

            if st.button("Atualizar adicional"):
                id = op.get_id_adicional()
                View.adicional_atualizar(id, descricao, valor)
                st.success("Adicional atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    @staticmethod
    def excluir():
        adicionais = View.adicional_listar()
        if len(adicionais) == 0:
            st.write("Nenhum adicional encontrado.")
        else:
            op = st.selectbox("Exclusão de Adicionais", adicionais)

            if st.button("Excluir"):
                id = op.get_id_adicional()
                View.adicional_excluir(id)
                st.success("Adicional excluído com sucesso")
                time.sleep(2)
                st.rerun()
