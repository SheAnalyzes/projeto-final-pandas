from readFile import ReadFile
from intercept import Intercept
from connectionDB import ConnectionDB

while True:
    print("Digite a opção na ordem do passo a passo")
    print("1 - Lendo os arquivos csv")
    print("2 - Interceptar operações fraudulentas com python")
    print("3 - Gerar arquivos csv")
    print("4 - Salvar dados no Banco SQL")
    print("5 - Sair")
    print("-"*50)
    print("Digite o número da opção:")
    option = int(input())

    if option == 1:
        print("-"*100)
        print("Dataframe de clientes")
        clients_df = ReadFile.Clients()
        print("-"*100)
        print(clients_df)
        print("Dataframe de todas as transações realizadas")
        transaction_df = ReadFile.Transaction()
        print(transaction_df)
        print("-"*100)

    if option == 2:
        print("-"*100)
        print("Interceptando todas as transações fraudulentas")
        transaction_fraud = Intercept.Transaction(transaction_df)
        print(transaction_fraud)
        print("-"*100)
        print("Encontrando os clientes envolvidos")
        clients_fraud = Intercept.Client(clients_df, transaction_df)
        print(clients_fraud)
        print("-"*100)

    if option == 3:
        print("-"*100)
        print("Criando csv dos arquivos de carga...")
        clients_df.to_csv('./reports/clients.csv', index=False)
        transaction_df.to_csv('./reports/transactions.csv', index=False)
        print("-"*100)
        print("Criando csv dos arquivos encontrados...")
        clients_fraud.to_csv('./reports/clients_fraud.csv', index=False)
        transaction_fraud.to_csv('./reports/transaction_fraud.csv', index=False)
        print("-"*100)

    if option == 4:
        print("-"*100)
        print("Aguarde... Salvando operações no Banco. ")
        conexao = ConnectionDB()
        conexao.clients()
        conexao.clients_fraud()
        conexao.transactions()
        conexao.transaction_fraud()
        conexao.closeConnection()
        print("-"*100)

    if option == 5:
        exit()