import streamlit as st
from config.Settings import UseSettings
from config.Auth import Auth

settings = UseSettings.get_settings()

st.set_page_config(
    page_title="Visualização de Dados - CPTM",
    page_icon="🚉",
    layout="wide",
    initial_sidebar_state="collapsed"
)

home = st.Page("./all_pages/home.py", title="Como usar", icon=":material/home:")
infographic = st.Page("./all_pages/infographic.py", title="Infográfico", icon=":material/image:")
general = st.Page("./all_pages/general.py", title="Informações Gerais", icon=":material/settings_applications:")
compare_lines = st.Page("./all_pages/compare_lines.py", title="Comparar Linhas", icon=":material/transform:")

pages = [home, infographic, general, compare_lines]
Auth.auth_page(pages=pages)

with st.sidebar:
    st.markdown("---")
    st.markdown(
        """
        <div style="text-align: center; margin-top: auto;">
            <img src="https://res.cloudinary.com/dhzeiuxse/image/upload/v1733775790/Cptm_icon.svg_xre2pl.png" alt="Logo CPTM" style="width: 80%; max-width: 150px;">
        </div>
        """,
        unsafe_allow_html=True,
    )
