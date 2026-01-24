import streamlit as st
import datetime as dt
from datetime import date

JSON_TESTE = [
    {
        "id": 101,
        "hospede": "João da Silva",
        "tipo_quarto": "Suíte Casal",
        "numero_quarto": "12B",
        "checkin": "2026-02-15",
        "checkout": "2026-02-19",
        "valor_diaria": 150.00,
        "pago": True,
        "tipo_pagamento": "Cartão de Crédito",
        "adicionais": [
            {"nome": "Água mineral (frigo)", "preco": 5.5, "quantidade": 2},
            {"nome": "KitKat", "preco": 8.0, "quantidade": 1},
        ],
    },
    {
        "id": 102,
        "hospede": "Maria Pereira",
        "tipo_quarto": "Quarto Simples",
        "numero_quarto": "05",
        "checkin": "2026-03-01",
        "checkout": "2026-03-03",
        "valor_diaria": 80.0,
        "pago": False,
        "tipo_pagamento": "Dinheiro",
        "adicionais": [],
    },
    {
        "id": 103,
        "hospede": "Bruno Rocha",
        "tipo_quarto": "Family",
        "numero_quarto": "21",
        "checkin": "2026-01-10",
        "checkout": "2026-01-13",
        "valor_diaria": 220.0,
        "pago": True,
        "tipo_pagamento": "Cartão de Débito",
        "adicionais": [{"nome": "Café da manhã", "preco": 30.0, "quantidade": 3}],
    },
]


class PerfilHospedeUI:
    @staticmethod
    def main():
        st.set_page_config(page_title="Minhas Reservas", layout="wide")

        st.markdown("## Suas Reservas")

        PerfilHospedeUI.listar()

    @staticmethod
    def listar():
        try:
            reservas = JSON_TESTE
        except Exception as e:
            st.error(f"Erro ao carregar reservas: {e}")
            return

        texto_busca = st.sidebar.text_input("Buscar por Nome, Quarto ou ID")
        mapa_status = {"Todos": "todos", "Pagos": "pagos", "Não Pagos": "não pagos"}
        rotulo_status = st.sidebar.selectbox(
            "Status do Pagamento", list(mapa_status.keys())
        )
        status = mapa_status[rotulo_status]

        intervalo_datas = st.sidebar.date_input(
            "Período (Check-in)", [date(2025, 1, 1), date(2027, 12, 31)]
        )
        if isinstance(intervalo_datas, tuple) and len(intervalo_datas) == 2:
            inicio, fim = intervalo_datas
        else:
            inicio, fim = (
                (intervalo_datas, intervalo_datas)
                if isinstance(intervalo_datas, date)
                else (date(2025, 1, 1), date(2027, 12, 31))
            )

        mapa_ordenacao = {
            "Check-in": "checkin",
            "Check-out": "checkout",
            "ID": "id",
            "Hóspede": "hospede",
        }
        rotulo_ordenacao = st.sidebar.selectbox(
            "Ordenar por", list(mapa_ordenacao.keys())
        )
        ordenar_por = mapa_ordenacao[rotulo_ordenacao]

        for reserva in reservas:
            reserva.setdefault("adicionais", [])

        reservas_filtradas = []
        for reserva in reservas:
            try:
                data_checkin_temp = (
                    PerfilHospedeUI._converter_data(reserva["checkin"])
                    if reserva.get("checkin")
                    else None
                )
            except Exception:
                data_checkin_temp = None

            termo_busca = texto_busca.lower()
            if termo_busca:
                if (
                    termo_busca not in str(reserva.get("hospede", "")).lower()
                    and termo_busca not in str(reserva.get("numero_quarto", "")).lower()
                    and termo_busca not in str(reserva.get("id", "")).lower()
                ):
                    continue

            if status == "pagos" and not reserva.get("pago", False):
                continue
            if status == "não pagos" and reserva.get("pago", False):
                continue

            if data_checkin_temp and (
                data_checkin_temp < inicio or data_checkin_temp > fim
            ):
                continue

            reservas_filtradas.append(reserva)

        try:
            reservas_filtradas = sorted(
                reservas_filtradas,
                key=lambda x: (
                    x.get(ordenar_por) if ordenar_por in x else x.get(ordenar_por, "")
                ),
            )
        except Exception:
            pass

        PerfilHospedeUI._aplicar_estilos()

        colunas = st.columns(2)
        if not reservas_filtradas:
            st.info("Nenhuma reserva encontrada com os filtros atuais.")

        for i, reserva in enumerate(reservas_filtradas):
            coluna = colunas[i % 2]
            with coluna:
                qtd_diarias = (
                    PerfilHospedeUI._calcular_diarias(
                        reserva["checkin"], reserva["checkout"]
                    )
                    if reserva.get("checkin") and reserva.get("checkout")
                    else 0
                )
                total = PerfilHospedeUI._calcular_total(reserva)
                classe_pagamento = "pago-true" if reserva.get("pago") else "pago-false"

                # Construção do HTML dos adicionais considerando quantidade
                adicionais_html = ""
                for item in reserva.get("adicionais", []):
                    # Se não houver quantidade definida, assume 1 para compatibilidade
                    qtd = float(item.get("quantidade", 1))
                    preco_unit = float(item.get("preco", 0))
                    total_item = qtd * preco_unit

                    # Formata 2.0 como 2, mas mantém 2.5 como 2.5
                    qtd_display = int(qtd) if qtd.is_integer() else qtd

                    adicionais_html += f"<div>- <b>{qtd_display}x</b> {item['nome']}: {PerfilHospedeUI._formatar_dinheiro(total_item)}</div>"

                html_card = f"""
                <div class='res-card'>
                    <div style='display:flex;justify-content:space-between;align-items:center'>
                        <div>
                            <div style='font-weight:700;font-size:16px; color:var(--text-color)'>Reserva #{reserva.get('id')} — {reserva.get('hospede')}</div>
                            <div class='meta'>{reserva.get('tipo_quarto')} • Quarto {reserva.get('numero_quarto')}</div>
                        </div>
                        <div>
                            <div class='pago {classe_pagamento}'>{'Pago' if reserva.get('pago') else 'Não Pago'}</div>
                        </div>
                    </div>
                    <hr class='custom-hr'>
                    <div style='display:flex;justify-content:space-between;gap:12px'>
                        <div>
                            <div class='meta'>Check-in</div>
                            <div>{PerfilHospedeUI._formatar_data_br(reserva.get('checkin'))}</div>
                        </div>
                        <div>
                            <div class='meta'>Check-out</div>
                            <div>{PerfilHospedeUI._formatar_data_br(reserva.get('checkout'))}</div>
                        </div>
                        <div>
                            <div class='meta'>Diárias</div>
                            <div>{qtd_diarias}</div>
                        </div>
                        <div>
                            <div class='meta'>Valor Total</div>
                            <div style='font-weight:700'>{PerfilHospedeUI._formatar_dinheiro(total)}</div>
                        </div>
                    </div>
                    <div style='margin-top:8px'>
                        <div class='meta'>Pagamento</div>
                        <div>{reserva.get('tipo_pagamento', '-')}</div>
                    </div>
                    <div style='margin-top:6px'>
                        <div class='meta'>Adicionais</div>
                        <div>{adicionais_html or '<span class="meta">Nenhum</span>'}</div>
                    </div>
                </div>
                """
                st.markdown(html_card, unsafe_allow_html=True)

        st.sidebar.markdown("---")
        st.sidebar.markdown(
            "**Dica:** Agora este app detecta automaticamente se seu Streamlit está em Light ou Dark Mode."
        )

    # --- Métodos Auxiliares e de Formatação ---

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
        .pago {
            display: inline-block;
            padding: 6px 10px;
            border-radius: 999px;
            font-weight: 600;
        }
        .pago-true {
            background-color: rgba(5, 150, 105, 0.15);
            color: #059669;
            border: 1px solid #059669;
        }
        .pago-false {
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
        s = s.replace(",", "X").replace(".", ",").replace("X", ".")
        return f"R$ {s}"

    @staticmethod
    def _calcular_total(reserva):
        base = float(
            reserva.get("valor_diaria", 0)
        ) * PerfilHospedeUI._calcular_diarias(reserva["checkin"], reserva["checkout"])

        # SOMA DOS ADICIONAIS COM QUANTIDADE
        total_adicionais = 0.0
        for item in reserva.get("adicionais", []):
            preco = float(item.get("preco", 0))
            qtd = float(item.get("quantidade", 1))  # Default 1 se não existir
            total_adicionais += preco * qtd

        return round(base + total_adicionais, 2)


if __name__ == "__main__":
    PerfilHospedeUI.main()
