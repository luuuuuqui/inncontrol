import streamlit as st
import pandas as pd
from views import View
import time
import datetime as dt
from decimal import Decimal


class ManterPagamentoUI:
    @staticmethod
    def main():
        st.header("Gestão de Pagamentos")
        tab1, tab2, tab3, tab4 = st.tabs(
            ["Listar", "Registrar (Inserir)", "Atualizar", "Excluir"]
        )

        with tab1:
            ManterPagamentoUI.listar()
        with tab2:
            ManterPagamentoUI.inserir()
        with tab3:
            ManterPagamentoUI.atualizar()
        with tab4:
            ManterPagamentoUI.excluir()

    @staticmethod
    def listar():
        pagamentos = View.pagamento_listar()
        if not pagamentos:
            st.info("Nenhum pagamento registrado.")
            return

        dic_pagamentos = []
        for p in pagamentos:
            # --- Recuperação de Objetos Relacionados ---
            reserva = View.reserva_listar_id(p.get_id_reserva())
            nome_hospede = "Desconhecido"

            if reserva:
                hospede = View.hospede_listar_id(reserva.get_id_hospede())
                if hospede:
                    usuario = View.usuario_listar_id(hospede.get_id_usuario())
                    if usuario:
                        nome_hospede = usuario.get_nome()

            # --- Formatação de Valores e Datas ---
            # CORREÇÃO: Converter para Decimal antes de formatar para evitar erro se vier como string
            valor_obj = Decimal(p.get_valor_total())
            valor_formatado = f"R$ {valor_obj:.2f}".replace(".", ",")

            try:
                data_pag = dt.datetime.strptime(
                    p.get_data_pagamento(), "%Y-%m-%d"
                ).strftime("%d/%m/%Y")
            except:
                data_pag = p.get_data_pagamento()

            dic_pagamentos.append(
                {
                    "ID Pagto": f"#{p.get_id_pagamento()}",
                    "Reserva": f"#{p.get_id_reserva()}",
                    "Hóspede": nome_hospede,
                    "Data": data_pag,
                    "Valor": valor_formatado,
                    "Forma": p.get_forma_pagamento(),
                    "Status": ManterPagamentoUI._formatar_status_icone(p.get_status()),
                }
            )

        df = pd.DataFrame(dic_pagamentos)
        st.dataframe(df, hide_index=True, use_container_width=True)

    @staticmethod
    def inserir():
        reservas = View.reserva_listar()

        if not reservas:
            st.error("Não há reservas cadastradas para efetuar pagamentos.")
            return

        # Seleção de Reserva
        reserva_selecionada = st.selectbox(
            "Selecione a Reserva para pagar:",
            reservas,
            format_func=lambda r: ManterPagamentoUI._formatar_resumo_reserva(r),
            key="ins_reserva_pagamento",  # Adicionado key
        )

        # --- PRÉVIA DO VALOR ---
        if reserva_selecionada:
            try:
                # O método de cálculo da view já retorna Decimal, então aqui costuma ser seguro
                valor_previsto = View.reserva_calcular_pagamento(
                    reserva_selecionada.get_id_reserva()
                )
                st.info(
                    f"💰 Valor total calculado para esta reserva: **R$ {valor_previsto:.2f}**"
                )
            except Exception as e:
                st.warning(f"Não foi possível calcular o valor prévio: {e}")

        col1, col2 = st.columns(2)
        with col1:
            data_pagamento = st.date_input(
                "Data do Pagamento:",
                value=dt.datetime.now(),
                format="DD/MM/YYYY",
                key="ins_data_pagamento",  # Adicionado key
            )

        with col2:
            forma_pagamento = st.selectbox(
                "Forma de Pagamento:",
                [
                    "Pix",
                    "Cartão de Crédito",
                    "Cartão de Débito",
                    "Dinheiro",
                    "Transferência",
                ],
                key="ins_forma_pagamento",  # Adicionado key
            )

        status = st.selectbox(
            "Status do Pagamento:",
            ("Confirmado", "Pendente", "Estornado"),
            key="ins_status_pagamento",
        )  # Adicionado key

        if st.button("Registrar Pagamento", key="btn_ins_pagamento"):  # Adicionado key
            try:
                View.pagamento_registrar(
                    reserva_selecionada.get_id_reserva(),
                    data_pagamento,
                    forma_pagamento,
                    status,
                )
                st.success("Pagamento registrado com sucesso!")
                time.sleep(1)
                st.rerun()
            except ValueError as ve:
                st.error(f"Erro de Validação: {ve}")
            except Exception as e:
                st.error(f"Erro ao inserir: {e}")

    @staticmethod
    def atualizar():
        pagamentos = View.pagamento_listar()

        if not pagamentos:
            st.info("Nenhum pagamento encontrado.")
            return

        # Selectbox para escolher qual pagamento editar
        pagamento_op = st.selectbox(
            "Selecione o pagamento para editar:",
            pagamentos,
            format_func=lambda p: ManterPagamentoUI._formatar_resumo_pagamento(p),
            key="upd_select_pagamento",
        )

        # Recuperar dados atuais
        try:
            data_atual = dt.datetime.strptime(
                pagamento_op.get_data_pagamento(), "%Y-%m-%d"
            ).date()
        except:
            data_atual = dt.date.today()

        lista_formas = [
            "Pix",
            "Cartão de Crédito",
            "Cartão de Débito",
            "Dinheiro",
            "Transferência",
        ]
        # Segurança caso a forma salva não esteja na lista
        forma_atual = pagamento_op.get_forma_pagamento()
        idx_forma = (
            lista_formas.index(forma_atual) if forma_atual in lista_formas else 0
        )

        lista_status = ["Confirmado", "Pendente", "Estornado"]
        status_atual = pagamento_op.get_status()
        idx_status = (
            lista_status.index(status_atual) if status_atual in lista_status else 0
        )

        # --- Formulário de Edição ---
        st.caption(
            "Nota: O valor será recalculado automaticamente com base nos consumos atuais da reserva."
        )

        col1, col2 = st.columns(2)

        # CORREÇÃO: Usamos o ID do pagamento na KEY dos campos.
        # Isso força o Streamlit a recriar o componente quando mudamos o pagamento selecionado,
        # garantindo que os valores (datas, selectbox) sejam atualizados visualmente.
        with col1:
            nova_data = st.date_input(
                "Data do Pagamento:",
                value=data_atual,
                format="DD/MM/YYYY",
                key=f"upd_data_{pagamento_op.get_id_pagamento()}",
            )
        with col2:
            nova_forma = st.selectbox(
                "Forma de Pagamento:",
                lista_formas,
                index=idx_forma,
                key=f"upd_forma_{pagamento_op.get_id_pagamento()}",
            )

        novo_status = st.selectbox(
            "Status:",
            lista_status,
            index=idx_status,
            key=f"upd_status_{pagamento_op.get_id_pagamento()}",
        )

        if st.button("Salvar Alterações", key="btn_upd_pagamento"):
            try:
                View.pagamento_atualizar(
                    pagamento_op.get_id_pagamento(),
                    pagamento_op.get_id_reserva(),
                    nova_data,
                    nova_forma,
                    novo_status,
                )
                st.success("Pagamento atualizado e valor recalculado com sucesso!")
                time.sleep(1)
                st.rerun()
            except Exception as e:
                st.error(f"Erro ao atualizar: {e}")

    @staticmethod
    def excluir():
        pagamentos = View.pagamento_listar()

        if not pagamentos:
            st.info("Nenhum pagamento encontrado.")
            return

        pagamento_op = st.selectbox(
            "Selecione o pagamento para excluir:",
            pagamentos,
            format_func=lambda p: ManterPagamentoUI._formatar_resumo_pagamento(p),
            key="del_select_pagamento",  # Adicionado key
        )

        # CORREÇÃO: Converter para Decimal antes de formatar no warning
        valor_obj = Decimal(pagamento_op.get_valor_total())
        st.warning(f"Tem certeza que deseja excluir o pagamento de R$ {valor_obj:.2f}?")

        if st.button(
            "Excluir Pagamento", type="primary", key="btn_del_pagamento"
        ):  # Adicionado key
            try:
                View.pagamento_excluir(pagamento_op.get_id_pagamento())
                st.success("Pagamento excluído com sucesso!")
                time.sleep(1)
                st.rerun()
            except Exception as e:
                st.error(f"Erro ao excluir: {e}")

    # --- MÉTODOS AUXILIARES DE FORMATAÇÃO ---

    @staticmethod
    def _formatar_status_icone(status):
        match status:
            case "Pendente":
                return "⏳ Pendente"
            case "Confirmado" | "Pago":
                return "✅ Confirmado"
            case "Estornado":
                return "↩️ Estornado"
            case _:
                return status

    @staticmethod
    def _formatar_resumo_reserva(r):
        """Formata a reserva no dropdown de inserção"""
        h = View.hospede_listar_id(r.get_id_hospede())
        nome = "Desconhecido"
        if h:
            u = View.usuario_listar_id(h.get_id_usuario())
            if u:
                nome = u.get_nome()

        return f"Reserva {r.get_id_reserva()} - {nome} ({r.get_data_checkin()} a {r.get_data_checkout()})"

    @staticmethod
    def _formatar_resumo_pagamento(p):
        """Formata o pagamento no dropdown de atualização/exclusão"""
        # CORREÇÃO: Converter para Decimal antes de formatar
        valor_obj = Decimal(p.get_valor_total())
        return f"ID {p.get_id_pagamento()} - Reserva {p.get_id_reserva()} - R$ {valor_obj:.2f} ({p.get_status()})"
