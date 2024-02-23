import sqlite3

conn = sqlite3.connect("contas.db")

cursor = conn.cursor()

dados = [
    ("João de Bezerra", '123.654.987-45', 'Rua Amendoin'),
    ("Rogério da Silva Vieira","236.459.985-78", "Rua mendez de sá"),
    ("Ana Maria de santos", "465.653.987-85", "Rua nada de nada"),
    ("Paula dos Anjos", "123.659.987-89", 'Rua joão de judas'),
    ('Paulo Roger de Andrade', '456.986.985-98', 'Av acima das nivens'),
    ('Sendo de Lima', '123.456.789-96', 'Viela dos sonhos')
]
for dado in dados:
    cursor.execute("INSERT INTO clientes(nome,cpf,endereco) VALUES (?, ?, ?)", dado)
    conn.commit()


print("Dados inseridos dos cliente inserido com sucesso")

AGENCIA = '0001'
dados_contas = [
    ("Conta Corrente", AGENCIA, '00001', 120.23, 1),
    ("Conta Corrente", AGENCIA, '00002', 1200.00, 2),
    ("Conta Corrente", AGENCIA, '00003', 1000.00, 3),
    ("Conta Corrente", AGENCIA, '00004', 85.23, 4),
    ("Conta Corrente", AGENCIA, '00005', 0.65, 5),
    ("Conta Corrente", AGENCIA, '00006', 112000.63, 4),
]
for dado in dados_contas:
    cursor.execute("INSERT INTO contas(tipo, agencia, numero, saldo, id_clientes) VALUES (?, ?, ?, ?, ?)", dado)
    conn.commit()

print("Dados da conta inserido com sucesso")

conn.close()