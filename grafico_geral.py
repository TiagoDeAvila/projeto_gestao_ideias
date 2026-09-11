import streamlit as st
import sqlite3
import pandas as pd
import altair as alt
st.set_page_config(layout="wide")
st.markdown("""
<style>

/* Cards das métricas */
[data-testid="stMetric"] {
    background-color: #1E2530;
    border: 1px solid #303846;
    padding: 18px;
    border-radius: 12px;
}

/* Número da métrica */
[data-testid="stMetricValue"] {
    font-size: 28px;
    font-weight: 700;
}

/* Nome da métrica */
[data-testid="stMetricLabel"] {
    font-size: 14px;
}

/* Títulos */
h1, h2, h3 {
    font-weight: 700;
}

/* Linha divisória */
hr {
    margin-top: 25px;
    margin-bottom: 25px;
}

</style>
""", unsafe_allow_html=True) 


st.title("📊 Painel de Gestão de Ideias")
st.caption("Acompanhamento dos principais indicadores do processo de inovação.")


conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()
cursor.execute(""" 
    SELECT COUNT(*)
    FROM ideias_registradas """)
total = cursor.fetchone()[0]

cursor.execute("""
    SELECT status, COUNT(*)
    FROM ideias_registradas
    GROUP BY status
""")
dados_status = cursor.fetchall()

cursor.execute("""
    SELECT area, COUNT(*)
    FROM ideias_registradas
    GROUP BY area
""")

dados_area = cursor.fetchall()

contagem = dict(dados_status)
recebidas = contagem.get("Recebida", 0)
em_analise = contagem.get("Em análise", 0)
aprovadas = contagem.get("Aprovada", 0)
reprovadas = contagem.get("Reprovada", 0)

st.subheader("📌 Indicadores Gerais")
st.caption("Resumo consolidado das ideias registradas na plataforma.")

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("📋Total",total)
col2.metric("📥Recebidas", recebidas)
col3.metric("🔎Em análise", em_analise)
col4.metric("✅Aprovadas", aprovadas)
col5.metric("❌Reprovadas", reprovadas)

if total > 0:
    taxa = (aprovadas / total) * 100
else:
    taxa = 0
st.text(f"Taxa de aceitação: {taxa:.0f}%") 

st.divider()

st.subheader("📊 Distribuição por Área")

df_status = pd.DataFrame(
    dados_status,
    columns=["Status", "Quantidade"]
)
status_completos = ["Recebida", "Em análise", "Aprovada", "Reprovada"]


contagem_area = dict(dados_area)

TI = contagem_area.get("TI", 0)
RH = contagem_area.get("RH", 0)
operacoes = contagem_area.get("Operações", 0)
vendas = contagem_area.get("Vendas", 0)

col1, col2, col3, col4, = st.columns(4)

col1.metric("💻TI", TI)
col2.metric("👥RH", RH)
col3.metric("⚙️Operações", operacoes)
col4.metric("📈Vendas", vendas)

df_area = pd.DataFrame(
    dados_area,
    columns=["Area", "Quantidade"]
)
df_status = (
    df_status.set_index("Status")
    .reindex(status_completos, fill_value=0)
    .reset_index()
)
grafico_status = alt.Chart(df_status).mark_bar().encode(
    x=alt.X(
        "Status:N",
        title="Status",
        axis=alt.Axis(labelAngle=0)
    ),
    y=alt.Y(
        "Quantidade:Q",
        title="Quantidade"
    ),
    tooltip=[
        alt.Tooltip("Status:N", title="Status"),
        alt.Tooltip("Quantidade:Q", title="Quantidade")
    ]
).properties(
    height=500
)

base_area = alt.Chart(df_area).transform_joinaggregate(
    Total="sum(Quantidade)"
).transform_calculate(
    Porcentagem="datum.Quantidade / datum.Total"
)
rosca_area = base_area.mark_arc(
    innerRadius=90,
    outerRadius=180
).encode(
    theta=alt.Theta("Quantidade:Q"),
    color=alt.Color(
        "Area:N",
        legend=alt.Legend(title="Área")
    ),
    tooltip=[
        alt.Tooltip("Area:N", title="Área"),
        alt.Tooltip("Quantidade:Q", title="Quantidade"),
        alt.Tooltip("Porcentagem:Q", title="Porcentagem", format=".1%")
    ]
)
texto_area = base_area.mark_text(
    radius=135,
    size=14,
    fontWeight="bold"
).encode(
    
    text=alt.Text("Porcentagem:Q", format=".1%")
)
grafico_area = rosca_area.properties(
    width=500,
    height=500
)

col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Distribuição por Status")
    st.altair_chart(grafico_status, use_container_width=True)

with col2:
    st.subheader("🏢 Distribuição por Área")
    st.altair_chart(grafico_area, use_container_width=True)