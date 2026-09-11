import streamlit as st

dashboard = st.Page(
    "grafico_geral.py",
    title="📊 Painel de Gestão",
    default=True
)
cadastro = st.Page(
    "pages/app.py",
    title="➕ Registrar Ideia",
)
ideias = st.Page(
    "pages/ideias_cadastradas.py",
    title="📋 Gestão de Ideias",
)

pagina = st.navigation([dashboard, cadastro, ideias])

pagina.run()

st.sidebar.image(image = 'https://telebitbrasil.com.br/wp-content/uploads/2025/07/logo-150.png')