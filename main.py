from readFile import ReadFile
from intercept import Intercept
from connectionDB import ConnectionDB
import time


while True:
    print("Digite uma das opções abaixo: ")
    print("1 - Juntar os arquivos de carga")
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
        ReadFile.clients()
        print("-"*100)
        time.sleep(2)
        print("Dataframe das transações de entrada")
        ReadFile.transaction_in()
        print("-"*100)
        time.sleep(2)
        print("Dataframe das transações de saída")
        ReadFile.transaction_out()
        print("-"*100)
        time.sleep(2)
        print("Dataframe de todas as transações realizadas")
        ReadFile.transactions()
        print("-"*100)
        time.sleep(2)

    if option == 2:
        print("-"*100)
        print("Interceptando todas as transações fraudulentas")
        Intercept.transactions_fraud()
        print("-"*100)
        time.sleep(2)
        print("Encontrando os clientes envolvidos")
        Intercept.client_fraud()
        print("-"*100)
        time.sleep(2)
        print("Encontrando todas as transações com flag de fraude e tipo de transação")
        Intercept.transactions_db()
        print("-"*100)
        time.sleep(2)

    if option == 3:
        print("-"*100)
        print("Aguarde... Conectando com o banco de dados. ")
        print("-"*100)
        conexao = ConnectionDB()
        print("Salvando a tabela clientes...")
        conexao.clients()
        print("-"*100)
        time.sleep(2)

    if option == 4:
        print("-"*100)
        print("Aguarde... Conectando com o banco de dados. ")
        print("-"*100)
        conexao = ConnectionDB()
        print("Salvando a tabela transacoes...")
        conexao.transactions()
        print("-"*100)
        time.sleep(2)

    if option == 5:
        print("-"*100)
        print("Programa encerrado.")
        exit()