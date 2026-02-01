import streamlit as st
from views import View
import pandas as pd


class RecepcionistaConsultasUI:
    @staticmethod
    def main():
        st.header("Consulta de Acomodações")
        tab1, tab2 = st.tabs(["Quartos", "Tipos de Quarto"])

        with tab1:
            quartos = View.quarto_listar()
            if quartos:
                df = pd.DataFrame(
                    [
                        {
                            "Número": q.get_numero(),
                            "Bloco": q.get_bloco(),
                            "Tipo ID": q.get_id_quarto_tipo(),
                        }
                        for q in quartos
                    ]
                )
                st.dataframe(df, use_container_width=True, hide_index=True)
            else:
                st.info("Sem quartos cadastrados.")

        with tab2:
            tipos = View.tipoquarto_listar()
            if not tipos:
                st.info("Nenhum tipo de quarto cadastrado.")
                return

            dic_tipos = []
            for t in tipos:
                dic_tipos.append(
                    {
                        "ID": t.get_id_tipoquarto(),
                        "Nome": t.get_nome(),
                        "Descrição": t.get_descricao(),
                        "Capacidade": f"{t.get_capacidade()} pessoa(s)",
                        "Valor Diária": f"R$ {float(t.get_valor_diaria()):.2f}".replace(
                            ".", ","
                        ),
                    }
                )

            df = pd.DataFrame(dic_tipos)
            st.dataframe(df, hide_index=True, use_container_width=True)
