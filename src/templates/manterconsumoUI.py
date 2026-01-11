import streamlit as st  # pyright: ignore[reportMissingImports]
import pandas as pd  # pyright: ignore[reportMissingImports]
from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP
from views import View
import time

"""
    id_consumo: int,
    id_reserva: int,
    id_adicional: int,
    quantidade: int,
    data_consumo: datetime,
"""


class ManterConsumoUI:
    @staticmethod
    def main():
        st.header("Teste de CRUD de Consumo")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1:
            ManterConsumoUI.listar()
        with tab2:
            ManterConsumoUI.inserir()
        with tab3:
            ManterConsumoUI.atualizar()
        with tab4:
            ManterConsumoUI.excluir()

    @staticmethod
    def listar():
        consumos = View.consumo_listar()
        if len(consumos) == 0:
            st.write("Nenhum consumo encontrado.")
        else:
            # Cria uma lista de dicionários personalizada para formatar o valor
            dic_consumos = []
            for c in consumos:
                c = c.to_dict()
                # Formata o valor float (ex: 6.99) para string moeda (ex: R$ 6,99)
                # ad["valor"] = f"R$ {c.get_valor()}".replace(".", ",")

                c["data_consumo"] = datetime.strptime(
                    c["data_consumo"], "%Y-%m-%d %H:%M:%S"
                ).strftime("%d/%m/%Y %H:%M:%S")

                c["nome_adicional"] = View.adicional_listar_id(
                    c["id_adicional"]
                ).get_descricao() # pyright: ignore[reportOptionalMemberAccess]

                # calcula o valor total do consumo
                valoradicional = Decimal(
                    View.adicional_listar_id(c["id_adicional"]).get_valor() # pyright: ignore[reportOptionalMemberAccess]
                )
                quantidade = Decimal(c["quantidade"])

                total = valoradicional * quantidade

                total = total.quantize(
                    Decimal("0.01"), rounding=ROUND_HALF_UP
                )  # só de precaução

                c["valor_total"] = f"R$ {total}".replace(".", ",")

                dic_consumos.append(c)

            df = pd.DataFrame(dic_consumos)

            df = df.reindex(
                columns=[
                    "id_consumo",
                    "id_reserva",
                    "id_adicional",
                    "nome_adicional",
                    "quantidade",
                    "data_consumo",
                    "valor_total",
                ]
            )

            df = df.rename(
                columns={
                    "id_consumo": "ID Consumo",
                    "id_reserva": "ID Reserva",
                    "id_adicional": "ID Adicional",
                    "nome_adicional": "Adicional",
                    "quantidade": "Quantidade",
                    "data_consumo": "Data",
                    "valor_total": "Valor Total",
                }
            )

            st.dataframe(df, hide_index=True)

    @staticmethod
    def inserir():
        reserva = st.number_input("Informe o ID da reserva:", step=1, min_value=0)

        adicional = st.selectbox(
            "Selecione o adicional:",
            View.adicional_listar(),
            format_func=lambda x: x.__str__(),
        ).get_id_adicional()

        quantidade = st.number_input("Informe a quantidade:", step=1, min_value=0)

        data_consumo = st.date_input("Informe a data do consumo:", format="DD/MM/YYYY")

        hora_consumo = st.time_input("Informe a hora do consumo:")

        data_hora_consumo = None

        if data_consumo and hora_consumo:
            data_hora_consumo = datetime.combine(data_consumo, hora_consumo)

        st.code(data_hora_consumo, language="python")

        bloquear = not (reserva and adicional and quantidade and data_hora_consumo)

        if st.button("Inserir", disabled=bloquear):
            try:
                View.consumo_inserir(reserva, adicional, quantidade, data_hora_consumo)
            except Exception as e:
                st.error("Erro ao inserir: {}".format(e))
            else:
                st.success("Consumo inserido com sucesso")
                time.sleep(2)
                st.rerun()

    @staticmethod
    def atualizar():
        consumos = View.consumo_listar()
        if len(consumos) == 0:
            st.write("Nenhum consumo encontrado.")
        else:
            op = st.selectbox(
                "Escolha o consumo a atualizar",
                consumos,
                format_func=lambda x: f"{x.get_id_consumo()} - Reserva: #{x.get_id_reserva()} - {x.get_quantidade()}x {View.adicional_listar_id(x.get_id_adicional()).get_descricao()} - {datetime.strptime(x.get_data_consumo(), "%Y-%m-%d %H:%M:%S").strftime("%d/%m/%Y %H:%M")}", # pyright: ignore[reportOptionalMemberAccess]
                key="selectboxatualizar",
            )

            if "ultimo_id_selecionado" not in st.session_state:
                st.session_state.ultimo_id_selecionado = None

            # Se o ID mudou, atualizamos as chaves do session_state com os dados do banco
            if st.session_state.ultimo_id_selecionado != op.get_id_consumo():
                st.session_state.ultimo_id_selecionado = op.get_id_consumo()
                st.session_state.reservaatualizar = op.get_id_reserva()
                st.session_state.adicionalatualizar = op.get_id_adicional()
                st.session_state.quantidadeatualizar = op.get_quantidade()
                st.session_state.dataconsumoatualizar = datetime.strptime(op.get_data_consumo(), "%Y-%m-%d %H:%M:%S").date()
                st.session_state.horaconsumoatualizar = datetime.strptime(op.get_data_consumo(), "%Y-%m-%d %H:%M:%S").time()

            reserva = st.number_input("Informe o ID da reserva:", key="reservaatualizar", step=1, min_value=0)

            adicional = st.selectbox(
                "Selecione o adicional a atualizar:",
                View.adicional_listar(),
                format_func=lambda x: x.__str__(),
            ).get_id_adicional()

            quantidade = st.number_input("Informe a quantidade:", key="quantidadeatualizar", step=1, min_value=0)

            data_consumo = st.date_input("Informe a data do consumo:", key="dataconsumoatualizar", format="DD/MM/YYYY")

            hora_consumo = st.time_input("Informe a hora do consumo:", key="horaconsumoatualizar")

            data_hora_consumo = None

            if data_consumo and hora_consumo:
                data_hora_consumo = datetime.combine(data_consumo, hora_consumo)

            bloquear = not (reserva and adicional and quantidade and data_hora_consumo)

            if st.button("Atualizar consumo", disabled=bloquear):
                id = op.get_id_consumo()
                View.consumo_atualizar(id, reserva, adicional, quantidade, data_hora_consumo)
                st.success("Consumo atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    @staticmethod
    def excluir():
        consumos = View.consumo_listar()
        if len(consumos) == 0:
            st.write("Nenhum consumo encontrado.")
        else:
            op = st.selectbox(
                "Escolha o consumo a atualizar",
                consumos,
                format_func=lambda x: f"{x.get_id_consumo()} - Reserva: #{x.get_id_reserva()} - {x.get_quantidade()}x {View.adicional_listar_id(x.get_id_adicional()).get_descricao()} - {datetime.strptime(x.get_data_consumo(), "%Y-%m-%d %H:%M:%S").strftime("%d/%m/%Y %H:%M")}",  # pyright: ignore[reportOptionalMemberAccess]
                key="selectboxatualizar",
            )

            if st.button("Excluir"):
                id = op.get_id_consumo()
                View.consumo_excluir(id)
                st.success("Consumo excluído com sucesso")
                time.sleep(2)
                st.rerun()
