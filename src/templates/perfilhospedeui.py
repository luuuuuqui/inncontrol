import streamlit as st  # pyright: ignore[reportMissingImports]
import datetime as dt
import time
from views import View


class PerfilHospedeUI:
    @staticmethod
    def meus_dados():
        st.header("Meus Dados:")
        usuario_id = st.session_state["usuario_id"]
        usuario = View.usuario_listar_id(usuario_id)

        if not usuario:
            st.error("Dados do usuário não encontrados.")
            return

        hospede = View.hospede_listar_por_usuario(usuario_id)

        col1, col2 = st.columns(2)

        with col1:
            novo_nome = st.text_input("Nome:", value=usuario.get_nome())
            novo_fone = st.text_input("Telefone:", value=usuario.get_fone())

        with col2:
            novo_email = st.text_input("Email:", value=usuario.get_email())
            if hospede:
                novo_endereco = st.text_input("Endereço:", value=hospede.get_endereco())
            else:
                novo_endereco = st.text_input("Endereço:", value="")

        col_salvar, col_senha = st.columns(2)

        with col_salvar:
            if st.button("Salvar Alterações", use_container_width=True, type="primary"):
                if not novo_nome or not novo_email:
                    st.error("Nome e email são obrigatórios.")
                else:
                    try:
                        View.usuario_atualizar(
                            usuario.get_id_usuario(),
                            novo_nome,
                            novo_fone,
                            novo_email,
                            usuario.get_tipo_perfil(),
                            usuario.get_id_perfil(),
                        )

                        if hospede and novo_endereco:
                            View.hospede_atualizar(
                                hospede.get_id_hospede(),
                                usuario.get_id_usuario(),
                                novo_endereco,
                            )
                        elif not hospede and novo_endereco:
                            View.hospede_inserir(
                                usuario.get_id_usuario(), novo_endereco
                            )

                        st.session_state["usuario_nome"] = novo_nome
                        st.success("Dados atualizados com sucesso!")
                        time.sleep(1)
                        st.rerun()
                    except Exception as e:
                        st.error(f"Erro: {e}")

        with col_senha:
            with st.expander("Alterar Senha"):
                senha_atual = st.text_input(
                    "Senha Atual:", type="password", key="senha_atual"
                )
                nova_senha = st.text_input(
                    "Nova Senha:", type="password", key="nova_senha"
                )
                confirmar_senha = st.text_input(
                    "Confirmar Senha:", type="password", key="confirmar_senha"
                )

                if st.button("Alterar Senha", use_container_width=True):
                    if not senha_atual:
                        st.error("Digite a senha atual.")
                    elif not nova_senha:
                        st.error("Digite a nova senha.")
                    elif nova_senha != confirmar_senha:
                        st.error("As senhas não coincidem.")
                    else:
                        try:
                            usuario_autenticado = View.usuario_autenticar(
                                usuario.get_email(), senha_atual
                            )
                            if not usuario_autenticado:
                                st.error("Senha atual incorreta.")
                            else:
                                View.usuario_atualizar_senha(
                                    usuario.get_id_usuario(), nova_senha
                                )
                                st.success("Senha atualizada com sucesso!")
                                time.sleep(1)
                                st.rerun()
                        except Exception as e:
                            st.error(f"Erro: {e}")

    @staticmethod
    def minhas_reservas():
        st.header("Minhas Reservas:")
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

                    checkout = PerfilHospedeUI._converter_data(reserva.get("checkout"))
                    if checkout >= hoje:
                        PerfilHospedeUI._renderizar_form_adicional(
                            reserva, opcoes_adicionais
                        )

    @staticmethod
    def _renderizar_info_reserva(reserva):
        checkin = PerfilHospedeUI._formatar_data_br(reserva.get("checkin"))
        checkout = PerfilHospedeUI._formatar_data_br(reserva.get("checkout"))
        dias = PerfilHospedeUI._calcular_diarias(
            reserva.get("checkin"), reserva.get("checkout")
        )

        adicionais_agrupados = {}
        total_consumo_geral = 0.0

        for item in reserva.get("adicionais", []):
            nome = item.get("nome", "Item Desconhecido")
            qtd = float(item.get("quantidade", 0))
            preco = float(item.get("preco", 0))
            total_item = qtd * preco

            if nome in adicionais_agrupados:
                adicionais_agrupados[nome]["qtd"] += qtd
                adicionais_agrupados[nome]["total"] += total_item
            else:
                adicionais_agrupados[nome] = {"qtd": qtd, "total": total_item}
            total_consumo_geral += total_item

        itens_html = ""
        for nome, dados in adicionais_agrupados.items():
            qtd_fmt = int(dados["qtd"]) if dados["qtd"].is_integer() else dados["qtd"]
            itens_html += f"<div>- <b>{qtd_fmt}x</b> {nome}: {PerfilHospedeUI._formatar_dinheiro(dados['total'])}</div>"

        subtotal_html = ""
        if total_consumo_geral > 0:
            subtotal_html = f"<div style='font-size:13px; opacity:0.8;'>Total em consumos: {PerfilHospedeUI._formatar_dinheiro(total_consumo_geral)}</div>"

        pago = reserva.get("pago")
        status_txt = "Pago" if pago else "Pendente"
        status_cls = "payment-paid" if pago else "payment-pending"

        html = f"""
        <div style='display:flex;justify-content:space-between;align-items:center'>
            <div>
                <div style='font-weight:700;font-size:16px'>#{reserva.get("id")} — {reserva.get("hospede")}</div>
                <div class='meta'>{reserva.get("tipo_quarto")} • Quarto {reserva.get("numero_quarto")}</div>
            </div>
            <div class='payment {status_cls}'>{status_txt}</div>
        </div>
        <hr class='custom-hr'>
        <div style='display:flex;justify-content:space-between;gap:10px'>
            <div><div class='meta'>Check-in</div><div>{checkin}</div></div>
            <div><div class='meta'>Check-out</div><div>{checkout}</div></div>
            <div><div class='meta'>Diárias</div><div>{dias}</div></div>
            <div>
                <div class='meta'>Total Geral</div>
                <div style='font-weight:700'>{PerfilHospedeUI._formatar_dinheiro(reserva.get("total"))}</div>
            </div>
        </div>
        <div style='margin-top:8px'>
            <div class='meta'>Método Pagamento</div>
            <div>{reserva.get("tipo_pagamento", "-")}</div>
        </div>
        <div style='margin-top:6px; margin-bottom:10px;'>
            <div style="display:flex; justify-content:space-between; align-items:flex-end;">
                <div class='meta'>Consumo</div>
                {subtotal_html}
            </div>
            <div style="margin-top:2px;">{itens_html or '<span class="meta" style="font-style:italic">Nenhum item consumido.</span>'}</div>
        </div>
        """
        st.markdown(html, unsafe_allow_html=True)

    @staticmethod
    def _renderizar_form_adicional(reserva, opcoes):
        with st.expander("Adicionar Consumo"):
            if not opcoes:
                st.info("Nenhum item disponível.")
                return

            reserva_id = reserva.get("id")
            col_item, col_qtd = st.columns([3, 1])

            with col_item:
                selecao = st.selectbox(
                    "Item",
                    options=list(opcoes.keys()),
                    key=f"sel_{reserva_id}",
                    label_visibility="collapsed",
                )

            with col_qtd:
                qtd = st.number_input(
                    "Qtd",
                    min_value=1,
                    step=1,  # Adicionado step para habilitar os botões + e -
                    value=1,
                    key=f"qtd_{reserva_id}",
                    label_visibility="collapsed",
                )

            item_obj = opcoes[selecao]
            total_previsto = float(item_obj.get_valor()) * qtd

            col_total, col_btn = st.columns([2, 1])
            with col_total:
                st.markdown(
                    f"<div style='margin-top:5px; font-size:14px'>Total do pedido: <b>{PerfilHospedeUI._formatar_dinheiro(total_previsto)}</b></div>",
                    unsafe_allow_html=True,
                )

            with col_btn:
                if st.button(
                    "Confirmar", key=f"btn_{reserva_id}", use_container_width=True
                ):
                    try:
                        View.consumo_inserir(
                            reserva_id,
                            item_obj.get_id_adicional(),
                            qtd,
                            dt.datetime.now(),
                        )
                        st.success("Salvo!")
                        time.sleep(1)
                        st.rerun()
                    except Exception as e:
                        st.error(f"Erro: {e}")

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
        return PerfilHospedeUI._converter_data(d).strftime("%d/%m/%Y")

    @staticmethod
    def _calcular_diarias(checkin, checkout):
        delta = (
            PerfilHospedeUI._converter_data(checkout)
            - PerfilHospedeUI._converter_data(checkin)
        ).days
        return max(delta, 0)

    @staticmethod
    def _formatar_dinheiro(v):
        try:
            v = float(str(v).replace(",", "."))
        except Exception:
            v = 0.0
        return f"R$ {v:,.2f}".replace(",", "@").replace(".", ",").replace("@", ".")


