import streamlit as st  # pyright: ignore[reportMissingImports]
import pandas as pd
from datetime import datetime
from decimal import Decimal
from views import View
import time


class ManterConsumoUI:
    @staticmethod
    def main():
        st.header("Gerenciar Consumo")
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
        if not consumos:
            st.info("Nenhum consumo registrado.")
            return

        dic_consumos = []
        for c in consumos:
            cd = c.to_dict()

            adicional = View.adicional_listar_id(c.get_id_adicional())
            nome_adicional = (
                adicional.get_descricao() if adicional else "Adicional Removido"
            )
            valor_unitario = (
                Decimal(adicional.get_valor()) if adicional else Decimal("0.00")
            )

            quantidade = Decimal(c.get_quantidade())
            total = valor_unitario * quantidade

            try:
                data_obj = datetime.strptime(cd["data_consumo"], "%Y-%m-%d %H:%M:%S")
                data_fmt = data_obj.strftime("%d/%m/%Y %H:%M")
            except Exception:
                data_fmt = str(cd["data_consumo"])

            dic_consumos.append(
                {
                    "ID": c.get_id_consumo(),
                    "ID Reserva": c.get_id_reserva(),
                    "Adicional": nome_adicional,
                    "Qtd": int(quantidade),
                    "Data": data_fmt,
                    "Total": f"R$ {total:.2f}".replace(".", ","),
                }
            )

        df = pd.DataFrame(dic_consumos)
        st.dataframe(df, hide_index=True, use_container_width=True)

    @staticmethod
    def inserir():
        id_reserva = st.number_input("ID da Reserva:", min_value=1, step=1)

        adicionais = View.adicional_listar()
        if not adicionais:
            st.warning("Cadastre adicionais primeiro.")
            return

        adicional_selecionado = st.selectbox(
            "Adicional:",
            adicionais,
            format_func=lambda a: f"{a.get_descricao()} (R$ {a.get_valor()})",
        )

        quantidade = st.number_input("Quantidade:", min_value=1, step=1, value=1)

        col1, col2 = st.columns(2)
        data = col1.date_input("Data:", value=datetime.now())
        hora = col2.time_input("Hora:", value=datetime.now().time())

        if st.button("Inserir Consumo"):
            if adicional_selecionado is None:
                st.error("Selecione um adicional.")
                return

            assert adicional_selecionado is not None  # Type narrowing for type checker

            data_hora = datetime.combine(data, hora)
            try:
                View.consumo_inserir(
                    id_reserva,
                    adicional_selecionado.get_id_adicional(),
                    quantidade,
                    data_hora,
                )
                st.success("Consumo registrado!")
                time.sleep(1)
                st.rerun()
            except Exception as e:
                st.error(f"Erro: {e}")

    @staticmethod
    def atualizar():
        consumos = View.consumo_listar()
        if not consumos:
            st.info("Nenhum consumo para editar.")
            return

        op = st.selectbox(
            "Selecione o Consumo:",
            consumos,
            format_func=lambda c: ManterConsumoUI._formatar_consumo_resumo(c),
        )

        if op is None:
            return

        assert op is not None  # Type narrowing for type checker

        try:
            dt_atual = datetime.strptime(op.get_data_consumo(), "%Y-%m-%d %H:%M:%S")
        except Exception:
            dt_atual = datetime.now()

        adicionais = View.adicional_listar()
        idx_adic = ManterConsumoUI._obter_indice(
            adicionais, op.get_id_adicional(), lambda a: a.get_id_adicional()
        )

        # Campos
        novo_reserva = st.number_input(
            "ID Reserva:", value=op.get_id_reserva(), min_value=1
        )

        novo_adicional = st.selectbox(
            "Adicional:",
            adicionais,
            index=idx_adic,
            format_func=lambda a: f"{a.get_descricao()} (R$ {a.get_valor()})",
        )

        nova_qtd = st.number_input(
            "Quantidade:", min_value=1, step=1, value=op.get_quantidade()
        )

        col1, col2 = st.columns(2)
        nova_data = col1.date_input("Data:", value=dt_atual.date())
        nova_hora = col2.time_input("Hora:", value=dt_atual.time())

        if st.button("Salvar Alterações"):
            if novo_adicional is None:
                st.error("Selecione um adicional.")
                return

            assert novo_adicional is not None  # Type narrowing for type checker

            nova_dt_full = datetime.combine(nova_data, nova_hora)
            try:
                View.consumo_atualizar(
                    op.get_id_consumo(),
                    novo_reserva,
                    novo_adicional.get_id_adicional(),
                    nova_qtd,
                    nova_dt_full,
                )
                st.success("Consumo atualizado!")
                time.sleep(1)
                st.rerun()
            except Exception as e:
                st.error(f"Erro: {e}")

    @staticmethod
    def excluir():
        consumos = View.consumo_listar()
        if not consumos:
            st.info("Nenhum consumo para excluir.")
            return

        op = st.selectbox(
            "Selecione o Consumo para excluir:",
            consumos,
            format_func=lambda c: ManterConsumoUI._formatar_consumo_resumo(c),
        )

        if op is None:
            return

        assert op is not None  # Type narrowing for type checker

        if st.button("Excluir"):
            try:
                View.consumo_excluir(op.get_id_consumo())
                st.success("Consumo excluído!")
                time.sleep(1)
                st.rerun()
            except Exception as e:
                st.error(f"Erro: {e}")

    # --- Helpers ---
    @staticmethod
    def _formatar_consumo_resumo(c):
        a = View.adicional_listar_id(c.get_id_adicional())
        desc = a.get_descricao() if a else "?"
        return f"ID {c.get_id_consumo()} - Res. #{c.get_id_reserva()} - {c.get_quantidade()}x {desc}"

    @staticmethod
    def _obter_indice(lista, id_alvo, get_id_func):
        for i, item in enumerate(lista):
            if get_id_func(item) == id_alvo:
                return i
        return 0
