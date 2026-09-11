import streamlit as st 
import sqlite3
from datetime import datetime
st.set_page_config(page_title="Sistema de Gestão de Ideias | Telebit",page_icon="💡",layout="wide")
conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS ideias_registradas(           
               id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,       
               titulo TEXT NOT NULL,
               descriçao TEXT NOT NULL,
               responsavel TEXT NOT NULL,
               area TEXT NOT NULL,
               impacto INTEGER NOT NULL,
               urgencia INTEGER NOT NULL,
               esforço INTEGER NOT NULL,
               prioridade INTEGER NOT NULL,
               horario TEXT NOT NULL,
               status TEXT NOT NULL
               )
               """)

conexao.commit()

def cadastro():
    cursor.execute("""INSERT INTO ideias_registradas
            (titulo,descriçao,area,responsavel,impacto,urgencia,esforço,prioridade,horario,status) VALUES
            (?,?,?,?,?,?,?,?,?,?)""",(titulo,descriçao,area,responsavel,impacto,urgencia,esforco,prioridade,horario,status))
    conexao.commit()

colunas = st.columns([5, 1])
with colunas[1]:
    st.image(
    image='https://telebitbrasil.com.br/wp-content/uploads/2025/07/logo-150.png',
    width=300
)
def escolhas():
    return list(range(1,6))

st.title("💡 Registro de Nova Ideia")
st.caption("Cadastre uma nova proposta para avaliação e acompanhamento.")
st.subheader("📝 Informações da Ideia")

titulo = st.text_input("Titulo da ideia")
descriçao = st.text_area("Descrição e Justificativa da Ideia")
col1, col2 = st.columns(2)

with col1:
    responsavel = st.text_input("Responsável")

with col2:
    area = st.selectbox(
        "Área Solicitante",
        ["Selecione uma Área", "TI", "RH", "Operações", "Vendas"]
    )

st.subheader("📊Critérios de avaliação")
st.caption("Avalie a ideia considerando os critérios abaixo.")


col1, col2, col3 = st.columns(3)

with col1:
    impacto = st.selectbox(
        "Impacto no negócio",
        ["Selecione uma opção", 1, 2, 3, 4, 5]
    )

with col2:
    urgencia = st.selectbox(
        "Urgência",
        ["Selecione uma opção", 1, 2, 3, 4, 5]
    )

with col3:
    esforco = st.selectbox(
        "Esforço de Implementação",
        ["Selecione uma opção", 1, 2, 3, 4, 5]
    )
  
cadastrar_ideia = st.button("Registrar Ideia",use_container_width=True)

def invalida():
    st.error("Por favor, preencha todos os campos obrigatórios")
if cadastrar_ideia:
    if (
    not titulo
    or not descriçao
    or not responsavel
    or area == "Selecione uma Área"
    or impacto == "Selecione uma opção"
    or urgencia == "Selecione uma opção"
    or esforco == "Selecione uma opção"
):
        invalida()
    else:
            horario = datetime.today().strftime("%d/%m/%Y %H:%M")
            status = "Recebida"
            prioridade = ((impacto*2)+(urgencia*2) - esforco)
            cadastro()
            st.success("Ideia cadastrada com sucesso")