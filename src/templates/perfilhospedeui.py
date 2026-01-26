import streamlit as st
import datetime as dt
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

        usuario_id = st.session_state["usuario_id"]
        hospede = View.hospede_listar_por_usuario(usuario_id)

        if not hospede:
            st.warning("Perfil de hóspede não encontrado.")
            return

        try:
            reservas = View.reservas_listar_hospede(hospede.get_id_hospede())
        except Exception as e:
            st.warning(f"Erro ao carregar reservas: {e}")
            reservas = []

        # Prepara dicionário de produtos para o selectbox
        opcoes_adicionais = {}
        try:
            for item in View.adicional_listar():
                label = f"{item.get_descricao()} ({PerfilHospedeUI._formatar_dinheiro(item.get_valor())})"
                opcoes_adicionais[label] = item
        except Exception:
            pass

        PerfilHospedeUI._aplicar_estilos()

        if not reservas:
            st.info("Nenhuma reserva encontrada.")
            return

        colunas = st.columns(2)
        hoje = dt.date.today()

        for i, reserva in enumerate(reservas):
            with colunas[i % 2]:
                with st.container(border=True):
                    PerfilHospedeUI._renderizar_info_reserva(reserva)
                    
                    # Exibe formulário apenas se a reserva estiver ativa
                    checkout = PerfilHospedeUI._converter_data(reserva.get('checkout'))
                    if checkout >= hoje:
                        PerfilHospedeUI._renderizar_form_adicional(reserva, opcoes_adicionais)

    @staticmethod
    def _renderizar_info_reserva(reserva):
        checkin = PerfilHospedeUI._formatar_data_br(reserva.get('checkin'))
        checkout = PerfilHospedeUI._formatar_data_br(reserva.get('checkout'))
        dias = PerfilHospedeUI._calcular_diarias(reserva.get('checkin'), reserva.get('checkout'))
        
        # Lista de consumos
        itens_html = ""
        for item in reserva.get("adicionais", []):
            qtd = float(item.get("quantidade", 0))
            preco = float(item.get("preco", 0))
            total = qtd * preco
            qtd_fmt = int(qtd) if qtd.is_integer() else qtd
            itens_html += f"<div>- <b>{qtd_fmt}x</b> {item['nome']}: {PerfilHospedeUI._formatar_dinheiro(total)}</div>"

        # Definição de estilos baseados no pagamento
        pago = reserva.get('pago')
        status_txt = "Pago" if pago else "Pendente"
        status_cls = "payment-paid" if pago else "payment-pending"

        html = f"""
        <div style='display:flex;justify-content:space-between;align-items:center'>
            <div>
                <div style='font-weight:700;font-size:16px'>#{reserva.get('id')} — {reserva.get('hospede')}</div>
                <div class='meta'>{reserva.get('tipo_quarto')} • Quarto {reserva.get('numero_quarto')}</div>
            </div>
            <div class='payment {status_cls}'>{status_txt}</div>
        </div>
        <hr class='custom-hr'>
        <div style='display:flex;justify-content:space-between;gap:10px'>
            <div><div class='meta'>Check-in</div><div>{checkin}</div></div>
            <div><div class='meta'>Check-out</div><div>{checkout}</div></div>
            <div><div class='meta'>Diárias</div><div>{dias}</div></div>
            <div>
                <div class='meta'>Total</div>
                <div style='font-weight:700'>{PerfilHospedeUI._formatar_dinheiro(reserva.get('total'))}</div>
            </div>
        </div>
        <div style='margin-top:8px'>
            <div class='meta'>Método Pagamento</div>
            <div>{reserva.get('tipo_pagamento', '-')}</div>
        </div>
        <div style='margin-top:6px; margin-bottom:10px;'>
            <div class='meta'>Consumo</div>
            <div>{itens_html or '<span class="meta" style="font-style:italic">Nenhum item consumido.</span>'}</div>
        </div>
        """
        st.markdown(html, unsafe_allow_html=True)

    @staticmethod
    def _renderizar_form_adicional(reserva, opcoes):
        with st.expander("Adicionar Consumo"):
            if not opcoes:
                st.info("Nenhum item disponível.")
                return

            reserva_id = reserva.get('id')
            col_item, col_qtd = st.columns([3, 1])
            
            with col_item:
                selecao = st.selectbox(
                    "Item",
                    options=list(opcoes.keys()),
                    key=f"sel_{reserva_id}",
                    label_visibility="collapsed"
                )
            
            with col_qtd:
                qtd = st.number_input(
                    "Qtd",
                    min_value=1,
                    value=1,
                    key=f"qtd_{reserva_id}",
                    label_visibility="collapsed"
                )

            item_obj = opcoes[selecao]
            total_previsto = float(item_obj.get_valor()) * qtd

            col_total, col_btn = st.columns([2, 1])
            with col_total:
                st.markdown(
                    f"<div style='margin-top:5px; font-size:14px'>Total: <b>{PerfilHospedeUI._formatar_dinheiro(total_previsto)}</b></div>",
                    unsafe_allow_html=True
                )
            
            with col_btn:
                if st.button("Confirmar", key=f"btn_{reserva_id}", use_container_width=True):
                    try:
                        View.consumo_inserir(
                            reserva_id,
                            item_obj.get_id_adicional(),
                            qtd,
                            dt.datetime.now()
                        )
                        st.success("Salvo!")
                        time.sleep(1)
                        st.rerun()
                    except Exception as e:
                        st.error(f"Erro: {e}")

    @staticmethod
    def _aplicar_estilos():
        st.markdown("""
        <style>
        .meta { font-size: 13px; opacity: 0.7; }
        .payment {
            padding: 4px 10px; border-radius: 999px; font-size: 12px; font-weight: 600;
            border: 1px solid #ccc;
        }
        .payment-paid { background-color: rgba(5, 150, 105, 0.1); color: #059669; border-color: #059669; }
        .payment-pending { background-color: rgba(220, 38, 38, 0.1); color: #dc2626; border-color: #dc2626; }
        hr.custom-hr { margin: 8px 0; border: 0; border-top: 1px solid rgba(128,128,128,0.2); }
        [data-testid="stExpander"] { border: none; box-shadow: none; }
        [data-testid="stExpander"] details {
            border: 1px dashed rgba(128,128,128,0.3); border-radius: 8px; background-color: rgba(128,128,128,0.05);
        }
        </style>
        """, unsafe_allow_html=True)

    @staticmethod
    def _converter_data(s):
        if isinstance(s, dt.datetime): return s.date()
        if isinstance(s, dt.date): return s
        return dt.datetime.strptime(s, "%Y-%m-%d").date()

    @staticmethod
    def _formatar_data_br(d):
        return PerfilHospedeUI._converter_data(d).strftime("%d/%m/%Y")

    @staticmethod
    def _calcular_diarias(checkin, checkout):
        delta = (PerfilHospedeUI._converter_data(checkout) - PerfilHospedeUI._converter_data(checkin)).days
        return max(delta, 0)

    @staticmethod
    def _formatar_dinheiro(v):
        try:
            v = float(str(v).replace(',', '.'))
        except Exception:
            v = 0.0
        return f"R$ {v:,.2f}".replace(",", "@").replace(".", ",").replace("@", ".")

if __name__ == "__main__":
    PerfilHospedeUI.main()