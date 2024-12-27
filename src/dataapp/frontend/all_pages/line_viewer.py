import streamlit as st
from graphs.BuildGraph import BuildGraph
from config.constants import VIEWS, LINES

metro_line = st.selectbox(
    'Escolha uma linha para comparar:', 
    LINES,
    key={"select_col_" + str("line_viewer")}
)
if metro_line:
    st.subheader(metro_line)
    st.write(f"Dados da {metro_line}")
    for view_name, view_table in VIEWS.items():
        BuildGraph.render_graph(view_table=view_table, view_name=view_name, metro_line=metro_line)
