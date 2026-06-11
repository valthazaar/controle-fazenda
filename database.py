import sqlite3


def conectar():
    return sqlite3.connect("fazenda.db")


def criar_tabelas():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS animais(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        brinco TEXT UNIQUE NOT NULL,
        raca TEXT NOT NULL,
        idade INTEGER NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pesagens(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        animal_id INTEGER NOT NULL,
        peso REAL NOT NULL,
        data_pesagem TEXT NOT NULL,
        FOREIGN KEY(animal_id) REFERENCES animais(id)
    )
    """)

    conn.commit()
    conn.close()