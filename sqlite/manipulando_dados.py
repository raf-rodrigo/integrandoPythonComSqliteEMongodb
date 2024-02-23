import sqlite3
from pprint import pprint

conn = sqlite3.connect("contas.db")

cursor = conn.cursor()

# iNSERIR NOVO REGISTRO NA TABELA
cursor.execute("INSERT INTO clientes(nome, cpf, endereco) VALUES (?,?,?)",
               ("Paula Cristina", "236.541.965-65", 'Rua Cristal'))

cursor.execute("INSERT INTO contas(tipo, agencia, numero, saldo, id_clientes) VALUES (?,?,?,?,?)",
               ("Conta Corrente", "0001", "00007", 256.69, 7))
conn.commit()
print("Dados de clientes inseridos com sucesso")
print("Dados da conta inseridos com sucesso")


# ATUALIZAR DADOS DE UMA TABELA
cursor.execute("UPDATE clientes SET endereco = ? where id = ?", ("Rua Santa Crista", 2))
cursor.execute("UPDATE contas SET saldo = ? where id_clientes = ?", (152.00, 6))

print("Endereço atualizado com sucesso")
print("Saldo atualizado com sucesso")

# SELECIONAR TODOS OS DADOS DE UMA TABELA
print("Selecionando todos os clientes")
cursor.execute("SELECT * FROM clientes")
clientes = cursor.fetchall()
for cliente in clientes:
    print(cliente)

print("Selecionado todas as contas")
cursor.execute("SELECT * FROM contas")
contas = cursor.fetchall()
for conta in contas:
    print(conta)

# EXECUTANDO JUNÇÃO ENTRE AS TABELAS CONTAS E CLIENTES
print("Todas as contas")
cursor.execute("""
            SELECT clientes.nome, clientes.cpf, contas.numero, contas.saldo 
            FROM clientes 
            INNER JOIN contas ON clientes.id = contas.id_clientes
               """)
results = cursor.fetchall()
for result in results:
    pprint(result)


print("Conta específica")
id = 3
cursor.execute("""
            SELECT clientes.nome, clientes.cpf, contas.numero, contas.saldo 
            FROM clientes 
            INNER JOIN contas ON clientes.id = contas.id_clientes 
            WHERE clientes.id = ? 
           """, (id,))

result = cursor.fetchall()
print(f"Resulta da conta com id = {id}")
print(result)


# EXCLUIR O DADOS DE UMA TABELA
id = 7
print(f"Excluindo com conta com o id = {id}")
conn.execute("BEGIN TRANSACTION")
# excluir as contas associadas ao cliente
cursor.execute("DELETE FROM contas WHERE id_clientes = ?", (id,))
# excluir o cliente
cursor.execute("DELETE FROM clientes WHERE id = ?", (id,))
conn.commit()
print(f"Cliente e conta com id = {id}, excluida com sucesso")
conn.close()