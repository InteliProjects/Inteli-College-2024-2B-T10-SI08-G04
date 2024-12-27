import streamlit as st
from graphs.BuildGraph import BuildGraph

VALIDATION_VIEWS = {
    "Distribuição de Movimentação por Período": "passag_per_tipo_dia",
    "Total de Validações por Dia": "totalValidacoesPerDia",
    "Distribuição por Tipo de Bilhete": "bilh_tipo_dia",
}

DEFAULT_METRO_LINE = "Linha 7"

st.title("Informações Gerais - Validações")
st.markdown(
    """
    Nesta página, você encontrará gráficos detalhados sobre os diferentes tipos de validações relacionadas aos bilhetes utilizados na CPTM.
    """
)

for view_name, view_table in VALIDATION_VIEWS.items():
    st.subheader(view_name)
    try:
        BuildGraph.render_graph(view_table=view_table, view_name=view_name, metro_line=DEFAULT_METRO_LINE)
    except Exception as e:
        st.error(f"Erro ao carregar o gráfico '{view_name}': {str(e)}")