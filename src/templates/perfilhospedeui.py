import streamlit as st # pyright: ignore[reportMissingImports]
import datetime as dt
from datetime import date
from views import View
import time

class PerfilHospedeUI:
    @staticmethod
    def main():
        st.set_page_config(page_title="Minhas Reservas", layout="wide")
        st.markdown("## Suas Reservas")
        PerfilHospedeUI.listar()

    @staticmethod
    def listar():
        if "usuario_id" not in st.session_state:
            st.warning("Faça login para visualizar suas reservas.")
            return

        id_usuario = st.session_state["usuario_id"]
        hospede = View.hospede_listar_por_usuario(id_usuario)

        if hospede is None:
            st.warning("Perfil de hóspede não encontrado.")
            return

        id_hospede = hospede.get_id_hospede()

        reservas = []
        try:
            reservas = View.reservas_listar_hospede(id_hospede)
        except Exception as e:
            st.warning(f"Não foi possível carregar suas reservas: {e}.")

        # Carrega lista de adicionais e prepara dicionário de opções (Nome -> Objeto)
        opcoes_adicionais = {}
        try:
            lista = View.adicional_listar()
            for item in lista:
                # Cria um rótulo único para o selectbox
                lbl = f"{item.get_descricao()} ({PerfilHospedeUI._formatar_dinheiro(item.get_valor())})"
                opcoes_adicionais[lbl] = item
        except Exception:
            opcoes_adicionais = {}

        PerfilHospedeUI._aplicar_estilos()

        colunas = st.columns(2)
        if not reservas:
            st.info("Nenhuma reserva encontrada.")

        hoje = dt.datetime.now().date()

        for i, r in enumerate(reservas):
            coluna = colunas[i % 2]
            with coluna:
                with st.container(border=True):
                    # --- Dados da Reserva ---
                    checkin_date = PerfilHospedeUI._converter_data(r.get('checkin'))
                    checkout_date = PerfilHospedeUI._converter_data(r.get('checkout'))

                    qtd_diarias = (
                        PerfilHospedeUI._calcular_diarias(r["checkin"], r["checkout"])
                        if r.get("checkin") and r.get("checkout")
                        else 0
                    )

                    pagamento_css = "payment-paid" if r.get("pago") else "payment-pending"

                    adicionais_html = ""
                    for item in r.get("adicionais", []):
                        qtd = float(item.get("quantidade", 1))
                        preco_unit = float(item.get("preco", 0))
                        total_item = qtd * preco_unit
                        qtd_display = int(qtd) if qtd.is_integer() else qtd
                        
                        adicionais_html += f"<div>- <b>{qtd_display}x</b> {item['nome']}: {PerfilHospedeUI._formatar_dinheiro(total_item)}</div>"

                    html_info = f"""
                    <div style='display:flex;justify-content:space-between;align-items:center'>
                        <div>
                            <div style='font-weight:700;font-size:16px; color:var(--text-color)'>#{r.get('id')} — {r.get('hospede')}</div>
                            <div class='meta'>{r.get('tipo_quarto')} • Quarto {r.get('numero_quarto')}</div>
                        </div>
                        <div>
                            <div class='payment {pagamento_css}'>{'Pago' if r.get('pago') else 'Pendente'}</div>
                        </div>
                    </div>
                    <hr class='custom-hr'>
                    <div style='display:flex;justify-content:space-between;gap:12px'>
                        <div>
                            <div class='meta'>Check-in</div>
                            <div>{PerfilHospedeUI._formatar_data_br(r.get('checkin'))}</div>
                        </div>
                        <div>
                            <div class='meta'>Check-out</div>
                            <div>{PerfilHospedeUI._formatar_data_br(r.get('checkout'))}</div>
                        </div>
                        <div>
                            <div class='meta'>Diárias</div>
                            <div>{qtd_diarias}</div>
                        </div>
                        <div>
                            <div class='meta'>Valor Total</div>
                            <div style='font-weight:700'>{PerfilHospedeUI._formatar_dinheiro(r.get('total'))}</div>
                        </div>
                    </div>
                    <div style='margin-top:8px'>
                        <div class='meta'>Pagamento</div>
                        <div>{r.get('tipo_pagamento', '-')}</div>
                    </div>
                    <div style='margin-top:6px; margin-bottom:10px;'>
                        <div class='meta'>Adicionais / Consumo</div>
                        <div>{adicionais_html or '<span class="meta" style="font-style:italic">Nenhum item consumido.</span>'}</div>
                    </div>
                    """
                    st.markdown(html_info, unsafe_allow_html=True)

                    # --- Área de Ação: Adicionar Consumo ---
                    if checkout_date >= hoje:
                        with st.expander("Adicionar Consumo"):
                            if not opcoes_adicionais:
                                st.info("Não há itens disponíveis no cardápio.")
                            else:
                                # Placeholder para mensagens fora das colunas estreitas
                                msg_placeholder = st.empty()

                                c1, c2 = st.columns([3, 1])
                                with c1:
                                    label_selecionado = st.selectbox(
                                        "Item",
                                        options=list(opcoes_adicionais.keys()),
                                        key=f"item_sel_{r.get('id')}",
                                        label_visibility="collapsed"
                                    )
                                    item_obj = opcoes_adicionais[label_selecionado]

                                with c2:
                                    qtd_input = st.number_input(
                                        "Qtd",
                                        min_value=1,
                                        step=1,
                                        value=1,
                                        key=f"qtd_input_{r.get('id')}",
                                        label_visibility="collapsed"
                                    )
                                
                                subtotal = 0.0
                                if item_obj:
                                    try:
                                        val_str = str(item_obj.get_valor()).replace(',', '.')
                                        valor_float = float(val_str)
                                        subtotal = valor_float * qtd_input
                                    except:
                                        subtotal = 0.0

                                c_resumo, c_btn = st.columns([2, 1])
                                with c_resumo:
                                    st.markdown(
                                        f"<div style='margin-top:5px; font-size:15px; color:var(--text-color)'>"
                                        f"Total previsto: <b>{PerfilHospedeUI._formatar_dinheiro(subtotal)}</b>"
                                        f"</div>", 
                                        unsafe_allow_html=True
                                    )
                                with c_btn:
                                    if st.button("Confirmar", key=f"btn_save_{r.get('id')}", use_container_width=True):
                                        try:
                                            View.consumo_inserir(
                                                r.get('id'),
                                                item_obj.get_id_adicional(),
                                                qtd_input,
                                                dt.datetime.now()
                                            )
                                            # Usa o placeholder para mostrar a mensagem na largura total
                                            msg_placeholder.success("Adicionado com sucesso!")
                                            time.sleep(1)
                                            st.rerun()
                                        except Exception as e:
                                            msg_placeholder.error(f"Erro: {e}")

    @staticmethod
    def _aplicar_estilos():
        st.markdown(
            """
        <style>
        :root {
            /* borda e fundo */
            --border-strong: #111;
            --border-subtle: #80808033;
            --border-dashed: #8080804c;
            --bg-subtle: #8080800c;

            /* status - pagamento confirmado */
            --status-paid-text: #059669;
            --status-paid-bg: #05966926;

            /* status - pagamento pendente */
            --status-pending-text: #dc2626;
            --status-pending-bg: #dc262626;
        }

        .meta {
            font-size: 13px;
            color: var(--text-color);
            opacity: 0.7;
        }

        .payment {
            display: inline-block;
            padding: 4px 10px;
            border-radius: 999px;
            font-size: 15px;
            font-weight: 600;
            border: 1px solid var(--border-strong);
        }

        .payment-paid {
            background-color: var(--status-paid-bg);
            color: var(--status-paid-text);
            border-color: var(--status-paid-text);
        }

        .payment-pending {
            background-color: var(--status-pending-bg);
            color: var(--status-pending-text);
            border-color: var(--status-pending-text);
        }

        hr.custom-hr {
            margin: 8px 0;
            border: 0;
            border-top: 1px solid var(--border-subtle);
        }

        [data-testid="stExpander"] {
            background-color: transparent;
            border: none;
            box-shadow: none;
        }

        [data-testid="stExpander"] details {
            border: 1px dashed var(--border-dashed);
            border-radius: 8px;
            background-color: var(--bg-subtle);
        }

        [data-testid="stExpander"] summary {
            padding-left: 10px;
            color: var(--primary-color);
            font-weight: 600;
        }
        </style>
        """,
            unsafe_allow_html=True,
        )

    @staticmethod
    def _converter_data(s):
        if isinstance(s, dt.datetime):
            return s.date()
        if isinstance(s, dt.date):
            return s
        return dt.datetime.strptime(s, "%Y-%m-%d").date()

    @staticmethod
    def _formatar_data_br(d):
        d = PerfilHospedeUI._converter_data(d)
        return d.strftime("%d/%m/%Y")

    @staticmethod
    def _calcular_diarias(checkin, checkout):
        delta = (
            PerfilHospedeUI._converter_data(checkout)
            - PerfilHospedeUI._converter_data(checkin)
        ).days
        return delta if delta > 0 else 0

    @staticmethod
    def _formatar_dinheiro(v):
        try:
            val_str = str(v).replace(',', '.')
            v = float(val_str)
        except Exception:
            v = 0.0
        s = f"{v:,.2f}"
        s = s.replace(",", "@").replace(".", ",").replace("@", ".")
        return f"R$ {s}"

    @staticmethod
    def _calcular_total(reserva):
        base = float(
            reserva.get("valor_diaria", 0)
        ) * PerfilHospedeUI._calcular_diarias(reserva["checkin"], reserva["checkout"])

        total_adicionais = 0.0
        for item in reserva.get("adicionais", []):
            try:
                preco = float(str(item.get("preco", 0)).replace(',', '.'))
                qtd = float(item.get("quantidade", 1))
                total_adicionais += preco * qtd
            except:
                pass

        return round(base + total_adicionais, 2)

if __name__ == "__main__":
    PerfilHospedeUI.main()