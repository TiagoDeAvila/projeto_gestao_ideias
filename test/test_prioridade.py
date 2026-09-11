import sqlite3


def test_banco():
    conexao = sqlite3.connect(":memory:")
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE ideias (
            id INTEGER PRIMARY KEY,
            titulo TEXT,
            status TEXT
        )
    """)

    cursor.execute("""
        INSERT INTO ideias (titulo, status)
        VALUES (?, ?)
    """, ("Ideia teste", "Recebida"))

    cursor.execute("SELECT * FROM ideias")
    ideia = cursor.fetchone()

    assert ideia[1] == "Ideia teste"
    assert ideia[2] == "Recebida"