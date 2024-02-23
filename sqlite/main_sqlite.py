import sqlite3

conn = sqlite3.connect("contas.db")

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        nome TEXT NOT NULL,
        cpf VARCHAR(15) NOT NULL UNIQUE,
        endereco TEXT NOT NULL,
        abertura TIMESTAMP default CURRENT_TIMESTAMP
    );
""")

cursor.execute("""
    create table if not exists contas(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        tipo varchar(15) NOT NULL,
        agencia integer NOT NULL,
        numero integer NOT NULL,
        saldo decimal NOT NULL,
        id_clientes integer NOT NULL,
        abertura TIMESTAMP default CURRENT_TIMESTAMP,
        FOREIGN KEY (id_clientes) REFERENCES clientes(id)
    );
""")

conn.close()
print("Tabelas criadas com sucesso no banco contas")