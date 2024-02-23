import pymongo as pyM
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://rafrodrigo:YNWAq6EvhXn52UHZ@cluster0.nt3vlbe.mongodb.net/?retryWrites=true&w=majority"
client = pyM.MongoClient(uri)
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


db = client.clients
collection = db.banco

AGENCIA = "0001"


posts = [{
        "nome":"Aluisio Silva",
        "cpf":"123.456.789-32",
        "endereco":{
            "logradouro":"Rua Azulão",
            "numero":1123,
            "complemento":"Casa 2",
            "bairro":"Nascimento",
            "cidade":"São Paulo",
            "uf":"SP"
        },
        "agencia":AGENCIA,
        "numeroConta":"00001",
        "tipoConta":"Corrente",
        "saldo":300.00
    },
    {
        "nome":"João de Bezzerra Santos",
        "cpf":"987.654.321.-98",
        "endereco":{
            "logradouro":"Rua Sobe e Desce",
            "numero":23,
            "bairro":"Nova Luz",
            "cidade":"São Bernado",
            "uf":"SP"
        },
        "agencia":AGENCIA,
        "numeroConta":"00002",
        "tipoConta":"Corrente",
        "saldo":1000.00
    },
    {
        "nome": "Ana Maria de Andrade",
        "cpf": "159.753.654-23",
        "endereco": {
            "logradouro": "Avenida Ana Paula de Lima",
            "numero": 12356,
            "complemento":"apt 32",
            "bairro": "Cidade Nova",
            "cidade": "São Paulo",
            "uf": "SP"
        },
        "agencia": AGENCIA,
        "numeroConta": "00003",
        "tipoConta": "Corrente",
        "saldo": 150.00
    },
    {
        "nome": "Tania de Lima Vassoura",
        "cpf": "125.156.157-56",
        "endereco": {
            "logradouro": "Rua Lagoa da Enseada",
            "numero": "sn",
            "bairro": "Aparecida",
            "cidade": "São Caetano",
            "uf": "SP"
        },
        "agencia": AGENCIA,
        "numeroConta": "00004",
        "tipoConta": "Corrente",
        "saldo": 11000.00
    },
    {
        "nome": "Talis da Gama",
        "cpf": "251.259.258-36",
        "endereco": {
            "logradouro": "Rua Não Proibida",
            "numero": 84,
            "bairro": "Kilombo",
            "cidade": "Sorocaba",
            "uf": "SP"
        },
        "agencia": AGENCIA,
        "numeroConta": "00005",
        "tipoConta": "Corrente",
        "saldo": 0.00
    },
    {
        "nome": "Benedito Cruz",
        "cpf": "789.632.154-96",
        "endereco": {
            "logradouro": "Rua Encantado",
            "numero": 1102,
            "complemento":"apt 1145",
            "bairro": "Estado da União",
            "cidade": "São Paulo",
            "uf": "SP"
        },
        "agencia": AGENCIA,
        "numeroConta": "00006",
        "tipoConta": "Corrente",
        "saldo": 15.00
    },
    {
        "nome": "Elieser Frontana",
        "cpf": "562.631.754-89",
        "endereco": {
            "logradouro": "Não Informada"
        },
        "agencia": AGENCIA,
        "numeroConta": "00007",
        "tipoConta": "Corrente",
        "saldo": 11500.00
    },
    {
        "nome": "Genivaldo da Conceição Cruz",
        "cpf": "546.659.562-63",
        "endereco": {
            "logradouro": "Viela da Paz",
            "numero": 45,
            "bairro": "Santo Estado",
            "cidade": "São Bernado",
            "uf": "SP"
        },
        "agencia": AGENCIA,
        "numeroConta": "00008",
        "tipoConta": "Corrente",
        "saldo": 852.32
    },
    {
        "nome": "Maria Maria de Maria José",
        "cpf": "874.851.263-54",
        "endereco": {
            "logradouro": "Rua Do não acredito",
            "numero": "sn",
            "complemento":"casa 25 da fonte azul",
            "bairro": "Bairro Novo",
            "cidade": "Adradinante",
            "uf": "Mg"
        },
        "agencia": AGENCIA,
        "numeroConta": "00009",
        "tipoConta": "Corrente",
        "saldo": 45236.56
    }
]

postando = collection.insert_many(posts)


