import streamlit as st
from graphs.BuildGraph import BuildGraph

VIEWS = {
    "Heatmap Para Visualização de PCD por Hora e Linha": "pcd_hora_linha",
    "Acompanhamento PCD": "pcd",
}

if "pages" not in st.session_state:
    st.session_state.pages = ["Linha 7"]

if "refresh" not in st.session_state:
    st.session_state.refresh = False

num_cols = len(st.session_state.pages) if len(st.session_state.pages) > 0 else 1

if len(st.session_state.pages) < 3: 
    cols_main = st.columns([85, 15])
    if cols_main[1].button("Adicionar Página"):
        nova_pagina = f"Página {len(st.session_state.pages) + 1}"
        st.session_state.pages.append(nova_pagina)
        st.rerun()

with st.container():
    cols = st.columns(num_cols)
    for i, page in enumerate(st.session_state.pages):
        with cols[i]:
            if st.button("Apagar Coluna", key={"bt_col" + str(i)}):
                st.session_state.pages.pop(i)
                st.rerun()
            metro_line = st.selectbox(
                'Escolha uma linha para comparar:', 
                ['Linha 7', 'Linha 10', 'Linha 11', 'Linha 12', 'Linha 13', 'Serviço 710'],
                key={"select_col_" + str(i)}
            )
            if metro_line:
                st.subheader(metro_line)
                st.write(f"Dados da {metro_line}")
                for view_name, view_table in VIEWS.items():
                    BuildGraph.render_graph(view_table=view_table, view_name=view_name, metro_line=metro_line)
