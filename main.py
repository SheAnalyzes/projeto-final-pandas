from readFile import ReadFile
from intercept import Intercept
from connectionDB import ConnectionDB
import time

while True:
    print("Digite uma das opções abaixo: ")
    print("1 - Juntando os arquivos de carga")
    print("2 - Interceptar operações fraudulentas com pandas")
    print("3 - Salvar dados dos clientes no banco")
    print("4 - Salvar dados das transações no banco")
    print("5 - Sair")
    print("-"*50)
    print("Digite o número da opção:")
    option = int(input())

    if option == 1:
        print("-"*100)
        print("Dataframe de clientes")
        clients_df = ReadFile.Clients()
        print("-"*100)
        time.sleep(2)
        print("Dataframe de todas as transações realizadas")
        transaction_df = ReadFile.Transactions()
        print("-"*100)
        time.sleep(2)

    if option == 2:
        print("-"*100)
        print("Interceptando todas as transações fraudulentas")
        Intercept.Transactions()
        print("-"*100)
        time.sleep(2)
        print("Encontrando os clientes envolvidos")
        Intercept.Client()
        print("-"*100)
        time.sleep(2)

    if option == 3:
        print("-"*100)
        print("Aguarde... Conectando com o banco de dados. ")
        print("-"*100)
        conexao = ConnectionDB()
        print("Salvando dados dos clientes...")
        conexao.clients()
        print("-"*100)
        time.sleep(2)
        print("Salvando dados dos clientes fraudulentos...")
        conexao.clients_fraud()
        print("Fechando conexão.")
        conexao.closeConnection()
        print("-"*100)
        time.sleep(2)

    if option == 4:
        print("-"*100)
        print("Aguarde... Conectando com o banco de dados. ")
        print("-"*100)
        conexao = ConnectionDB()
        print("Salvando todas as transações...")
        conexao.transactions()
        print("-"*100)
        time.sleep(2)
        print("Salvando as transações com fraude...")
        conexao.transaction_fraud()
        print("Fechando conexão.")
        conexao.closeConnection()
        print("-"*100)
        time.sleep(2)

    if option == 5:
        print("-"*100)
        print("Programa encerrado.")
        exit()