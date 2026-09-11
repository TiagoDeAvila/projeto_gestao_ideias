import streamlit as st
import sqlite3
st.title("📋 Gestão de Ideias")
st.caption("Consulte, acompanhe e gerencie as ideias registradas na plataforma.")
st.subheader("📂 Repositório de Ideias")
st.set_page_config(layout="wide")
conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

def atualizar_status():
    cursor.execute(
    "UPDATE ideias_registradas SET status = ? WHERE id = ?",
                    (novo_status, id_ideia))
    conexao.commit()
    st.rerun()

def exluir():
    cursor.execute(
                "DELETE FROM ideias_registradas WHERE id = ?",
                (id_ideia,)
            )

cursor.execute(""" SELECT id,titulo,area,responsavel,prioridade,horario,status,descriçao FROM 
 ideias_registradas ORDER BY prioridade DESC""")
ideias = cursor.fetchall()

col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11= st.columns(
    [1, 2, 2, 2, 2, 2, 2, 1, 1, 2 ,1]
)

col1.write("ID")
col2.write("Título")
col3.write("Área")
col4.write("Responsável")
col5.write("Prioridade")
col6.write("Data de registro")
col8.write("Detalhes")
col10.write("Status")

with st.popover("Filtro de pesquisas"):
    filtro_status = st.selectbox(
    "Status",
    ["Todos", "Em análise", "Aprovada", "Reprovada"])
    filtro_area = st.selectbox(
        "Área",
        ["Todos", "TI","Vendas","Operações","RH"]
    )

pesquisa = st.text_input("Buscar ideias").lower()
if "editar_id" not in st.session_state:
    st.session_state.editar_id = None

for ideia in ideias:
    id_ideia = ideia[0]
    titulo = ideia[1]
    area = ideia[2]
    responsavel = ideia[3]
    prioridade = ideia[4]
    horario = ideia[5]
    status = ideia[6]
    descriçao = ideia[7]
    
    dados = (titulo + responsavel + horario + status).lower()
    if pesquisa not in dados:
        continue
    if filtro_status != "Todos" and status != filtro_status:
        continue
    if filtro_area != "Todos" and area !=filtro_area:
        continue

    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11= st.columns(
    [1, 2, 2, 2, 2, 2, 2, 1, 1, 2 ,1]
)

    col1.write(id_ideia)
    col2.write(titulo)
    col4.write(area)
    col5.write(responsavel)
    col6.write(prioridade)
    col7.write(horario)
    with col8.popover("👁️ Ver"):
        st.markdown("**Descrição e Justificativa**")
        st.write(descriçao)
    if col9.button("Editar", key=f"editar_{id_ideia}"):
        st.session_state.editar_id = id_ideia
    opçoes_status = ("Recebida","Em análise","Reprovada","Aprovada")

    novo_status = col10.selectbox("status",opçoes_status,
                                 index=opçoes_status.index(status),
                 key=f"numeraçao_status{id_ideia}",
                 label_visibility="collapsed")

    if novo_status != status:
        atualizar_status()


    if st.session_state.editar_id == id_ideia:

        novo_titulo = st.text_input(
            "Título",
            value=titulo,
            key=f"titulo_{id_ideia}"
        )

        novo_responsavel = st.text_input(
            "Responsável",
            value=responsavel,
            key=f"responsavel_{id_ideia}"
        )

        if st.button("Salvar alterações", key=f"salvar_{id_ideia}"):
            if (
                not novo_titulo
                or not novo_responsavel
            ):
                st.error ("Por favor, preencha todos os campos obrigatórios")
            else:
                cursor.execute("""
                    UPDATE ideias_registradas
                    SET titulo = ?, responsavel = ? 
                    WHERE id = ?
                """, (novo_titulo, novo_responsavel, id_ideia))

                conexao.commit()

                st.session_state.editar_id = None
                st.rerun()
            
    if col11.button("Excluir", key=f"excluir_{id_ideia}"):
            exluir()

            conexao.commit()
            st.rerun()