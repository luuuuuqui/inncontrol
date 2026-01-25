import streamlit as st
import datetime as dt
from datetime import date
from views import View


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

        PerfilHospedeUI._aplicar_estilos()  # aplica css

        colunas = st.columns(2)
        if not reservas:
            st.info("Nenhuma reserva encontrada.")

        for i, r in enumerate(reservas):
            coluna = colunas[i % 2]
            with coluna:
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

                html_card = f"""
                <div class='res-card'>
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
                    <div style='margin-top:6px'>
                        <div class='meta'>Adicionais</div>
                        <div>{adicionais_html or '<span class="meta">Essa reserva não possui adicionais.</span>'}</div>
                    </div>
                </div>
                """
                st.markdown(html_card, unsafe_allow_html=True)

    # métodos auxiliares e de formatação
    @staticmethod
    def _aplicar_estilos():
        st.markdown(
            """
        <style>
        .res-card {
            background-color: var(--secondary-background-color);
            border: 1px solid rgba(128, 128, 128, 0.2);
            border-radius: 12px;
            padding: 14px;
            margin: 8px 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .meta {
            font-size: 13px;
            color: var(--text-color);
            opacity: 0.7;
        }
        .payment {
            display: inline-block;
            padding: 6px 10px;
            border-radius: 999px;
            font-weight: 600;
        }
        .payment-paid {
            background-color: rgba(5, 150, 105, 0.15);
            color: #059669;
            border: 1px solid #059669;
        }
        .payment-pending {
            background-color: rgba(220, 38, 38, 0.15);
            color: #dc2626;
            border: 1px solid #dc2626;
        }
        hr.custom-hr {
            margin: 8px 0;
            border: 0;
            border-top: 1px solid rgba(128, 128, 128, 0.2);
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
        return (
            PerfilHospedeUI._converter_data(checkout)
            - PerfilHospedeUI._converter_data(checkin)
        ).days

    @staticmethod
    def _formatar_dinheiro(v):
        try:
            v = float(v)
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
            preco = float(item.get("preco", 0))
            qtd = float(item.get("quantidade", 1))
            total_adicionais += preco * qtd

        return round(base + total_adicionais, 2)


if __name__ == "__main__":
    PerfilHospedeUI.main()
