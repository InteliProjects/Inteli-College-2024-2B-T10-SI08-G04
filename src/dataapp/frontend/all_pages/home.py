import streamlit as st

# Título e descrição
st.markdown(
    """
    <div style="padding: 20px; border-radius: 10px; background-color: rgba(30, 31, 38, 0.97);">
        <h1>Bem-vindo ao DataApp - Visualização de Dados da CPTM</h1>
        <p>Este aplicativo foi desenvolvido para visualização e análise dos dados relacionados às operações da CPTM. 
        As visualizações são organizadas por linha e incluem gráficos e tabelas baseados nas views disponíveis no banco de dados.</p>
        <h3>Como navegar:</h3>
        <ul>
            <li>Use o <strong>menu na lateral</strong> para selecionar a página correspondente à linha que deseja visualizar.</li>
            <li>Cada linha apresenta os dados de diferentes views disponíveis no sistema.</li>
            <li>Os gráficos e tabelas são atualizados automaticamente com base nos dados do banco ClickHouse.</li>
        </ul>
        <h3>Features:</h3>
        <ul>
            <li><strong>Visualização de Dados Operacionais:</strong> Dados como movimentação de passageiros, intervalos de trens, validações por dia, entre outros.</li>
            <li><strong>Análises Gráficas:</strong> Gráficos interativos para entender padrões e insights.</li>
            <li><strong>Dados Atualizados:</strong> Conexão direta com o banco de dados ClickHouse.</li>
        </ul>
        <hr>
        <div style="text-align: center; font-size: 16px; margin-top: 40px; margin-bottom: 40px;">
        Desenvolvido para a <a href="https://www.cptm.sp.gov.br/" target="_blank" style="color: #fff; text-decoration: underline;">CPTM</a>.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Links úteis
st.markdown(
    """
    
    """
)

# criar background da página
st.markdown(
    """
    <style>
    body {
        background-color: #eaeaea;
        opacity: 1;
        background: url('https://res.cloudinary.com/dhzeiuxse/image/upload/v1733774288/cptmfundo_bmbvdr.png') no-repeat center center fixed;
        background-size: cover;
    }
    .st-emotion-cache-13k62yr {
        background: transparent;
    }
    </style>
    """,
    unsafe_allow_html=True,
)